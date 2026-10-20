#!/usr/bin/env python3
"""Gezielte GL-Redukt-Prüfung für Homework 1.2 und die Lösungen von 1.3.

Nur Standardbibliothek; Aufruf: python3 pruefe_redukte.py
Die vorhandenen Dateien werden ausschließlich gelesen. clingo erhält die
berechneten Redukte über stdin; es werden keine temporären Dateien erzeugt.
Dieser kleine Prüfer ersetzt nicht den zentralen Testlauf aller Grundprogramme.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
import subprocess


@dataclass(frozen=True)
class Regel:
    kopf: str
    positiv: tuple[str, ...] = ()
    negativ: tuple[str, ...] = ()


def lesen(text: str) -> list[Regel]:
    """Parser nur für die aussagenlogischen Programme 1.1 a / 1.2 a,b."""
    text = re.sub(r"%\*.*?\*%", "", text, flags=re.S)
    text = re.sub(r"%[^\n]*", "", text)
    regeln = []
    for roh in text.split("."):
        if not roh.strip():
            continue
        teile = roh.strip().split(":-")
        assert len(teile) in (1, 2), roh
        kopf = teile[0].strip()
        assert re.fullmatch(r"[a-z][a-z0-9_]*", kopf), kopf
        positiv, negativ = [], []
        if len(teile) == 2:
            for literal in teile[1].split(","):
                literal = literal.strip()
                if literal.startswith("not "):
                    atom = literal[4:].strip()
                    negativ.append(atom)
                else:
                    atom = literal
                    positiv.append(atom)
                assert re.fullmatch(r"[a-z][a-z0-9_]*", atom), atom
        regeln.append(Regel(kopf, tuple(positiv), tuple(negativ)))
    return regeln


def redukt(regeln: list[Regel], kandidat: frozenset[str]) -> list[Regel]:
    """Zuerst Regeln mit verletztem not löschen, danach übriges not entfernen."""
    return [Regel(r.kopf, r.positiv) for r in regeln
            if not (set(r.negativ) & kandidat)]


def fixpunkt(regeln: list[Regel]) -> list[frozenset[str]]:
    """Synchroner T_P-Fixpunkt ab leerer Menge, ohne doppelte Schlussstufe."""
    assert all(not r.negativ for r in regeln)
    stufen = [frozenset()]
    while True:
        neu = frozenset(r.kopf for r in regeln
                        if set(r.positiv) <= stufen[-1])
        assert stufen[-1] <= neu
        if neu == stufen[-1]:
            return stufen
        stufen.append(neu)


def ausgabe(regeln: list[Regel]) -> str:
    assert all(not r.negativ for r in regeln)
    return "\n".join(r.kopf + (" :- " + ", ".join(r.positiv)
                               if r.positiv else "") + "." for r in regeln)


def clingo_modelle(text: str) -> set[frozenset[str]]:
    prozess = subprocess.run(["/usr/bin/clingo", "--outf=2", "0", "-"],
                             input=text, text=True, capture_output=True,
                             check=False)
    assert prozess.returncode in (10, 30), (prozess.returncode, prozess.stderr)
    daten = json.loads(prozess.stdout)
    assert daten["Result"] == "SATISFIABLE", daten
    assert daten["Models"]["More"] == "no", daten
    zeugen = [frozenset(w["Value"]) for c in daten["Call"]
              for w in c.get("Witnesses", [])]
    assert daten["Models"]["Number"] == len(zeugen), daten
    return set(zeugen)


def menge(zeichen: str) -> frozenset[str]:
    return frozenset(zeichen)


def anzeigen(atome: frozenset[str]) -> str:
    return "{" + ",".join(sorted(atome)) + "}"


def main() -> None:
    ordner = Path(__file__).resolve().parent
    # Die Redukttexte sind unabhängig aus den Originalregeln abgeleitete
    # Sollwerte. Auch doppelte Fakten werden beim Strukturvergleich erhalten.
    soll = {
        "a": [
            ("X1", "", "a. b. b :- e. c :- a. c :- b. d. e :- a,d. e :- b.", "abcde"),
            ("X2", "ac", "a. b :- e. c :- a. c :- b. e :- a,d.", "ac"),
            ("X3", "abe", "a. b :- e. e :- a,d. e :- b.", "a"),
            ("1.3: M2", "bcd", "b. c :- a. c :- b. d. e :- a,d.", "bcd"),
        ],
        "b": [
            ("X1", "acdf", "a. c :- a. c :- d. d :- c,e. d. f.", "acdf"),
            ("X2", "bcde", "b. c :- a. c :- d. d :- c,e. e.", "be"),
            ("X3", "be", "b. b. c :- a. c :- d. d :- c,e. e.", "be"),
            ("1.3: M2", "bf", "b. c :- a. c :- d. d :- c,e. f.", "bf"),
        ],
    }
    erwartete_modelle = {"a": {menge("ac"), menge("bcd")},
                         "b": {menge("acdf"), menge("be"), menge("bf")}}
    for teil, faelle in soll.items():
        text = (ordner / teil / "programm.lp").read_text(encoding="utf-8")
        regeln = lesen(text)
        modelle = clingo_modelle(text)
        assert modelle == erwartete_modelle[teil], (teil, modelle)
        print(f"1.2 {teil}: alle clingo-Modelle korrekt: "
              + ", ".join(sorted(anzeigen(m) for m in modelle)))
        for name, roh, erwarteter_text, erwartete_atome in faelle:
            kandidat = menge(roh)
            positiv = redukt(regeln, kandidat)
            assert positiv == lesen(erwarteter_text), (teil, name, positiv)
            stufen = fixpunkt(positiv)
            kleinstes = stufen[-1]
            assert kleinstes == menge(erwartete_atome), (teil, name, stufen)
            assert clingo_modelle(ausgabe(positiv)) == {kleinstes}
            stabil = kleinstes == kandidat
            assert stabil == (kandidat in erwartete_modelle[teil])
            print(f"  {name}: Kandidat={anzeigen(kandidat)}, "
                  f"LM={anzeigen(kleinstes)}, stabil={stabil}")
            print("    T-Stufen: " + " -> ".join(anzeigen(s) for s in stufen))
    positiv = lesen((ordner.parent / "ue1.1" / "a" / "programm.lp")
                    .read_text(encoding="utf-8"))
    stufen = fixpunkt(positiv)
    assert stufen[-1] == menge("acdeghk")
    print("1.1 a, T-Stufen: " + " -> ".join(anzeigen(s) for s in stufen))
    print("OK: alle Reduktstrukturen, Fixpunkte und clingo-Gegenprüfungen bestanden.")


if __name__ == "__main__":
    main()
