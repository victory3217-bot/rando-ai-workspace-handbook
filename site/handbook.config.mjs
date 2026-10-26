// Single place for handbook-specific settings shared by astro.config.mjs and
// scripts/sync-content.mjs. Chapter text lives in ../ko and ../en; the status of
// every chapter lives in ../content-manifest.json.

import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));

export const SITE_ROOT = here;
export const REPO_ROOT = join(here, "..");

// Public address once the handbook is published. Nothing is deployed in Phase 2A.
export const SITE_URL = "https://victory3217-bot.github.io";
export const BASE = "/rando-ai-workspace-handbook/";

export const HANDBOOK_TITLE = {
	ko: "AI 워크스페이스 구축 핸드북",
	en: "AI Workspace Handbook",
};

export const STATUSES = ["Planned", "Draft", "Translated", "Reviewed", "Published", "Needs Update"];

// An English chapter becomes a page only at these statuses. Anything earlier
// (or no English file at all) produces no English page.
export const EN_RELEASABLE = ["Reviewed", "Published"];

// Sidebar groups. Part membership is only used for navigation; chapter IDs
// (AW-CHnn / AW-OPnn) never change.
export const PARTS = [
	{
		dir: "part-1",
		label: { ko: "Part 1 — AI 워크스페이스 이해", en: "Part 1 — Understanding the AI Workspace" },
		chapters: ["AW-CH01", "AW-CH02", "AW-CH03"],
	},
	{
		dir: "part-2",
		label: { ko: "Part 2 — 개인 AI 업무환경 구축", en: "Part 2 — Building Your Personal AI Work Environment" },
		chapters: ["AW-CH04", "AW-CH05", "AW-CH06", "AW-CH07"],
	},
	{
		dir: "part-3",
		label: { ko: "Part 3 — AI와 업무자료 활용", en: "Part 3 — Working with AI and Your Documents" },
		chapters: ["AW-CH08", "AW-CH09", "AW-CH10", "AW-CH11"],
	},
	{
		dir: "part-4",
		label: { ko: "Part 4 — 운영과 완성", en: "Part 4 — Operating and Completing Your Workspace" },
		chapters: ["AW-CH12", "AW-CH13", "AW-CH14"],
	},
	{
		dir: "optional",
		label: { ko: "선택·심화", en: "Optional / Advanced" },
		chapters: ["AW-OP01", "AW-OP02", "AW-OP03"],
	},
];

export function loadManifest() {
	const raw = JSON.parse(readFileSync(join(REPO_ROOT, "content-manifest.json"), "utf8"));
	return raw.entries;
}

// "AW-CH01" -> "CH01"
export function fileStem(chapterId) {
	return chapterId.replace(/^AW-/, "");
}

export function partOf(chapterId) {
	return PARTS.find((p) => p.chapters.includes(chapterId));
}

export function isEnglishEnabled(entries) {
	return entries.some((e) => e.language === "en" && EN_RELEASABLE.includes(e.status));
}

export function enabledLocales(entries) {
	return isEnglishEnabled(entries) ? ["ko", "en"] : ["ko"];
}
