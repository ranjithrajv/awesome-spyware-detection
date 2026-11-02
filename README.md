# Awesome Spyware Detection [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, indicators, investigations, and resources for detecting and exposing spyware and stalkerware.

Spyware is no longer a niche threat. Mercenary products such as Pegasus, Predator, and Graphite are sold to governments, while consumer-grade stalkerware is a few clicks and a credit card away. This list collects the open-source tooling, forensic methodology, and primary-source reporting needed to **find it, prove it, and talk about it**.

Detection is probabilistic. A clean scan means "no known indicators found", not "not infected". Treat every entry here as a starting point, not a verdict.

**Tags:** `(archived)` upstream is archived · `(unmaintained)` no commits or releases in 2+ years · `(niche)` small community script · `(commercial)` closed source · `(requires root)` privileged access needed.

**For trainers and helplines:** a print-ready [one-page handout](docs/handout.md). **For tools and agents:** [data/index.json](data/index.json) and [llms.txt](llms.txt).

## Contents

- [If you suspect you are infected](#if-you-suspect-you-are-infected)
- [Choose a detection tool](#choose-a-detection-tool)
- [Mobile detection and triage](#mobile-detection-and-triage)
- [Forensic acquisition and analysis](#forensic-acquisition-and-analysis)
- [DFIR at scale](#dfir-at-scale)
- [Stalkerware](#stalkerware)
- [Network-level detection](#network-level-detection)
- [Desktop and endpoint](#desktop-and-endpoint)
- [Reverse engineering and malware analysis](#reverse-engineering-and-malware-analysis)
- [Indicators and threat intelligence](#indicators-and-threat-intelligence)
- [Exposés and investigations](#exposés-and-investigations)
- [Legal and policy](#legal-and-policy)
- [Organizations and victim support](#organizations-and-victim-support)
- [Research and methodology](#research-and-methodology)
- [Academic research](#academic-research)
- [Related awesome lists](#related-awesome-lists)

## If you suspect you are infected

**Do not tip off the operator.** Avoid reinstalling, resetting, or "cleaning" the device before you have preserved evidence, and avoid discussing the suspicion on the device itself.

**Preserve first.** Take a forensic backup or acquisition before changing anything; see the forensic acquisition section below.

**Scan with more than one tool.** Different tools cover different indicator sets and platforms.

**Get human help.** Contact a digital-security helpline; they can advise on safety planning as well as forensics.

### Reading the results

**A matching indicator is not proof.** Shared hosting, CDNs, and preinstalled apps produce benign matches.

**Timestamps matter.** A hit outside the suspected compromise window is weak evidence.

**Corroborate across independent sources.** Device forensics, network captures, and account logs together are stronger than any single tool.

**Backups contain residue** from previous devices and accounts.

**Secondary reporting recycles indicators.** Check the primary report before acting on a list.

**A clean scan is not a clean device.** Zero-days and targeted implants often leave no public indicators.

**Never make public accusations** from a single tool's output.

## Choose a detection tool

| Tool                    | Platforms                           | What it examines                                             | Requirements                  | A hit means                                | Best for                        |
| ----------------------- | ----------------------------------- | ------------------------------------------------------------ | ----------------------------- | ------------------------------------------ | ------------------------------- |
| **MVT**                 | Android, iOS                        | Backups, full-system dumps, indicators, device configuration | Python; no root for backups   | A known indicator that needs corroboration | Deep forensic triage            |
| **Zero-Breach Toolkit** | Android, iOS, Windows, macOS, Linux | Traces of known mercenary spyware                            | Double-click app              | An indicator match                         | Fast, guided first pass         |
| **SpyGuard**            | Any device on your Wi-Fi            | Network flows such as DNS and TLS                            | Debian-like host or appliance | Suspicious traffic                         | Ongoing network monitoring      |
| **PhoneHackScan**       | Android, iPhone                     | Guided device checks                                         | Python 3.10 or newer          | A suspicious artifact                      | Consumer self-check             |
| **spytrap-adb**         | Android                             | Installed apps, permissions, device configuration            | USB debugging                 | A suspicious app or setting                | Stalkerware checks without root |
| **sentinel**            | Windows, Linux, macOS               | Files, processes, persistence, configuration                 | Read-only Rust binary         | A rule match                               | Broad offline sweep             |

No tool on this list can prove a device is clean. Read the notes above on reading results before acting on any output.

## Mobile detection and triage

- [Mobile Verification Toolkit (MVT)](https://github.com/mvt-project/mvt) - Amnesty International's forensic toolkit for indicators of compromise on Android and iOS. The de-facto standard.
- [mvt2timesketch](https://github.com/haxrob/mvt2timesketch) - Converts MVT output into a Timesketch-compatible timeline. (niche)
- [PhoneHackScan](https://github.com/UCYBERS/PhoneHackScan) - Android and iPhone intrusion check with a guided workflow.
- [SpyGuard](https://github.com/SpyGuard/SpyGuard) - Network-flow monitoring for signs of compromise, built on Suricata and usable as a kiosk.
- [Zero-Breach Toolkit](https://github.com/interplains/Zero-Breach-Toolkit) - Double-click check for traces of mercenary spyware such as Pegasus, Predator, Graphite, and Candiru.

## Forensic acquisition and analysis

- [ALEAPP](https://github.com/abrignoni/ALEAPP) - Android Logs Events And Protobuf Parser for building timelines from device data.
- [androidqf](https://github.com/mvt-project/androidqf) - Android Quick Forensics: fast, structured evidence collection from a device without root.
- [iLEAPP](https://github.com/abrignoni/iLEAPP) - iOS Logs, Events, And Plist Parser for building a timeline from a full file-system or backup.
- [libimobiledevice](https://github.com/libimobiledevice/libimobiledevice) - Cross-platform library for talking to iOS devices, including the backups MVT analyzes.
- [pymobiledevice3](https://github.com/doronz88/pymobiledevice3) - Pure-Python iDevice stack for backups, sysdiagnose, crash logs, and on-device service access.

## DFIR at scale

- [Artemis](https://github.com/puffyCid/artemis) - Cross-platform forensic artifact collector and parser written in Rust.
- [Chainsaw](https://github.com/WithSecureOpenSource/chainsaw) - Rapid search and hunting through Windows forensic artifacts.
- [Forensic Artifacts](https://github.com/ForensicArtifacts/artifacts) - Shared repository of digital-forensic artifact definitions.
- [Hayabusa](https://github.com/Yamato-Security/hayabusa) - Sigma-based threat hunting and fast Windows event-log timelines.
- [IRIS](https://github.com/dfir-iris/iris-web) - Collaborative incident-response and case-management platform.
- [Plaso](https://github.com/log2timeline/plaso) - Super-timeline engine that normalizes artifacts from many sources.
- [Timesketch](https://github.com/google/timesketch) - Collaborative forensic timeline analysis.
- [Velociraptor](https://github.com/Velocidex/velociraptor) - Endpoint visibility and DFIR collection at fleet scale.

## Stalkerware

- [android-stalkerware](https://github.com/diskurse/android-stalkerware) - Technical write-ups and sample analysis of Android stalkerware families. (unmaintained)
- [Coalition Against Stalkerware](https://stopstalkerware.org/) - Practical guidance, risk assessment, and a directory of support organizations.
- [MVT-PCAPDroid](https://github.com/BARGHEST-ngo/MVT-PCAPDroid) - Flattens MVT indicators for use with PCAPdroid's DNS and traffic views. (niche)
- [spytrap-adb](https://github.com/spytrap-org/spytrap-adb) - Tests a phone for stalkerware over ADB and USB debugging, no root required.
- [stalkerware-indicators](https://github.com/AssoEchap/stalkerware-indicators) - Community-maintained indicators for stalkerware apps, including package names and certificates.

## Network-level detection

### Traffic capture and analysis

- [PCAPdroid](https://github.com/emanuele-f/PCAPdroid) - No-root network monitor, firewall, and PCAP dumper for Android.
- [Suricata](https://github.com/OISF/suricata) - IDS/IPS engine for signature-based network detection.
- [Wireshark](https://github.com/wireshark/wireshark) - Packet analysis for inspecting captured traffic.
- [Zeek](https://github.com/zeek/zeek) - Network security monitor that produces high-level connection and protocol logs.

### DNS filtering and tracker blocking

- [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) - Network-wide DNS filtering with per-client query logging.
- [Exodus Privacy](https://github.com/Exodus-Privacy/exodus) - Platform for auditing trackers bundled in Android applications.
- [Pi-hole](https://github.com/pi-hole/pi-hole) - DNS sinkhole for blocking known command-and-control and telemetry domains.
- [RethinkDNS](https://github.com/celzero/rethink-app) - DNS-over-HTTPS, DNS-over-Tor, WireGuard proxying, firewall, and connection tracking on Android.
- [TrackerControl](https://github.com/TrackerControl/tracker-control-android) - Monitors and blocks trackers and ads per app.

### Cell-site and IMSI detection

- [Android IMSI-Catcher Detector](https://github.com/CellularPrivacy/Android-IMSI-Catcher-Detector) - Detects IMSI catchers, StingRays, and silent SMS on Android.
- [Rayhunter](https://github.com/EFForg/rayhunter) - Low-cost cell-site-simulator detection built on a mobile hotspot.
- [SnoopSnitch](https://github.com/srlabs/snoopsnitch) - Baseband analysis for IMSI catchers and suspicious network behavior. (unmaintained, Qualcomm)

## Desktop and endpoint

- [BlockBlock](https://github.com/objective-see/BlockBlock) - Monitors persistence locations on macOS and alerts when something installs itself.
- [ClamAV](https://github.com/Cisco-Talos/clamav) - Open-source antivirus engine, useful for scanning acquired files and mail.
- [DoNotDisturb](https://github.com/objective-see/DoNotDisturb) - Detects physical-access tampering with a Mac.
- [KnockKnock](https://github.com/objective-see/KnockKnock) - Enumerates persistently installed software on macOS, AutoRuns-style.
- [LuLu](https://github.com/objective-see/LuLu) - Free, open-source macOS firewall with per-process outbound visibility.
- [Lynis](https://github.com/CISOfy/lynis) - Security auditing tool for Unix-like systems, including persistence and configuration checks.
- [osquery](https://github.com/osquery/osquery) - SQL-powered endpoint instrumentation for hunting suspicious processes, launch items, and network state.
- [OverSight](https://github.com/objective-see/OverSight) - Alerts when the Mac microphone or camera is activated.
- [privacy.sexy](https://github.com/undergroundwires/privacy.sexy) - Script generator that enforces privacy and hardening baselines on Windows, macOS, and Linux.
- [ReiKey](https://github.com/objective-see/ReiKey) - Detects persistent keyboard event taps used by keyloggers. (unmaintained)
- [sentinel](https://github.com/jamixm4-crypto/sentinel) - Offline, read-only scanner for keyloggers, stalkerware, RATs, and monitoring agents.
- [sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) - High-quality Sysmon configuration template for Windows event tracing.
- [TaskExplorer](https://github.com/objective-see/TaskExplorer) - Explores running processes, signatures, and loaded libraries on macOS.
- [WindowsSpyBlocker](https://github.com/crazy-max/WindowsSpyBlocker) - Blocks Windows telemetry and spying endpoints.

## Reverse engineering and malware analysis

### Android app analysis

- [androguard](https://github.com/androguard/androguard) - Python library for reverse engineering and analyzing Android applications.
- [APKiD](https://github.com/rednaga/APKiD) - Identifies packers, protectors, and obfuscators in Android apps.
- [Apktool](https://github.com/iBotPeaches/Apktool) - Reverse engineering of Android APK files.
- [diffuse](https://github.com/JakeWharton/diffuse) - Diffs two APK or AAB files, ideal for spotting what changed in a spyware update.
- [jadx](https://github.com/skylot/jadx) - Dex-to-Java decompiler.
- [Quark-Engine](https://github.com/ev-flow/quark-engine) - Android malware scoring engine based on behavioral patterns.

### iOS app analysis

- [frida-ios-dump](https://github.com/AloneMonkey/frida-ios-dump) - Pulls decrypted IPAs from a jailbroken device for analysis.
- [Grapefruit](https://github.com/ChiChou/grapefruit) - Open-source iOS and Android security testing suite, formerly Passionfruit.

### Runtime instrumentation

- [Frida](https://github.com/frida/frida) - Dynamic instrumentation toolkit for runtime inspection on Android and iOS.
- [House](https://github.com/nccgroup/house) - Runtime mobile analysis toolkit with a web GUI. (unmaintained)
- [Medusa](https://github.com/Ch0pin/medusa) - Modular mobile application analysis framework.
- [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) - Automated static and dynamic analysis for Android, iOS, and Windows apps.
- [objection](https://github.com/sensepost/objection) - Runtime mobile exploration built on Frida, with scripted checks for common weaknesses.
- [RMS](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security) - Web interface for manipulating Android and iOS apps at runtime.

### Native and binary analysis

- [capa](https://github.com/mandiant/capa) - Identifies capabilities in executables, including spyware loaders and droppers.
- [FLOSS](https://github.com/mandiant/flare-floss) - Extracts obfuscated strings from malware automatically.
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) - Software reverse engineering framework for native components and implants.

## Indicators and threat intelligence

### Indicator feeds

- [abuse.ch](https://abuse.ch/) - MalwareBazaar, ThreatFox, URLhaus, and Feodo Tracker feeds for fresh infrastructure.
- [Amnesty International investigations](https://github.com/AmnestyTech/investigations) - Indicators of compromise from Amnesty's cyber investigations, including NSO Group infrastructure.
- [FinSpy Tools](https://github.com/devio/FinSpy-Tools) - Tooling for analyzing FinSpy and FinFisher components and infrastructure. (unmaintained)
- [MVT indicators](https://github.com/mvt-project/mvt-indicators) - Index and collection of MVT-compatible indicators.
- [Pegasus samples](https://github.com/9aylas/Pegasus-samples) - Archived Android and iOS samples attributed to Pegasus. (reference dump)

### Threat-intelligence platforms

- [IntelOwl](https://github.com/intelowlproject/IntelOwl) - Enrichment and analysis of indicators at scale.
- [MISP](https://github.com/MISP/MISP) - Open-source threat intelligence and indicator sharing platform.
- [OpenCTI](https://github.com/OpenCTI-Platform/opencti) - Knowledge graph for structured threat intelligence.

### Detection rules

- [Sigma](https://github.com/SigmaHQ/sigma) - Vendor-agnostic detection rule format and rule repository.
- [YARA](https://github.com/VirusTotal/yara) - Pattern matching for identifying and classifying malware samples.

## Exposés and investigations

- [Amnesty Security Lab](https://www.amnesty.org/en/tech/) - Technical investigations and forensic methodology from Amnesty International.
- [BLASTPASS](https://citizenlab.ca/blastpass-nso-group-iphone-zero-click-zero-day-exploit-captured-in-the-wild/) - Citizen Lab's discovery of a zero-click exploit used to deliver Pegasus.
- [Citizen Lab research](https://citizenlab.ca/research/) - Ongoing publications on mercenary spyware, zero-days, and civil-society targeting.
- [FORCEDENTRY](https://citizenlab.ca/research/forcedentry-nso-group-imessage-zero-click-exploit-captured-in-the-wild/) - Citizen Lab's analysis of NSO's zero-click iMessage exploit.
- [Google Threat Analysis Group](https://blog.google/threat-analysis-group/) - Disclosures of commercial spyware and exploit chains.
- [Graphite Caught](https://citizenlab.ca/research/first-forensic-confirmation-of-paragons-ios-mercenary-spyware-finds-journalists-targeted/) - First forensic confirmation of Paragon Solutions' Graphite spyware on journalists' phones.
- [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) - Vendor research on spyware infrastructure and campaigns.
- [Operation Triangulation](https://securelist.com/operation-triangulation/109842/) - Kaspersky's analysis of a long-running iOS implant campaign.
- [The Pegasus Project](https://www.occrp.org/en/project/the-pegasus-project) - OCCRP-led consortium investigation into NSO Group's Pegasus and its targets.
- [The Predator Files](https://www.amnesty.org/en/documents/act10/7245/2023/en/) - Amnesty International and EIC investigation into the Intellexa alliance and Predator spyware.

## Legal and policy

- [Article 19](https://www.article19.org/) - Freedom-of-expression advocacy on surveillance and spyware.
- [EFF border searches](https://www.eff.org/issues/border-searches) - Rights and practical guidance for device searches at borders.
- [EFF spyware](https://www.eff.org/tags/spyware) - Reporting and analysis on spyware policy and investigations.
- [EU PEGA inquiry briefing](https://www.europarl.europa.eu/RegData/etudes/BRIE/2024/761472/IPOL_BRI%282024%29761472_EN.pdf) - European Parliament research briefing on the PEGA inquiry's findings and recommendations.
- [Privacy International spyware](https://privacyinternational.org/learn/spyware) - Explainer on commercial spyware and the surveillance industry.
- [UN Special Rapporteur on privacy](https://www.ohchr.org/en/special-procedures/sr-privacy) - UN mandate tracking surveillance, spyware, and the right to privacy.
- [US Treasury Intellexa action](https://home.treasury.gov/news/press-releases/jy2155) - 2024 sanctions against Intellexa Consortium entities over Predator spyware; several individual designations were later lifted.
- [Wassenaar Arrangement](https://www.wassenaar.org/) - Multilateral export-control regime covering intrusion software and surveillance tools.

## Organizations and victim support

- [Access Now Digital Security Helpline](https://www.accessnow.org/help/) - Free, 24/7 incident response and safety planning for civil society.
- [Amnesty Security Lab get help](https://securitylab.amnesty.org/get-help/) - Contact channel for targeted individuals seeking technical support.
- [Citizen Lab](https://citizenlab.ca/) - Interdisciplinary research on information controls and spyware.
- [Committee to Protect Journalists](https://cpj.org/) - Safety resources and advocacy for journalists under digital threat.
- [Digital First Aid Kit](https://digitalfirstaid.org/) - Guided self-help for digital emergencies, including suspected device compromise.
- [EFF Surveillance Self-Defense](https://ssd.eff.org/) - Practical threat modeling and device-hardening guides.
- [NNEDV Safety Net](https://techsafety.org/) - US tech-abuse and stalkerware guidance for survivors and advocates.
- [OCCRP](https://www.occrp.org/) - Investigative reporting on surveillance and organized crime.
- [Privacy International](https://www.privacyinternational.org/) - Research and advocacy on the surveillance industry.

## Research and methodology

- [Exploit archaeology](https://www.virusbulletin.com/uploads/pdf/conference/vb2022/papers/VB2022-Exploit-archaeology-a-forensic-history-of-in-the-wild-NSO-Group-exploits.pdf) - Conference paper tracing NSO exploit chains and the artifacts they leave behind.
- [Forensic Methodology Report](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/) - The methodology behind MVT and modern iOS spyware forensics.
- [MVT documentation](https://docs.mvt.re/en/latest/) - Reference for indicator formats, forensic workflows, and result interpretation.

## Academic research

- [A Review of Mobile Surveillanceware](https://www.mdpi.com/2079-9292/14/14/2763) - 2025 review of targeted mobile spyware capabilities, detection, and countermeasures.
- [Current Research, Challenges, and Future Directions in Stalkerware](https://www.scitepress.org/Papers/2025/133717/133717.pdf) - 2025 review of stalkerware research and open problems.
- [Thwart Me If You Can](https://arxiv.org/abs/2508.02454) - 2025 empirical analysis of Android platform armoring against stalkerware.
- [Towards Stalkerware Detection with Precise Warnings](https://dl.acm.org/doi/10.1145/3485832.3485901) - ACSAC 2021 paper on generating precise stalkerware warnings.
- [arXiv cs.CR](https://arxiv.org/list/cs.CR/recent) - Recent cryptography and security preprints.
- [NDSS Symposium](https://www.ndss-symposium.org/) - Network and Distributed System Security Symposium proceedings.
- [USENIX Security](https://www.usenix.org/conferences/byname/108) - Symposium proceedings covering systems and network security research.

## Related awesome lists

- [android-security-awesome](https://github.com/ashishb/android-security-awesome) - Android security resources.
- [awesome-cybersecurity-blueteam](https://github.com/fabacab/awesome-cybersecurity-blueteam) - Defensive security resources.
- [awesome-malware-analysis](https://github.com/rshipp/awesome-malware-analysis) - Broader malware analysis tooling.
- [awesome-mobile-security](https://github.com/vaib25vicky/awesome-mobile-security) - Android and iOS security research.
- [awesome-privacy](https://github.com/pluja/awesome-privacy) - Privacy-respecting services and alternatives.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

---

Licensed under [CC0 1.0 Universal](LICENSE). Last reviewed: 2026-11-02.
