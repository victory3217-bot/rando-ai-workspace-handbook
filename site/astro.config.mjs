import { existsSync } from "node:fs";
import { join } from "node:path";
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import {
	SITE_ROOT,
	SITE_URL,
	BASE,
	HANDBOOK_TITLE,
	PARTS,
	EXTRA_GROUPS,
	loadManifest,
	enabledLocales,
} from "./handbook.config.mjs";

const entries = loadManifest();
const locales = enabledLocales(entries);
// Korean is always a superset of English (enforced by the audit), so with two locales English is the
// Starlight default: Starlight only creates fallback pages FROM the default locale TO the others.
const defaultLocale = locales.includes("en") ? "en" : "ko";

// Starlight is only told about a locale once that locale has releasable
// content. With a single configured locale no /en/ route exists at all, and
// Starlight cannot serve Korean text under an English URL as "fallback".
const localeConfig = {
	ko: { label: "한국어", lang: "ko" },
	en: { label: "English", lang: "en" },
};
const configuredLocales = Object.fromEntries(locales.map((l) => [l, localeConfig[l]]));
const title = Object.fromEntries(locales.map((l) => [l, HANDBOOK_TITLE[l]]));

// A sidebar group is shown only if the sync step generated at least one chapter
// page for it, so unwritten parts do not appear as empty groups.
const generatedChapters = join(SITE_ROOT, "src", "content", "docs", "ko", "chapters");
const chapterSidebar = PARTS.filter((p) => existsSync(join(generatedChapters, p.dir))).map((p) => ({
	label: p.label[defaultLocale],
	translations: Object.fromEntries(locales.filter((l) => l !== defaultLocale).map((l) => [l, p.label[l]])),
	items: [{ autogenerate: { directory: `chapters/${p.dir}` } }],
}));

// Workshop materials, reference pages and the instructor guide (Korean only). Shown only if the sync
// step generated them; the instructor group is collapsed so answers are not in view by default.
const generatedKo = join(SITE_ROOT, "src", "content", "docs", "ko");
const extraSidebar = EXTRA_GROUPS.filter((g) => existsSync(join(generatedKo, g.dir))).map((g) => ({
	label: g.label[defaultLocale],
	translations: Object.fromEntries(locales.filter((l) => l !== defaultLocale).map((l) => [l, g.label[l]])),
	collapsed: g.collapsed === true,
	items: [{ autogenerate: { directory: g.dir } }],
}));

export default defineConfig({
	site: SITE_URL,
	base: BASE,
	integrations: [
		starlight({
			title,
			defaultLocale,
			locales: configuredLocales,
			components: {
				Banner: "./src/components/HandbookBanner.astro",
				LanguageSelect: "./src/components/LanguageSelect.astro",
			},
			routeMiddleware: "./src/route-data.ts",
			customCss: ["./src/styles/custom.css"],
			// Public site: general pages are indexable. Only the instructor guide pages (which contain the
			// answers) carry their own noindex tag; see EXTRA_PAGES and scripts/sync-content.mjs.
			sidebar: [...chapterSidebar, ...extraSidebar],
		}),
	],
});
