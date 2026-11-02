# Discovery

Where the list is submitted, what is possible today, and the exact text to paste. Status as of 2026-11-02.

## Status

| Directory | Type | Method | Status | Notes |
|---|---|---|---|---|
| [Cugu/awesome-forensics](https://github.com/Cugu/awesome-forensics) | Awesome list | Pull request | **Open** — [#154](https://github.com/cugu/awesome-forensics/pull/154) | Added under Related Awesome Lists, alphabetically after Social Engineering |
| [rshipp/awesome-malware-analysis](https://github.com/rshipp/awesome-malware-analysis) | Awesome list | Pull request | **Blocked** | Interactions restricted to collaborators; revisit later |
| [llmstxt.site](https://llmstxt.site/submit) | llms.txt directory | Web form | **Submitted 2026-11-02** | Awaiting listing; submitted under the maintainer's GitHub identity |
| [llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub) | llms.txt directory | Web form / manual PR | **Open** — [#2286](https://github.com/thedaviddias/llms-txt-hub/pull/2286) | Web form requires GitHub sign-in, so the documented manual-PR path was used |
| [awesome.re](https://github.com/sindresorhus/awesome) | Awesome index | Pull request | **Blocked until 2026-12-02** | 30-day maturity rule, and PRs are temporarily disabled |
| GitHub topics | Discovery | Done | **Live** | awesome-list, spyware, stalkerware, forensics, pegasus, privacy, ios, android |

## llms.txt directory submissions

Use these values in the forms. Do not add tracking parameters.

| Field | Value |
|---|---|
| Name | Awesome Spyware Detection |
| URL | `https://github.com/ranjithrajv/awesome-spyware-detection` |
| llms.txt | `https://github.com/ranjithrajv/awesome-spyware-detection/blob/main/llms.txt` |
| JSON index | `https://github.com/ranjithrajv/awesome-spyware-detection/blob/main/data/index.json` |
| Category | Security / Developer Tools |
| Description | Curated, CC0-licensed resources for detecting and exposing spyware and stalkerware, including a comparison matrix, false-positive guidance, and a printable handout. |
| License | CC0-1.0 |

Note for reviewers: the repository is a content list, not a web application. `llms.txt` uses the llmstxt.org format and links to the canonical Markdown files.

## awesome.re submission

Eligibility and process, verified against `sindresorhus/awesome` on 2026-11-02:

- [ ] **At least 30 days old** — created 2026-11-02, eligible **2026-12-02**.
- [x] Awesome badge in the README.
- [x] `awesome-lint` passes in CI.
- [x] CC0 license.
- [ ] **PRs re-enabled** — currently disabled by the maintainer.
- [ ] **Review at least 4 other open PRs** — required, and "looks good" does not count.
- [ ] One commit per suggestion, no draft PR, no AI-generated PR.
- [ ] Entry at the bottom of the **Security** category, URL ending in `#readme`.
- [ ] PR title `Add Spyware Detection` (no "Awesome", no "Update readme").

Entry to add:

```markdown
- [Spyware Detection](https://github.com/ranjithrajv/awesome-spyware-detection#readme) - Detecting and exposing spyware and stalkerware.
```

Before submitting, re-read `create-list.md` and `pull_request_template.md`; both change over time.

## Other places worth considering

| Target | Why | Caution |
|---|---|---|
| `hslatman/awesome-threat-intelligence` | Indicator and CTI overlap | Only if a related-lists section exists; one PR at a time |
| `meirwah/awesome-incident-response` | DFIR audience | Same |
| `ashishb/osx-and-ios-security-awesome` | iOS/macOS tooling overlap | Check whether lists are accepted |
| Newsroom security newsletters | Practitioner audience | Pitch as a handout, not a link drop |
| Digital-security training calendars | Workshop material | Use `docs/outreach.md` |

Do not open more than one submission per directory, and wait for a response before following up.

## Tracking

Record every submission in `docs/impact.md` with date, target, and outcome. If a PR is rejected, note the stated reason and whether the list can be adjusted.
