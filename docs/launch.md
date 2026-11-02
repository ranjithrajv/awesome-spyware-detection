# Launch kit

A channel-by-channel plan for launching the list with the comparison matrix and the handout as the hook. Posting is manual: there are no accounts or APIs wired up here, and this kit deliberately avoids automation and vote requests.

## Pre-flight

- [ ] CI green: index freshness, `awesome-lint`, link check.
- [ ] Handout rendered and printed once to check pagination.
- [ ] `docs/outreach.md` ready for direct sends.
- [ ] `CITATION.cff` present for researchers.
- [ ] Maintainer affiliation disclosed in every post.

## Assets

| Asset | Use |
|---|---|
| Comparison matrix | The hook: "which tool do I run?" |
| Handout (`docs/handout.md`) | The artefact people save and share |
| "Reading the results" | The differentiator: anti-overclaiming |
| `data/index.json` / `llms.txt` | For tool builders and agents |

## Hacker News

**Format:** `Show HN: Spyware detection tools and the caveats that matter`

Rules and tactics:

- Post as a maker: this is something you built and maintain.
- Tuesday–Thursday, 08:00–10:00 US Eastern tends to get more eyes; avoid weekends.
- No "please upvote", no voting rings, no link shorteners.
- Be present for the first three hours. Answer technical questions with specifics, not marketing.
- Expect the strongest pushback on: false positives, "this is just a link list", and vendor naming. Answer with the matrix, the primary sources, and the false-positive section.

First comment draft:

> I kept seeing the same problem: people find a spyware story, download one tool, get a clean result, and conclude they are safe. This list puts the tools next to what each one can actually examine, plus a one-page handout for trainers and helplines.
>
> Two things I would particularly like feedback on: which Windows and macOS stalkerware resources are missing, and whether the "a hit means" column is honest enough.

## r/netsec

r/netsec is technical and strict about self-promotion. A bare link to a list may be removed.

- Frame it as a technical resource with original analysis: the false-positive mechanics, indicator lifetime, and why device backups are not proof.
- Put the substance in the post body; link the repo once.
- Check the current subreddit rules before posting; if a resource must go in a weekly thread, use that instead.
- Disclose that you maintain it.

**Title:** `Spyware detection: what each tool can and cannot prove`

## r/privacy

- Text post, not a link post.
- Lead with the practical handout, then the repo.
- Read the self-promotion rules; some weeks only allow resource posts.
- Expect questions about commercial tools and affiliate links: state plainly that there are none.

**Title:** `A free one-page guide to checking a phone for spyware (and why a clean scan is not proof)`

## OSINT communities

- **r/OSINT**: frame around investigative use, chain of custody, and corroboration. Do not present it as a hacking toolkit.
- **OSINT Curious and similar Slack/Discord spaces**: ask a moderator before posting; these are communities, not billboards.
- **Bellingcat Discord and similar**: same rule — ask first, contribute in discussion, link only when relevant.

**Title:** `Spyware exposure investigations: tooling, indicators, and the corroboration step`

## Sequence

1. Day 1: r/privacy and r/OSINT (lower risk, useful feedback).
2. Day 2: Hacker News `Show HN`.
3. Day 3: r/netsec if the first two went well and the rules allow it.
4. Week 2: direct outreach to trainers and helplines (`docs/outreach.md`).
5. Week 4: reassess; do not repost the same link in the same community.

## Comment bank

| Question | Answer |
|---|---|
| "Is this reliable?" | No single tool is. The list explains what each tool examines and why a clean scan is not proof. |
| "Why isn't vendor X included?" | Inclusion is not endorsement; send a PR with verification and it will be reviewed against the criteria. |
| "Isn't this helping stalkers?" | The list is defensive-only and excludes offensive tooling. Detection guidance is already public in vendor and NGO reports. |
| "Do you have proof it works?" | The tools are independently maintained; this list verifies links and structure, not the efficacy of each tool. |
| "Why CC0?" | So trainers, translators, and helplines can reuse it without legal friction. |

## What not to do

- Do not ask for upvotes, shares, or stars.
- Do not post the same link to five subreddits in an hour.
- Do not DM at-risk individuals; route through support organizations.
- Do not claim endorsement by Citizen Lab, Amnesty, or any listed project.
- Do not argue with removal decisions; ask what would make it acceptable.

## Execution log

| Date | Channel | Outcome |
|---|---|---|
| 2026-11-03 | r/OSINT | **Posted, then removed** — https://old.reddit.com/r/OSINT/comments/1xm5kd5/ ; "Tool" flair applied, removal reason not public |
| 2026-11-03 | r/privacy | **Skipped** — R3 bans all self-promotion; posting would risk a ban |
| 2026-11-03 | Hacker News | **Blocked by HN** — Show HN temporarily restricted; `/submit` redirected to `/showlim`. No post made. |

r/privacy needs a different approach: a third-party write-up, or contributing the handout to a thread where it answers an existing question. Do not repost the repo there.

HN's `/showlim` notice says Show HNs are temporarily restricted because of submission volume. Do not work around it by reposting the same link as a regular story; wait, contribute normally, and retry later. The submission copy stays ready in this file.

### r/OSINT follow-up

Do not repost. Send modmail once and ask for the reason, offering to fix the post:

> Hi mods — I posted a free, CC0 resource on spyware-detection tooling and it was removed. I had applied the Tool flair and disclosed that I maintain it. Could you tell me which rule it fell under, and whether a revised post would be welcome? Happy to keep it out of the sub if it is not a fit. Thanks.
