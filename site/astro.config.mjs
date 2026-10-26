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
	loadManifest,
	enabledLocales,
} from "./handbook.config.mjs";

const entries = loadManifest();
const locales = enabledLocales(entries);

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
	label: p.label.ko,
	translations: { en: p.label.en },
	items: [{ autogenerate: { directory: `chapters/${p.dir}` } }],
}));

export default defineConfig({
	site: SITE_URL,
	base: BASE,
	integrations: [
		starlight({
			title,
			defaultLocale: "ko",
			locales: configuredLocales,
			components: { Banner: "./src/components/HandbookBanner.astro" },
			customCss: ["./src/styles/custom.css"],
			// Unpublished draft: keep out of search engines. Remove this line when the
			// handbook is approved for public release.
			head: [{ tag: "meta", attrs: { name: "robots", content: "noindex, nofollow" } }],
			sidebar: chapterSidebar,
		}),
	],
});
