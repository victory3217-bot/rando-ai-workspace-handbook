import { defineCollection } from "astro:content";
import { docsLoader, i18nLoader } from "@astrojs/starlight/loaders";
import { docsSchema, i18nSchema } from "@astrojs/starlight/schema";

export const collections = {
	docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
	// Starlight reads this optional collection at build time to look for custom UI
	// strings (src/content/i18n/<lang>.json). Declaring it keeps the build log clean.
	i18n: defineCollection({ loader: i18nLoader(), schema: i18nSchema() }),
};
