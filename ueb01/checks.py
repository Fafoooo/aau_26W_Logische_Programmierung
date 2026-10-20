#!/usr/bin/env python3
"""Alle Lösungen durch clingo UND einen unabhängigen GL-Redukt-Prüfer testen.

Aufruf aus jedem Verzeichnis: python3 /pfad/zu/ueb01/checks.py
Benötigt Python >= 3.10 und das Kommando clingo; keine Python-Zusatzpakete.
Der Parser unterstützt absichtlich nur die endlichen Grundprogramme dieses Blatts.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Rule:
    head: str
    positive: frozenset[str] = frozenset()
    negative: frozenset[str] = frozenset()


def split_body(text: str) -> list[str]:
    """Nur Kommas außerhalb von Argumentklammern trennen Literale."""
    parts, start, depth = [], 0, 0
    for index, char in enumerate(text):
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            assert depth >= 0, text
        elif char == "," and depth == 0:
            parts.append(text[start:index].strip())
            start = index + 1
    assert depth == 0, text
    parts.append(text[start:].strip())
    assert all(parts), text
    return parts


def atom(text: str) -> str:
    cleaned = re.sub(r"\s+", "", text)
    assert re.fullmatch(r"[a-z][a-z0-9_]*(?:\((?:[a-z][a-z0-9_]*|[0-9]+)(?:,(?:[a-z][a-z0-9_]*|[0-9]+))*\))?", cleaned), text
    return cleaned


def parse(source: str) -> list[Rule]:
    source = re.sub(r"%\*.*?\*%", "", source, flags=re.S)
    source = re.sub(r"%[^\n]*", "", source)
    result = []
    for statement in source.split("."):
        if not statement.strip():
            continue
        fields = statement.strip().split(":-")
        assert len(fields) in (1, 2), statement
        positive, negative = set(), set()
        if len(fields) == 2:
            for literal in split_body(fields[1]):
                if literal.startswith("not "):
                    negative.add(atom(literal[4:]))
                else:
                    positive.add(atom(literal))
        result.append(Rule(atom(fields[0]), frozenset(positive), frozenset(negative)))
    return result


def reduct(rules: list[Rule], candidate: frozenset[str]) -> list[Rule]:
    return [Rule(r.head, r.positive) for r in rules if r.negative.isdisjoint(candidate)]


def least_steps(rules: list[Rule]) -> list[frozenset[str]]:
    """Synchroner positiver Konsequenzoperator ab der leeren Menge."""
    assert all(not r.negative for r in rules)
    steps = [frozenset()]
    while True:
        following = frozenset(r.head for r in rules if r.positive <= steps[-1])
        assert steps[-1] <= following
        if following == steps[-1]:
            return steps
        steps.append(following)


def stable_models(rules: list[Rule]) -> set[frozenset[str]]:
    if all(not r.negative for r in rules):
        return {least_steps(rules)[-1]}
    # Nicht im Kopf vorkommende Atome können im kleinsten Reduktmodell nie entstehen.
    heads = sorted({r.head for r in rules})
    models = set()
    for bits in product((False, True), repeat=len(heads)):
        candidate = frozenset(a for a, selected in zip(heads, bits) if selected)
        if least_steps(reduct(rules, candidate))[-1] == candidate:
            models.add(candidate)
    return models


def classical_model(rules: list[Rule], candidate: frozenset[str]) -> bool:
    return all(not (r.positive <= candidate and r.negative.isdisjoint(candidate))
               or r.head in candidate for r in rules)


def solve_clingo(source: str) -> set[frozenset[str]]:
    binary = shutil.which("clingo")
    assert binary, "clingo fehlt: https://potassco.org/clingo/"
    run = subprocess.run([binary, "--outf=2", "--warn=none", "0", "-"],
                         input=source, capture_output=True, text=True, timeout=30)
    assert run.returncode in (10, 20, 30), (run.returncode, run.stderr)
    data = json.loads(run.stdout)
    assert data["Result"] in ("SATISFIABLE", "UNSATISFIABLE"), data
    assert data["Models"]["More"] == "no", data
    witnesses = [frozenset(w["Value"]) for call in data["Call"]
                 for w in call.get("Witnesses", [])]
    assert data["Models"]["Number"] == len(witnesses), data
    assert len(set(witnesses)) == len(witnesses), data
    assert (data["Result"] == "SATISFIABLE") == bool(witnesses), data
    return set(witnesses)


def letters(text: str) -> frozenset[str]:
    return frozenset(text)


def show(model: frozenset[str]) -> str:
    return "{" + ", ".join(sorted(model)) + "}"


def expectations() -> dict[str, set[frozenset[str]]]:
    """Von der mathematischen Lösung vorgegebene Sollmodelle, keine Solver-Ausgabe."""
    expected = {
        "uebung/ue1.1/a": {letters("acdg")},
        "uebung/ue1.1/b": {frozenset({
            "likes(kate,fish)", "likes(kate,soup)", "likes(mike,beef)", "likes(mike,cake)",
            "likes(paul,duck)", "likes(paul,pork)", "likes(tina,beef)", "likes(tina,soup)",
            "order(beef)", "order(soup)", "happy(kate)", "happy(mike)", "happy(tina)"})},
        "uebung/ue1.2/a": {letters("abde"), letters("ce")},
        "uebung/ue1.2/b": {letters("acde"), letters("be")},
        "hausuebung/ue1.1/a": {letters("acdeghk")},
        "hausuebung/ue1.1/b": {frozenset({
            "conn(amsterdam,brussels)", "conn(brussels,cologne)", "conn(cologne,amsterdam)",
            "tour(amsterdam,cologne)", "tour(brussels,amsterdam)", "tour(cologne,brussels)",
            "finish(brussels)"})},
        "hausuebung/ue1.2/a": {letters("ac"), letters("bcd")},
        "hausuebung/ue1.2/b": {letters("acdf"), letters("be"), letters("bf")},
    }
    for variant in ("uebung", "hausuebung"):
        for part in ("a", "b"):
            expected[f"{variant}/ue1.3/{part}"] = expected[f"{variant}/ue1.2/{part}"]
    birds = {"canary(tweety)", "penguin(tux)", "bird(tweety)", "bird(tux)"}
    expected["uebung/ue1.4/a"] = {
        frozenset(birds | {f"{t}(tweety)", f"{u}(tux)"}
                  | ({"flies(tweety)"} if t == "ok" else set()))
        for t, u in product(("injured", "ok"), repeat=2)
    }
    expected["hausuebung/ue1.4/a"] = {
        frozenset(birds | {"walks(tux)", f"{choice}(tweety)"})
        for choice in ("walks", "flies")
    }
    nums = {f"num({n})" for n in (1, 2, 3)}
    expected["uebung/ue1.4/b"] = {frozenset(nums | {f"lucky({n})" for n in (1, 2, 3)})}
    expected["hausuebung/ue1.4/b"] = {
        frozenset(nums | {f"{'lucky' if n == chosen else 'unlucky'}({n})" for n in (1, 2, 3)})
        for chosen in (None, 1, 2, 3)
    }
    return expected


def test_helpers() -> None:
    assert split_body("likes(kate,fish), not happy(kate)") == ["likes(kate,fish)", "not happy(kate)"]
    assert least_steps(parse("a :- b. b :- a.")) == [frozenset()]
    assert stable_models(parse("a :- not b. b :- not a.")) == {letters("a"), letters("b")}
    assert not stable_models(parse("p :- not p."))
    assert stable_models(parse("a. b :- a.")) == {letters("ab")}
    for text in ("a :- a.", "p :- not p.", "a :- not b. b :- not a."):
        assert stable_models(parse(text)) == solve_clingo(text)


def test_candidates() -> None:
    x1, x2 = letters("abde"), letters("be")
    expected = {"a": [(x1, letters("abde"), True), (x2, letters("abde"), False)],
                "b": [(x1, letters("b"), False), (x2, letters("be"), True)]}
    for part, cases in expected.items():
        rules = parse((ROOT / f"uebung/ue1.2/{part}/programm.lp").read_text())
        for candidate, least, stable in cases:
            steps = least_steps(reduct(rules, candidate))
            assert steps[-1] == least, (part, candidate, steps)
            assert (steps[-1] == candidate) == stable
            print(f"  Exercise 1.2 {part}: X={show(candidate)}, LM={show(least)}, stabil={stable}")


def main() -> None:
    test_helpers()
    expected = expectations()
    actual_files = {p.parent.relative_to(ROOT).as_posix()
                    for p in ROOT.glob("*/ue1.*/*/programm.lp")}
    assert actual_files == set(expected), (actual_files - set(expected), set(expected) - actual_files)
    for name, wanted in sorted(expected.items()):
        path = ROOT / name / "programm.lp"
        source = path.read_text(encoding="utf-8")
        rules = parse(source)
        assert rules
        by_reduct = stable_models(rules)
        by_clingo = solve_clingo(source)
        assert by_reduct == wanted, (name, by_reduct, wanted)
        assert by_clingo == wanted, (name, by_clingo, wanted)
        assert all(classical_model(rules, m) for m in wanted)
        assert (path.parent / "antwort.md").is_file(), f"Antwort fehlt: {name}"
        print(f"OK {name}: {len(wanted)} Answer Set(s); clingo = GL-Prüfer = Soll")
        for model in sorted(wanted, key=lambda m: sorted(m)):
            print("  " + show(model))
    for variant in ("uebung", "hausuebung"):
        for part in ("a", "b"):
            original = parse((ROOT / variant / "ue1.2" / part / "programm.lp").read_text())
            repeated = parse((ROOT / variant / "ue1.3" / part / "programm.lp").read_text())
            assert original == repeated, (variant, part)
    test_candidates()
    loop = parse((ROOT / "uebung/quiz/gegenbeispiel_1.lp").read_text())
    assert classical_model(loop, frozenset()) and classical_model(loop, letters("a"))
    assert stable_models(loop) == {frozenset()}
    odd = (ROOT / "uebung/quiz/gegenbeispiel_4.lp").read_text()
    assert classical_model(parse(odd), letters("p"))
    assert stable_models(parse(odd)) == solve_clingo(odd) == set()
    print(f"OK: {len(expected)} Aufgabenprogramme, Quiz, Redukte und Prüfer-Selbsttests bestanden.")
    print("Zusätzlich: python3 hausuebung/ue1.2/pruefe_redukte.py")


if __name__ == "__main__":
    main()
