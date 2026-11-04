# Contributing

Thanks for helping make this list better. The goal is a **defensive** resource: tools and reporting that help people detect, investigate, and expose spyware — not build it.

## What belongs here

Include a resource if it is:

- **Relevant** — it helps detect, analyze, investigate, or expose spyware, stalkerware, or commercial surveillance.
- **Useful** — it works, it is documented, and it is not a placeholder or an abandoned proof of concept.
- **Accessible** — freely available where possible. Commercial products are acceptable only when they are a de-facto standard and clearly labeled.
- **Primary** — link to the original project, report, or maintainer rather than a blog rewrite.

Do **not** submit:

- Spyware, stalkerware, RATs, keyloggers, or "FUD" builders, even for research.
- Unverified indicator dumps or scraped lists with no provenance.
- Marketing pages, affiliate links, or SEO content farms.
- Duplicates of an existing entry.

## Format

Add entries to the most relevant section, in **alphabetical order** by the displayed name:

```markdown
- [Name](https://example.com) — One sentence, plain language, no marketing adjectives.
```

Guidelines for the description:

- Start with a capital letter and end with a period.
- Say what it does and who it is for, not how great it is.
- Mention the platform when it is not obvious: `(Android, iOS)`, `(macOS)`.

## Tags

Use only these trailing tags, and only when they matter to a reader deciding whether to use the tool:

| Tag | Meaning |
|---|---|
| `(archived)` | The upstream repository is archived. |
| `(unmaintained)` | No commit or release in two or more years. |
| `(niche)` | Small community script with limited support. |
| `(commercial)` | Closed source or paid. |
| `(requires root)` | Needs root or jailbreak for its main functionality. |
| `(beta)` | Pre-1.0 or experimental; interfaces may change. |

Do not use tags as a substitute for a description. If a tool is unmaintained but still uniquely useful, keep it and add `(unmaintained)` rather than deleting it. Remove entries only when they no longer work at all or have been fully superseded.

## Submitting

1. Fork the repository and create a branch.
2. Make your change, keeping the diff focused.
3. If you added, removed, or edited an entry, regenerate the machine-readable exports and commit them:
   ```sh
   node scripts/build-index.mjs
   ```
   This updates `data/index.json` and `llms.txt`; CI fails if they are out of date.
4. Open a pull request that explains **why** the resource is useful and how you verified it.
5. If you maintain the linked project, say so.

## Review criteria

Maintainers check that links resolve, descriptions are accurate, and the resource fits the scope above. Dead links are removed; if a project is archived, it may stay only if it remains uniquely useful, marked as archived.

## Code of conduct

Be respectful and assume good faith. This list deals with surveillance of real people; do not post victim identities, private data, or unfounded accusations. When in doubt, link to published, attributable reporting.
