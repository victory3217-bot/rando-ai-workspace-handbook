import { defineRouteMiddleware } from '@astrojs/starlight/route-data';
import { getCollection } from 'astro:content';

const base = import.meta.env.BASE_URL.replace(/\/$/, '');
const docs = await getCollection('docs', ({ data }) => import.meta.env.MODE !== 'production' || data.draft === false);
const existing = new Set(docs.map((d) => d.id.replace(/\/index$/, '')));

type SidebarEntry = { type: 'link' | 'group'; entries?: SidebarEntry[] };

// Drop sidebar groups that have no pages in the current language (for example a Part whose
// chapters are not published in English yet), so the contents list shows approved pages only.
function withoutEmptyGroups(entries: SidebarEntry[]): SidebarEntry[] {
	return entries
		.map((entry) => (entry.type === 'group' ? { ...entry, entries: withoutEmptyGroups(entry.entries ?? []) } : entry))
		.filter((entry) => entry.type !== 'group' || (entry.entries?.length ?? 0) > 0);
}

export const onRequest = defineRouteMiddleware((context) => {
	const route = context.locals.starlightRoute;

	// Starlight adds <link rel="alternate" hreflang="..."> for every configured language, whether or
	// not the page exists in that language. Keep only the alternates that point to a real page.
	route.head = route.head.filter((tag) => {
		if (tag.tag !== 'link' || tag.attrs?.rel !== 'alternate' || !tag.attrs?.hreflang) return true;
		const pathname = new URL(String(tag.attrs.href)).pathname;
		const id = pathname.slice(base.length).replace(/^\/|\/$/g, '');
		return existing.has(id);
	});

	route.sidebar = withoutEmptyGroups(route.sidebar as SidebarEntry[]) as typeof route.sidebar;
});
