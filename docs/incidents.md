# Incidents and investigations

A dated record of publicly documented spyware cases, with the reporting and technical work that established each one. It is meant to answer three questions: what happened, how it was found out, and where to read the primary evidence.

This is not a complete census. Many infections are never discovered, many discoveries are never published, and many published cases are never confirmed forensically. Inclusion here means the case has attributable, public documentation — not that every claim in it is settled.

## How to read this file

- **Targeted** means a number or device was selected by an operator. **Infected** means traces of compromise were found on the device. The two are not the same, and reporting often blurs them.
- **Attribution is layered.** A device artifact can establish the spyware family with high confidence while saying nothing about which government deployed it. Treat vendor attribution as a separate claim from forensic attribution.
- **A notification is not a diagnosis.** Apple, Meta and Google warnings are high-signal leads, but they are deliberately vague and have produced false positives. They are the start of an investigation, not the end.
- **Dates are first public disclosure**, not necessarily when the intrusion happened. Several cases below were discovered years after the fact.
- **Court findings and settlements** appear under the original incident, because they usually resolve an old case rather than create a new one.
- **Cases and programmes are different units.** Most entries are victim-level cases with a device at the centre. The [mass deployments](#mass-deployments-and-state-programmes) section covers programme-level collection and tooling, which is documented through leaks, procurement records or platform telemetry. Do not compare the two as if they were the same kind of evidence.

## Timeline

| First disclosed | Case | Product | How it surfaced |
|---|---|---|---|
| 2026-10 | Serbia: rector and prosecutor | Pegasus, NoviSpy | Device forensics after Apple notification |
| 2026-10 | Poland: NSO had access to harvested data | Pegasus | Prosecutors' forensic review of the system |
| 2026-07 | Morocco: intelligence whistleblower | Pegasus | Whistleblower, leaked targeting records, forensics |
| 2026-02 | Greece: first convictions | Predator | Criminal trial following 2022 disclosure |
| 2025-06 | Paragon Graphite in Europe | Graphite | Apple and WhatsApp notifications, device forensics |
| 2025-03 | Serbia: BIRN journalists | Pegasus | Amnesty technical briefing |
| 2024-02 | Jordan: HRW staff and others | Pegasus | Access Now / Citizen Lab forensic study |
| 2023-10 | Predator Files | Predator | Consortium investigation, leaked contracts |
| 2023-10 | India: Apple threat notifications | Unattributed | Bulk Apple notifications to journalists and politicians |
| 2023-09 | BLASTPASS | Pegasus | Zero-click exploit captured in the wild |
| 2023-06 | Operation Triangulation | Unattributed iOS implant | Kaspersky's own network and devices |
| 2022-06 | Hermit | Hermit (RCS Lab) | Google TAG detection and attribution |
| 2022-04 | CatalanGate | Pegasus, Candiru | Citizen Lab forensic study |
| 2022-01 | Poland: opposition under Pegasus | Pegasus | Amnesty forensic investigation |
| 2022-01 | Greece: Predatorgate | Predator | SMS warning, MEP complaint, journalism |
| 2021-09 | FORCEDENTRY | Pegasus | Exploit captured from a target's phone |
| 2021-07 | The Pegasus Project | Pegasus | Leaked targeting dataset, 17 newsrooms |
| 2021-07 | Candiru | Candiru | Microsoft and Citizen Lab research |
| 2019-05 | WhatsApp zero-click | Pegasus | Exploit analysis, victim notifications |
| 2018-10 | Khashoggi and Saudi Pegasus | Pegasus | Device forensics on a dissident's phone |
| 2016-08 | Trident / Ahmed Mansoor | Pegasus | Target forwarded the attack SMS to researchers |
| 2015-07 | Hacking Team leak | Galileo | 400 GB of internal data published |
| 2014-08 | FinFisher proliferation | FinSpy | Internet-wide scanning for C2 servers |

Programme-level cases — bulk collection, state implant platforms and leaked tooling — are covered separately in [Mass deployments and state programmes](#mass-deployments-and-state-programmes), because they are rarely anchored to a single victim or device.

## 2026

### Serbia: Pegasus and NoviSpy against the student movement

**Product:** NSO Pegasus, NoviSpy (Android) · **Targets:** student activists, academics, a prosecutor · **Established by:** Citizen Lab, Amnesty Security Lab, SHARE Foundation

On 19 October 2026, six days before parliamentary elections, Citizen Lab and the SHARE Foundation reported that the iPhone of Vladan Đokić, rector of the University of Belgrade and a supporter of the student movement, had been infected with Pegasus in 2026. A prosecutor, Rade Bajić, received an Apple threat notification. A separate Citizen Lab brief published on 2 September 2026 confirmed Pegasus on the phone of a student protest organiser, and SHARE counted at least 14 people targeted in 2026. Investigations also documented NoviSpy, an Android tool used against activists, showing that the campaign mixed a mercenary iOS product with locally developed mobile malware.

**Detection:** Apple threat notifications, followed by full-file-system forensic analysis; Android cases relied on log artifacts rather than a single indicator. The cluster is a good example of why one platform's clean scan says nothing about another device owned by the same person.

**Coverage:** [Citizen Lab](https://citizenlab.ca/research/pegasus-spyware-serbian-pro-democracy/) · [Citizen Lab, September brief](https://citizenlab.ca/research/pegasus-spyware-infection-of-serbian-activist/) · [Balkan Insight](https://balkaninsight.com/2026/10/19/serbians-linked-to-protest-movement-allegedly-hit-by-spyware-attacks/bi/) · [CyberScoop](https://cyberscoop.com/pegasus-novispy-variant-spyware-found-on-devices-of-serbian-activists/)

### Poland: prosecutors say NSO had access to harvested data

**Product:** NSO Pegasus · **Targets:** opposition politicians, prosecutors, lawyers, journalists · **Established by:** Polish National Prosecutor's Office, ABW forensic experts, parliamentary inquiry

Poland bought Pegasus in 2017 under the Law and Justice government and used it against hundreds of people, including the head of the then-opposition's 2019 election campaign and, later, Prime Minister Donald Tusk's wife and daughter. On 12 October 2026 the National Prosecutor's Office published findings that the Central Anti-Corruption Bureau never had full control of the system: some administrative passwords were held elsewhere, the infection module stayed under NSO's exclusive control, and harvested data left Poland through servers managed by the vendor. Prosecutors did not conclude that NSO actually read specific operations. Former security officials have been charged, and the affair is still working through Polish courts.

**Detection:** This case was solved by institutional review — comparing what the system was authorised to do with what it could do — rather than by finding malware on a phone. For an individual, the practical lesson is that device-side traces can be absent even when a lawful operator has full access.

**Coverage:** [Notes from Poland, October 2026](https://notesfrompoland.com/2026/10/12/israeli-producer-had-access-to-data-harvested-by-poland-using-pegasus-spyware-say-prosecutors/) · [Amnesty International, 2022 findings](https://www.amnesty.org/en/latest/news/2022/01/poland-use-of-pegasus-spyware-to-hack-politicians-highlights-threat-to-civil-society/) · [Balkan Insight, 2025](https://balkaninsight.com/2025/02/25/pegasus-in-poland-a-flight-for-justice-that-never-took-off/rd/)

### Morocco: an intelligence insider describes Pegasus use

**Product:** NSO Pegasus · **Targets:** journalists, human rights defenders, Spanish and French politicians, Guardia Civil officers · **Established by:** Forbidden Stories consortium, Amnesty Security Lab, whistleblower testimony

A former member of Morocco's DGST, speaking under the pseudonym Safir, described how the domestic intelligence service began using Pegasus in 2017 after a demonstration at a villa in Rabat. The consortium, coordinated by Forbidden Stories and including Le Monde, Haaretz, El Confidencial, Die Zeit and the Guardian, corroborated the account with leaked emails, targeting records and device forensics. The records show more than 200 Spanish numbers selected for targeting by a user believed to be Morocco, including Prime Minister Pedro Sánchez and Defence Minister Margarita Robles, whose phones were confirmed infected in 2021. A Spanish investigation was shelved in January 2026 over Israel's failure to cooperate. The consortium found no evidence of Pegasus use by Morocco after late 2021.

**Detection:** Amnesty's forensic analysis of the leaked Pegasus dataset, matched against device artifacts and operator infrastructure. The case shows how a leaked targeting list becomes evidence only when it is tied to a specific device and a specific account.

**Coverage:** [The Guardian](https://www.theguardian.com/news/2026/jul/16/morocco-intelligence-insider-reveals-widespread-use-hacking-software-pegasus) · [Amnesty Security Lab, "Inside Pegasus"](https://securitylab.amnesty.org/latest/2026/07/inside-pegasus-the-evolution-of-the-worlds-most-notorious-spyware/)

### Greece: first convictions in the Predator scandal

**Product:** Intellexa Predator · **Targets:** 87 people, including ministers, military officers, journalists and an MEP · **Established by:** Athens court, European Parliament, journalism

In 2022, MEP and PASOK leader Nikos Androulakis was warned by European Parliament IT staff about a malicious text message, and financial journalist Thanasis Koukakis was found to have been targeted. The subsequent scandal exposed Predator use against 87 people, a third of whom had also been under lawful surveillance by the national intelligence service EYP. On 26 February 2026 an Athens court convicted four people who had marketed the software — Felix Bitzios, Yiannis Lavranos, Tal Dilian and Sara Hamou — of violating communications confidentiality and illegally accessing data. The sentences were suspended pending appeal, and the court referred the file to prosecutors to examine possible felonies, including espionage. No government official has been convicted.

**Detection:** The case began with a target-side warning about a suspicious SMS — the same pattern as Trident in 2016 — and was confirmed through device analysis and operator records. It is a reminder that initial infection vectors are often social, not purely technical.

**Coverage:** [BBC](https://www.bbc.com/news/articles/cj6dx4886rpo) · [RSF](https://rsf.org/en/predatorgate-scandal-greece-rsf-denounces-political-sabotage-investigation) · [Amnesty International](https://www.amnesty.org/en/latest/news/2023/01/greeces-surveillance-scandal-must-shake-us-out-of-complacency/)

## 2025

### Paragon Graphite in Europe

**Product:** Paragon Solutions Graphite · **Targets:** journalists and migration activists in Italy and elsewhere in Europe · **Established by:** Citizen Lab, WhatsApp, Apple, Italian prosecutors

In January 2025, WhatsApp told Fanpage.it editor Francesco Cancellato that he had been targeted with Paragon's Graphite. On 29 April 2025, Apple sent threat notifications to a small group of iOS users; two journalists allowed forensic analysis. Citizen Lab's 12 June 2025 report confirmed with high confidence that both had been targeted, identified a shared attacker iMessage account and a server at `46.183.184[.]91`, and documented the zero-click chain later assigned CVE-2025-43200 and fixed in iOS 18.3.1. WhatsApp said about 90 people had been targeted. In March 2026, Rome and Naples prosecutors independently confirmed that three Android devices — Cancellato's and those of activists Luca Casarini and Giuseppe Caccia — were compromised in a coordinated campaign on the night of 14 December 2024.

**Detection:** A platform notification opened the case; the confirmation came from device logs, shared attacker infrastructure and the Android indicator Citizen Lab calls BIGPRETZEL. The Italian parliamentary inquiry had earlier failed to confirm Cancellato's compromise, which is a useful warning about the limits of reviews that do not examine the device.

**Coverage:** [Citizen Lab](https://citizenlab.ca/research/first-forensic-confirmation-of-paragons-ios-mercenary-spyware-finds-journalists-targeted/) · [The Guardian, March 2026](https://www.theguardian.com/world/2026/mar/06/italy-activists-and-journalist-targeted-by-spyware-in-2024-prosecutors-confirm) · [Citizen Lab on the prosecutors' findings](https://citizenlab.ca/italian-prosecutors-confirm-journalist-was-hacked-with-paragon-spyware/) · [Amnesty International](https://www.amnesty.org/en/latest/news/2025/06/italy-new-case-of-journalist-targeted-with-graphite-spyware-confirms-widespread-use-of-unlawful-surveillance/)

### Serbia: BIRN journalists targeted with Pegasus

**Product:** NSO Pegasus · **Targets:** investigative journalists at BIRN · **Established by:** Amnesty Security Lab, SHARE Foundation

In March 2025, Amnesty's Security Lab published a technical briefing finding that journalists at the Balkan Investigative Reporting Network had been targeted with Pegasus. The findings were part of a wider pattern of spyware use against Serbian civil society that escalated during the 2024–2026 protest movement. Serbian authorities denied the findings.

**Detection:** Device forensics and comparison against known Pegasus indicators, published with enough technical detail for others to reproduce. Amnesty's brief is one of the clearer public examples of a newsroom-scale response: preserve devices, analyse in a trusted environment, publish indicators without exposing victims.

**Coverage:** [Amnesty International](https://www.amnesty.org/en/latest/news/2025/03/serbia-birn-journalists-targeted-with-pegasus-spyware/) · [European Federation of Journalists](https://europeanjournalists.org/blog/2025/03/28/serbia-spyware-attacks-on-birn-journalists-further-deepen-press-freedom-crisis/) · [Amnesty technical briefing](https://www.amnesty.org/en/documents/eur70/9186/2025/en/)

## 2024

### Jordan: Pegasus against HRW staff and civil society

**Product:** NSO Pegasus · **Targets:** at least 30 journalists, lawyers, activists and Human Rights Watch staff · **Established by:** Access Now, Citizen Lab

A forensic study published on 1 February 2024 found Pegasus on the phones of more than 30 people in Jordan, including four Human Rights Watch staff. The investigation combined device analysis with operator infrastructure and victim testimony. Jordan denied using the spyware.

**Detection:** Access Now's digital security helpline collected devices, Citizen Lab performed the forensic analysis, and the two published a joint account. This is the standard civil-society response model: helpline intake, trusted lab analysis, coordinated publication.

**Coverage:** [Human Rights Watch](https://www.hrw.org/news/2024/02/01/spyware-targets-human-rights-watch-staff-jordan) · [Al Jazeera](https://www.aljazeera.com/news/2024/2/1/journalists-activists-targeted-in-jordan-with-israeli-made-pegasus-spyware) · [Access Now report](https://www.accessnow.org/publication/between-a-hack-and-a-hard-place-how-pegasus-spyware-crushes-civic-space-in-jordan/)

## 2023

### Predator Files

**Product:** Intellexa Predator · **Targets:** civil society, politicians and officials in several countries · **Established by:** Amnesty Security Lab, European Investigative Collaborations and partner newsrooms

Published in October 2023, the Predator Files combined leaked contracts, operator documents and device forensics to map how the Intellexa alliance sold Predator and its "as-a-service" infrastructure. The reporting documented targeting in Greece and beyond, and showed how the same product was rebranded and resold through intermediaries. It built on earlier work on Cytrox, the vendor behind Predator, whose iOS chain Citizen Lab had analysed in 2021.

**Detection:** The investigation relied on commercial and procurement records as much as on malware artifacts. For defenders, it is a reminder that supply-chain and reseller documentation can establish a case when device traces are gone.

**Coverage:** [Amnesty International](https://www.amnesty.org/en/documents/act10/7245/2023/en/) · [Citizen Lab on Cytrox/Predator](https://citizenlab.ca/research/pegasus-vs-predator-dissidents-doubly-infected-iphone-reveals-cytrox-mercenary-spyware/)

### India: Apple threat notifications and the limits of attribution

**Product:** Unattributed mercenary spyware · **Targets:** opposition politicians, journalists and activists · **Established by:** Apple notifications; partial independent analysis

On 31 October 2023, Apple sent threat notifications to a number of Indian journalists and opposition figures, warning that their devices may have been targeted by state-sponsored attackers. The Indian government demanded an explanation and ordered an investigation; Apple did not attribute the activity, and no forensic confirmation was published for most recipients. The episode matters because it shows what a notification can and cannot establish: it is a strong lead, but without device analysis it does not identify the product, the operator or the intrusion date.

**Detection:** Treat notifications as triage. Preserve the device, capture a backup or full file system, and look for exploit artifacts and known indicators rather than relying on the warning alone.

**Coverage:** [The Washington Post](https://www.washingtonpost.com/world/2023/10/31/india-phone-hacking-apple/) · [The New York Times](https://www.nytimes.com/2023/11/01/world/asia/india-apple-threat-notification.html) · [Amnesty International](https://www.amnesty.org/en/latest/news/2023/10/global-india-apple-notifications-highlight-the-unabated-threat-of-unlawful-targeted-surveillance/)

### BLASTPASS

**Product:** NSO Pegasus · **Targets:** civil society and journalists, including a Washington-based organisation and individuals in Mexico · **Established by:** Citizen Lab, Apple

Citizen Lab's September 2023 report documented a zero-click iMessage exploit chain that abused PassKit to deliver Pegasus without any user interaction. Apple assigned CVE-2023-41064 and CVE-2023-41061 and shipped fixes in iOS 16.6.1. The exploit was notable for needing no link, attachment or user action: the device could be compromised while locked. Apple's Lockdown Mode blocked the attack path.

**Detection:** The case was caught because a target's device was analysed after suspicious activity, and because the exploit chain left artifacts in logs. For high-risk users, Lockdown Mode is the single most effective mitigation documented here, and a clean scan after the fact is not proof of safety.

**Coverage:** [Citizen Lab](https://citizenlab.ca/2023/09/blastpass-nso-group-iphone-zero-click-zero-day-exploit-captured-in-the-wild/)

### Operation Triangulation

**Product:** Unattributed iOS implant · **Targets:** Kaspersky employees and other iOS users · **Established by:** Kaspersky

Kaspersky disclosed in June 2023 that its own corporate Wi-Fi network had been used to compromise iPhones with a complex, multi-stage implant it named TriangleDB. The attack chain used four zero-days, including a hardware-assisted bypass of memory protections, and appeared to date back to 2019. Kaspersky published the details at the 37th Chaos Communication Congress in December 2023. Attribution remains unresolved.

**Detection:** Kaspersky found the campaign through its own network monitoring and then analysed device backups and sysdiagnose data. It is a rare public example of an implant that survived multiple iOS updates and was found by an organisation monitoring its own estate rather than by a victim report.

**Coverage:** [Kaspersky Securelist](https://securelist.com/operation-triangulation/109842/)

## 2022

### Greece: Predatorgate

**Product:** Intellexa Predator · **Targets:** MEP Nikos Androulakis, journalist Thanasis Koukakis and dozens of others · **Established by:** European Parliament, Citizen Lab, Greek journalism

This is the disclosure that became the 2026 conviction above. In 2022 Androulakis was told by European Parliament IT staff that he had received a malicious link, and Koukakis was found to have been targeted. Reporting by Documento and others revealed that Predator was sold in Greece while its use by the state was not clearly lawful; a law passed later that year legalised surveillance under conditions. The affair became known as Greece's Watergate and led to a European Parliament inquiry into Pegasus and equivalent spyware.

**Detection:** A suspicious message, a target who reported it, and device analysis. The Greek case also showed how a target can be under both lawful and unlawful surveillance at the same time, which complicates the forensic picture.

**Coverage:** [BBC](https://www.bbc.com/news/articles/cj6dx4886rpo) · [RSF](https://rsf.org/en/predatorgate-scandal-greece-rsf-denounces-political-sabotage-investigation)

### Hermit

**Product:** RCS Lab Hermit · **Targets:** users in Italy and Kazakhstan · **Established by:** Google Threat Analysis Group, Lookout

In June 2022, Google TAG attributed a spyware campaign to Italy-based RCS Lab and its Hermit product. The malware was delivered through SMS messages that posed as operator or government notices and, on iOS, relied on a malicious configuration profile. Google notified affected Android users and referred the iOS cases to Apple. Lookout published a technical analysis of the Android implant. The campaign was notable for combining a commercial vendor with local telecom infrastructure.

**Detection:** Android users could be identified through Google Play Protect and device scanning; iOS cases required checking installed configuration profiles and device management settings. Both are things a non-expert can inspect.

**Coverage:** [Google Threat Analysis Group](https://blog.google/threat-analysis-group/italian-spyware-vendor-targets-users-in-italy-and-kazakhstan/)

### CatalanGate

**Product:** NSO Pegasus and Candiru · **Targets:** more than 60 Catalan politicians, lawyers, activists and journalists · **Established by:** Citizen Lab

Citizen Lab's April 2022 study found extensive targeting of Catalan independence figures using both Pegasus and Candiru. Spain's CNI acknowledged that it had legally targeted some individuals, while denying others. The case illustrated how two vendors can be used against the same community, and how lawful and unlawful surveillance can be hard to separate from the outside.

**Detection:** Device forensics across a large number of phones, with indicators split between the two products. CatalanGate is one of the best public examples of correlating a cluster of victims rather than treating each phone in isolation.

**Coverage:** [Citizen Lab](https://citizenlab.ca/2022/04/catalangate-extensive-mercenary-spyware-operation-against-catalans-using-pegasus-candiru/) · [Amnesty International](https://www.amnesty.org/en/latest/news/2022/04/spain-pegasus-spyware-catalans-targeted/)

### Poland: the opposition under Pegasus

**Product:** NSO Pegasus · **Targets:** opposition politicians, lawyers, prosecutors and journalists · **Established by:** Amnesty International, Polish Senate inquiry, prosecutors

Amnesty's January 2022 investigation found Pegasus on the phone of Senator Krzysztof Brejza, then a leading opposition figure, and documented targeting of other critics of the Law and Justice government. Poland had bought Pegasus in 2017. A Senate committee and later a parliamentary inquiry established that the system had been used far beyond what courts had been told, and that the purchase was financed through the justice ministry. The 2026 prosecutor findings above added that the vendor retained technical access to harvested data.

**Detection:** Amnesty analysed Brejza's device after he was told by Citizen Lab that he might have been targeted. The case is a template for opposition figures: preserve the phone, involve an independent lab, and expect legal proceedings to take years.

**Coverage:** [Amnesty International](https://www.amnesty.org/en/latest/news/2022/01/poland-use-of-pegasus-spyware-to-hack-politicians-highlights-threat-to-civil-society/) · [Notes from Poland, 2026](https://notesfrompoland.com/2026/10/12/israeli-producer-had-access-to-data-harvested-by-poland-using-pegasus-spyware-say-prosecutors/)

## 2021

### FORCEDENTRY

**Product:** NSO Pegasus · **Targets:** Bahraini activists, including members of the Bahrain Center for Human Rights · **Established by:** Citizen Lab

In September 2021, Citizen Lab captured and analysed an NSO zero-click iMessage exploit that abused a compression library bug, CVE-2021-30860, to install Pegasus. The attack required no user interaction and was fixed in iOS 14.8. The report documented the exploit chain in enough detail for Apple and others to reproduce the finding, and became one of the most-cited examples of a "zero-click" mobile attack.

**Detection:** The exploit was identified from a target's device and from the attacker's infrastructure, not from a signature. It reinforced the value of analysing backups and logs rather than scanning for known malware files.

**Coverage:** [Citizen Lab](https://citizenlab.ca/2021/09/forcedentry-nso-group-imessage-zero-click-exploit-captured-in-the-wild/)

### The Pegasus Project

**Product:** NSO Pegasus · **Targets:** more than 50,000 phone numbers selected as possible targets · **Established by:** Forbidden Stories, Amnesty Security Lab and 17 newsrooms

Published on 18 July 2021, the Pegasus Project analysed a leaked dataset of more than 50,000 numbers that had been selected for Pegasus targeting. The consortium included the Guardian, Washington Post, Le Monde and OCCRP. The reporting linked the list to journalists, activists, politicians and heads of state, and prompted investigations across Europe. NSO disputed the interpretation of the data, and the presence of a number on the list was not proof of infection.

**Detection:** The project combined forensic analysis of a sample of devices with analysis of the leaked targeting database. Its methodology is a model for handling large datasets responsibly: verify a subset forensically, publish the method, and avoid treating list membership as proof.

**Coverage:** [The Guardian series](https://www.theguardian.com/news/series/pegasus-project) · [OCCRP](https://www.occrp.org/en/project/the-pegasus-project)

### Candiru

**Product:** Candiru · **Targets:** activists, journalists and dissidents in at least ten countries · **Established by:** Microsoft, Citizen Lab

In July 2021, Citizen Lab published "Hooking Candiru", mapping a lesser-known vendor that sold spyware to governments and used Windows zero-days as well as mobile exploits. In October 2021, Microsoft's Threat Intelligence Center documented a Candiru campaign that exploited Windows vulnerabilities to install malware on targets' machines. The vendor was later sanctioned by the United States.

**Detection:** Microsoft found the campaign through endpoint telemetry, while Citizen Lab worked from victim devices. The case is a useful reminder that mercenary surveillance is not only a phone problem: the same targets were attacked on Windows.

**Coverage:** [Citizen Lab](https://citizenlab.ca/research/hooking-candiru-another-mercenary-spyware-vendor-comes-into-focus/) · [The Record on Microsoft's findings](https://therecord.media/windows-spyware-and-zero-days-linked-to-prodigious-israeli-hack-for-hire-company)

## 2019

### WhatsApp: the NSO zero-click and the lawsuit that followed

**Product:** NSO Pegasus · **Targets:** about 1,400 WhatsApp users, including journalists, activists and diplomats · **Established by:** WhatsApp, Citizen Lab, courts

In May 2019, WhatsApp disclosed that an NSO exploit, CVE-2019-3568, allowed attackers to install Pegasus through a crafted voice call. The company attributed the attack to NSO and notified about 1,400 users. Citizen Lab and others analysed the infrastructure and victims. In May 2025, a US court found NSO liable in WhatsApp's lawsuit, a ruling Amnesty called a momentous win for accountability.

**Detection:** WhatsApp's server-side telemetry identified the anomalous calls, and victim-side analysis confirmed the implant. The case is one of the few where platform-level detection, not a device scan, drove the discovery.

**Coverage:** [Amnesty International on the ruling](https://www.amnesty.org/en/latest/news/2025/05/ruling-against-nso-group-in-whatsapp-case-a-momentous-win/) · [Citizen Lab](https://citizenlab.ca/whatsapp-voice-calls-used-to-inject-nso-group-spyware-in-phones/) · [Knight First Amendment Institute case file](https://knightcolumbia.org/cases/whatsapp-v-nso-group)

## 2018

### Khashoggi and Saudi-linked Pegasus

**Product:** NSO Pegasus · **Targets:** Saudi dissidents and journalists, including Omar Abdulaziz and Jamal Khashoggi's circle · **Established by:** Citizen Lab, subsequent forensic reporting

In October 2018, Citizen Lab reported that the phone of Saudi dissident Omar Abdulaziz, then living in Canada, had been compromised with Pegasus, and that the spyware was linked to Saudi operators. The finding was published shortly after Jamal Khashoggi's murder and helped establish that Pegasus was being used against Saudi critics abroad. Later reporting found Pegasus on the phone of Khashoggi's wife months before his death.

**Detection:** Device forensics and operator infrastructure analysis. The case also showed how diaspora communities are targeted across borders, and why Canadian and other authorities were slow to treat the findings as a security matter.

**Coverage:** [Citizen Lab](https://citizenlab.ca/research/the-kingdom-came-to-canada-how-saudi-linked-digital-espionage-reached-canadian-soil/) · [The Washington Post, republished by Citizen Lab](https://citizenlab.ca/the-washington-post-a-uae-agency-put-pegasus-spyware-on-phone-of-jamal-khashoggis-wife-months-before-his-murder-new-forensics-show/)

## 2016

### Trident and Ahmed Mansoor

**Product:** NSO Pegasus · **Targets:** UAE human rights defender Ahmed Mansoor · **Established by:** Citizen Lab, Lookout

On 10 and 11 August 2016, Ahmed Mansoor received SMS messages promising "new secrets" about detainees tortured in UAE prisons. He forwarded them to Citizen Lab instead of clicking. Working with Lookout, researchers found a chain of three iOS zero-days — later called Trident — that would have installed Pegasus. Apple fixed the vulnerabilities in iOS 9.3.4 within days. The case is the origin story of public Pegasus research and of the "don't click, preserve, report" advice that still governs high-risk users.

**Detection:** The target's decision to report the message, rather than any automated tool, made the discovery possible. It remains the clearest illustration that user behaviour and trusted reporting channels are part of the detection chain.

**Coverage:** [Citizen Lab](https://citizenlab.ca/research/million-dollar-dissident-iphone-zero-day-nso-group-uae/) · [Nextgov](https://www.nextgov.com/cybersecurity/2016/08/cyber-espionage-spyware-exploits-3-zero-days/143964/) · [ABC News](https://abcnews.com/Technology/attempt-hack-top-human-rights-activist-exposed-unprecedented/story?id=41671098)

## 2015

### The Hacking Team leak

**Product:** Hacking Team Galileo RCS · **Targets:** customers' targets in multiple countries, including journalists and activists · **Established by:** WikiLeaks, independent researchers

In July 2015, unknown attackers published roughly 400 GB of internal data from the Italian surveillance vendor Hacking Team, including emails, contracts, source code and product documentation. WikiLeaks mirrored the archive. The leak revealed customers including Sudan and Kazakhstan and showed how "lawful intercept" products were exported to governments with poor human rights records. It also produced a large corpus of indicators that defenders used for years.

**Detection:** This was a supply-chain leak, not a victim discovery, but it gave network defenders concrete domains, certificates and malware samples. It is a reminder that vendor infrastructure, once exposed, becomes durable detection material.

**Coverage:** [WikiLeaks archive](https://wikileaks.org/hackingteam/emails/) · [Citizen Lab commentary](https://citizenlab.ca/research-on-hacking-team-and-finfisher-highlighted-in-motherboard/)

## 2014

### FinFisher's global proliferation

**Product:** Gamma International FinSpy · **Targets:** activists, journalists and dissidents in dozens of countries · **Established by:** Citizen Lab

Citizen Lab's 2014 research mapped FinFisher command-and-control servers in more than 20 countries, showing that the "lawful intercept" product was deployed far beyond the democracies its vendor claimed to serve. The work combined internet-wide scanning with malware analysis and legal research, and helped establish the template for investigating spyware vendors through their infrastructure.

**Detection:** Rather than relying on victim reports, researchers scanned the internet for FinFisher's server fingerprints. That approach is still used to find spyware infrastructure at scale, and it is why network-level monitoring belongs in a detection programme.

**Coverage:** [Citizen Lab](https://citizenlab.ca/research/you-only-click-twice-finfishers-global-proliferation-2/)

## Mass deployments and state programmes

The cases above are anchored to specific victims and, usually, a specific device. The programmes below are documented at the level of a collection system, an implant platform or a leaked toolset. They set the environment that targeted spyware operates in, and several of them are how spyware tooling escaped into general circulation.

| First disclosed | Programme | What was deployed | Documented scale | Evidence |
|---|---|---|---|---|
| 2010-06 | Stuxnet | PLC rootkit and Windows worm | Natanz centrifuge disruption | Symantec, later reporting |
| 2012-05 | Flame | Modular espionage platform | ~1,000 machines, Middle East | Kaspersky, CrySyS |
| 2013-06 | Snowden / NSA–GCHQ | PRISM, Upstream, XKeyscore, Tempora, MUSCULAR | Bulk collection across providers and cables | Snowden documents |
| 2014-11 | Regin | Modular backdoor platform | Telecoms and governments, 2008–2014 | Kaspersky analysis |
| 2015-02 | Equation Group | GrayFish, EquationDrug, Fanny | Thousands of victims, 30+ countries | Kaspersky analysis |
| 2016-08 | Shadow Brokers | Leaked NSA exploit tooling | Global, via WannaCry and NotPetya | Guardian, Ars Technica |
| 2017-03 | Vault 7 | CIA tooling (Weeping Angel, Athena, Hive) | A toolset, not one deployment | WikiLeaks publication |
| 2018-01 | Dark Caracal | Android and Windows spyware | Thousands of victims, 21+ countries | Lookout and EFF |
| 2019-01 | Project Raven | Mercenary hacking unit, not a product | Dozens of state-selected targets | Reuters investigation |
| 2020-12 | SolarWinds | SUNBURST supply-chain backdoor | 18,000 downloaders, dozens compromised | Microsoft, FireEye, CISA |
| 2024-10 | Salt Typhoon | Telecom network intrusion | Multiple US carriers | CISA, CRS |

The largest commercial investigations — the Pegasus Project's 50,000-plus numbers and the Predator Files — appear in the case sections above because they are built from victim-level evidence, even though their scale is programme-sized.

### Stuxnet: the first known cyberweapon with physical effects

**Platform:** PLC rootkit, Windows worm, USB propagation · **Target:** Iran's Natanz uranium-enrichment plant · **Established by:** Symantec, independent researchers, later reporting on Operation Olympic Games

Stuxnet was discovered in June 2010 after a Belarusian security firm found it spreading through Windows machines, but it had been operating since at least 2009. It was the first worm to carry a programmable-logic-controller rootkit: it targeted Siemens Step 7 software and, inside Natanz, manipulated centrifuge speeds while reporting normal operation to operators. It used four Windows zero-days and stolen code-signing certificates, and spread to air-gapped networks through USB drives. Reporting based on interviews with US officials later described it as part of Operation Olympic Games, a joint US–Israeli effort; about 1,000 centrifuges were taken offline.

**Detection:** This is an operations-technology problem before it is an endpoint problem. Defenders need PLC logic integrity checks, OT network monitoring, USB media control, and Windows patch management. Antivirus caught early samples but not the targeted payload; the lesson is that the PLC, not the PC, is the target.

**Coverage:** [Symantec Stuxnet dossier](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en) · [The New York Times on Operation Olympic Games](https://www.nytimes.com/2012/06/01/world/middleeast/obama-ordered-wave-of-cyberattacks-against-iran.html)

### Flame: a modular platform built for espionage

**Platform:** Flame (sKyWIper) · **Reach:** roughly 1,000 machines, mainly in the Middle East · **Established by:** Kaspersky, CrySyS Lab

Flame was found in May 2012 during Kaspersky's investigation of malware at Iran's oil ministry. It was a roughly 20 MB modular platform written partly in Lua, with Bluetooth and USB propagation, audio recording, screenshot capture, keystroke logging and a self-destruct command. It shared code with Stuxnet, and later reporting attributed it to the United States and Israel. The CrySyS Lab's independent analysis, published as sKyWIper, confirmed the platform's unusual complexity.

**Detection:** File-size and modularity anomalies, Lua script detection, command-and-control domains, and certificate abuse — Flame used a spoofed Microsoft Terminal Services certificate to sign components. Network monitoring and memory analysis were more useful than signature scanning alone.

**Coverage:** [Kaspersky Securelist](https://securelist.com/the-flame-questions-and-answers/34344/) · [CrySyS sKyWIper analysis](https://www.crysys.hu/skywiper/skywiper.pdf)

### Snowden: NSA and GCHQ bulk collection

**Programmes:** PRISM, Upstream, XKeyscore, Tempora, MUSCULAR, Boundless Informant, CO-TRAVELER, Bullrun · **Reach:** global, with collection from major US internet companies and fibre-optic cables · **Established by:** Edward Snowden's documents, published by the Guardian and The Washington Post from June 2013

This is the programme layer rather than a spyware-on-a-phone case, and the distinction matters. PRISM collected data from major US providers; Upstream tapped cables and infrastructure; XKeyscore provided a query interface over collected content; Tempora buffered undersea-cable traffic for GCHQ; MUSCULAR accessed internal links between Google and Yahoo data centres; Boundless Informant visualised metadata collection; CO-TRAVELER correlated location data; Bullrun worked against encryption. The disclosures led to the 2014 PCLOB review, the 2015 USA Freedom Act, the invalidation of the EU–US Safe Harbor arrangement in Schrems I, and the lapse of the Section 215 telephony-metadata authority in 2020.

**Detection:** Bulk collection is invisible to device forensics. There is no implant to find on the phone, and no scan that establishes whether a message was also copied in transit. Detection here means network measurement, certificate and route analysis, provider transparency reports, and legal or regulatory challenge. For a defender, the practical consequence is that a clean device does not mean a private conversation.

**Coverage:** [The Guardian, NSA files](https://www.theguardian.com/us-news/the-nsa-files) · [EFF, NSA spying](https://www.eff.org/nsa-spying) · [ACLU, NSA surveillance](https://www.aclu.org/issues/national-security/privacy-and-surveillance/nsa-surveillance)

### Regin: a multi-stage platform aimed at telecoms

**Platform:** Regin · **Targets:** telecom operators, governments, financial institutions and researchers · **Established by:** Symantec, Kaspersky

Symantec disclosed Regin in November 2014, after tracing it back to at least 2008. It was a multi-stage modular backdoor with encrypted command-and-control and interchangeable payloads, used against telecom operators, governments, financial institutions and researchers. Kaspersky's later analysis focused on its use against GSM network infrastructure, which put call metadata and lawful-intercept systems in scope. Attribution remains unresolved, though the targets and tradecraft point to a state programme.

**Detection:** Network logs and unusual command-and-control protocols, memory forensics, and GSM signalling analysis. Multi-stage loaders mean file-based indicators age quickly; infrastructure and behaviour are more durable.

**Coverage:** [Kaspersky on Regin and GSM networks](https://securelist.com/the-regin-platform-nation-state-ownage-of-gsm-networks/67741/)

### Equation Group: an implant platform at scale

**Platforms:** EquationDrug, GrayFish, Fanny, DoubleFantasy, TripleFantasy · **Reach:** thousands of victims in more than 30 countries · **Established by:** Kaspersky, February 2015

Kaspersky described the Equation Group as the most advanced actor it had analysed, with operations dating back to at least 2001. The group used bootkits, a registry-based virtual file system, and — most unusually — reprogrammed hard-drive and SSD firmware so that the implant survived operating-system reinstalls. The Fanny worm spread through USB drives into air-gapped networks. Victims included government and diplomatic institutions, telecoms, energy and nuclear organisations, and military targets. Kaspersky linked the group's code to Stuxnet and Flame but did not formally name a state; later reporting widely associated it with the US NSA.

**Detection:** This is the case that breaks the assumption that reinstalling the operating system cleans a machine. Firmware-level persistence requires comparing firmware hashes against vendor baselines, inspecting boot integrity, and using out-of-band analysis. Most endpoint antivirus products of the era could not see it.

**Coverage:** [Kaspersky Securelist](https://securelist.com/equation-the-death-star-of-malware-galaxy/68750/) · [Kaspersky report mirror](https://wikileaks.org/ciav7p1/cms/files/Equation_group_questions_and_answers.pdf)

### Shadow Brokers: when state exploits become commodity attacks

**Programme:** Leaked Equation Group/NSA exploit tooling · **Reach:** global, through WannaCry and NotPetya · **Established by:** the Shadow Brokers releases, security researchers

The Shadow Brokers appeared in August 2016, auctioning what they claimed were tools stolen from the Equation Group. In April 2017 they released the most damaging cache, including EternalBlue, EternalRomance and DoublePulsar. EternalBlue exploited SMBv1 (MS17-010); WannaCry used it in May 2017 to hit more than 200,000 computers in 150 countries, and NotPetya followed in June. The leak did not deploy spyware itself, but it turned state exploit capability into mass criminal infrastructure.

**Detection:** Patch MS17-010, disable SMBv1, monitor for DoublePulsar and anomalous SMB traffic, and keep offline backups. The strategic point is speed: a leaked exploit becomes commodity within weeks, so patch latency is a security control in its own right.

**Coverage:** [The Guardian](https://www.theguardian.com/technology/2017/may/17/hackers-shadow-brokers-threatens-issue-more-leaks-hacking-tools-ransomware) · [Ars Technica](https://arstechnica.com/information-technology/2017/04/nsa-leaking-shadow-brokers-just-dumped-its-most-damaging-release-yet/)

### Vault 7: the CIA toolset leak

**Tooling:** Weeping Angel, Athena, Hive, Pandemic, Grasshopper · **Reach:** a toolset rather than a single deployment · **Established by:** WikiLeaks, March 2017

On 7 March 2017, WikiLeaks began publishing "Year Zero", 8,761 documents from the CIA's Center for Cyber Intelligence describing tools for compromising phones, smart TVs, routers and air-gapped machines. Weeping Angel turned a Samsung television into a listening device; Athena and Hive targeted Windows; Pandemic was a persistence tool for remote machines. A later release, Vault 8, included source code. The leak did not reveal a mass deployment, but it exposed how offensive tooling is built, stored and lost — and how quickly a leaked tool becomes someone else's mass incident. The Shadow Brokers entry above is the clearest demonstration of that path; Vault 7 itself never produced a WannaCry-scale outbreak.

**Detection:** The immediate defensive value was in the details: affected products, persistence methods, command-and-control patterns, and the fact that firmware and supply-chain positions were in scope. Vendors used the documents to patch; defenders used them to hunt. The strategic lesson is that tool proliferation is a detection problem before it is a malware problem.

**Coverage:** [WikiLeaks Vault 7](https://wikileaks.org/vault7/) · [The Guardian explainer](https://www.theguardian.com/technology/2017/mar/08/wikileaks-vault-7-cia-documents-hacked-what-you-need-to-know) · [The Guardian on the industry response](https://www.theguardian.com/technology/2017/mar/08/wikileaks-cia-leak-apple-vault-7-documents)

### Dark Caracal: mobile spyware in 21 countries

**Product:** Custom Android and Windows spyware · **Targets:** thousands of victims, including military personnel, journalists, lawyers, medical professionals and activists · **Established by:** Lookout and EFF, January 2018

Published on 18 January 2018, the Dark Caracal investigation documented a long-running campaign that stole hundreds of gigabytes from thousands of victims in more than 21 countries. Operators distributed trojanised apps and phishing messages, then exfiltrated messages, call logs, photos, location and documents. Researchers assessed that the campaign was administered from a building belonging to the Lebanese General Security Directorate in Beirut. It was one of the first public demonstrations that nation-state mobile spyware was not confined to a handful of high-value phones.

**Detection:** App provenance and sideloading checks, mobile threat defence, and network indicators for the command-and-control domains. The campaign also showed why "is this app in the store?" is not a sufficient test: distribution relied on social engineering and fake or repackaged apps.

**Coverage:** [EFF press release](https://www.eff.org/press/releases/eff-and-lookout-uncover-new-malware-espionage-campaign-infecting-thousands-around) · [Lookout technical report](https://www.lookout.com/threat-intelligence/article/dark-caracal-mobile-apt) · [Lookout PDF](https://www.lookout.com/documents/reports/lookout-dark-caracal-20180118-us.pdf)

### Project Raven: mercenary hacking at state scale

**Programme:** A covert hacking unit of former NSA operators, later inside the UAE firm DarkMatter · **Targets:** dissidents, journalists, activists, foreign officials and US persons · **Established by:** Reuters, January 2019

Reuters' investigation revealed Project Raven, a UAE programme staffed largely by former US intelligence personnel that hacked the accounts and devices of the state's critics. It began in 2014 and moved into DarkMatter in 2016. Former employees described targeting US citizens and said the mission had crossed a line; the reporting also showed how commercial cover — a cybersecurity company — can host an offensive unit. Later US action debarred former operatives from certain export privileges.

**Detection:** The cases were account takeovers and device compromises rather than a branded spyware product, so detection looked like phishing triage, mailbox audit, and mobile forensics. The more important lesson is structural: mercenary capacity can be bought, and the vendor may be a company with a legitimate security business.

**Coverage:** [Reuters investigation](https://www.reuters.com/investigates/special-report/usa-spying-raven/) · [CyberScoop on the US response](https://cyberscoop.com/former-us-intelligence-ops-state-department/)

### SolarWinds: a supply-chain backdoor at mass scale

**Platform:** SUNBURST backdoor in SolarWinds Orion · **Reach:** about 18,000 customers downloaded the trojanised update; dozens were followed up with hands-on intrusion · **Established by:** FireEye, Microsoft, CISA

In December 2020, FireEye disclosed that its own breach had led it to a supply-chain compromise of SolarWinds Orion. Attackers had inserted the SUNBURST backdoor into legitimate, digitally signed Orion updates; about 18,000 customers downloaded them, and a smaller number — including US Treasury, Commerce and the Department of Homeland Security — were singled out for further intrusion. The United States and United Kingdom later attributed the campaign to Russia's SVR, tracked as APT29 and NOBELIUM. It was a mass deployment in the precise sense: the malware reached far more organisations than were ever targeted, and trust in a signed update was the delivery mechanism.

**Detection:** Anomalous signed binaries, DNS beacons to attacker infrastructure, identity and cloud logs, and supply-chain provenance checks. EDR that trusted signed software needed behavioural rules; the incident pushed SBOMs and vendor-risk review into mainstream practice.

**Coverage:** [Microsoft analysis](https://www.microsoft.com/en-us/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/) · [FireEye report via Google Cloud](https://cloud.google.com/blog/topics/threat-intelligence/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor) · [CISA advisory AA20-352A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a)

### Salt Typhoon: compromising the wiretap infrastructure

**Actor:** China-linked group tracked as Salt Typhoon · **Targets:** US telecommunications carriers and internet providers, including lawful-intercept systems · **Established by:** FBI, CISA, congressional researchers

In late 2024, US agencies confirmed that a China-linked actor had compromised the networks of multiple US telecommunications carriers and internet providers. The intruders reached lawful-intercept systems — the infrastructure carriers maintain to execute court-ordered wiretaps — and stayed in some networks for months. The campaign matters less as mobile spyware than as the weaponisation of the carriers' own surveillance plumbing: the collection capability was already built, and the attackers took it over. CISA and international partners published hardening guidance in 2025, and the Congressional Research Service documented the federal response.

**Detection:** Telecom-side signalling and log analysis, router and configuration integrity, lawful-intercept system audits, and netflow. Endpoint spyware scanning cannot see this class of compromise; it is a network-integrity and provider-accountability problem.

**Coverage:** [CISA joint advisory AA25-239A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a) · [Congressional Research Service report](https://www.congress.gov/crs_external_products/IF/PDF/IF12798/IF12798.14.pdf)

## Stalkerware

Stalkerware is consumer-grade spyware sold to individuals, usually to monitor a partner or family member. The cases below are included because they show the same detection and accountability dynamics at a smaller scale.

### SpyFone and the first FTC stalkerware ban

**Product:** SpyFone, HiddenApp · **Targets:** thousands of people monitored without consent · **Established by:** US Federal Trade Commission

In September 2021, the FTC banned SpyFone and its CEO from the surveillance business and ordered the company to delete data it had collected. The agency found that the company had marketed its apps for covert monitoring, failed to secure the data, and exposed victims' information. It was the first FTC ban of its kind and set a precedent for treating stalkerware as a consumer-protection problem, not just a privacy one.

**Detection:** Stalkerware usually requires device administrator privileges or a sideloaded app on Android, and a configuration profile or jailbreak on iOS. Checking device administrators, accessibility services and profiles is a fast first pass; a factory reset is often the only reliable cleanup.

**Coverage:** [FTC announcement](https://www.ftc.gov/news-events/news/press-releases/2021/09/ftc-bans-spyfone-ceo-surveillance-business-orders-company-delete-all-secretly-stolen-data)

### TheTruthSpy: a stalkerware network and its leaks

**Product:** TheTruthSpy and affiliated apps · **Targets:** tens of thousands of devices, largely in the US and Europe · **Established by:** TechCrunch, Malwarebytes, independent researchers

In October 2022, TechCrunch identified TheTruthSpy as a network of stalkerware apps operating under multiple names and exposed its weak security. Subsequent research found that the service had leaked victims' data, and in 2025 Malwarebytes reported a further flaw that exposed more victims. The case illustrates a recurring pattern: stalkerware vendors collect extremely sensitive data with little security, so the people being monitored are harmed twice — first by the surveillance, then by the breach.

**Detection:** Look for known package names and C2 domains, unusual battery or data use, and apps with device-administrator rights. Because the apps are rebranded frequently, indicator lists go stale; behaviour-based checks age better.

**Coverage:** [TechCrunch investigation](https://techcrunch.com/2022/10/26/inside-thetruthspy-stalkerware/) · [Malwarebytes, 2025](https://www.malwarebytes.com/blog/news/2025/08/more-vulnerable-stalkerware-victims-data-exposed-in-new-thetruthspy-flaw)

## Accountability and policy

Court cases, sanctions and export controls increasingly determine what spyware is available and who can be held responsible. These are the main public milestones.

- **March 2024** — The US Treasury sanctioned members of the Intellexa consortium, including Tal Dilian and Sara Hamou, for trafficking in commercial spyware. [Treasury press release](https://home.treasury.gov/news/press-releases/jy2155)
- **April 2024** — The European Parliament adopted the PEGA committee's recommendations on Pegasus and equivalent spyware, calling for stronger controls and victim support.
- **May 2025** — A US court found NSO Group liable in WhatsApp's lawsuit. [Amnesty statement](https://www.amnesty.org/en/latest/news/2025/05/ruling-against-nso-group-in-whatsapp-case-a-momentous-win/)
- **February 2026** — The Treasury removed three Intellexa-linked people from its sanctions list, prompting criticism from US lawmakers. [CyberScoop](https://cyberscoop.com/treasury-removes-intellexa-spyware-linked-trio-from-sanctions-list/)

Sanctions and court rulings are not detection tools, but they change the threat landscape: they can freeze a vendor's operations, expose ownership networks, and give victims a route to evidence that device analysis alone cannot provide.

## Corrections

This file is maintained alongside the main list. If a date, attribution or link is wrong, open an issue or a pull request with the primary source. Do not add a case on the strength of a single news report if a technical report or court document is available; link the strongest source and note what remains unresolved.
