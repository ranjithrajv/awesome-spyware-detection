# Awesome Spyware Detection [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, indicators, investigations, and resources for detecting and exposing spyware and stalkerware.

Spyware is no longer a niche threat. Mercenary products such as Pegasus, Predator, and Graphite are sold to governments, while consumer-grade stalkerware is a few clicks and a credit card away. This list collects the open-source tooling, forensic methodology, and primary-source reporting needed to **find it, prove it, and talk about it**.

Detection is probabilistic. A clean scan means "no known indicators found", not "not infected". Treat every entry here as a starting point, not a verdict.

## Contents

- [If you suspect you are infected](#if-you-suspect-you-are-infected)
- [Mobile detection and triage](#mobile-detection-and-triage)
- [Forensic acquisition and analysis](#forensic-acquisition-and-analysis)
- [Stalkerware](#stalkerware)
- [Network-level detection](#network-level-detection)
- [Desktop and endpoint](#desktop-and-endpoint)
- [Reverse engineering and malware analysis](#reverse-engineering-and-malware-analysis)
- [Indicators and threat intelligence](#indicators-and-threat-intelligence)
- [Exposés and investigations](#exposés-and-investigations)
- [Organizations and victim support](#organizations-and-victim-support)
- [Research and methodology](#research-and-methodology)
- [Related awesome lists](#related-awesome-lists)
- [Contributing](#contributing)

## If you suspect you are infected

1. **Do not tip off the operator.** Avoid reinstalling, resetting, or "cleaning" the device before you have preserved evidence, and avoid discussing the suspicion on the device itself.
2. **Preserve first.** Take a forensic backup or acquisition before changing anything — see [Forensic acquisition and analysis](#forensic-acquisition-and-analysis).
3. **Scan with more than one tool.** Different tools cover different indicator sets and platforms.
4. **Get human help.** Contact a digital-security helpline (see [Organizations and victim support](#organizations-and-victim-support)); they can advise on safety planning as well as forensics.

## Mobile detection and triage

- [detekt](https://github.com/eReader/detekt) — macOS tool that scans iOS backups and the host for spyware artifacts.
- [Mobile Verification Toolkit (MVT)](https://github.com/mvt-project/mvt) — Amnesty International's forensic toolkit for indicators of compromise on Android and iOS. The de-facto standard.
- [mvt2timesketch](https://github.com/haxrob/mvt2timesketch) — Converts MVT output into a Timesketch-compatible timeline for correlation.
- [PhoneHackScan](https://github.com/UCYBERS/PhoneHackScan) — Android and iPhone intrusion check with a guided workflow.
- [sentinel](https://github.com/jamixm4-crypto/sentinel) — Cross-platform defensive detector for spyware, stalkerware, and surveillance software.
- [SpyGuard](https://github.com/SpyGuard/SpyGuard) — Enhanced fork of TinyCheck that watches network traffic for signs of compromise.
- [Zero-Breach Toolkit](https://github.com/interplains/Zero-Breach-Toolkit) — Cross-platform check for traces of mercenary spyware (Pegasus, Predator, Graphite, Candiru) on phones and computers.

## Forensic acquisition and analysis

- [ALEAPP](https://github.com/abrignoni/ALEAPP) — Android Logs Events And Protobuf Parser for building timelines from device data.
- [androidqf](https://github.com/mvt-project/androidqf) — Android Quick Forensics: fast, structured evidence collection from a device without root.
- [iLEAPP](https://github.com/abrignoni/iLEAPP) — iOS Logs, Events, And Plist Parser for building a timeline from a full file-system or backup.
- [libimobiledevice](https://github.com/libimobiledevice/libimobiledevice) — Cross-platform library for talking to iOS devices, including the backups MVT analyzes.

## Stalkerware

- [android-stalkerware](https://github.com/diskurse/android-stalkerware) — Technical write-ups and sample analysis of Android stalkerware families.
- [Coalition Against Stalkerware](https://stopstalkerware.org/) — Practical guidance, risk assessment, and a directory of support organizations.
- [MVT-PCAPDroid](https://github.com/BARGHEST-ngo/MVT-PCAPDroid) — Flattens MVT indicators for use with PCAPdroid's DNS and traffic views.
- [spytrap-adb](https://github.com/spytrap-org/spytrap-adb) — Tests a phone for stalkerware over ADB and USB debugging, no root required.
- [stalkerware-indicators](https://github.com/AssoEchap/stalkerware-indicators) — Community-maintained indicators for stalkerware apps (package names, certificates, signatures).

## Network-level detection

- [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) — Network-wide DNS filtering with per-client query logging.
- [Android IMSI-Catcher Detector](https://github.com/CellularPrivacy/Android-IMSI-Catcher-Detector) — Detects IMSI catchers, StingRays, and silent SMS on Android.
- [Exodus Privacy](https://github.com/Exodus-Privacy/exodus) — Platform for auditing trackers bundled in Android applications.
- [NetGuard](https://github.com/M66B/NetGuard) — Per-app internet blocking without root.
- [PCAPdroid](https://github.com/emanuele-f/PCAPdroid) — No-root network monitor, firewall, and PCAP dumper for Android.
- [Pi-hole](https://github.com/pi-hole/pi-hole) — DNS sinkhole for blocking known command-and-control and telemetry domains.
- [Rayhunter](https://github.com/EFForg/rayhunter) — Low-cost cell-site-simulator (IMSI catcher) detection built on a mobile hotspot.
- [RethinkDNS](https://github.com/celzero/rethink-app) — DNS-over-HTTPS/Tor, WireGuard proxying, firewall, and connection tracking on Android.
- [SnoopSnitch](https://github.com/srlabs/snoopsnitch) — Android baseband analysis for IMSI catchers and suspicious network behavior (Qualcomm devices).
- [Suricata](https://github.com/OISF/suricata) — IDS/IPS engine for signature-based network detection.
- [TrackerControl](https://github.com/TrackerControl/tracker-control-android) — Monitors and blocks trackers and ads per app.
- [Wireshark](https://github.com/wireshark/wireshark) — Packet analysis for inspecting captured traffic.
- [Zeek](https://github.com/zeek/zeek) — Network security monitor that produces high-level connection and protocol logs.

## Desktop and endpoint

- [BlockBlock](https://github.com/objective-see/BlockBlock) — Monitors persistence locations on macOS and alerts when something installs itself.
- [ClamAV](https://github.com/Cisco-Talos/clamav) — Open-source antivirus engine, useful for scanning acquired files and mail.
- [KnockKnock](https://github.com/objective-see/KnockKnock) — Enumerates persistently installed software on macOS, AutoRuns-style.
- [LuLu](https://github.com/objective-see/LuLu) — Free, open-source macOS firewall with per-process outbound visibility.
- [Lynis](https://github.com/CISOfy/lynis) — Security auditing tool for Unix-like systems, including persistence and configuration checks.
- [osquery](https://github.com/osquery/osquery) — SQL-powered endpoint instrumentation for hunting suspicious processes, launch items, and network state.
- [privacy.sexy](https://github.com/undergroundwires/privacy.sexy) — Script generator that enforces privacy and hardening baselines on Windows, macOS, and Linux.
- [sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) — High-quality Sysmon configuration template for Windows event tracing.
- [WindowsSpyBlocker](https://github.com/crazy-max/WindowsSpyBlocker) — Blocks Windows telemetry and spying endpoints.

## Reverse engineering and malware analysis

- [androguard](https://github.com/androguard/androguard) — Python library for reverse engineering and analyzing Android applications.
- [APKiD](https://github.com/rednaga/APKiD) — Identifies packers, protectors, and obfuscators in Android apps.
- [Apktool](https://github.com/iBotPeaches/Apktool) — Reverse engineering of Android APK files.
- [capa](https://github.com/mandiant/capa) — Identifies capabilities in executables, including spyware loaders and droppers.
- [diffuse](https://github.com/JakeWharton/diffuse) — Diffs two APK or AAB files, ideal for spotting what changed in a spyware update.
- [FLOSS](https://github.com/mandiant/flare-floss) — Extracts obfuscated strings from malware automatically.
- [Frida](https://github.com/frida/frida) — Dynamic instrumentation toolkit for runtime inspection on Android and iOS.
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) — Software reverse engineering framework for native components and implants.
- [House](https://github.com/nccgroup/house) — Runtime mobile analysis toolkit with a web GUI.
- [jadx](https://github.com/skylot/jadx) — Dex-to-Java decompiler.
- [Medusa](https://github.com/Ch0pin/medusa) — Modular mobile application analysis framework.
- [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) — Automated static and dynamic analysis for Android, iOS, and Windows apps.
- [objection](https://github.com/sensepost/objection) — Runtime mobile exploration built on Frida, with scripted checks for common weaknesses.
- [Quark-Engine](https://github.com/ev-flow/quark-engine) — Android malware scoring engine based on behavioral "crime" patterns.
- [RMS](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security) — Web interface for manipulating Android and iOS apps at runtime.

## Indicators and threat intelligence

- [abuse.ch](https://abuse.ch/) — MalwareBazaar, ThreatFox, URLhaus, and Feodo Tracker feeds for fresh infrastructure.
- [Amnesty International investigations](https://github.com/AmnestyTech/investigations) — Indicators of compromise from Amnesty's cyber investigations, including NSO Group infrastructure.
- [FinSpy Tools](https://github.com/devio/FinSpy-Tools) — Tooling for analyzing FinSpy/FinFisher components and infrastructure.
- [IntelOwl](https://github.com/intelowlproject/IntelOwl) — Enrichment and analysis of indicators at scale.
- [MISP](https://github.com/MISP/MISP) — Open-source threat intelligence and indicator sharing platform.
- [MVT indicators](https://github.com/mvt-project/mvt-indicators) — Index and collection of MVT-compatible indicators.
- [OpenCTI](https://github.com/OpenCTI-Platform/opencti) — Knowledge graph for structured threat intelligence.
- [Pegasus samples](https://github.com/9aylas/Pegasus-samples) — Archived Android and iOS samples attributed to Pegasus. Handle with care.
- [Sigma](https://github.com/SigmaHQ/sigma) — Vendor-agnostic detection rule format and rule repository.
- [Surveillance Industry](https://github.com/Ringmast4r/Surveillance-Industry) — Country-by-country dossiers on spyware vendors and state agencies.
- [TheHive](https://github.com/TheHive-Project/TheHive) — Case management for investigations and incident response.
- [YARA](https://github.com/VirusTotal/yara) — Pattern matching for identifying and classifying malware samples.

## Exposés and investigations

- [Amnesty Security Lab](https://www.amnesty.org/en/tech/) — Technical investigations and forensic methodology from Amnesty International.
- [BLASTPASS](https://citizenlab.ca/blastpass-nso-group-iphone-zero-click-zero-day-exploit-captured-in-the-wild/) — Citizen Lab's discovery of a zero-click exploit used to deliver Pegasus.
- [Citizen Lab research](https://citizenlab.ca/research/) — Ongoing publications on mercenary spyware, zero-days, and civil-society targeting.
- [FORCEDENTRY](https://citizenlab.ca/research/forcedentry-nso-group-imessage-zero-click-exploit-captured-in-the-wild/) — Citizen Lab's analysis of NSO's zero-click iMessage exploit.
- [Google Threat Analysis Group](https://blog.google/threat-analysis-group/) — Disclosures of commercial spyware and exploit chains.
- [Graphite Caught](https://citizenlab.ca/research/first-forensic-confirmation-of-paragons-ios-mercenary-spyware-finds-journalists-targeted/) — First forensic confirmation of Paragon Solutions' Graphite spyware on journalists' phones.
- [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) — Vendor research on spyware infrastructure and campaigns.
- [Operation Triangulation](https://securelist.com/operation-triangulation/109842/) — Kaspersky's analysis of a long-running iOS implant campaign.
- [The Pegasus Project](https://www.occrp.org/en/project/the-pegasus-project) — OCCRP-led consortium investigation into NSO Group's Pegasus and its targets.
- [The Predator Files](https://www.amnesty.org/en/documents/act10/7245/2023/en/) — Amnesty International and EIC investigation into the Intellexa alliance and Predator spyware.

## Organizations and victim support

- [Access Now Digital Security Helpline](https://www.accessnow.org/help/) — Free, 24/7 incident response and safety planning for civil society.
- [Citizen Lab](https://citizenlab.ca/) — Interdisciplinary research on information controls and spyware.
- [Coalition Against Stalkerware](https://stopstalkerware.org/) — Support directory and guidance for stalkerware victims.
- [EFF Surveillance Self-Defense](https://ssd.eff.org/) — Practical threat modeling and device-hardening guides.
- [OCCRP](https://www.occrp.org/) — Investigative reporting on surveillance and organized crime.
- [Privacy International](https://www.privacyinternational.org/) — Research and advocacy on the surveillance industry.

## Research and methodology

- [Forensic Methodology Report: How to Catch NSO Group's Pegasus](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/) — The methodology behind MVT and modern iOS spyware forensics.
- [Exploit archaeology: a forensic history of in-the-wild NSO Group exploits](https://www.virusbulletin.com/uploads/pdf/conference/vb2022/papers/VB2022-Exploit-archaeology-a-forensic-history-of-in-the-wild-NSO-Group-exploits.pdf) — Conference paper tracing NSO exploit chains and the artifacts they leave behind.
- [MVT documentation](https://docs.mvt.re/en/latest/) — Reference for indicator formats, forensic workflows, and result interpretation.

## Related awesome lists

- [android-security-awesome](https://github.com/ashishb/android-security-awesome) — Android security resources.
- [awesome-cybersecurity-blueteam](https://github.com/fabacab/awesome-cybersecurity-blueteam) — Defensive security resources.
- [awesome-malware-analysis](https://github.com/rshipp/awesome-malware-analysis) — Broader malware analysis tooling.
- [awesome-mobile-security](https://github.com/vaib25vicky/awesome-mobile-security) — Android and iOS security research.
- [awesome-privacy](https://github.com/pluja/awesome-privacy) — Privacy-respecting services and alternatives.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## License

[CC0 1.0 Universal](LICENSE) — public domain dedication.
