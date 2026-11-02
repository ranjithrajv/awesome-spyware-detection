# Spyware check: a one-page guide

A free, print-ready handout for trainers, helplines, newsrooms, and anyone advising a person who may be targeted. Copy, translate, and redistribute without permission — CC0 1.0.

Full list and updates: <https://github.com/ranjithrajv/awesome-spyware-detection>

---

## 1. Before you scan

- **Do not tip off the operator.** Do not reset, reinstall, or "clean" the device first, and do not discuss the suspicion on the device.
- **Preserve evidence.** Take a backup or forensic acquisition before changing settings or removing apps.
- **Use more than one tool.** Tools cover different platforms and indicator sets.
- **Get human help early.** A helpline can advise on safety planning, not just forensics.

## 2. Pick a tool

| Situation | Tool | Needs |
|---|---|---|
| iPhone or Android, suspected mercenary spyware | [MVT](https://github.com/mvt-project/mvt) | A computer, Python, a backup |
| Fast first pass across phone or computer | [Zero-Breach Toolkit](https://github.com/interplains/Zero-Breach-Toolkit) | Double-click app |
| Android stalkerware, no root | [spytrap-adb](https://github.com/spytrap-org/spytrap-adb) | USB debugging |
| Ongoing monitoring of a device on your Wi-Fi | [SpyGuard](https://github.com/SpyGuard/SpyGuard) | A small Debian host |

## 3. Read the results honestly

- **A hit is not proof.** Shared infrastructure and preinstalled apps cause benign matches.
- **Check the timing.** A match outside the suspected window is weak evidence.
- **Corroborate.** Device forensics, network captures, and account logs together are stronger than one tool.
- **A clean scan is not a clean device.** Targeted implants often leave no public indicators.
- **Do not accuse anyone publicly** based on a single tool's output.

## 4. Get help

- **Access Now Digital Security Helpline** — free, 24/7, many languages: <https://www.accessnow.org/help/>
- **Amnesty Security Lab** — support for targeted individuals: <https://securitylab.amnesty.org/get-help/>
- **Coalition Against Stalkerware** — guidance and local support: <https://stopstalkerware.org/>
- **Digital First Aid Kit** — guided self-help: <https://digitalfirstaid.org/>

---

*Detection is probabilistic. No tool and no scan can guarantee that a device is clean. This handout is not legal advice.*
