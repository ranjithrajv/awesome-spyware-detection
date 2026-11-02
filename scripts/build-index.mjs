#!/usr/bin/env node
/**
 * Builds machine-readable views of the list from README.md:
 *   - data/index.json  structured entries for tools and agents
 *   - llms.txt         llmstxt.org-style plain text index
 *
 * Deterministic: output depends only on README.md, so CI can diff it.
 */

import { readFile, writeFile, mkdir } from "node:fs/promises";
import { dirname, join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname;
const README = join(ROOT, "README.md");

const ENTRY = /^- \[(.+?)\]\((https?:\/\/[^\s)]+)\)\s+-\s+(.+)$/;
const ENTRY_WITH_TAG = /^(.*?)\s+\(([^()]+)\)\s*$/;

function slug(text) {
  return text
    .toLowerCase()
    .replace(/[^\p{L}\p{N}\s-]/gu, "")
    .trim()
    .replace(/\s+/g, "-");
}

function splitTags(description) {
  const match = description.match(ENTRY_WITH_TAG);
  if (!match) return { description, tags: [] };

  const tags = match[2]
    .split(",")
    .map((tag) => tag.trim().toLowerCase())
    .filter(Boolean);

  return { description: match[1].trim(), tags };
}

const markdown = await readFile(README, "utf8");
const lines = markdown.split("\n");

const sections = [];
let section = null;
let subsection = null;
let lastReviewed = null;

for (const line of lines) {
  const reviewed = line.match(/Last reviewed:\s*(\d{4}-\d{2}-\d{2})/);
  if (reviewed) lastReviewed = reviewed[1];

  const h2 = line.match(/^## (.+)$/);
  if (h2) {
    section = { title: h2[1].trim(), slug: slug(h2[1]), items: [], subsections: [] };
    sections.push(section);
    subsection = null;
    continue;
  }

  const h3 = line.match(/^### (.+)$/);
  if (h3 && section) {
    subsection = { title: h3[1].trim(), slug: slug(h3[1]), items: [] };
    section.subsections.push(subsection);
    continue;
  }

  const entry = line.match(ENTRY);
  if (!entry || !section) continue;

  const { description, tags } = splitTags(entry[3].trim());
  const item = { name: entry[1].trim(), url: entry[2].trim(), description, tags };

  (subsection ?? section).items.push(item);
}

// Keep only sections that actually contain entries.
const CONTENT_SECTIONS = sections
  .filter((s) => !["contents", "contributing"].includes(s.slug))
  .map((s) => ({ ...s, subsections: s.subsections.filter((sub) => sub.items.length > 0) }))
  .filter((s) => s.items.length > 0 || s.subsections.length > 0);

const count = CONTENT_SECTIONS.reduce(
  (total, s) => total + s.items.length + s.subsections.reduce((n, sub) => n + sub.items.length, 0),
  0,
);

const index = {
  name: "Awesome Spyware Detection",
  description:
    "A curated list of tools, indicators, investigations, and resources for detecting and exposing spyware and stalkerware.",
  repository: "https://github.com/ranjithrajv/awesome-spyware-detection",
  license: "CC0-1.0",
  last_reviewed: lastReviewed,
  count,
  tag_legend: {
    archived: "Upstream repository is archived.",
    unmaintained: "No commit or release in two or more years.",
    niche: "Small community script with limited support.",
    commercial: "Closed source or paid.",
    "requires root": "Needs root or jailbreak for its main functionality.",
  },
  sections: CONTENT_SECTIONS.map((s) => ({
    title: s.title,
    slug: s.slug,
    items: s.items,
    ...(s.subsections.length
      ? {
          subsections: s.subsections.map((sub) => ({
            title: sub.title,
            slug: sub.slug,
            items: sub.items,
          })),
        }
      : {}),
  })),
};

function renderEntries(items, { indent = "" } = {}) {
  return items
    .map((item) => {
      const tags = item.tags.length ? ` (${item.tags.join(", ")})` : "";
      return `${indent}- [${item.name}](${item.url}): ${item.description}${tags}`;
    })
    .join("\n");
}

const llms = [
  "# Awesome Spyware Detection",
  "",
  "> " + index.description,
  "",
  "A defensive, curated list for detecting and exposing spyware and stalkerware: detection tools, forensic acquisition, DFIR at scale, indicators, investigations, legal and policy context, and academic research.",
  "",
  "Machine-readable index: https://github.com/ranjithrajv/awesome-spyware-detection/blob/main/data/index.json",
  "",
  ...CONTENT_SECTIONS.flatMap((s) => {
    const out = [`## ${s.title}`, ""];
    if (s.items.length) out.push(renderEntries(s.items), "");
    for (const sub of s.subsections) {
      out.push(`### ${sub.title}`, "", renderEntries(sub.items), "");
    }
    return out;
  }),
  "## Metadata",
  "",
  `- Repository: ${index.repository}`,
  `- License: ${index.license}`,
  `- Entries: ${index.count}`,
  `- Last reviewed: ${index.last_reviewed ?? "unreleased"}`,
  "",
].join("\n");

await mkdir(dirname(join(ROOT, "data/index.json")), { recursive: true });
await writeFile(join(ROOT, "data/index.json"), JSON.stringify(index, null, 2) + "\n", "utf8");
await writeFile(join(ROOT, "llms.txt"), llms, "utf8");

console.log(`Wrote data/index.json and llms.txt (${index.count} entries, ${CONTENT_SECTIONS.length} sections)`);
