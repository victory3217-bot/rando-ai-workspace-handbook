#!/usr/bin/env python3
"""Structure audit for the AI Workspace Handbook (read-only).

Source mode (default): checks content-manifest.json against ko/ and en/.
Build mode (--dist site/dist): additionally checks the built site.

Nothing is written, moved or deleted. Exit code 0 = no failures, 1 = failures.
Checks that could not be run are reported as SKIP, never as PASS.

Usage:
    python tools/content_audit.py
    python tools/content_audit.py --dist site/dist
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "/rando-ai-workspace-handbook/"

CORE = [f"AW-CH{n:02d}" for n in range(1, 15)]
OPTIONAL = [f"AW-OP{n:02d}" for n in range(1, 4)]
EXPECTED_IDS = CORE + OPTIONAL

STATUSES = ["Planned", "Draft", "Translated", "Reviewed", "Published", "Needs Update"]
EN_RELEASABLE = ["Reviewed", "Published"]
KO_DONE = ["Reviewed", "Published"]
FIELDS = ["chapter_id", "title", "language", "status", "last_reviewed"]

SECTIONS = {
    "ko": [
        "1. 학습목표",
        "2. 핵심 개념",
        "3. 업무 적용 사례",
        "4. 준비물",
        "5. 단계별 실습",
        "6. 결과 검증",
        "7. 오류 해결",
        "8. 완료 체크리스트",
        "9. 참고자료",
    ],
    "en": [
        "1. Learning Objectives",
        "2. Core Concepts",
        "3. Workplace Application",
        "4. What You Need",
        "5. Step-by-Step Practice",
        "6. Verify the Result",
        "7. Troubleshooting",
        "8. Completion Checklist",
        "9. References",
    ],
}

# Repositories confirmed PUBLIC with `gh repo view` on 2026-10-26. A harness case may
# only name one of these. Update this list only after re-checking visibility.
PUBLIC_REPOS = {
    "pricing-harness",
    "rando-promotion-harness",
    "oda-project-reviewer",
    "rando-client-discovery-harness",
    "business-planning-handbook",
    "pricing-handbook",
}
# Confirmed PRIVATE on 2026-10-26. Must never appear in chapter text.
PRIVATE_REPOS = {"rando-client-discovery-app", "rando-client-discovery-training"}

CASE_FIELDS = ["저장소:", "파일 경로:", "확인한 내용:", "진행 상태:", "확인일:"]
CASE_FIELDS_EN = ["Repository:", "File path:", "What was confirmed:", "Status:", "Verified on:"]

results: list[tuple[str, str, str]] = []  # (PASS|FAIL|SKIP, check, detail)


def record(kind: str, check: str, detail: str = "") -> None:
    results.append((kind, check, detail))


def stem(chapter_id: str) -> str:
    return chapter_id.removeprefix("AW-")


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def load_manifest():
    path = ROOT / "content-manifest.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        record("FAIL", "manifest: readable JSON", str(exc))
        return None
    record("PASS", "manifest: readable JSON")
    return data.get("entries", [])


def check_manifest(entries) -> None:
    bad = []
    for i, e in enumerate(entries):
        missing = [f for f in FIELDS if f not in e]
        extra = [f for f in e if f not in FIELDS]
        if missing or extra:
            bad.append(f"entry {i}: missing={missing} extra={extra}")
    record("FAIL" if bad else "PASS", "manifest: only the five agreed fields", "; ".join(bad))

    bad = [f"{e.get('chapter_id')}/{e.get('language')}: {e.get('status')}" for e in entries if e.get("status") not in STATUSES]
    record("FAIL" if bad else "PASS", "manifest: status values allowed", "; ".join(bad))

    bad = []
    for e in entries:
        v = e.get("last_reviewed")
        if v is not None and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(v)):
            bad.append(f"{e.get('chapter_id')}/{e.get('language')}: {v}")
    record("FAIL" if bad else "PASS", "manifest: last_reviewed is null or YYYY-MM-DD", "; ".join(bad))

    for lang in ("ko", "en"):
        ids = [e["chapter_id"] for e in entries if e.get("language") == lang]
        dup = sorted({i for i in ids if ids.count(i) > 1})
        missing = [i for i in EXPECTED_IDS if i not in ids]
        extra = [i for i in ids if i not in EXPECTED_IDS]
        problems = []
        if dup:
            problems.append(f"duplicate={dup}")
        if missing:
            problems.append(f"missing={missing}")
        if extra:
            problems.append(f"unexpected={extra}")
        record("FAIL" if problems else "PASS", f"manifest[{lang}]: AW-CH01..14 + AW-OP01..03 exactly once", "; ".join(problems))

    bad = [
        e["chapter_id"]
        for e in entries
        if e.get("language") == "en"
        and e.get("status") in EN_RELEASABLE
        and next((k["status"] for k in entries if k["chapter_id"] == e["chapter_id"] and k["language"] == "ko"), "") not in KO_DONE
    ]
    record("FAIL" if bad else "PASS", "manifest: English Reviewed/Published only after Korean Reviewed/Published", ", ".join(bad))


def chapter_files(lang: str) -> dict[str, Path]:
    d = ROOT / lang / "chapters"
    if not d.exists():
        return {}
    return {p.stem: p for p in sorted(d.glob("*.md"))}


def h2_list(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^##\s+(.+?)\s*$", strip_comments(text), flags=re.M)]


def check_files(entries) -> None:
    for lang in ("ko", "en"):
        files = chapter_files(lang)
        wanted = {stem(e["chapter_id"]): e for e in entries if e.get("language") == lang}

        stray = [s for s in files if s not in wanted]
        record("FAIL" if stray else "PASS", f"files[{lang}]: every chapter file is a registered chapter", ", ".join(stray))

        planned_with_file = [s for s, e in wanted.items() if e["status"] == "Planned" and s in files]
        record("FAIL" if planned_with_file else "PASS", f"files[{lang}]: Planned chapters have no file", ", ".join(planned_with_file))

        missing = [s for s, e in wanted.items() if e["status"] != "Planned" and s not in files]
        record("FAIL" if missing else "PASS", f"files[{lang}]: non-Planned chapters have a file", ", ".join(missing))

        id_bad, sec_bad = [], []
        for s, path in files.items():
            if s not in wanted:
                continue
            text = path.read_text(encoding="utf-8")
            m = re.match(r"\s*<!--\s*chapter_id:\s*(AW-[A-Z]{2}\d{2})\s*-->", text)
            if not m or m.group(1) != wanted[s]["chapter_id"]:
                id_bad.append(f"{path.name}: first-line chapter_id={m.group(1) if m else None}")
            got = h2_list(text)
            if got != SECTIONS[lang]:
                sec_bad.append(f"{path.name}: {got}")
        record("FAIL" if id_bad else "PASS", f"files[{lang}]: chapter_id comment matches file name and manifest", "; ".join(id_bad))
        record("FAIL" if sec_bad else "PASS", f"files[{lang}]: nine standard sections in order", "; ".join(sec_bad))


LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)\)")


def check_links_and_cases() -> None:
    link_bad, md_bad, private_bad, case_bad, repo_bad = [], [], [], [], []
    for lang in ("ko", "en"):
        for stem_, path in chapter_files(lang).items():
            raw = path.read_text(encoding="utf-8")
            text = strip_comments(raw)
            for target in LINK.findall(text):
                if re.match(r"^(https?:|mailto:|#)", target):
                    continue
                if target.split("#")[0].endswith(".md"):
                    md_bad.append(f"{path.relative_to(ROOT)} -> {target}")
                    continue
                if not (path.parent / target.split("#")[0]).exists():
                    link_bad.append(f"{path.relative_to(ROOT)} -> {target}")
            for name in PRIVATE_REPOS:
                if name in raw:
                    private_bad.append(f"{path.relative_to(ROOT)} mentions {name}")
            # every harness-case block must carry all five fields and name a public repo
            for block in re.findall(r"^> \*\*(?:하네스 사례|Harness case)[^\n]*\n(?:>[^\n]*\n?)+", text, flags=re.M):
                fields = CASE_FIELDS if lang == "ko" else CASE_FIELDS_EN
                absent = [f for f in fields if f not in block]
                if absent:
                    case_bad.append(f"{path.relative_to(ROOT)}: missing {absent}")
                repo = re.search(r"(?:저장소|Repository):\s*([A-Za-z0-9._-]+)", block)
                if not repo or repo.group(1) not in PUBLIC_REPOS:
                    repo_bad.append(f"{path.relative_to(ROOT)}: repo={repo.group(1) if repo else None}")
    record("FAIL" if link_bad else "PASS", "links: relative file links resolve", "; ".join(link_bad))
    record("FAIL" if md_bad else "PASS", "links: no chapter-to-chapter .md links (they break on the site)", "; ".join(md_bad))
    record("FAIL" if private_bad else "PASS", "cases: no private repository named in chapters", "; ".join(private_bad))
    record("FAIL" if case_bad else "PASS", "cases: every harness case has the five required fields", "; ".join(case_bad))
    record("FAIL" if repo_bad else "PASS", "cases: every harness case names a repository on the public allowlist", "; ".join(repo_bad))


PLACEHOLDER = "〔작성 예정〕"
SRC_REF = re.compile(r"`?\[(S\d+)\]`?")
SRC_ROW = re.compile(r"^\|\s*(S\d+)\s*\|(.*)\|\s*$", re.M)
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
LEGACY_TAGS = re.compile(r"\[(개념|공식|해설)\]")  # the pre-2C inline label scheme must not come back
OFFICIAL_BOX = "> **공식 문서 확인"
GUIDE_PHRASES = ("읽는 방법", "일반 설명", "저자 해석", "좌우로 밀어")

# Fictional values that are allowed to look like personal data in teaching material.
SAFE_PHONE = {"010-0000-0000", "010-1234-5678"}
PERSONAL_PATTERNS = [
    ("resident registration number", re.compile(r"\b\d{6}-[1-4]\d{6}\b")),
    ("phone number", re.compile(r"\b0\d{1,2}-\d{3,4}-\d{4}\b")),
    ("email address", re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})")),
    ("API key / token", re.compile(r"\b(sk-[A-Za-z0-9_-]{16,}|AKIA[0-9A-Z]{12,}|ghp_[A-Za-z0-9]{20,}|xox[bap]-[A-Za-z0-9-]{10,})\b")),
]


def check_content_quality(entries) -> None:
    """Body-level checks for chapters that exist as drafts or later."""
    title_bad, legend_bad, ph_bad, src_bad, tag_bad, pii_bad = [], [], [], [], [], []
    legacy_bad, disc_bad, copy_bad = [], [], []
    for lang in ("ko", "en"):
        wanted = {stem(e["chapter_id"]): e for e in entries if e.get("language") == lang}
        for s, path in chapter_files(lang).items():
            if s not in wanted:
                continue
            raw = path.read_text(encoding="utf-8")
            text = strip_comments(raw)
            rel = str(path.relative_to(ROOT))

            # H1 must be "CHxx. <manifest title>"
            h1 = re.search(r"^#\s+(.+?)\s*$", text, flags=re.M)
            expect = f"{s}. {wanted[s]['title']}"
            if not h1 or h1.group(1).strip() != expect:
                title_bad.append(f"{rel}: H1={h1.group(1) if h1 else None!r} expected={expect!r}")

            # source-label legend present (ko only; the English edition has no body yet)
            if lang == "ko":
                missing_guide = [g for g in GUIDE_PHRASES if g not in text]
                if missing_guide:
                    legend_bad.append(f"{rel}: missing {missing_guide}")
                if LEGACY_TAGS.search(text):
                    legacy_bad.append(rel)
                if "```" not in text:
                    copy_bad.append(rel)
                # the information-tier scheme must never be presented as a legal or official standard
                if s == "CH03" and "법적 분류나 공인된 기준이 아닙니다" not in text:
                    disc_bad.append(rel)

            # chapters declared as having a body must not keep placeholders
            if lang == "ko" and PLACEHOLDER in text:
                ph_bad.append(f"{rel}: {text.count(PLACEHOLDER)}x")

            # every [S#] reference resolves to a row with an https URL and a YYYY-MM-DD check date
            rows = {m.group(1): m.group(2) for m in SRC_ROW.finditer(text)}
            for ref in sorted(set(SRC_REF.findall(text))):
                if ref not in rows:
                    src_bad.append(f"{rel}: {ref} has no source row")
            for ref, cells in rows.items():
                if "https://" not in cells:
                    src_bad.append(f"{rel}: {ref} has no https URL")
                if not DATE.search(cells):
                    src_bad.append(f"{rel}: {ref} has no check date")

            # every official-documentation box needs a check date and a source number on every bullet
            lines = text.splitlines()
            i = 0
            while i < len(lines):
                if lines[i].startswith(OFFICIAL_BOX):
                    head = lines[i]
                    j = i
                    block = []
                    while j < len(lines) and lines[j].startswith(">"):
                        block.append(lines[j])
                        j += 1
                    if not DATE.search(head):
                        tag_bad.append(f"{rel}: official box without check date: {head[:50]!r}")
                    for b in block[1:]:
                        if re.match(r">\s*-\s", b) and not SRC_REF.search(b):
                            tag_bad.append(f"{rel}: bullet without source number: {b[:50]!r}")
                    i = j
                else:
                    i += 1

            # teaching material must not contain real-looking personal data or secrets
            for label, pat in PERSONAL_PATTERNS:
                for m in pat.finditer(text):
                    value = m.group(0)
                    if label == "phone number" and value in SAFE_PHONE:
                        continue
                    if label == "email address" and (m.group(1).lower().endswith(("example.com", "example.org", "example.net", "test"))):
                        continue
                    pii_bad.append(f"{rel}: {label} {value!r}")
    record("FAIL" if title_bad else "PASS", "content: chapter H1 matches manifest title", "; ".join(title_bad))
    record("FAIL" if legend_bad else "PASS", "content: reading guide (일반 설명 / 저자 해석 / table-scroll hint) present in Korean chapters", "; ".join(legend_bad))
    record("FAIL" if legacy_bad else "PASS", "content: no leftover [개념]/[공식]/[해설] inline tags", ", ".join(legacy_bad))
    record("FAIL" if disc_bad else "PASS", "content: CH03 states the information tiers are not a legal or official standard", ", ".join(disc_bad))
    record("FAIL" if copy_bad else "PASS", "content: Korean chapters contain at least one copyable practice template", ", ".join(copy_bad))
    record("FAIL" if ph_bad else "PASS", "content: no 〔작성 예정〕 placeholder left in Korean chapters", "; ".join(ph_bad))
    record("FAIL" if src_bad else "PASS", "content: every [S#] reference has a row with https URL and check date", "; ".join(src_bad))
    record("FAIL" if tag_bad else "PASS", "content: every 공식 문서 확인 box has a check date and a source number on each bullet", "; ".join(tag_bad[:5]))
    record("FAIL" if pii_bad else "PASS", "content: no real-looking personal data or secrets in teaching material", "; ".join(pii_bad[:8]))


def check_support_docs(entries) -> None:
    need = ["README.md", "VERSION", "CHANGELOG.md", "glossary.md", "source-map.md", "content-manifest.json"]
    absent = [n for n in need if not (ROOT / n).exists()]
    record("FAIL" if absent else "PASS", "docs: README, VERSION, CHANGELOG, glossary, source-map, manifest exist", ", ".join(absent))

    sm = ROOT / "source-map.md"
    if sm.exists():
        text = sm.read_text(encoding="utf-8")
        missing = [i for i in chapter_files("ko") if f"AW-{i}" not in text]
        record("FAIL" if missing else "PASS", "docs: source-map.md covers every existing chapter", ", ".join(missing))
    else:
        record("SKIP", "docs: source-map.md covers every existing chapter", "source-map.md missing")


class Hrefs(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.hrefs.append(a["href"])
        if a.get("id"):
            self.ids.add(a["id"])


def page_for(dist: Path, href: str) -> Path | None:
    path = href.split("#")[0].split("?")[0]
    if not path.startswith(BASE):
        return None
    rel = path[len(BASE):]
    candidates = [dist / rel] if rel.endswith(".html") else [dist / rel / "index.html", dist / rel]
    for c in candidates:
        if c.is_file():
            return c
    return dist / "__missing__" / rel


def check_dist(dist: Path, entries) -> None:
    if not dist.exists():
        record("SKIP", "dist: build output present", f"{dist} not found - run the build first")
        return
    record("PASS", "dist: build output present")

    ko_expected = {
        stem(e["chapter_id"]).lower()
        for e in entries
        if e["language"] == "ko" and e["status"] != "Planned" and (ROOT / "ko" / "chapters" / f"{stem(e['chapter_id'])}.md").exists()
    }
    ko_built = {p.parent.name for p in (dist / "ko" / "chapters").glob("*/*/index.html")} if (dist / "ko" / "chapters").exists() else set()
    problems = []
    if ko_built != ko_expected:
        problems.append(f"expected={sorted(ko_expected)} built={sorted(ko_built)}")
    record("FAIL" if problems else "PASS", "dist: Korean chapter pages == existing, non-Planned Korean chapters", "; ".join(problems))

    en_releasable = {
        stem(e["chapter_id"]).lower()
        for e in entries
        if e["language"] == "en" and e["status"] in EN_RELEASABLE and (ROOT / "en" / "chapters" / f"{stem(e['chapter_id'])}.md").exists()
    }
    en_dir = dist / "en"
    en_built = {p.parent.name for p in (en_dir / "chapters").glob("*/*/index.html")} if (en_dir / "chapters").exists() else set()
    if en_built - en_releasable:
        record("FAIL", "dist: no unreleased English chapter page", f"built={sorted(en_built - en_releasable)}")
    elif not en_releasable and en_dir.exists():
        record("FAIL", "dist: no /en/ output while no English chapter is releasable", "dist/en exists")
    else:
        record("PASS", "dist: no unreleased English chapter page")

    hangul_in_en = []
    if en_dir.exists():
        for p in en_dir.rglob("*.html"):
            if re.search(r"[가-힣]{5,}", re.sub(r"<[^>]+>", "", p.read_text(encoding="utf-8", errors="ignore"))):
                hangul_in_en.append(str(p.relative_to(dist)))
    record("FAIL" if hangul_in_en else "PASS", "dist: no Korean text served under /en/", ", ".join(hangul_in_en[:5]))

    broken, anchors, checked = [], [], 0
    cache: dict[Path, Hrefs] = {}
    for page in dist.rglob("*.html"):
        parser = Hrefs()
        parser.feed(page.read_text(encoding="utf-8", errors="ignore"))
        cache[page] = parser
    for page, parser in cache.items():
        for href in parser.hrefs:
            if href.startswith(("http:", "https:", "mailto:", "tel:", "#", "javascript:")):
                continue
            if href.startswith("/") and not href.startswith(BASE):
                broken.append(f"{page.relative_to(dist)} -> {href} (outside base path)")
                continue
            target = page_for(dist, href) if href.startswith("/") else None
            if target is None:
                continue
            checked += 1
            if not target.is_file():
                broken.append(f"{page.relative_to(dist)} -> {href}")
                continue
            frag = href.split("#")[1] if "#" in href else ""
            if frag and target in cache and frag not in cache[target].ids:
                anchors.append(f"{page.relative_to(dist)} -> {href}")
    record("FAIL" if broken else "PASS", f"dist: internal links resolve ({checked} checked)", "; ".join(broken[:10]))
    record("FAIL" if anchors else "PASS", "dist: in-site #anchors exist", "; ".join(anchors[:10]))

    sample = dist / "ko" / "index.html"
    if sample.exists():
        html = sample.read_text(encoding="utf-8", errors="ignore")
        ok = 'name="robots"' in html and "noindex" in html
        record("PASS" if ok else "FAIL", "dist: noindex present while unpublished")
    else:
        record("SKIP", "dist: noindex present while unpublished", "dist/ko/index.html missing")

    record("PASS" if (dist / "pagefind").exists() else "FAIL", "dist: search index (pagefind) generated")


def main() -> int:
    # Chapter titles are Korean; keep Windows consoles from printing mojibake.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", help="path to the built site (site/dist) to audit as well")
    args = ap.parse_args()

    entries = load_manifest()
    if entries is not None:
        check_manifest(entries)
        check_files(entries)
        check_links_and_cases()
        check_content_quality(entries)
        check_support_docs(entries)
        if args.dist:
            check_dist((ROOT / args.dist) if not Path(args.dist).is_absolute() else Path(args.dist), entries)
        else:
            record("SKIP", "dist checks", "run with --dist site/dist after a build")

    width = max(len(c) for _, c, _ in results)
    for kind, check, detail in results:
        print(f"[{kind}] {check.ljust(width)}" + (f"  -> {detail}" if detail and kind != "PASS" else ""))
    fails = sum(1 for k, _, _ in results if k == "FAIL")
    skips = sum(1 for k, _, _ in results if k == "SKIP")
    passes = sum(1 for k, _, _ in results if k == "PASS")
    print(f"\nPASS={passes} FAIL={fails} SKIP={skips}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
