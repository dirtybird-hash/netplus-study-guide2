# CompTIA Network+ (N10-009) — Master Study Guide

**Built from 23 course transcripts (Days 1–18), reorganized by exam domain.**
**Lab-ready for Cisco Packet Tracer 9.0.1.** Lab stubs are marked 🔧 — call **TORA** to have any of them expanded into a full build with step-by-step instructions, exact configs, and break/fix challenges.

---

## How to use this guide

This is reorganized **by exam domain**, not by course day, because the exam tests by domain. Each section is cross-referenced back to its source transcript so you can go re-watch the original.

Reading order that works:

1. **First pass** — read a domain end to end, ignore the 🔧 stubs. Build the map.
2. **Second pass** — work the *Exam traps* boxes. These are where the test writers live.
3. **Third pass** — call **TORA** on the labs for that domain. Build it, break it, fix it.
4. **Drill** — Appendix A (ports), Appendix B (subnetting), Appendix C (commands) are pure memorization. Do these daily, not in a block.

**Notation used throughout:**

| Mark | Meaning |
|---|---|
| 🔧 | Packet Tracer lab stub — call TORA to expand |
| ⚠️ | Exam trap — commonly missed or deliberately confused |
| 📌 | Memorize verbatim — likely a direct recall question |
| 🔗 | A+ crossover — you already know this, connect it forward |

---

## Exam at a glance

| Domain | Weight | Where it lives in this guide |
|---|---|---|
| 1.0 Networking Concepts | 23% | Part 1 — sections 1.1–1.8 |
| 2.0 Infrastructure | 20% | Part 2 — sections 2.1–2.4 |
| 3.0 Network Operations | 19% | Part 3 — sections 3.1–3.5 |
| 4.0 Network Security | 14% | Part 4 — sections 4.1–4.3 |
| 5.0 Troubleshooting & Tools | 24% | Part 5 — sections 5.1–5.5 |

**Format:** max 90 questions, 90 minutes, 720/900 to pass. Multiple choice plus performance-based questions (PBQs).

⚠️ Domains 5.0 and 1.0 together are **47% of the exam**. Troubleshooting is the single heaviest domain and it is where most people lose points, because it is applied rather than recall. Do not treat it as the chapter you get to last.

📌 **The PBQ reality:** performance-based questions typically ask you to drag cables to the right ports, configure a small addressing scheme, place devices in a topology, or step a scenario through the troubleshooting methodology. Every one of those is something you can rehearse in Packet Tracer. That is why this guide is lab-heavy.

---

## Source material

| Source | Feeds |
|---|---|
| Day 1 — The OSI Reference Model · Understanding OSI | 1.1 |
| Day 2 — Network Topologies, Architectures & Types | 1.5, 1.6, 2.3 |
| Day 3 — Cables & Connectors | 1.5 |
| Day 4 — Networking Appliances | 1.2 |
| Day 5 — Ethernet Switching & Wireless Standards | 2.2, 2.3 |
| Day 6 — IPv4 Network Addressing | 1.7 |
| Day 7 — IP Addressing Schemes and Subnetting | 1.7 |
| Day 8 — Routing & Switching Technologies | 2.1, 2.2 |
| Day 9 — Network Implementations | 2.1, 2.4 |
| Day 10 — Ports & Protocols | 1.4 |
| Day 11 — Modern Network Environments | 1.8 |
| Day 12 — Troubleshooting Network Issues | 5.2, 5.3, 5.4, 5.5 |
| Day 13 — Disaster Recovery & High Availability | 3.3 |
| Day 14 — Network Management & IP Services | 3.4, 3.5 |
| Day 14 — Network Operations | 3.1, 3.2 |
| Day 15 — Network Security Concepts & Solutions | 4.1 |
| Day 15 — Physical Security & Network Hardening | 4.3 |
| Day 16 — Network Monitoring & DR Concepts | 3.2, 3.3 |
| Day 16 — Troubleshooting Methodologies | 5.1 |
| Day 17 — Wireless Configurations & Physical Installations | 2.3, 2.4 |
| Day 18 — Cloud Computing Concepts | 1.3 |
| Day 18 — Organizational Processes & Procedures | 3.1 |
| **Written from scratch** | **4.2 Attacks · 5.4 performance content** |

*(Day 4 and Day 13-PortsProtos in the source folder duplicate Day 4-Appliances and Day 10.)*

📌 **Section numbering follows the published CompTIA N10-009 objectives.** An earlier revision of this guide numbered several sections incorrectly — Domain 2 had routing and switching swapped, Domain 3 had documentation and IP services swapped, and Domains 4 and 5 were missing sections entirely. See the changelog.

⚠️ **Professor Messer's course notes are *not* a source for this guide.** They are copyrighted and separately purchased. **Appendix G** cross-references this guide to their page numbers so the two can be read side by side.

---
# PART 1 — Networking Concepts (Domain 1.0, 23%)

## 1.1 The OSI Reference Model

*Source: Day 1 — The OSI Reference Model; Understanding OSI*

### What the OSI model actually is

The OSI model comes from the **ISO** (International Organization for Standardization) — the same body that standardizes everything from accounting practices to shipping container dimensions. It is **not software, not hardware, and not a protocol suite.** It is a set of guidelines telling manufacturers *what functions must happen* at each stage of network communication, while leaving *how* to implement them entirely up to the vendor.

That distinction is the whole point. Because every vendor agrees on the functional boundaries, an Ethernet NIC from one company works with a switch from another, and an email sent from Windows arrives readable on Linux.

⚠️ **Trap:** The exam will offer "OSI is a protocol suite" or "OSI defines which frequencies Wi-Fi uses" as distractors. It does neither. The protocols we actually run are TCP/IP; OSI is the *model we map them onto*. And OSI says frequencies must be defined — it does not define them. The IEEE and FCC do that.

### The seven layers

Top down, 7 → 1:

| # | Layer | One-word job | PDU | Lives here |
|---|---|---|---|---|
| 7 | Application | User interface | Data | HTTP/S, FTP, DNS, POP3, SMTP, DHCP |
| 6 | Presentation | Translation | Data | ASCII/EBCDIC, JPEG/MOV encoding, compression, SSL/TLS encryption |
| 5 | Session | Conversation control | Data | Session setup/teardown, checkpoints, tunneling, NetBIOS, RPC, NFS |
| 4 | Transport | End-to-end delivery | Segment (TCP) / Datagram (UDP) | TCP, UDP, port numbers |
| 3 | Network | Routing | Packet | IP, IP addresses, subnet masks, routers, NAT, fragmentation |
| 2 | Data Link | Node-to-node | Frame | MAC addresses, switches, Ethernet, PPP, HDLC |
| 1 | Physical | Bits on the wire | Bit | Cables, fiber, connectors, radio signals, NICs |

📌 **Mnemonics.** Top down (7→1): **All People Seem To Need Data Processing.** Bottom up (1→7): **Please Do Not Throw Sausage Pizza Away.** Learn both directions — questions come at you from either end.

### Layer by layer, with what you'll actually be asked

**Layer 1 — Physical.** "Bedknobs and broomsticks — things you can lay your hands on." Cables, fiber, connectors, NICs, the signal itself, frequencies, bit rate. Also *encoding* (how a 1 vs a 0 is represented) and *media access* rules like the old CSMA/CD. Any two distinguishable states can encode binary — two light frequencies, presence/absence of light, even sonar tones between submarines.

Layer 1 troubleshooting = loopback tests, cable testers, checking adapters, looking for wireless interference.

**Layer 2 — Data Link.** Node-to-node delivery. This is where the **frame** is built by adding physical (MAC) addressing to whatever came down from Layer 3. Responsibilities: physical addressing, framing, media access control, flow control, and error control (which at this layer means *retransmission of a frame*).

The MAC address is a **12-character hexadecimal** value burned into the NIC. First half identifies the manufacturer (the OUI), second half is the node address. Globally unique by registration.

Layer 2 splits into two sublayers:
- **LLC (Logical Link Control)** — interfaces up to the network layer, handles connectionless vs connection-oriented behavior
- **MAC (Media Access Control)** — interfaces down to the physical media, owns the hardware address

⚠️ **Trap:** "MAC" here is **Media Access Control**, nothing to do with Apple. Expect this to be tested as a definition question.

Layer 2 protocols named in the course: SDLC, HDLC, SLIP, PPP, LAP. Switches are Layer 2 devices — they forward on destination MAC.

**Layer 3 — Network.** Connects nodes *across* multiple networks, where Layer 2 only got you across one. Builds the **packet** and applies logical (IP) addressing. Functions: packetizing, logical addressing, **fragmentation** (chopping packets down when a downstream network can't carry the original size, and labeling the pieces for reassembly), routing (best-path determination), internetworking, and address conversion via **NAT**.

**Layer 4 — Transport.** End-to-end delivery. The "post office layer." Creates a single logical pipeline so the upper layers never have to know what the network in between looks like. Owns:
- **TCP** — connection-oriented, sequenced, error-checked, three-way handshake
- **UDP** — connectionless, no error checking, faster
- Port numbers ("service point addressing")
- Session multiplexing, message acknowledgement, traffic control

The **three-way handshake**: PC1 proposes a starting sequence number, PC2 acknowledges and proposes its own, and both increment as data flows. Each side's acknowledgement tells the other *which sequence number it expects next* — which is how missing data gets detected and retransmitted, and how out-of-order arrivals get reassembled in the right order.

📌 The connection-oriented vs connectionless split is the same idea at Layers 2 and 4. **Streaming video → connectionless.** If a frame of a hockey game drops, retransmitting it is useless — the puck has already gone behind the net, and replaying a past moment is worse than a brief dropout. **Financial data → connection-oriented.** Every byte of that invoice has to arrive.

**Layer 5 — Session.** Establishes, maintains, and gracefully terminates conversations. Establishment covers finding the far end *by name*, negotiating parameters (encryption? QoS?), and **logging in**. Maintenance includes **checkpoints** — so a failed 10 GB transfer resumes partway rather than restarting. Termination is the graceful shutdown.

Also owns dialog control: **simplex** (one way only), **half-duplex** (both directions, not simultaneously), **full-duplex** (both directions at once, if hardware and software support it).

Protocols cited: NetBIOS, DNS, RPC, NFS.

**Layer 6 — Presentation.** The "translation layer." Converts application formats into a common wire format and back. Character encoding (**ASCII** and **EBCDIC**), data conversion (serial stream ↔ block format, integers, floating point, CRLF), **compression**, and **encryption/decryption**.

⚠️ **Trap worth understanding, not just memorizing:** the course places **SSL/TLS encryption at Layer 6.** Some other sources put TLS at 5, or argue it spans 5–7. In the Wireshark walkthrough, SSL is described as encapsulating layers 5, 6, and 7 together. For the exam, if a question asks where *application encryption/decryption* happens, answer **Presentation (6)**.

**Layer 7 — Application.** The interface between the user (or a user-facing application) and the network stack. Not just browsers — a word processor saving to a network drive traverses the whole stack. Protocols: HTTP, FTP, DHCP, DNS, SMTP, POP3.

📌 Protocols, not applications, are what make interoperability work. Chrome and Firefox interoperate with any web server because they all speak HTTP/HTML — not because the browsers are alike.

### Peer-layer communication

Each layer on the sending device communicates logically with **the same layer** on the receiving device. The session layer on PC1 authenticates against the session layer on PC2. Data physically travels 7→1 down the sender, across the medium (through intermediate devices that operate at their own layers), then 1→7 up the receiver.

**Encapsulation** is the term for adding layer information as data moves down the stack. Decapsulation is stripping it on the way up.

### Mapping the real world to layers

This is the highest-value table in the section. The exam asks "at what layer is X?" constantly.

| You see / hear | Layer |
|---|---|
| Bad cable, bad fiber, wireless interference, loopback test | 1 |
| Ethernet frame, MAC address, EUI-48 / EUI-64, switch, switching | 2 |
| IP address, subnet mask, router, routing, NAT, fragmentation | 3 |
| TCP port, UDP port, segment, three-way handshake | 4 |
| Session start/stop/restart, tunneling, control protocols | 5 |
| SSL/TLS encrypt-decrypt, ASCII/EBCDIC, compression, JPEG | 6 |
| The application itself, what's on the screen, HTTP/FTP/DNS | 7 |

### The Wireshark decode — read it as a layer stack

The course walks a captured frame in Wireshark. Learn this as a pattern, because it appears in troubleshooting questions:

| Wireshark line | Layer |
|---|---|
| `Frame 88: 2005 bytes on wire` | 1 |
| `Ethernet II, Src: …, Dst: …` | 2 |
| `Internet Protocol, Src: 72.14.247.19` | 3 |
| `Transmission Control Protocol, Dst Port: 443` | 4 |
| `Secure Sockets Layer` (encapsulates the rest) | 5, 6, 7 |

Reading top-to-bottom in the Wireshark detail pane = reading **bottom-up** through the OSI model.

### Why the model matters operationally

Two reasons the exam cares:

1. **Common language.** Say "layer 3 problem" and every engineer in any organization knows you mean IP/routing.
2. **Troubleshooting isolation.** Symptoms point to layers. No link light → Layer 1. Can ping by IP but not by name → Layer 7 (DNS). Can reach local hosts but not remote → Layer 3.

🔗 **A+ crossover:** you already troubleshoot this way — check the cable before you reinstall the OS. OSI just gives the instinct a formal structure.

### 🔧 LAB 1.1 — OSI Layer Isolation Walkthrough *(call TORA)*
Build a two-switch, one-router topology and deliberately induce a failure at Layers 1, 2, 3, and 7 in sequence. Use Packet Tracer's Simulation Mode with PDU inspection to watch encapsulation happen frame by frame, then diagnose each break by layer.

---
## 1.2 Networking Appliances, Applications, and Functions

*Source: Day 4 — Networking Appliances*

### Switches

The most common device on a corporate network and the point of contact for endpoints.

**How a switch learns.** When a host sends its first frame, that frame always contains the host's own source MAC address. The switch records **MAC address → port** in its MAC address table. It repeats this for every host that transmits.

**What happens on a cache miss.** If a frame arrives for a destination MAC the switch doesn't know, it **floods** the frame out **all ports** looking for the destination. Once it learns that MAC, flooding stops for that address.

📌 This is why switched networks are quieter than hubbed ones — after the initial learning period, traffic is delivered only to the correct port instead of every port.

**Layer 2 vs Layer 3 switch:**

| | Layer 2 switch | Layer 3 switch |
|---|---|---|
| Forwards on | MAC address | IP address |
| Unit of data | Frame | Packet |
| Routing | No | Yes (limited vs a router) |
| Scope | Within one LAN only | Within and **between** LANs/VLANs |
| Speed | Fast | Fast — **faster than a router** |
| Cost | Lower | Higher; higher port density |
| Where | Access layer | Distribution layer, large enterprise |

⚠️ **Why a Layer 3 switch beats a router on speed:** a router does much deeper packet analysis — QoS classification, richer policy, more inspection — not just a destination-IP lookup. Dollar for dollar, a router is slower than a Layer 3 switch at the pure inter-VLAN forwarding job.

**ARP — the glue between Layer 3 and Layer 2.** Data ultimately has to leave through a NIC, and NICs address by MAC. **Address Resolution Protocol** resolves a known **logical address (IP)** into the **physical address (MAC)** needed for final delivery on the wire.

📌 **VLANs.** A single physical switch can be logically divided — take a 24-port switch, put 12 ports in one LAN and 12 in another. Hosts within a VLAN reach each other freely; traffic *between* VLANs must be routed, which is exactly where you apply control. **You need a Layer 3 device (router or Layer 3 switch) to route between VLANs.**

### Routers

Connects two or more **packet-switched** networks. On receiving data, a router **strips the framing information and the MAC address**, examines the destination IP, and uses the **network portion** to make a forwarding decision.

- If the destination network is **not** directly connected → find the best route, forward to the next hop.
- If the destination network **is** directly connected → examine the **host portion** and deliver to that host.

**Routing tables** are built manually (static) or automatically via **routing protocols** that share information between routers.

**Router types by role:**

| Type | Position |
|---|---|
| **Core** | Center of large networks; moves data between major networks, buildings, thousands of users |
| **Edge** | Between the corporate network and the outside — other organizations, the internet |
| **Distribution** | Closer to clients; heavy inter-VLAN routing; connects user-facing networks |
| **Wireless** | Home: multifunction (AP + switch + router + WAN). Corporate: wireless is usually a separate device on a switch, routing still done by routers |
| **Virtual** | Software routers inside virtualized/cloud environments, moving traffic between VMs |

**Purchase considerations:** connectivity (interface count and types), setup and management (serial console vs web management), security feature depth, flexibility (expansion slots for fiber or extra Ethernet), wireless capability, **bandwidth vs throughput**, automatic updates, QoS controls, interface count for mesh designs, and guest network / per-user isolation.

⚠️ 📌 **Bandwidth ≠ throughput.** A router may have six gigabit interfaces and still be unable to actually pass six gigabits — throughput depends on the internal system board, processor, and **how much inspection the enabled security features are doing**. This distinction shows up in scenario questions about a "slow" router that is nominally fast enough.

### Load balancers

Sits between users and back-end servers and **distributes incoming requests** across multiple machines (often virtual servers).

**What it delivers:**
- **High availability / reliability** — if a back-end server fails, the user doesn't see it, because the user is connected to the load balancer, which they perceive *as* the server. The request is seamlessly served by another server holding the same content.
- **Scalability** — spin up more virtual servers as load grows; the load balancer starts using 4 or 5 instead of 3, invisibly to the user.
- **Application security** — control which users or groups reach which applications; external users see one set of resources, internal users another.
- **Application performance** — hold response times steady under increasing load.

📌 **Distribution is not just round-robin.** Load balancers continuously monitor the traffic and load on back-end servers and can direct a request to **the server with the least load**.

### Proxy servers

Works **on behalf of the internal client**. The client's request is intercepted; **the proxy** goes out to the internet, not the client.

**Benefits:**
- **Usage control** — restrict which sites are reachable and at what times of day.
- **Bandwidth saving via caching** — the proxy fetches and caches the page locally. The second user requesting it is served from the local cache over the fast internal network instead of the slow internet link.
- **Privacy** — external servers see only the proxy making requests, never the internal clients.
- **Security concentration** — you can harden *one* proxy thoroughly rather than trying to harden 3,000 workstations and making mistakes.

**Features:** access control via **URL filtering** (or IP ranges), **content scanning** (inbound malware and inappropriate content), and **outbound inspection** — catching things like Social Security numbers leaving the organization. Exemptions can be granted per-user or by username/password.

⚠️ **Proxy vs load balancer, stated as the exam wants it:** a **proxy acts on behalf of the client** (forward, outbound). A **load balancer acts on behalf of the servers** (inbound distribution). Direction is the discriminator.

### Firewalls

A security device that stops unauthorized access **between networks** and monitors traffic in **both directions** — it can block traffic leaving as well as entering. What it stops depends entirely on **administrator-defined policy**. Usually placed between the untrusted outside (internet) and the trusted inside, but it can be deployed internally too.

**Hardware vs software:** a hardware firewall is a purpose-built self-contained appliance. A software firewall (e.g. the one built into Windows) is one component among many on a host, protecting that host's network connection.

**Firewall types by OSI layer** — this table is heavily tested:

| Type | OSI layer | Filters on |
|---|---|---|
| **Packet filtering** | Network (3) | IP addresses — source/destination, network portion |
| **Circuit-level** | Transport (4) | **Port numbers** (HTTP 80, SMTP 25) |
| **Application firewall** | Application (7) | **Entire reassembled files/messages** — e.g. scanning an email body for credit card numbers |
| **Stateful** | Tracks connection state | Whether the session was initiated from inside |
| **Next-generation (NGFW)** | Multiple | Combines the above across several layers |

📌 **Stateful firewall, worked example** (this is the classic exam scenario): your browser requests a page on **port 80**. Your PC picks a random source port, say **3355**, for the reply. The web server responds to 3355 and the stateful firewall **allows it, because the PC initiated the connection.** An unsolicited inbound connection to port 3355 from outside is **blocked**, because no internal host started it.

⚠️ An application-layer firewall has to **reassemble the entire message** to inspect it — that's why deeper inspection costs more money and more processing.

**The DMZ / screened subnet.** Place one firewall at the internet perimeter and a second behind it; the space between is the **DMZ (demilitarized zone)**. Put the web server there. Open port 80 on the **outer** firewall so the public can reach it; **close port 80 on the inner** firewall. Internal users retrieve data from the server on a *different* port that is open on the inner firewall only. **If the web server is attacked, only the DMZ host is exposed — the internal network isn't reachable from it.**

**Purchase considerations:** technical objectives, placement, required speed, which OSI layer it must inspect at, traffic inspection depth, and cost — deeper inspection is more expensive because it must maintain throughput while doing more work.

### IDS and IPS

An **Intrusion Detection System** monitors for malicious activity, suspicious traffic patterns (unusual increases or decreases), and **security policy violations** — for example, users on one network reaching a network they shouldn't.

📌 ⚠️ **The IDS/IPS distinction is about placement, and this is the single most tested fact here:**

| | IDS | IPS |
|---|---|---|
| Placement | **Out-of-band** — monitors a copy of traffic | **In-band / in-line** — all traffic passes through it |
| Action | **Alerts.** Traffic keeps flowing | **Blocks.** Can automatically stop traffic |
| Risk of a false positive | Nuisance alert | **Stops legitimate traffic — network work halts** |

Many products do both. **Standard practice: deploy in detection mode first**, spend the first few months tuning and identifying false alarms, then enable prevention once you trust its judgment.

**Classification by location:**
- **NIDS (network-based)** — inspects all traffic across the network.
- **HIDS (host-based)** — software running on a **high-value asset**, e.g. the server holding the financial database, giving extra scrutiny to traffic in and out of that host specifically.

**Classification by detection method:**

| | Signature-based | Anomaly-based |
|---|---|---|
| How | Downloads a vendor signature database on a schedule; matches traffic against known threats | Observes the network with admin input to learn what "normal" looks like over days or weeks |
| Strength | Reliable on known threats | **Adaptable; can catch a threat faster than signatures, including things not yet in any database** |
| Weakness | **Misses anything not in the database** | **More prone to false positives** |

**Advantages of IDS:** false positives can be tuned out ("that Friday traffic spike was the sale"); data examined in **protocol context** (web requests crossing a network segment with no web servers is worth a look); supports **post-attack analysis** by preserving what the network looked like during the attack; supports **compliance** evidence; and improves general efficiency by surfacing things like broadcast storms from a misconfigured device.

⚠️ **IDS limitations — expect these as "which is a weakness" questions:**
- **Source addresses can be spoofed**, and this is very hard for an IDS to detect.
- **Encrypted packets can't be read** without decryption keys. An attacker can flood an IDS with encrypted traffic that passes through uninspected — or simply overwhelms the system.
- **Analytic limitations** — both the system's analysis capability *and* whether the humans reading the output can distinguish a real threat from noise.
- **False alarms**, which on an IPS means shutting down production traffic.

### NAS vs SAN

**NAS (Network Attached Storage).** A device with multiple disks, connected to the **Ethernet** network through a switch, sharing files to many computers. Files appear to users like an ordinary Windows share — find it by name, log in with credentials, access files. Managed through its own built-in web page over HTTPS.

- **File-level** access using standard network protocols: **NFS** (Linux) and **SMB** (Windows).
- Lower cost, easy administration, RAID redundancy (mirroring, RAID 5), scalable both by adding drives and by buying more units.
- 📌 **Faster and cheaper than cloud storage** for local use — cloud access goes over the internet link, which is far slower than the internal network, and carries an ongoing cost rather than a one-time purchase.

**SAN (Storage Area Network).** Far more robust — built for high-performance and mission-critical applications. Runs on a **fiber network** in the background with a **Fibre Channel switch**, not an Ethernet switch.

📌 ⚠️ **The core difference:** NAS is **file-level over Ethernet in packets**. SAN is **block-level**, and the storage **appears to the client as a directly attached device like a local hard disk**. That is why SAN transfers are much faster.

SAN characteristics: more expensive units, much faster drives, RAID arrays, massive scalability (limited mainly by the network), a dedicated **metadata server** managing the RAID arrays with its own OS, and strong disaster recovery through multiple drives across multiple cabinets and servers.

*Use case given:* video editors sharing large media files can be connected **directly to the Fibre Channel switch by fiber**, off the Ethernet network entirely, because they need that throughput.

### Wireless access points

A special-purpose device for WLANs that acts as a **bridge between the wired and wireless networks**. Every AP eventually connects to a wired network to reach resources like the internet.

- **Home:** a multifunction device — AP + switch + router + internet connection in one box.
- **Corporate:** a **separate device**, typically ceiling-mounted, with an Ethernet run back to a switch in the closet. Multiple APs are managed **centrally** from a wireless controller.

📌 APs on different switches may be on **different subnets** (traffic between them must route) **or share the same subnet** — both designs are common.

**Client-side connection options:** built-in adapters (most modern laptops and mobile devices), PC card adapters (older laptops), USB adapters, and expansion-slot cards (desktops, which usually lack built-in wireless).

**Why wireless needs stronger security than wired.** On copper, the conversation is inside the cable — eavesdropping requires physical access to the closet. On wireless, **the signal is floating in the air and anyone with an adapter can monitor it.** Hence more robust, and different, security controls.

**Benefits:** extends service where wired is impractical or too expensive; **external APs** mounted on building exteriors provide outdoor campus coverage that wiring can't reasonably deliver.

**Wireless threats introduced here:**

| Threat | What it is |
|---|---|
| **SSID broadcast** | The network name, broadcast so clients can find it. You *can* hide it, but ⚠️ **hiding the SSID is weak security** — freely downloadable software can force the AP to reveal it |
| **Rogue AP** | An unauthorized AP connected to the company network. 📌 **Often not an attacker at all** — just an employee who wanted wireless and plugged one in. Doubly dangerous because that employee lacks the skill to secure it, so any passerby can get in |
| **Evil twin** | An AP broadcasting **the same SSID as a legitimate one**. Users see two identical networks and pick one essentially at random, not realizing one is malicious |

### CDN — Content Delivery Network

A **worldwide collection of caching servers** that serve content to local users, reducing latency and improving application response time.

**How it works.** Your origin server is in Canada. A user in Europe requests content by URL. The request is intercepted and served by a **CDN point-of-presence (PoP) server** in Europe. **Origin servers periodically push updated content** to the PoP servers so cached content stays fresh. The next European user is served locally instead of pulling across transoceanic fiber.

**Used for:** web applications, **media files and streaming video** (bandwidth-heavy, so proximity helps a lot), and corporate cloud storage.

⚠️ **Pricing scales with data volume** — a static web page is far cheaper to serve than gigabytes of cloud storage.

**Configuration options:**
- **Geo-filtering** — allow or deny based on **source IP**, since IP ranges are allocated to countries. Used to block content in jurisdictions where it isn't permitted.
- **Content compression** — browsers check whether a site supports compression; enabling it reduces data transferred and speeds access.
- **Caching rules / site acceleration** — cache specific content where it's actually used (English pages in the US, French pages in France). Faster *and* cheaper.
- **Custom domains** — create subdomains pointing at caching servers so content appears to originate closer to the user.

### QoS — Quality of Service

Manages traffic to reduce **packet loss, latency, and jitter**, and lets an organization prioritize traffic for higher-performing applications. Less important traffic **waits** so that important traffic goes first.

📌 ⚠️ **"Important" here means delay-intolerant, not business-critical.** A payroll file is business-critical, but it can arrive slightly out of order with small delays and still reassemble perfectly. **Video cannot.** This inversion is a favorite exam trick — the correct answer prioritizes voice and video *over* a financial transfer, even though the financial data is "more important" in a business sense.

**Delay-sensitive traffic:** IPTV, gaming, **VoIP**, streaming media, video conferencing.

**Mechanism:** a **code is inserted into the frames** of prioritized traffic. Switches and routers along the path read these markings and prioritize accordingly, holding other traffic.

### VPN — Virtual Private Network

An **encrypted connection** between two endpoints. The source scrambles, the destination unscrambles.

**Deployment shapes:**
- **Host-to-host** — PC to PC, or PC to server.
- **Site-to-site** — internal traffic is unencrypted, but traffic leaving for a branch office in another country is encrypted at the boundary and decrypted on arrival.
- **Remote access** — from the business demarc to a home worker's computer.

📌 It's **"virtual"** because it isn't a separate physical network — it traverses the public network (telephone or cable infrastructure), but encryption makes it function as a private one. Anyone intercepting it sees scrambled traffic because they lack the keys.

### TTL — Time to Live

A mechanism built into IP to manage packet lifespan. A misdirected packet could otherwise bounce between routers indefinitely, clogging the network. **TTL is a hop count, not a clock** — each router decrements it, and when it reaches zero the packet is discarded.

⚠️ **Correction to the source material.** The transcript states the default TTL is 16 hops. That figure is **RIP's maximum hop count (16 = unreachable/infinity)**, not the IP TTL default. Real IP TTL defaults are typically **64 (Linux/macOS), 128 (Windows), or 255 (many network devices)**. Know the real numbers — the 64/128 distinction is genuinely useful, because a `ping` reply's TTL value hints at the responding OS and how many hops away it is.

### 🔧 LAB 1.2 — Appliance Placement and Traffic Control *(call TORA)*
Build an enterprise topology with a DMZ (dual firewall), an internal Layer 3 switch doing inter-VLAN routing, a server farm, and wireless APs. Verify MAC learning and flooding behavior in Simulation Mode, prove the stateful firewall's inbound/outbound asymmetry, and demonstrate ARP resolution frame by frame. Break/fix: rogue AP introduction, evil twin, and a misconfigured DMZ rule that exposes the internal network.

---
## 1.3 Cloud Computing Concepts and Connectivity

*Source: Day 18 — Cloud Computing Concepts*

### The basic proposition

Cloud providers let organizations run applications in the provider's data centers instead of buying hardware and software themselves. The organization **rents** compute, storage, and networking rather than owning it.

### Service models

📌 The exam tests these constantly, usually as "who manages what."

| Model | You manage | Provider manages | Example use |
|---|---|---|---|
| **IaaS** (Infrastructure as a Service) | OS, middleware, runtime, applications, data | Virtualization, servers, storage, networking | You want VMs and control over them |
| **PaaS** (Platform as a Service) | Applications and data only | Everything below — including OS and runtime | Developers who want tools ready to go without provisioning servers |
| **SaaS** (Software as a Service) | Nothing but your data and user configuration | Everything | Email, CRM, productivity suites |

📌 **The memory hook:** as you move IaaS → PaaS → SaaS, **you manage less and the provider manages more.** SaaS uses a **software distribution model** — the application is centrally hosted and licensed by subscription rather than installed and owned.

### Deployment models

| Model | Where it lives | Key characteristics |
|---|---|---|
| **Public cloud** | Provider's infrastructure, shared | Offers infrastructure, resources, applications, and storage. Lowest cost of entry, maximum elasticity. ⚠️ Risk of **vendor lock-in**, and interconnecting multiple cloud vendors can be difficult |
| **Private cloud** | The organization's **own data center** | Full control over data and its management. Used where regulation demands it — 📌 **government organizations that must guarantee data stays under their own lock and key** |
| **Hybrid cloud** | Both | Host a private cloud for sensitive workloads, use public cloud for **elasticity** and **speed to market** |
| **Community cloud** | Shared by organizations with common requirements | Shared compliance or industry concerns |

📌 **The hybrid use case worth remembering:** a development team needs an environment fast. Sourcing servers, licensing software, and setting it all up creates long lead time. Spinning up **PaaS with tools ready to go** collapses that lead time. Meanwhile the regulated data stays in the private cloud. That's the efficiency-and-performance argument for hybrid in one sentence.

### VPC — Virtual Private Cloud

Your **logically isolated section** of a public cloud provider's infrastructure. Private in the sense that the resources are dedicated to you, even though the underlying physical infrastructure is shared.

**VPC building blocks:**

| Component | Role |
|---|---|
| **Subnets** | How resources are separated from other tenants in the shared environment |
| **VLANs** | Connect subnets. ⚠️ Must be **routed through a Layer 3 device**, where you apply access lists to allow/deny between subnets |
| **VPN** | Encrypts data point to point, keeping it private from other tenants and outside observers |
| **NAT** | Connects the internet to your subnets and back; sits at the network edge |
| **BGP** | 📌 Border Gateway Protocol **advertises your network** so others — your company or the internet — can find and reach it |

**Advantages:** cost reduction (especially for small businesses that don't need the hardware or software), and **elasticity** — 📌 if you need compute in April but not in May, the cloud **shrinks as well as grows.**

### Network security groups and security lists

Both control which traffic is allowed to and from cloud resources — a **virtual firewall**.

**NSG (Network Security Group).** A group of **resources that share a similar security posture**. Example: five web servers that all need port 80 blocked and 443 allowed, forcing everyone to use HTTPS. Group them, apply one rule set.

- **Components:** the **virtual NIC** and the **security rules**. Rules are applied to the vNICs attached to those resources — filtering happens at that level.
- **Resources that can join a group:** compute instances (VMs running your applications), database systems, storage (attached via IP and a network card), and load balancers.

**Security lists** apply at the **subnet/packet level** — traditional filtering based on network numbers.

📌 ⚠️ **The distinction the exam wants:** a **security list filters by subnet/network number**; an **NSG filters based on the actual resource**, which the course describes as operating at a higher layer — closer to the application layer of the OSI model. NSG = resource-aware. Security list = network-aware.

### Cloud gateways

Cloud resources live on a **private network inside the provider**. The **cloud gateway** lets those resources reach the internet, and lets customers reach their cloud services from outside.

**How it used to work vs now:**
- **Traditionally:** you built a VM, installed NAT translation software, added multiple NICs, installed firewall services. Wanted a second connection? Build a second VM.
- **Today:** the provider offers it **as a service** — already built, you just attach it to your network.

**Why the managed version is better:** it is **horizontally scaled** across the provider's entire infrastructure, **redundant** (like all provider services, across multiple locations), **highly available**, and reachable over the provider's many high-speed connections. It handles both **IPv4 and IPv6**.

⚠️ **Requires a public IPv4 and IPv6 address.** Internal addresses are private IPv4; external must be publicly routable. IPv6 addresses are routable by default.

### Connection methods to the cloud

Two main options, and the trade-offs are exam-relevant:

| | VPN over internet | Direct / dedicated connection |
|---|---|---|
| Cost | Lower | Higher |
| Performance | Variable — shares the public internet | Consistent, predictable |
| Setup | Fast | Longer lead time |
| Best for | General workloads, remote access | Sustained high-volume or latency-sensitive workloads |

⚠️ **Billing model questions to ask a provider** (the transcript flags these explicitly):
- If you need more bandwidth, do **you** have to initiate that, or does the provider scale it automatically and bill you for the scaling?
- Are you charged for **bandwidth**, or for the **amount of data transferred**? Providers differ, and it materially changes cost.

### NFV — Network Functions Virtualization

Replacing dedicated hardware network appliances — routers, firewalls, load balancers — with **software running on standard servers**.

⚠️ 📌 **The security consequence, and this is the tested insight:** because these functions now run as software on shared hosts, the **attack surface changes shape**. Compromise the physical host and you can compromise **all the network devices hosted on it**. Compromise the **hypervisor** and you compromise **every VM running on it**. Traditional network security measures have to be applied differently in a virtualized environment — you are no longer defending discrete boxes.

### Scalability and elasticity

⚠️ These are related but **not synonyms**, and the exam distinguishes them.

| | **Scalability** | **Elasticity** |
|---|---|---|
| Meaning | The ability to **grow** capacity to meet demand | The ability to **grow *and shrink*** automatically as demand changes |
| Direction | Primarily up/out | **Both directions** |
| Timeframe | Planned | Dynamic, often automatic |

**Scaling types:**
- **Vertical (scale up)** — add resources to an existing machine (more CPU, more RAM).
- **Horizontal (scale out)** — add more machines.

📌 **The economic argument.** In a physical environment you must lay out capital for hardware, software, network infrastructure, people, and training *before* you can do anything. In a virtualized environment that initial outlay isn't there — **you pay as you use.**

⚠️ **The elasticity security concern — a genuinely good exam trap.** In a physical environment, a compromised machine is still sitting on the floor with its OS intact and you can investigate it forensically. In an elastic environment, a VM spun up for a task that becomes infected **may be automatically destroyed before you get a chance to investigate it.** Elasticity and forensic evidence preservation are in tension.

### Multitenancy

Multiple customers **share cloud resources** — the same physical compute may run web pages for several customers, and the network may be shared. **Data is kept separate; some infrastructure is shared.**

📌 Isolation in a multitenant environment is achieved through the VPC building blocks above: **subnets** to separate resources, **VLANs** with access lists for controlled routing between them, **VPNs** for encryption in transit, and **NAT** at the edge.

⚠️ Multitenancy is where compliance questions concentrate. If the data is regulated — the transcript's example is credit card information under PCI — shared infrastructure raises questions that a private cloud avoids entirely. That is often the real reason an organization chooses private or hybrid over public.

### 🔧 LAB 1.3 — Hybrid Cloud Connectivity Model *(call TORA)*
Packet Tracer can't run real cloud services, but it models the connectivity well. Build an on-premises network with a cloud-connected branch: configure a site-to-site VPN to a simulated cloud VPC, apply ACLs that emulate network security groups vs subnet security lists, and demonstrate the backhaul problem from section 1.8 by measuring path latency with and without direct cloud access.

---
## 1.4 Ports, Protocols, and Services

*Source: Day 10 — Ports & Protocols*

Pure memorization, and the exam takes full advantage of that. There is no clever technique here — there is spaced repetition. Appendix A is the drill sheet; this section is the understanding that makes the drill stick.

### Why ports exist

An IP address gets data to the right **host**. A port gets it to the right **application** on that host. The course calls this "service point addressing" — it is a Layer 4 function.

- **Well-known ports:** 0–1023
- **Registered ports:** 1024–49151
- **Dynamic / ephemeral ports:** 49152–65535 (what your client picks as a source port)

### The master port table

📌 **Memorize every row.** Group them by the pairings below rather than learning 30 isolated numbers.

| Port | Protocol | TCP/UDP | Purpose |
|---|---|---|---|
| **20** | FTP (data) | TCP | File transfer — data channel |
| **21** | **FTP (control)** | TCP | File transfer — commands |
| **22** | **SSH / SFTP / SCP** | TCP | Secure remote shell and file transfer |
| **23** | **Telnet** | TCP | Remote shell — **unencrypted** |
| **25** | **SMTP** | TCP | Sending mail |
| **53** | **DNS** | **TCP and UDP** | Name resolution |
| **67 / 68** | **DHCP** | UDP | 67 = server, 68 = client |
| **69** | **TFTP** | UDP | Trivial file transfer |
| **80** | **HTTP** | TCP | Web, unencrypted |
| **110** | **POP3** | TCP | Mail retrieval — downloads |
| **123** | **NTP** | UDP | Time synchronization |
| **143** | **IMAP** | TCP | Mail retrieval — syncs |
| **161 / 162** | **SNMP** | UDP | 161 = queries, 162 = **traps** |
| **389** | **LDAP** | TCP | Directory services |
| **443** | **HTTPS** | TCP | Web over TLS |
| **445** | **SMB** | TCP | Windows file/printer sharing |
| **514** | Syslog | UDP | Log collection |
| **587** | SMTP (submission) | TCP | Modern mail submission with auth/TLS |
| **636** | **LDAPS** | TCP | LDAP over SSL/TLS |
| **993** | **IMAPS** | TCP | Secure IMAP |
| **995** | **POP3S** | TCP | Secure POP3 |
| **1433** | SQL Server | TCP | Microsoft database |
| **3306** | MySQL | TCP | Database |
| **3389** | **RDP** | TCP | Remote Desktop |
| **5060 / 5061** | SIP | TCP/UDP | VoIP signaling (5061 = secure) |

### Learn them as pairs — this is the trick

⚠️ The exam loves to swap a secure port for its insecure counterpart. Learn the **relationships**, not the isolated numbers:

| Insecure | Secure | Relationship |
|---|---|---|
| HTTP **80** | HTTPS **443** | The most-tested pair on the exam |
| FTP **21** | **SFTP 22** (over SSH) or **FTPS 989/990** (over TLS) | ⚠️ **These are different things — see below** |
| Telnet **23** | **SSH 22** | 23 → 22 |
| SMTP **25** | SMTP+TLS **587** | Submission port |
| POP3 **110** | POP3S **995** | +885 |
| IMAP **143** | IMAPS **993** | +850 |
| LDAP **389** | LDAPS **636** | Doubles, roughly |

📌 ⚠️ **SFTP vs FTPS — a guaranteed distractor.**
- **SFTP** = SSH File Transfer Protocol. Runs **over SSH, port 22**. A completely different protocol from FTP.
- **FTPS** = FTP Secure. It **is** FTP, wrapped in SSL/TLS, ports 989/990.

They sound nearly identical and are not related. If a question mentions SSH anywhere, the answer is SFTP on 22.

### Protocol notes worth knowing

**DNS (53).** Translates domain names to IP addresses. 📌 **Uses UDP for ordinary queries** (fast, small, single packet) and **TCP for zone transfers** and responses too large for a UDP datagram. "Which protocol uses both TCP and UDP on the same port?" → DNS.

**DHCP (67/68).** Automatically assigns full IP configuration to clients. The **DORA** sequence:

| Step | Message | Direction | Cast |
|---|---|---|---|
| **D** | **Discover** | Client → | Broadcast |
| **O** | **Offer** | ← Server | Broadcast/unicast |
| **R** | **Request** | Client → | Broadcast |
| **A** | **Acknowledge** | ← Server | Broadcast/unicast |

📌 Because Discover is a **broadcast**, and broadcasts don't cross routers, a DHCP server on another subnet requires a **relay agent / IP helper address** on the router. This is one of the most common real-world DHCP failures and a frequent exam scenario — symptom is an APIPA address on one subnet while another subnet works fine.

**FTP vs TFTP.** TFTP is a deliberately stripped-down file transfer: **UDP**, no authentication, no directory browsing, no encryption. Used for device firmware and config transfers where simplicity matters more than features. FTP is TCP, authenticated, full-featured.

**POP3 vs IMAP.** 📌 The defining difference: **POP3 downloads mail and typically removes it from the server** — mail lives on one device. **IMAP keeps mail on the server and synchronizes**, so all devices see the same state. For a user with a phone and a laptop who needs both in sync, the answer is always **IMAP**.

**SMTP (25).** Sends mail *outbound* only. ⚠️ It does not retrieve mail — POP3 and IMAP do. Many ISPs block outbound 25 to limit spam, which is why 587 exists for authenticated submission.

**SNMP (161/162).** Network device monitoring and management. 📌 **161 for polling/queries, 162 for traps.** A **trap** is unsolicited — the device pushes an alert to the manager rather than waiting to be asked. Data is organized in a **MIB (Management Information Base)** and addressed by **OID (Object Identifier)**.
⚠️ **SNMPv1 and v2c send community strings in cleartext. Only SNMPv3 adds authentication and encryption.** Any "harden SNMP" question resolves to v3.

**NTP (123).** Synchronizes clocks. Sounds trivial; is not. Kerberos authentication fails on clock skew, certificate validation fails, and log correlation across devices becomes impossible without it. **NTS** (Network Time Security) is the secured version.

**SMB (445).** Shared access to files, directories, printers. The Windows counterpart to **NFS** on Linux. ⚠️ Port 445 exposed to the internet is a serious finding — it's the vector for a long history of worms.

**SSH (22).** Encrypted remote shell, and the transport underneath SFTP and SCP. It replaced Telnet because **Telnet transmits credentials in cleartext**.

**LDAP (389) / LDAPS (636).** Directory services — querying user and resource objects in a directory such as Active Directory.

**HTTP (80) / HTTPS (443).** HTTPS is HTTP inside SSL/TLS. Look for the certificate — that's what makes the session verifiable, not just encrypted.

### TCP vs UDP

| | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Handshake | **Three-way (SYN, SYN-ACK, ACK)** | None |
| Ordering | Sequenced, reassembled in order | No guarantee |
| Error recovery | Acknowledgement and retransmission | None |
| Overhead | Higher | Lower |
| Speed | Slower | **Faster** |
| Use for | Web, email, file transfer — anything where every byte matters | **Voice, video, streaming, DNS queries, DHCP** — anything where a retransmit arrives too late to be useful |

📌 The hockey-game framing from Day 1 is the best mental model: retransmitting a dropped video frame shows you a moment that has already passed. A brief dropout is better than a replay. That is why real-time media chooses UDP.

**TCP flags you should recognize:**

| Flag | Meaning |
|---|---|
| **SYN** | Synchronize — open a connection |
| **ACK** | Acknowledge |
| **FIN** | Finish — graceful close |
| **RST** | Reset — abrupt termination, often "port closed" or "connection refused" |
| **PSH** | Push data to the application immediately |
| **URG** | Urgent |

⚠️ **RST in a capture is a diagnostic signal**, not just noise. It usually means the port is closed or a device actively refused the connection — different from a timeout, which suggests a firewall silently dropping.

### ICMP

Not a transport protocol and **has no ports** — it operates at Layer 3.

| Type | Message | Where you see it |
|---|---|---|
| 0 | Echo Reply | `ping` response |
| 3 | Destination Unreachable | No route, or a filtering device |
| 8 | Echo Request | `ping` |
| 11 | **Time Exceeded** | **How `traceroute` works** |

📌 **Traceroute is TTL manipulation.** Send a packet with TTL=1; the first router decrements to 0 and returns **Time Exceeded**, revealing hop 1. Then TTL=2 for hop 2, and so on. Understanding this explains why traceroute output can show gaps — some devices are configured not to reply.

### 🔧 LAB 1.4 — Protocol Capture and Port Behavior *(call TORA)*
Configure DNS, DHCP, HTTP/HTTPS, FTP, and email servers in Packet Tracer, then use Simulation Mode with protocol filters to capture the DORA exchange, a DNS query, a TCP three-way handshake, and an ICMP traceroute. Break/fix: wrong DHCP scope, missing IP helper address across a router, DNS pointing at a dead server, and a firewall ACL blocking 443 but not 80.

---
## 1.5 Transmission Media, Connectors, and Ethernet Standards

*Source: Day 3 — Cables & Connectors; Day 2 (802.3, Fibre Channel, transceivers)*

This section is dense with numbers. The exam loves it because it is unambiguous — either you know that OM3 is 40 Gbps at 300 m or you don't. Drill the tables.

### Copper: shielded vs unshielded

The vulnerability of any electrical signal on a metal wire is **EMI (electromagnetic interference)** — from strong power sources, radio sources, or anything magnetic.

- **STP (shielded twisted pair)** — adds a braided metal mesh around the internal cores. Better transmission characteristics, more expensive. Common in 1980s–90s **token ring**.
- **UTP (unshielded twisted pair)** — no shield. Cheaper. Became the standard as Ethernet took over.

📌 The twisting *itself* provides some EMI protection even without a shield — that's why UTP works at all. Twisting causes interference picked up on adjacent wires to cancel.

⚠️ **Why UTP won:** token ring never exceeded 16 Mbps, so STP's transmission advantage was irrelevant once Ethernet reached the gigabit range. Cost was the driver. As long as you follow installation guidelines — keep it away from strong power and radio sources — interference isn't a practical problem.

### UTP categories

| Category | Max speed | Notes |
|---|---|---|
| Cat 1 | — | Original telephone cable, no data |
| Cat 2 | 4 Mbps | Suitable for original token ring |
| Cat 3 | 10 Mbps | Distances up to ~100 m |
| Cat 4 | 16 Mbps | Token ring maximum |
| **Cat 5** | **100 Mbps** | "Fast Ethernet" |
| **Cat 5e** | **1 Gbps** | e = **enhanced** (not "extended") |
| **Cat 6** | 1 Gbps / **10 Gbps @ ~55 m** | 10 G only over roughly half the standard distance |
| **Cat 6a** | 1 Gbps / 10 Gbps | *a* = augmented; more insulation, better EMI resistance. **No difference in transmission spec vs Cat 6** |
| Cat 7 | 10 Gbps @ 100 m | Available but less common |
| Cat 8 | 40 Gbps | In development at time of recording |

📌 **Standard Ethernet distance limit is 100 meters.** This number appears everywhere. Memorize it.

### Coaxial and twinax

**Coax** — a single solid copper conductor at the core, surrounded by insulation, then a *grounded* conductive metal shield. The shield keeps interference out and signal in.

| Designation | Nickname | Speed | Distance |
|---|---|---|---|
| **10BASE5** | Thick Ethernet / Thicknet | 10 Mbps | ~500 m (5 × standard) |
| **10BASE2** | Thin Ethernet / Thinnet | 10 Mbps | ~185 m (~2 × standard) |

📌 **Decoding the naming convention** — this is worth internalizing because it generalizes:
- **10 / 100 / 1000 / 10G** = speed
- **BASE** = **baseband**
- **5 / 2 / T / F / S / L** = distance or media type

**Baseband vs broadband.** Baseband means the signal has access to the **entire bandwidth** of the cable — think of the waveform running from the top of the pipe to the bottom, with top = 1 and bottom = 0. Broadband uses **variations in frequency and amplitude** to carve the cable into multiple channels — which is how a single TV cable carries many channels, each occupying maybe 5% of available bandwidth. **Ethernet LANs use baseband.**

Modern coax types: **RG6** and **RG11**, used for cable TV, telephony, and internet delivery. Coax in a LAN is effectively extinct.

**Twinax / Twinaxial** — like coax but with **two conductors** instead of one, twisted, shielded, jacketed. Enables **differential signaling** (the receiver interprets the *difference* between the two signals). Used in the data center for very high speed over short runs (~10 m or less). Cost-effective vs fiber.

**DAC (Direct Attach Copper)** — twinax with **transceivers permanently attached** to each end, containing their own logic. Fixed cable length, plugs straight into high-speed switches, routers, or servers. Short runs, tens of Gbps, electromagnetically shielded.

**Plenum vs non-plenum.** The plenum is the air-handling space above a ceiling where cables and piping run. Ordinary cable jacket plastic emits **toxic fumes** when burned. **Plenum-rated cable is fire-resistant and must be used in plenum spaces**, because a fire there can distribute poisonous chemicals through the building's air before anyone notices it.

### Wiring standards: T568A and T568B

Defined by **TIA/EIA**. They apply to twisted pair and specify only the **color sequence** of the 8 wires (4 twisted pairs). **There is no functional difference between them.**

| Pin | T568A | T568B |
|---|---|---|
| 1 | White/Green | White/Orange |
| 2 | Green | Orange |
| 3 | White/Orange | White/Green |
| 4 | Blue | Blue |
| 5 | White/Blue | White/Blue |
| 6 | Orange | Green |
| 7 | White/Brown | White/Brown |
| 8 | Brown | Brown |

📌 The change between A and B is **swapping the green and orange pairs**. Pins 4, 5, 7, 8 are identical in both.

**Which to use:** match whatever is already installed; follow project specs; match internally-wired/hardwired components. Residential work typically favors 568A.

**Straight-through vs crossover.**

- **Straight-through** — same standard on both ends. Four wires send, four receive, and the port design assumes that alignment.
- **Crossover** — different standard on each end (568A on one, 568B on the other). Flips senders and receivers.

| Use straight-through | Use crossover |
|---|---|
| PC ↔ switch | PC ↔ PC |
| Switch ↔ router | Switch ↔ switch |
| PC ↔ hub | Switch ↔ hub |
| | Hub ↔ hub |
| | Router ↔ router |

📌 **The rule of thumb:** *different* device types → straight-through. *Same* device types → crossover. The reason is sender/receiver alignment — PC-to-PC with a straight-through cable sends into the other side's senders, so nothing works.

⚠️ You can identify a crossover cable visually: hold both clear connectors side by side. Straight-through looks identical on both ends; crossover doesn't.

🔗 **A+ crossover:** **crimping** is stripping bulk cable to bare copper, seating wires in the connector, and clamping. Large installs buy bulk cable and crimp to length because it's cheaper than pre-made patch cables.

### Fiber optic construction

Interior → exterior: **Core** (light travels here) → **Cladding** (often plexiglass, flexible) → **Primary coating** (protects inner components) → **Strength members** → **Cable jacket**.

### Single-mode vs multimode

| | Single-mode (SMF) | Multimode (MMF) |
|---|---|---|
| Core diameter | ~8.3 µm | 50 or 62.5 µm |
| Light source | High-powered **lasers** | **LEDs** or lasers |
| Modes carried | One beam, down the center | Multiple paths simultaneously |
| Distance | Long | Short |
| Typical use | Outdoor, telco, campus-to-campus | Indoor, data center patch cables |
| Cost | Higher per cable, cheaper over miles (fewer connection points) | Cheaper for short runs |

⚠️ **Counterintuitive but tested:** "multimode" sounds more capable, but **multimode is generally the less expensive option.** Single-mode is a dedicated, precision implementation. The multiple light paths in MMF interfere with each other, which is exactly why it can't go far.

### Fiber categories

**Single-mode — OS (Optical Service):**

| Type | Theoretical distance | Realistic | Use |
|---|---|---|---|
| **OS1** | up to 10 km | ~2–5 km | Indoor / campus, tunnels, pedways, airport terminals |
| **OS2** | up to 200 km | Far less in practice | Outdoor, telephone-pole runs, long haul |

**Multimode — OM (Optical Mode):**

| Type | Speed | Distance |
|---|---|---|
| **OM1** | 10 Gbps | 33 m |
| **OM2** | 10 Gbps | 82 m |
| **OM3** | 40 Gbps | 300 m |
| **OM4** | 40 Gbps | 550 m |
| **OM5** | 28 Gbps **per channel × 4 channels** | — |

📌 OM5 uses a different multiplexing method to run 4 channels. It's relatively new and increasingly deployed.

⚠️ These are **maximums at maximum distance.** Shorten the run and speed can increase — OM3 at 50 m might carry 100 Gbps rather than 40.

### Fiber connectors

All fiber connectors share three components: the **ferrule** (holds the core; light travels through it), the **connector body** (plastic, metal, or ceramic; holds the ferrule), and the **coupling mechanism** (friction-fit, clip, bayonet, or screw-on).

| Connector | Full name | Shape / mechanism | Notes |
|---|---|---|---|
| **LC** | Local Connector (a.k.a. Lucent, "little") | Square, friction/push, latch | **Most common in modern installs.** Ferrule **1.25 mm** — half the SC. Duplex = two separate ferrules |
| **ST** | Straight Tip | **Round**, **bayonet** — push and twist to lock | Being replaced by LC |
| **SC** | Subscriber Connector ("square connector") | Square, push-pull | Common at the home demarc for fiber service. Ferrule **2.5 mm** |
| **MT-RJ** | Mechanical Transfer Registered Jack | Small form factor | **Both cores in a single ferrule.** Multimode only, always full duplex. Higher density |

📌 **Duplex fiber needs two cores.** You cannot send and receive over a single core simultaneously — light traveling in opposite directions would interfere. Simplex single-core does exist for one-way applications (e.g. digital audio into an amplifier).

### UPC vs APC

This is about the **polish angle at the end face of the ferrule**, and it's about **back-reflection**.

- **UPC (Ultra Physical Contact)** — rounded/straight. Reflected light travels **straight back down the cable toward the source**, causing noise.
- **APC (Angled Physical Contact)** — flat but polished at an **8° angle**. Reflected light is deflected at an angle, bounces around inside the cable, and loses energy with every reflection — so far less makes it back to the source.

**Where APC matters:** high-frequency optical transmissions are more sensitive to back-reflection. Fiber-to-the-home carrying modulated video signals typically uses APC exclusively.

⚠️ 📌 **Never intermix UPC and APC.** They won't work correctly and you can **physically destroy the connectors** because the end faces don't mate. They are **color-coded** (commonly green for APC, blue for UPC) specifically to prevent this.

### Copper connectors

| Connector | Pins | Use |
|---|---|---|
| **RJ11** | 6 (often 4 wires used) | Telephone / landline |
| **RJ45** | **8** | Standard UTP Ethernet |
| **F-type** | — | Coax; screw-on "banjo" type; domestic TV equipment, satellite ground |

Both RJ types use the same plastic clip mechanism — you should hear the click, or you don't have a good connection.

### Optical transceivers

A **transceiver** converts electrical signals to light for transmission over fiber. Physically about the size of a flash drive, and **hot-pluggable** — which is what makes switches modular. Swap the transceiver, change the communication standard, keep the same switch.

| Type | Channels | Rate |
|---|---|---|
| **SFP** (small form-factor pluggable) | 1 | 100 Mbps – 4 Gbps |
| **SFP+** | 1 | **8 Gbps** (Fibre Channel) / **10 Gbps** (Ethernet, OTN) |
| **QSFP** (quad SFP) | **4** | 1 Gbps per channel |
| **QSFP+** | **4** | **10 Gbps per channel**; combinable into a single **40 Gbps** Ethernet link |

📌 SFP superseded **GBIC** (gigabit interface converter) at **half the physical volume** — meaning more transceivers per switch.

**Compatibility rules:**
- SFP and SFP+ are **nearly identical in size but not interchangeable in connection.** An SFP+ transceiver *can accept data from* an SFP transceiver at the lower rate.
- QSFP and QSFP+ **are** compatible both physically and in data communications — they negotiate down to the lowest common denominator.

### Ethernet over copper — standards

| Standard | Speed | Cabling | Distance |
|---|---|---|---|
| 10BASE-T | 10 Mbps | Twisted pair | 100 m |
| 100BASE-TX | 100 Mbps | Cat 5 UTP | 100 m |
| 1000BASE-T | 1 Gbps | Cat 5e / 6 / 6a / 7 | 100 m |
| 10GBASE-T | 10 Gbps | **Cat 6 → ~55 m**, Cat 7 → 100 m | see left |
| 40GBASE-T | 40 Gbps | Cat 7 / Cat 8 | ~30 m |

⚠️ The **X** in 100BASE-TX/FX was originally just a **placeholder** for T (twisted pair) or F (fiber). It carries no independent meaning and often gets dropped in conversation.

### Ethernet over fiber — standards

| Standard | Speed | Fiber type | Distance |
|---|---|---|---|
| 100BASE-FX | 100 Mbps | Fiber | Fast Ethernet era; still seen in automation systems |
| 100BASE-SX | 100 Mbps | MMF | Shorter wavelength; cheaper optics (LEDs not lasers) |
| **1000BASE-SX** | 1 Gbps | **MMF only** | **220 m** @ 62.5 µm, **500 m** @ 50 µm |
| **1000BASE-LX** | 1 Gbps | **SMF** (MMF possible) | **5 km** on SMF; falls back to SX distances on MMF |
| **10GBASE-SR** | 10 Gbps | MMF | Short range, ~30–50 m |
| **10GBASE-LR** | 10 Gbps | **SMF** | **Long reach, up to 10 km** |

📌 **The letter rule:** **S = short** distance, **L = long** distance. It holds across the whole naming scheme. R = range/reach.

### Wavelength division multiplexing

Splitting one physical fiber into channels by varying the **wavelength** of light — the optical equivalent of broadband over copper.

| | CWDM (Coarse) | DWDM (Dense) |
|---|---|---|
| Wavelength | Lower, from **1270 nm** | Higher, more precise |
| Channels | **18** | up to **88** |
| Channel width | 20 nm (13 nm channel + 7 nm spacing) | Much narrower |
| Distance | Travels **further** | Travels **less far** |
| Optics cost | Cheaper lasers (less precision needed) | More expensive |
| Bandwidth | Lower | **Higher** |

**Bidirectional WDM** — wavelengths can be distinct enough to travel in **opposite directions over the same fiber**. Requires more expensive components because reflection must be tightly controlled.

### Fibre Channel vs Ethernet

**Fibre Channel** is a rapid, **ordered and lossless** data delivery protocol using **block data transfers**, point-to-point, common in switched fabric environments. It runs over fiber **or** copper and is used mainly **between storage devices** in and between data centers.

📌 ⚠️ **The key exam fact:** Fibre Channel uses an **entirely separate protocol that does not map to the OSI model at all.** Ethernet transceivers use IEEE 802.3, which does map to OSI. This is the distinction to remember.

| | Fibre Channel | Ethernet |
|---|---|---|
| Raw speed | Lower | **Higher** |
| Reliability | **Higher** (lossless block transfer) | Lower |
| OSI mapping | **None** | 802.3, maps cleanly |
| Typical use | Storage ↔ switch ↔ server in the DC | LAN aggregation, switch-to-switch |
| Security | Benefits from protocol diversity | Front-end and back-end share attack surface |

📌 **The security argument:** if you run Ethernet on both the front end and the storage back end, an attacker's Ethernet tooling works against both. Running Fibre Channel on the back end means those tools simply don't apply. Protocol diversity as a defensive property.

Fibre Channel range extends to **5–10 km**, which supports **remote disaster recovery** — replicating large blocks off-site to another building on campus — and **business continuity**, bringing that remote data online quickly after an incident.

⚠️ **Fibre Channel connects only to Fibre Channel; Ethernet only to Ethernet.** SFP on one end means SFP on the other; QSFP means QSFP. These technologies match themselves and do not intermix.

### Cable management

**Patch panel.** The termination point where all the office wall ports converge in a central room. Cables are stripped to bare wire and **punched down** onto the back of the panel, hardwiring them. The front presents standard **RJ45** ports, from which patch cables run to switches.

**Cable trays.** Overhead or under-floor channels for running cable out of the way. 📌 **Use separate trays for data and power** — power sources cause EMI in close proximity to data cables.

**UPS (uninterruptible power supply).** Supplies backup power and conditions power against **brownouts and surges**.

⚠️ Two things the exam wants here:
1. A UPS is generally **not** meant to run equipment for hours. It provides enough runtime for a **graceful shutdown** rather than an instant power loss.
2. A UPS is a **battery**, and batteries — especially banks of them — are a **significant source of EMI**. Route data cabling away from them.

### 🔧 LAB 1.5 — Media Selection and Cable Fault Isolation *(call TORA)*
Build a multi-building campus in Packet Tracer requiring correct media choices at each segment (copper access, MMF between floors, SMF between buildings). Deliberately mis-select cable types — straight-through where crossover is needed, MMF where the distance demands SMF — and diagnose each failure from link-state and interface counters.

---
## 1.6 Topologies, Architectures, and Traffic Flow

*Source: Day 2 — Network Topologies, Architectures & Types*

### Physical topologies

**Star (hub-and-spoke).** Every node connects to one central device. This is what you actually see at the access layer of nearly every modern network.

- *Advantages:* one failed link kills only that node; easy to add nodes; simplified troubleshooting; point-to-point connections to a switch run at full cable speed.
- *Disadvantages:* central device is a single point of failure (lose a 48-port switch, lose 48 hosts); performance is bounded by the central device's throughput, not the cable speed; one damaged cable can in some cases disrupt the central device.

⚠️ **Hub vs switch:** the *topology* is identical, the *behavior* is not. A hub is "just an amplifier" with no forwarding intelligence — everything is one collision domain. A switch learns MAC addresses and creates dedicated point-to-point paths. Hubs are obsolete; the exam still tests the distinction.

**Mesh.** Every link is a point-to-point connection between two nodes.

- **Full mesh** — every node connects to every other node. Maximum redundancy; in a true full mesh *every node is a central node*.
- **Partial mesh** — most nodes have multiple paths, but not all-to-all.
- *Advantages:* traffic reroutes on failure; losing a node doesn't isolate the rest; dedicated links mean privacy and security (data isn't transiting third-party devices); fault identification is simple because each link is discrete; scales without interrupting existing communication.
- *Disadvantages:* cable count grows exponentially with node count; large physical footprint; expensive; complex to implement.

**Point-to-point.** Two devices, one dedicated link. Simplest architecture — and it keeps showing up inside more complex ones.

- *Advantages:* full bandwidth available to both ends; better security (no intermediary to compromise — an attacker would have to physically cut and splice the cable); lowest latency; minimal hardware; trivial troubleshooting.
- *Disadvantages:* a link failure is a total failure; scaling is expensive; unsuitable for large numbers of hosts.

📌 Point-to-point isn't just a crossover cable. A **PC-to-switch connection** is point-to-point. A **VPN tunnel** is a *virtual* point-to-point connection and carries many of the same properties. That reframing is exam-relevant.

**Hybrid.** Two or more topologies combined — and this is what real networks are. Typical shape: star at the access edge (hosts to switches), partial mesh higher up (switch to switch, to the core, out to the router).

The design logic: at the edge, a failed link costs you one user, who can move to another workstation. In the core, a failed link can cost you a hundred users. So you spend the money on redundancy where the blast radius is large, and you don't mesh everything — that's how you keep cost sane.

- *Advantages:* scalable (add an access switch at the bottom, add a core switch for a new building); flexible (shape traffic, allocate bandwidth, add capacity where bottlenecks appear); troubleshooting still straightforward because upper-layer links are point-to-point.
- *Disadvantages:* complex — **documentation and change tracking become critical**; someone plugging a PC into a core switch can break traffic and open security holes; more expensive as port density and forwarding rates go up.

### Data center architecture: spine-leaf

This is a favorite exam topic because it explains *why* an architecture changed, not just what it is.

**The old problem.** Traditional three-tier data center switching was all Layer 2. Redundant links at Layer 2 create loops, so you must run **Spanning Tree Protocol**, and STP works by **blocking redundant links until they're needed**. You paid for the links and then couldn't use them.

**The spine-leaf fix.**
- Servers connect to the **leaf** layer at **Layer 2**.
- Leaf switches connect to **spine** switches at **Layer 3**.
- Every leaf connects to every spine.
- Because leaf-to-spine is Layer 3, you can use **Layer 3 protocols to prevent loops** — no STP — and therefore use **all links simultaneously**.

📌 **The defining property:** any two leaf switches are always exactly **one hop** apart (leaf → spine → leaf). Latency is predictable and low regardless of how large the fabric grows.

**Scale out, not up.** Instead of adding *layers* (which adds hops and latency), you add more spine or leaf switches sideways, preserving the single-hop property.

*Advantages:* better performance than three-tier, chiefly in reduced delay; no STP so redundant cabling is fully utilized; greater capacity for VM traffic; horizontal scalability.

### Enterprise campus models

**Three-tier hierarchical model:**

| Layer | Devices | Role | OSI |
|---|---|---|---|
| **Access** | Switches | Where hosts plug in. Same-VLAN traffic never leaves here. Port security applied here. | Layer 2 |
| **Distribution** | Layer 3 switches / routers | Aggregates access switches. **Routes between VLANs.** Policy is applied here — which protocols pass, whether LAN A can talk to LAN B. | Layer 3 |
| **Core** | High-speed routers / L3 switches | Connects distribution blocks, other buildings, branch offices, the demarc and the internet. Optimized for speed and reliability. | Layer 3 |

📌 Security is applied at different layers for different purposes: **port protection at access** (lock out a PC that doesn't belong on that port), **policy filtering at distribution** (which traffic may cross between LANs).

**Two-tier / collapsed core.** Distribution and core are merged. Access layer remains.

- *Use case:* small-to-medium campuses, roughly ~1000 nodes or fewer.
- *Advantages:* simpler protocols, fewer devices to configure, easier traffic control, lower cost.
- *Disadvantages:* loss of resilience (you lose the multiple distribution-to-core paths); harder to manage aggregate traffic without a distinct core; limited scalability.
- ✅ It converts cleanly to three-tier later by adding a layer above the collapsed core.

### Traffic flow: east-west vs north-south

| | Direction | Meaning | Typical path |
|---|---|---|---|
| **East-west** | Horizontal | Traffic *within* a layer or within the data center — server to server, VM to VM | Mostly switches; fast |
| **North-south** | Vertical | Traffic *between* the data center and elsewhere — a workstation out to the internet | Crosses multiple device types, often a router; slower |

**Why east-west traffic exploded:**
- **Virtualization** — one physical server runs many VMs, so communication went from one-to-one to many-to-many.
- **Converged infrastructure** — collapsed layers and spine-leaf in the data center.
- The hypervisor now runs the *virtual network* too, so a lot of traffic never touches physical wire.

**Problems and responses:**
- *Higher latency* — every device that stops and inspects data adds delay. Response: migrate three-tier → spine-leaf so nothing is more than a hop or two away.
- *Insider threat* — east-west traffic never crosses the demarc, so perimeter defenses never see it. Response: **continuous monitoring**.
- *Lateral movement* — Response: **microsegmentation**, isolating VMs into their own segments (VLAN-style isolation) so production servers stay separated by business function.
- *Visibility* — Response: **software-defined networking**, which can monitor traffic between VMs inside a single physical host, not just on the physical network.

⚠️ Placement matters. Where you put a resource determines whether its traffic is east-west (switched, fast) or north-south (routed, slower). Expect scenario questions on this.

### 🔧 LAB 1.6 — Build All Four Topologies *(call TORA)*
Construct star, partial mesh, full mesh, and a hybrid three-tier campus in one Packet Tracer file. Measure convergence and path behavior after cutting links in each. Then build a spine-leaf fabric and demonstrate STP blocking a link in the Layer 2 design while the Layer 3 design uses both.

---
## 1.7 IPv4 Addressing, Subnetting, and IPv6

*Source: Day 6 — IPv4 Network Addressing; Day 7 — IP Addressing Schemes and Subnetting*

This is the most PBQ-heavy topic on the exam. You will be asked to *calculate*, not recall. Speed matters — build the reflex.

### Public vs private addressing

**RFC** = **Request for Comments**, the process by which TCP/IP is developed. Nobody owns TCP/IP, so any entity can propose a change; RFCs collect, review, and implement those proposals, each identified by number.

**RFC 1918** (1996) formalized private addressing. It categorized network needs:
1. LAN only, no external access (a classroom or lab)
2. LAN plus limited outside resources (e.g. a dedicated email service)
3. **LAN plus full internet access** — effectively every network today

| | Public | Private |
|---|---|---|
| Reachable from | Anywhere on the internet | Internal LAN only |
| Uniqueness | **Must be globally unique** | **Can duplicate freely** across organizations |
| Example | Web servers | Your home and work networks |

📌 **RFC 1918 private ranges — memorize exactly:**

| Range | CIDR | Classful equivalent |
|---|---|---|
| 10.0.0.0 – 10.255.255.255 | **10.0.0.0/8** | 255.0.0.0 |
| 172.16.0.0 – 172.31.255.255 | **172.16.0.0/12** | — |
| 192.168.0.0 – 192.168.255.255 | **192.168.0.0/16** | 255.255.0.0 |

⚠️ **Correction to the source material.** The transcript describes 172.16.0.0 as using a "16-bit subnet mask" and 192.168.0.0 as using a "24-bit" mask. Those are the *classful defaults for an individual network* inside each range, not the size of the reserved block itself. The reserved blocks are **/8, /12, and /16** respectively. Both framings show up on exams — know that 172.16.0.0/12 spans 172.16 through 172.31, which is exactly why the range stops at 31.

### Address classes

| Class | First octet | Default mask | CIDR | Networks | Hosts per network |
|---|---|---|---|---|---|
| **A** | 1–126 | 255.0.0.0 | /8 | 126 | 16,777,214 |
| **B** | 128–191 | 255.255.0.0 | /16 | 16,384 | 65,534 |
| **C** | 192–223 | 255.255.255.0 | /24 | 2,097,152 | 254 |
| **D** | 224–239 | — | — | **Multicast** | — |
| **E** | 240–255 | — | — | **Experimental / reserved** | — |

⚠️ **127 is missing on purpose** — the entire 127.0.0.0/8 block is reserved for **loopback**.

### Special addresses

| Address / range | Name | Purpose |
|---|---|---|
| **127.0.0.1** (whole /8) | **Loopback** | Tests the local TCP/IP stack without touching the network. If this fails, the problem is the local stack, not the cable |
| **169.254.0.0/16** | **APIPA / link-local** | Self-assigned when DHCP fails |
| **0.0.0.0** | Unspecified / default route | "This host" or "all networks" in a routing table |
| **255.255.255.255** | Limited broadcast | All hosts on the local segment |
| Network address (all host bits 0) | Network ID | Identifies the subnet — **not assignable to a host** |
| Broadcast address (all host bits 1) | Broadcast | Reaches all hosts in the subnet — **not assignable** |

📌 **This is why usable hosts = 2ⁿ − 2.** You lose the network address and the broadcast address in every subnet.

### APIPA — Automatic Private IP Addressing

When a client is configured for DHCP but **cannot reach a DHCP server**, it self-assigns an address from **169.254.0.0/16** (mask 255.255.0.0).

**What APIPA gives you:** local communication with other APIPA hosts on the same segment.
**What it does not give you:** a default gateway, DNS servers, or any route off the local network.

⚠️ 📌 **Seeing a 169.254.x.x address is a diagnostic gift.** It tells you unambiguously: the host's NIC and stack are working, but **DHCP is unreachable**. Look at the DHCP server, the scope (exhausted?), the relay/helper address, VLAN assignment, or the physical path between client and server. This appears constantly in troubleshooting questions.

### Default gateway

The router interface on the local subnet that a host sends traffic to when the destination is **not on its own subnet**.

How a host decides: it ANDs the destination IP with its own subnet mask and compares to its own network ID.
- **Same network** → deliver directly via ARP and the switch.
- **Different network** → **send the frame to the default gateway's MAC address**, with the *original destination IP* still intact at Layer 3.

📌 That last detail matters and gets tested: the **Layer 2 destination changes to the gateway, the Layer 3 destination does not change.** This is the core of how routing actually works at each hop.

⚠️ **Symptom pattern:** can reach local hosts, cannot reach anything remote → wrong or missing default gateway. Compare this to the DNS symptom (can ping IP, cannot ping name) — different layer, different fix.

### Transmission methods

| Method | Sends to | IPv4 support | Notes |
|---|---|---|---|
| **Unicast** | One specific host | ✅ | The default for most traffic |
| **Broadcast** | **All hosts** on the segment | ✅ | Does not cross a router. 255.255.255.255 or the subnet broadcast |
| **Multicast** | A **group** of interested hosts | ✅ | Class D, 224.0.0.0–239.255.255.255. Efficient for streaming to many receivers |
| **Anycast** | The **nearest** of several hosts sharing one address | ✅ | Used heavily by DNS root servers and CDNs |

📌 ⚠️ **IPv6 has NO broadcast.** It replaces broadcast with multicast (and adds anycast). "Which transmission method does IPv6 eliminate?" is a standard question.

### Subnetting — the method

Subnetting borrows bits **from the host portion** to create more networks, each with fewer hosts. You are always trading hosts for networks.

**The two formulas:**

| | Formula |
|---|---|
| Number of subnets | **2ⁿ** where n = bits borrowed |
| Usable hosts per subnet | **2ʰ − 2** where h = host bits remaining |

📌 **Powers of two — know these cold, both directions:**

| 2ⁿ | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 | 2048 | 4096 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

**Mask values per octet — the only eight numbers that can appear:**

| Bits in octet | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Octet value | 0 | 128 | 192 | 224 | 240 | 248 | 252 | 254 | 255 |

⚠️ If a question offers a mask octet that isn't in that row (like 255.255.200.0), it is invalid. Free points.

### The magic number method — do this under time pressure

This is the fastest reliable approach for PBQs.

1. **Find the interesting octet** — the one where the mask is neither 255 nor 0.
2. **Magic number = 256 − (mask value in that octet).** This is your **block size**.
3. **Subnets start at multiples of the magic number**, counting from 0 in that octet.
4. **Network address** = the multiple at or below your host's value.
5. **Broadcast** = next network address − 1.
6. **Usable range** = network + 1 through broadcast − 1.

**Worked example: 192.168.10.100/26**

- /26 → mask 255.255.255.**192**. Interesting octet = 4th.
- Magic number = 256 − 192 = **64**.
- Blocks: 0, 64, 128, 192.
- 100 falls in the **64** block.
- **Network: 192.168.10.64** · **Broadcast: 192.168.10.127** · **Usable: .65 – .126** · **62 hosts** (2⁶ − 2).

**Worked example: 172.16.0.0/20**

- /20 → mask 255.255.**240**.0. Interesting octet = 3rd.
- Magic number = 256 − 240 = **16**.
- Blocks in the third octet: 0, 16, 32, 48, 64 …
- First subnet: **172.16.0.0**, broadcast **172.16.15.255**, usable **172.16.0.1 – 172.16.15.254**.
- Hosts: 12 host bits → 2¹² − 2 = **4,094**.

### CIDR reference table

📌 Learn this table. It converts every subnetting question into a lookup.

| CIDR | Mask | Block size | Usable hosts |
|---|---|---|---|
| /8 | 255.0.0.0 | — | 16,777,214 |
| /16 | 255.255.0.0 | — | 65,534 |
| /20 | 255.255.240.0 | 16 (3rd octet) | 4,094 |
| /21 | 255.255.248.0 | 8 | 2,046 |
| /22 | 255.255.252.0 | 4 | 1,022 |
| /23 | 255.255.254.0 | 2 | 510 |
| /24 | 255.255.255.0 | 1 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | **2** |
| /31 | 255.255.255.254 | 2 | 0 (point-to-point special case) |
| /32 | 255.255.255.255 | 1 | Single host route |

📌 **/30 gives exactly 2 usable hosts** — the classic **router-to-router point-to-point link**. If a question mentions a serial or point-to-point WAN link and asks for the most efficient mask, the answer is /30.

**CIDR (Classless Inter-Domain Routing)** removed the rigid class boundaries, letting you use any prefix length and dramatically reducing address waste.

### VLSM — Variable Length Subnet Masking

Applying **different mask lengths to different subnets** of the same network, sized to actual need.

**Method:** sort requirements **largest first**, allocate each the smallest block that fits, then move to the next available boundary.

*Example — 192.168.1.0/24 must serve 50, 25, 10, and two 2-host WAN links:*

| Need | Allocate | Subnet | Usable |
|---|---|---|---|
| 50 hosts | /26 (62) | 192.168.1.0/26 | .1 – .62 |
| 25 hosts | /27 (30) | 192.168.1.64/27 | .65 – .94 |
| 10 hosts | /28 (14) | 192.168.1.96/28 | .97 – .110 |
| 2 hosts | /30 (2) | 192.168.1.112/30 | .113 – .114 |
| 2 hosts | /30 (2) | 192.168.1.116/30 | .117 – .118 |

⚠️ **Allocating largest-first is not optional.** Going smallest-first fragments the space and you will run out. This is the single most common VLSM mistake.

### Supernetting / route summarization

The **opposite of subnetting** — combining multiple contiguous networks into one larger advertised route by **moving the mask boundary left**.

*Example:* 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24 → summarize as **192.168.0.0/22**.

**Why:** shrinks routing tables, reduces router memory and CPU, speeds convergence, and hides internal instability from the rest of the network.

### NAT and PAT

**NAT (Network Address Translation)** translates private internal addresses to public external ones.

| Type | Mapping | Notes |
|---|---|---|
| **Static NAT** | One private ↔ one public, fixed | For internal servers that must be reachable from outside |
| **Dynamic NAT** | Private → any free public from a pool | Pool exhaustion blocks further hosts |
| **PAT / NAT overload** | **Many private → one public**, distinguished by **port number** | What virtually every home and small-office router does |

📌 **PAT (Port Address Translation)** is why an entire household shares one public IP. The router tracks a translation table of internal IP + internal port ↔ public IP + unique external port, and demultiplexes replies using the port number.

⚠️ NAT is a **Layer 3** function (it rewrites IP addresses). PAT touches **Layer 4** as well, because it manipulates ports. If asked which layer PAT operates at, the port involvement is the point.

### Subinterfaces

Converting **one physical interface into multiple logical interfaces**, each with its own IP address and VLAN assignment.

📌 This is the mechanism behind **router-on-a-stick** inter-VLAN routing: one physical router interface, trunked to a switch, carrying multiple VLANs — each VLAN terminating on its own subinterface, which acts as that VLAN's default gateway.

Notation: `GigabitEthernet0/0.10` is subinterface 10 on physical interface Gi0/0.

### Virtual IP (VIP)

An IP address **not bound to a single physical node**. Multiple devices can present or assume it.

**Where you'll see it:**
- **FHRP** (HSRP/VRRP/GLBP) — routers share a virtual gateway IP so clients never notice a failover.
- **Load balancers** — clients connect to the VIP, which fronts a pool of real servers.
- **Clustering** — the VIP moves to whichever node is active.

📌 The value is **transparency**: clients keep one address while the infrastructure behind it fails over or scales.

### IPv6

**Why:** IPv4 provides ~4.3 billion addresses and has exhausted them. IPv6 uses **128 bits** — 340 undecillion addresses.

**Format:** eight groups of four hex digits, colon-separated.
`2001:0db8:0000:0000:0000:ff00:0042:8329`

**Compression rules:**
1. Drop **leading zeros** in each group → `2001:db8:0:0:0:ff00:42:8329`
2. Replace **one** run of consecutive all-zero groups with `::` → `2001:db8::ff00:42:8329`

⚠️ 📌 **`::` may be used only once per address.** Twice would make the number of zero groups ambiguous. This is a guaranteed exam question.

**Address types:**

| Type | Prefix | Equivalent to |
|---|---|---|
| **Global unicast** | 2000::/3 | Public IPv4 |
| **Link-local** | **fe80::/10** | 169.254.x.x — auto-configured, required on every interface |
| **Unique local** | fc00::/7 | RFC 1918 private |
| **Multicast** | **ff00::/8** | Class D |
| **Loopback** | **::1** | 127.0.0.1 |
| **Unspecified** | :: | 0.0.0.0 |

**EUI-64.** Generates the 64-bit interface ID from the 48-bit MAC address:
1. Split the MAC in half.
2. Insert **FFFE** in the middle.
3. **Flip the 7th bit** of the first byte (the universal/local bit).

*Example:* MAC `00:1A:2B:3C:4D:5E` → `021A:2BFF:FE3C:4D5E`
(00 → binary 00000000 → flip bit 7 → 00000010 → **02**)

**SLAAC (Stateless Address Autoconfiguration).** A host builds its own address from a **Router Advertisement** prefix plus a locally generated interface ID — no DHCP server required. This is a genuine IPv6 capability with no IPv4 equivalent.

**IPv4 → IPv6 transition mechanisms:**
- **Dual stack** — run both simultaneously. The most common approach.
- **Tunneling** — encapsulate IPv6 inside IPv4 (6to4, Teredo) to cross IPv4-only infrastructure.
- **NAT64 / translation** — convert between the two protocols.

📌 **IPv6 vs IPv4 summary:**

| | IPv4 | IPv6 |
|---|---|---|
| Bits | 32 | 128 |
| Notation | Dotted decimal | Colon hexadecimal |
| Broadcast | Yes | **No — multicast replaces it** |
| Header | Variable length | Fixed 40 bytes, simpler |
| Fragmentation | By routers **and** hosts | **Hosts only** |
| Autoconfiguration | APIPA (link-local only) | **SLAAC (fully routable)** |
| IPsec | Optional | Designed in |
| NAT | Essential | Largely unnecessary |

### 🔧 LAB 1.7 — Subnetting Under Fire *(call TORA)*
Packet Tracer build requiring you to design a VLSM scheme for a five-department network from a single /24, configure router subinterfaces for inter-VLAN routing, apply PAT for internet access, and add IPv6 dual-stack alongside. Break/fix: overlapping subnets, an off-by-one gateway address, a host that lands on a network address, a DHCP scope that doesn't match the subnet, and an APIPA outbreak.

---
## 1.8 Modern Network Environments

*Source: Day 11 — Modern Network Environments*

### SDN — Software-Defined Networking

**The problem it solves.** A traditional switch or router is a small computer: memory, processor, OS, software — all dedicated to two jobs. Because hardware and software are welded together, and because every vendor uses different command languages and proprietary protocols, **central management is genuinely hard.** Configuring a switch differs from configuring a router, which differs again by vendor.

📌 **The core concept — plane separation.** Every network device does two distinct things:

| Plane | Job |
|---|---|
| **Data plane** (forwarding plane) | **Moves** the data through the network |
| **Control plane** | **Decides** how the data moves — consults routing tables, picks the best path |

SDN **separates the control plane from the hardware** and centralizes it in software.

**The three-tier SDN architecture:**

| Tier | What it does |
|---|---|
| **Application** | Where the administrator sits. One interface to configure heterogeneous switches and routers, and to read statistics |
| **Controller** | The translator. Converts the administrator's intent into each device's actual configuration language and pushes it down |
| **Infrastructure** (physical devices) | Still owns the **data plane** — actually forwards the traffic. No longer configured directly |

⚠️ **Communication is bidirectional.** Devices send **statistical data upward** — traffic patterns, flow volume, monitoring — which the application aggregates so the admin can see load and problems. A device receiving a packet for an unknown network can **request a path** via the controller, and the application pushes down the configuration to handle it.

**Key SDN capabilities:**
- **Application awareness** — 📌 this is the big one. Traditional filtering works on IP addresses and port numbers. If two applications share a port but you need to prioritize one over the other, port-based logic can't help. SDN can be **aware of the application making the request** and route accordingly. **Traditional networking cannot do this.**
- **Zero-touch provisioning** — configure devices remotely, no physical visit.
- **Transport agnosticism** — decisions made at the application layer rather than being constrained to network/transport layer information, giving much finer control.
- **Centralized policy management** — avoids the errors that creep in when the same configuration is entered manually over and over.

### SD-WAN

**The problem: backhaul.** Traditionally, a remote worker connected to the head office, and the head office connected to cloud services on the worker's behalf — so all traffic passed through head-office security. But that meant cloud data traveled **to the head office and then back out** to the remote worker. That duplication is called **backhaul**, and it causes congestion at head office and poor application performance.

⚠️ Meanwhile, security teams couldn't actually guarantee traffic was flowing through that controlled path — users could and did make their own direct cloud connections, bypassing controls entirely. Unpredictable traffic paths meant real security exposure in both **availability and privacy**.

**The SD-WAN fix.** Host the security policy, connection rules, and routing rules **in the cloud itself**, so policy applies to users connecting **directly** to cloud services. No backhaul required.

**Benefits:**
- **Routing control** from a single web-based dashboard
- **Simplified management** — one interface for cloud and internal traffic alike
- **Threat protection applied at the cloud level** instead of sourced back through head office
- **Reduced hardware cost** — traffic offloaded from the main office means you don't need the same high-speed links and security appliances there
- **Automation and scalability** — write one rule set, apply across multiple clouds
- **Better application performance** — users connect directly rather than going to two places
- **Reduced training burden** — one similar interface instead of many vendors' products

### VXLAN — Virtual Extensible LAN

**The problem: VLAN exhaustion.** The VLAN ID field in the Ethernet frame allows a maximum of **4,096 VLANs**. That sounds like plenty until you consider virtualization — one physical host running many virtual servers may need multiple VLANs and multiple MACs, inflating switch MAC tables. For a service provider hosting **500 customers**, that works out to roughly **80 VLANs each**. Not enough.

📌 **How VXLAN works.** It takes **Layer 2 frames and tunnels them inside Layer 3 (routable) traffic.**

Normally, Layer 2 information is **discarded at every router hop**. VXLAN **preserves** a VXLAN identifier inside the Layer 3 packet, so two hosts on opposite sides of a routed network believe they are on the same LAN.

**The encapsulation stack:** MAC frame → inside a **UDP** packet → given an **IP** header → given an **Ethernet** header for physical transit.

**What it buys you:**

| | VLAN | VXLAN |
|---|---|---|
| Max segments | **4,096** | **~16 million** |
| Scope | Single Layer 2 domain | **Anywhere IP can reach — worldwide** |
| Transport | Ethernet frame tag | Tunneled in UDP/IP |
| Standard | IEEE 802.1Q | IETF internet standard |

**Benefits:** runs on **any UDP-capable network** (i.e. any IP network); physical layout and geography become irrelevant; **multi-tenancy** — tenants cannot see each other's traffic because it's tunneled inside private point-to-point connections; and network segments can span **between data centers**, so two servers in different locations appear to be on the same physical network.

### Zero Trust Architecture (ZTA)

**The shift.** The traditional model assumed a corporate cubicle, corporate-owned and corporate-managed equipment, and security focused on the **perimeter**. Remote work and BYOD broke that assumption.

📌 **The zero trust principle:** verify **all aspects** of the network before granting access to any resource, and place protections **as close to the protected asset as possible.** If a database server needs protection, protect it *at that location*, so that whichever direction the request comes from, it is checked and verified.

**Identity and Access Management (IAM):**
- Identity should come from a **single source of truth** — one protected, managed database with everything needed to verify a person or system.
- **Multi-factor authentication** — "the days of just having a password are gone." Password *plus* a one-time code, etc.
- **Logging and auditing** as a standing security posture measure, so you can reconstruct what happened.
- **Identity governance** — the framework for verifying, storing, and using identity across the network.

**Managed vs unmanaged devices:**

| | Managed | Unmanaged |
|---|---|---|
| Ownership | Company-controlled | Personal / unknown |
| Security software | Company-installed | Unverifiable |
| Security posture | Known | ⚠️ **Cannot be guaranteed** |
| Access granted | Full | **Typically reduced** |

📌 The prerequisite step is **inventory** — you must know which devices are which before you can build access scenarios around them.

**Access decisions are made on:**
- **Destination / resource sensitivity** — more sensitive resources get stricter policy
- **Source** — who is the user, and do they have rights to this data
- **Device** — managed or unmanaged
- **Location** — inside the network, at home, elsewhere
- **Role** — manager vs accountant; editor vs viewer

**Platform selection criteria:** cloud-based (common interface, highly scalable, consistent across devices) vs local (often proprietary to the equipment, but you own it outright); how it integrates with existing technology; whether it can reach all inventory and assets through a common interface; and the granularity of **user action governance** — how much do you log?

📌 **The migration step matters and is easy to overlook.** Once policy is moved into the zero trust platform, you **disable the old network-level access policies**. Access is then available *only* through the ZTA platform, which is what actually protects applications, servers, and workloads from network-level attacks. Leaving the old paths open defeats the entire exercise.

### SASE — Secure Access Service Edge

📌 **The one-line definition:** a **cloud-native architecture that combines SD-WAN with security functions delivered as cloud services at the network edge.**

**Why it's needed.** In a hybrid cloud environment, the "edge" is no longer just the corporate perimeter — **every entry point into every cloud service is an edge.** Users connect from many locations and pull data directly from the cloud. SASE secures all of those edges with **one common solution**.

**Components:**

| Component | Function |
|---|---|
| **SD-WAN** | The foundation it operates on top of |
| **Secure Web Gateway (SWG)** | Encrypts and inspects connections to the cloud |
| **Firewall as a Service (FWaaS)** | Allow/deny traffic across all network connection points |
| **Cloud Access Security Broker (CASB)** | Watches client-to-cloud connections, checks for malware |
| **Zero Trust Network Access (ZTNA)** | Verifies users **and** verifies the cloud endpoints via certificates — confirming what you're connecting to really is that service |

**Advantages:** more control (a single interface across all connections, closing the bypass gap where users could connect around corporate-edge controls); data protection through encryption plus visibility from one console; **increased performance by eliminating backhaul**; less complexity than assembling multi-vendor edge equipment with different setups and training requirements; better monitoring and reporting from one tool; **visibility across clouds**; reduced integration effort; and a better user experience from more available bandwidth and lower response times.

### IaC — Infrastructure as Code

Creating and managing infrastructure — VMs, networking, storage, databases — **using code rather than manual processes**.

**Why:** a cloud provider may need to stand up hundreds, thousands, or tens of thousands of machines. Manual creation is impossibly slow, and it introduces inconsistency.

**Advantages:**
- **Faster deployment**
- **Fewer errors** — 📌 if the code is correct for machine 1, it is correct for machine 1,000
- **Consistency** — manual setups drift in subtle ways (differing storage allocations that change application performance)
- **Reduced configuration drift** — 📌 the key term. Configurations diverge over time, especially after post-deployment changes. Code applies a change identically across every machine so nothing drifts
- **Lower cost** — fewer people, less time
- **Automated environment setup/teardown** — critical for software development, deployment, and testing, where teams need machines quickly and then need them gone

### IPv6 in the modern context

*(Full IPv6 addressing detail is in section 1.7. This is the framing from Day 11.)*

- **128-bit** addresses vs IPv4's 32-bit. Enough to serve the entire globe.
- Written as **eight hextets** in colon-separated hexadecimal, values 0–F.
- Uses **CIDR slash notation** for the prefix length.
- ⚠️ **`::` collapses a run of consecutive zero groups.**

📌 **Link-local (`fe80::`).** Automatically self-configured on every IPv6-capable interface — you'll see it in `ipconfig /all` output even on a machine you consider IPv4-only. It is valid **only on the local link**. Its practical value: a host can use it to contact the router on its own subnet and obtain configuration **without broadcasting**, which makes local traffic quieter than IPv4's broadcast-based DHCP discovery.

⚠️ **Correction to the source material.** The transcript states the "default subnet mask" for IPv6 is **/32**. That is not right — a /32 is the size of a large allocation given to an ISP. The **standard prefix length for an IPv6 LAN segment is /64**, which is also what the Windows configuration dialog in the same lesson shows. Answer **/64** for a subnet.

📌 **A conceptual note the transcript makes well:** NAT was never designed as a security device. It became one incidentally, because inbound connections through a NAT device aren't permitted by default. That's a side effect, not a security architecture — and it's part of why IPv6, which doesn't need NAT, requires you to think about firewalling deliberately rather than relying on an accident.

### 🔧 LAB 1.8 — Modern Environment Concepts in Packet Tracer *(call TORA)*
Packet Tracer has limited SDN/SASE support, so this lab pairs a buildable component with a design exercise: build a multi-site WAN with a head-office backhaul path, measure the latency penalty, then re-architect for direct cloud access and document the security controls that must move with it. Includes an IPv6 dual-stack build with SLAAC and link-local verification.

---
# PART 2 — Infrastructure (Domain 2.0, 20%)

## 2.1 Routing Technologies and Bandwidth Management

*Source: Day 8 — Routing & Switching Technologies; Day 9 — Network Implementations*

### Static vs dynamic routing

**Static routing.** Routes between source and destination networks are **manually configured** by an administrator.

| Advantages | Disadvantages |
|---|---|
| No protocol overhead — no CPU, memory, or bandwidth spent on updates | **Does not adapt.** A failed link means manual intervention |
| Predictable and precise | Doesn't scale — administrative burden grows fast |
| More secure — no routing advertisements to intercept or spoof | Error-prone at scale |

📌 **Where static wins:** small networks, stub networks with only one way out, and the **default route** (`0.0.0.0/0`) — the "if I don't know where else to send this, send it here" entry.

**Dynamic routing.** Routers **learn routes from each other automatically** and adapt when the topology changes.

| Advantages | Disadvantages |
|---|---|
| Adapts automatically to failures | Consumes CPU, memory, and bandwidth |
| Scales to large networks | More complex to configure and troubleshoot |
| Less administrative overhead ongoing | Larger attack surface if not authenticated |

### Routing protocol classification

📌 Two axes. Know both — questions mix them.

**By scope:**

| Type | Meaning | Examples |
|---|---|---|
| **IGP** (Interior Gateway Protocol) | Within one autonomous system | RIP, OSPF, EIGRP |
| **EGP** (Exterior Gateway Protocol) | Between autonomous systems | **BGP** |

**By algorithm:**

| | **Distance Vector** | **Link State** |
|---|---|---|
| Knows | Only what neighbors tell it — "routing by rumor" | **The full topology map** |
| Metric | Hop count (RIP) | **Cost**, based on bandwidth (OSPF) |
| Updates | Periodic, full table to neighbors | **Triggered**, only on change; floods LSAs |
| Convergence | **Slow** | **Fast** |
| Resource use | Low CPU/memory | **Higher** CPU/memory |
| Loop risk | Higher — needs split horizon, poison reverse, hold-down timers | Lower — each router computes its own tree (SPF/Dijkstra) |
| Examples | RIP, RIPv2 | **OSPF**, IS-IS |

⚠️ **EIGRP is a hybrid** (Cisco calls it "advanced distance vector") — it uses distance-vector mechanics with link-state-like triggered updates and neighbor relationships. If a question offers "hybrid," that's EIGRP.

### The routing protocols in detail

| Protocol | Type | Metric | Max hops | Notes |
|---|---|---|---|---|
| **RIP / RIPv2** | Distance vector, IGP | **Hop count** | **15** (16 = unreachable) | Simple, slow to converge, small networks only. RIPv2 adds subnet mask support (classless) and multicast updates |
| **OSPF** | **Link state**, IGP | **Cost** (bandwidth-based) | Unlimited | Open standard, scales well, uses **areas** with **area 0** as the backbone. Runs Dijkstra's SPF |
| **EIGRP** | Hybrid, IGP | Bandwidth + delay (composite) | 255 | **Cisco-proprietary** (later opened). Fast convergence via DUAL and feasible successors |
| **BGP** | **Path vector**, EGP | AS-path and policy attributes | — | **The routing protocol of the internet.** Routes between autonomous systems; policy-driven rather than purely shortest-path |

📌 **RIP's 16-hop infinity** is the number the Day 4 transcript mistakenly attributed to IP TTL. Keep them separate: **RIP max = 15 usable hops, 16 = unreachable.**

📌 **BGP's role from the cloud section:** BGP is how you **advertise your network** so others can find and reach it. That's the practical framing.

### Route selection

When multiple paths to the same destination exist, a router decides in this order:

1. **Longest prefix match (most specific route) wins.** 📌 A route to 10.1.1.0/24 beats a route to 10.0.0.0/8 for traffic to 10.1.1.5 — **regardless of protocol or metric.** This is checked first and it is the single most tested route-selection fact.
2. **Administrative distance (AD)** — trustworthiness of the *source*, used when different protocols offer the same prefix. **Lower is better.**
3. **Metric** — used to break ties *within* the same protocol. Lower is better.

📌 **Administrative distance values to memorize:**

| Route source | AD |
|---|---|
| Directly connected | **0** |
| Static route | **1** |
| EIGRP (internal) | 90 |
| OSPF | **110** |
| RIP | **120** |
| External EIGRP | 170 |
| Unknown / unusable | **255** |

⚠️ A static route (AD 1) will **always** beat an OSPF route (AD 110) to the same prefix. If someone left a stale static route in place, dynamic routing "isn't working" — and this is a very common troubleshooting scenario.

### NAT and PAT

*(Covered in depth in section 1.7 — the essentials, restated in routing context.)*

**NAT** lets systems on a LAN reach the internet **without a public IP address for every LAN system**. **PAT** extends this by multiplexing many private hosts behind one public address using **port numbers**.

⚠️ NAT was never designed as a security control. It became one incidentally because inbound connections aren't permitted by default. Don't confuse a side effect with a firewall.

### FHRP — First Hop Redundancy Protocol

**The problem it solves.** Almost every production host has a default gateway configured, and in almost every case **there is only one**. If that gateway goes down, **all external connectivity is lost** for every host on that subnet.

**The solution.** Deploy **multiple routers**, and present clients with a **virtual IP address** as their default gateway. The VIP is **not bound to any real interface on any real router** — the protocol recognizes it as an address that exists purely to accept incoming client requests. One router is active; if it fails, another assumes the VIP.

📌 **The key property: clients never reconfigure anything.** They keep pointing at the same gateway address. Failover is invisible.

| Protocol | Standard? | Notes |
|---|---|---|
| **HSRP** | **Cisco-proprietary** | Active/standby |
| **VRRP** | **Open standard** | Master/backup — the vendor-neutral choice |
| **GLBP** | **Cisco-proprietary** | 📌 Adds **load balancing** — multiple routers forward simultaneously, not just one active |

⚠️ **HSRP and VRRP are active/standby: only one router forwards at a time.** GLBP is the one that actually load-balances. That distinction is a reliable exam question.

### Subinterfaces and router-on-a-stick

*(See section 1.7 for the addressing mechanics.)* Converting one physical interface into multiple logical ones, each with its own IP and VLAN, so a single router interface can be the default gateway for many VLANs across an 802.1Q trunk.

⚠️ Router-on-a-stick works but the single physical link is a **bandwidth bottleneck and a single point of failure**. A **Layer 3 switch** doing inter-VLAN routing in hardware is faster (see 1.2) and is what you'd deploy in production.

### Bandwidth management

**QoS** — covered in 1.2. The essential point: **prioritize delay-intolerant traffic** (voice, video, real-time) over delay-tolerant traffic (file transfers, backups, email), even when the delay-tolerant traffic is more "important" to the business.

**Traffic shaping vs policing:**

| | **Shaping** | **Policing** |
|---|---|---|
| Excess traffic | **Buffered and delayed** | **Dropped** (or re-marked) |
| Effect on throughput | Smooths bursts | Enforces a hard ceiling |
| Adds latency | Yes | No |

**Link aggregation (LAG / LACP / EtherChannel).** Bundles multiple physical links into one logical link for **more bandwidth and redundancy**. **LACP (802.3ad)** is the open standard for negotiating it.

📌 LAG solves part of the problem STP creates — it presents multiple physical links to STP as a **single logical link**, so STP doesn't block the redundant members.

### 🔧 LAB 2.1 — Routing and Redundancy *(call TORA)*
Multi-router topology running static routes, RIPv2, and OSPF simultaneously to demonstrate administrative distance in action. Configure router-on-a-stick inter-VLAN routing, then migrate it to a Layer 3 switch. Add HSRP/VRRP with a virtual gateway IP and prove failover by shutting the active router mid-ping. Break/fix: a stale static route overriding OSPF, a missing `network` statement, an OSPF area mismatch, and an FHRP priority misconfiguration that puts the wrong router in the active role.

---
## 2.2 Ethernet Switching Features

*Source: Day 5 — Ethernet Switching & Wireless Standards; Day 8 — Routing & Switching Technologies; Day 9 — Network Implementations*

### VLANs

A **logical grouping of devices** that abstracts away physical connections. Ports on the same switch can belong to different VLANs, and one VLAN can **span multiple switches**.

**Why:**
- **Segmentation** — broadcast traffic stays inside the VLAN, shrinking broadcast domains
- **Security** — separate finance from guest from production
- **Flexibility** — group by function or department, not by physical location
- **Performance** — fewer broadcasts per segment

📌 **Each VLAN is its own broadcast domain and requires its own subnet.** Traffic between VLANs must be **routed** by a Layer 3 device. This is the single most important VLAN fact.

**The VLAN database.** Stores VLAN IDs, names, and properties such as MTU. Stored in **`vlan.dat`** in **non-volatile memory**, so it survives a power cycle.

⚠️ **`vlan.dat` is separate from the running/startup config.** Erasing the startup configuration does **not** delete VLANs — you must delete `vlan.dat` separately. This trips people up in labs constantly.

**VTP (VLAN Trunking Protocol).** Distributes VLAN configuration from a central **VTP server** to all switches, so you don't configure every VLAN on every switch. ⚠️ **VTP is Cisco-proprietary** — in a mixed-vendor environment you'll need another approach.

**Default VLAN.** VLAN 1 on Cisco gear. 📌 Security best practice: **move user ports off VLAN 1** and change the native VLAN on trunks, because VLAN 1 carries control traffic and is a known target.

### Voice VLAN

A VLAN specifically allocated to **VoIP traffic**.

**Why separate voice:** voice is delay-intolerant (see QoS in 1.2). Isolating it lets you apply **QoS marking** consistently, keeps data traffic from starving calls, and simplifies both troubleshooting and security policy.

📌 The typical deployment: an IP phone with a built-in switch sits between the wall port and the PC. The single switchport carries **tagged voice traffic** on the voice VLAN and **untagged data traffic** on the access VLAN, simultaneously.

### 802.1Q trunking and port tagging

📌 **IEEE 802.1Q** is the standard for VLAN tagging. It inserts a **4-byte tag** into the Ethernet frame containing the VLAN ID.

| Port type | Carries | Tagging |
|---|---|---|
| **Access port** | **One** VLAN | **Untagged** — the end device is unaware of VLANs |
| **Trunk port** | **Multiple** VLANs | **Tagged** with 802.1Q, except the native VLAN |

**Native VLAN.** The one VLAN whose traffic crosses a trunk **untagged**. ⚠️ 📌 **The native VLAN must match on both ends of a trunk.** A mismatch causes traffic from one VLAN to silently land in another — a serious security problem (VLAN hopping) and a classic troubleshooting scenario. Symptom: hosts in different VLANs unexpectedly reach each other, or traffic disappears.

Because the VLAN ID field is 12 bits, the maximum is **4,096 VLANs** — the limitation VXLAN was created to solve (section 1.8).

### Switch interface configuration

Options you'll be asked about:

| Setting | What it does | Trap |
|---|---|---|
| **Speed** | 10/100/1000 Mbps | ⚠️ Hard-set on one side and auto on the other → **duplex mismatch** |
| **Duplex** | Half or full | Same trap |
| **Auto-negotiation** | Both ends negotiate speed and duplex | Best practice is **auto on both ends, or manual on both ends — never mixed** |
| **Port security** | Restricts which MACs may use a port | Applied at the **access layer** |
| **Administrative state** | `shutdown` / `no shutdown` | Ports may be administratively down |

📌 ⚠️ **Duplex mismatch is a top-tier exam symptom.** One side full duplex, the other half. The link comes up and works — but throughput collapses and you see **late collisions, CRC/FCS errors, and runts** on the interface counters. The connection is not "down," which is exactly why it's confusing. Look at interface error counters, not link lights.

**Port security modes:**
- **Protect** — drops violating frames silently
- **Restrict** — drops and logs/increments a counter
- **Shutdown** — 📌 the **default**; puts the port in **err-disabled** state, requiring manual recovery

### Power over Ethernet (PoE)

Standard Ethernet cable carries **electrical power as well as data**.

**Typical devices:** VoIP phones, wireless APs and Wi-Fi extenders, IP cameras.

**Benefits:**
- **Cost savings** — no separate power runs. 📌 The transcript's example is the key one: security cameras mounted **outside a building or high near a ceiling**, where there is no power. PoE means you only pull one Ethernet cable.
- **Safety and reliability** — power comes from a centralized, universally compatible source, and devices have built-in protection against overload and underpowering.
- **Scalability** — extend the network, not the electrical system.
- **Flexibility** — install anywhere Ethernet reaches.

**PoE standards — know the wattage tiers:**

| Standard | Name | Power at the port |
|---|---|---|
| **802.3af** | PoE | ~15.4 W |
| **802.3at** | PoE+ | ~30 W |
| **802.3bt** | PoE++ / 4PPoE | ~60 W (Type 3) / ~100 W (Type 4) |

⚠️ **Power budget is a real constraint.** A switch has a total PoE budget. Attaching more high-draw devices than the budget allows means some simply won't power on — a "the AP won't boot" symptom that has nothing to do with the network.

**PSE vs PD:** the **Power Sourcing Equipment** (switch or injector) supplies; the **Powered Device** consumes.

### Spanning Tree Protocol (STP)

**The problem.** Redundant links at Layer 2 create **switching loops**. Ethernet frames have **no TTL** — unlike IP packets — so a looping frame circulates forever. Broadcast frames multiply on every pass, producing a **broadcast storm** that saturates the network and can bring it down entirely.

📌 ⚠️ **"Why do Layer 2 loops need STP when Layer 3 loops resolve themselves?"** Because IP has TTL and Ethernet does not. That single fact is the answer to a whole family of exam questions.

**What STP does.** Builds a loop-free logical topology by **blocking redundant links**, keeping them in reserve. If an active link fails, a blocked link is brought up.

**How it converges:**
1. Elect a **root bridge** — the switch with the lowest **bridge ID** (bridge priority + MAC address). Lowest priority wins; MAC address breaks ties.
2. Each non-root switch selects one **root port** — its lowest-cost path toward the root.
3. Each segment selects one **designated port**.
4. All remaining ports are **blocked**.

**Port states (classic STP):**

| State | Forwards data? | Learns MACs? |
|---|---|---|
| Blocking | No | No |
| Listening | No | No |
| Learning | No | **Yes** |
| Forwarding | **Yes** | Yes |
| Disabled | No | No |

⚠️ Classic 802.1D convergence takes **30–50 seconds**. **RSTP (802.1w)** converges in seconds and is what you should prefer. **MSTP (802.1s)** maps multiple VLANs to spanning tree instances.

**PortFast / edge ports.** Skips listening and learning on ports connected to end devices so they forward immediately. 📌 **Never enable PortFast on a port connected to another switch** — you reintroduce the loop risk you were trying to prevent. Pair with **BPDU Guard**, which shuts the port down if it ever receives a BPDU.

**The trade-off STP forces** — and this connects back to spine-leaf in section 1.6: you paid for redundant links and STP won't let you use them. That's exactly why data centers moved leaf-to-spine connectivity to **Layer 3**.

### CSMA/CD and CSMA/CA

**CSMA/CD — Carrier Sense Multiple Access with Collision Detection.** The legacy Ethernet rule for shared media: listen before transmitting; if the medium is busy, wait; if two stations transmit at once, detect the collision, send a jam signal, and back off a random interval before retrying.

📌 ⚠️ **CSMA/CD is effectively obsolete on modern switched, full-duplex Ethernet** — there is no shared medium and therefore no collision domain. It mattered in the hub era. **If you see collisions on a modern full-duplex link, that is a duplex mismatch symptom, not normal operation.**

**CSMA/CA — Collision *Avoidance*.** Used by **wireless**, because a station cannot transmit and listen simultaneously, so collisions can't be *detected*. Instead it avoids them — check that the channel is idle, wait a random backoff, and optionally use RTS/CTS handshaking.

### ARP and NDP

**ARP (Address Resolution Protocol)** resolves a known **IPv4 address** to a **MAC address**. The host broadcasts "who has this IP?"; the owner replies with its MAC; the result is cached in the **ARP table**.

Useful commands: `arp -a` to view the cache, `arp -d` to clear it.

⚠️ **ARP is unauthenticated**, which is what makes **ARP spoofing / ARP poisoning** possible — an attacker answers for an IP that isn't theirs and inserts themselves in the path (on-path attack). Detection: two IPs mapping to the same MAC, or a gateway MAC that suddenly changes.

**NDP (Neighbor Discovery Protocol)** is the **IPv6 equivalent of ARP**, and does more:

| Function | Purpose |
|---|---|
| Neighbor Solicitation / Advertisement | Address resolution (ARP's job) |
| Router Solicitation / Advertisement | Finding routers and prefixes — enables **SLAAC** |
| Duplicate Address Detection | Verifies uniqueness before use |
| Redirect | Points a host at a better next hop |

📌 **NDP uses ICMPv6 multicast, not broadcast** — consistent with IPv6 having no broadcast at all.

### MTU and jumbo frames

**MTU (Maximum Transmission Unit)** is the largest payload an interface will carry in one frame. **Standard Ethernet MTU = 1500 bytes.**

**Jumbo frames** exceed that — typically **9000 bytes**. Fewer, larger frames mean less per-frame overhead and lower CPU load, which is why they're used in **storage networks and data centers**.

⚠️ 📌 **MTU must match end to end.** A mismatch causes fragmentation, or — worse — silent black-holing when packets have the **Don't Fragment** bit set and an intermediate link can't carry them. The classic symptom is maddening: **small packets (ping) succeed while large transfers fail or hang.** If you see "ping works but the file share times out," test with `ping -f -l <size>` (Windows) to find the real path MTU.

### 🔧 LAB 2.2 — Switching Deep Dive *(call TORA)*
Multi-switch build with VLANs spanning switches, 802.1Q trunks, a voice VLAN with a PC behind an IP phone, port security in all three violation modes, and STP root bridge manipulation. Break/fix: native VLAN mismatch, a duplex mismatch producing late collisions, an err-disabled port, a deliberately induced broadcast storm with STP disabled, and an MTU mismatch that passes ping but fails file transfer.

---
## 2.3 Wireless Technologies

*Source: Day 5 — Ethernet Switching & Wireless Standards; Day 17 — Wireless Configurations & Physical Installations; Day 2 — cellular*

### The frequency trade-off

📌 **The governing principle, stated once and applied everywhere:** *higher frequency = more data throughput but shorter range, because higher frequencies are more readily blocked by walls and obstructions.* Every wireless design decision comes back to this.

| Band | Range | Throughput | Channels | Interference |
|---|---|---|---|---|
| **2.4 GHz** | **Longer** | **Lower** | 11 in North America; only **1, 6, 11 non-overlapping** | **Heavy** — microwaves, Bluetooth, cordless phones, neighbors |
| **5 GHz** | **Shorter** | **Higher** | Many (~24) non-overlapping | Much less |
| **6 GHz** (Wi-Fi 6E) | **Shortest** (~11–12 m) | Highest | Most | Least — newly opened |

⚠️ 📌 **Channels 1, 6, and 11 are the only non-overlapping channels in 2.4 GHz.** This is a guaranteed exam question and a real-world design rule — adjacent APs must be on non-overlapping channels or they degrade each other.

**Why 2.4 GHz was chosen first.** The band was largely unoccupied — precisely *because* it's a poor band for long-distance transmission. **Water in the atmosphere absorbs energy at this frequency**, which is exactly why microwave ovens use it to heat food. Great for cooking, bad for distance. Over short distances it works fine.

**Why 6 GHz opened up.** Spectrum that was previously reserved (television broadcast moved to cable and satellite; some medical and military allocations) was freed for short-range use. Short range is a feature here — you're not interfering with anything 10 miles away.

### Wi-Fi standards

📌 Memorize speed, band, and the Wi-Fi generation name.

| Standard | Wi-Fi name | Band | Max speed | Notes |
|---|---|---|---|---|
| **802.11** (original) | — | 2.4 GHz | 1–2 Mbps | The baseline |
| **802.11a** | — | **5 GHz** | **54 Mbps** | First move to 5 GHz |
| **802.11b** | — | 2.4 GHz | **11 Mbps** | Backward compatible with 802.11 |
| **802.11g** | — | 2.4 GHz | **54 Mbps** | 802.11a speeds on the 2.4 band |
| **802.11n** | **Wi-Fi 4** | **2.4 and 5** | 600 Mbps | Introduced **MIMO** |
| **802.11ac** | **Wi-Fi 5** | 5 GHz | 433 Mbps – **1.3 Gbps+** | Channel bonding, MU-MIMO |
| **802.11ax** | **Wi-Fi 6** | 2.4 and 5, **simultaneously** | **9.6 Gbps** | OFDMA |
| **802.11ax** | **Wi-Fi 6E** | **6 GHz** | 9.6 Gbps | Same standard, new band |

⚠️ 📌 **The backward-compatibility trap.** If an older, slower client (say 802.11b) associates with a modern AP on the same band, the AP falls back to accommodate it and **the whole network slows down** — because the AP waits on the slow client. This is why "one old device is killing our Wi-Fi" is a legitimate diagnosis and why you segregate legacy devices onto their own SSID/band.

**Throughput techniques introduced over time** (all of them are *encoding and channel* tricks, not new frequencies):
- **MIMO (Multiple Input Multiple Output)** — multiple antennas distinguish a signal arriving directly from one that reflected off a wall, and encode them as separate streams for multiplied throughput.
- **Channel bonding** — combine multiple channels for a single bandwidth-hungry station. ⚠️ Trade-off: other stations get less.
- **OFDMA** — the technique 4G/LTE also uses; subdivides channels for many simultaneous users.

### Cellular

| Generation | Technology | Key characteristics |
|---|---|---|
| 1G | Analog | Voice only |
| **2G** | **GSM**, CDMA | 📌 GSM digitized and **compressed** voice; operates at **900/1800 MHz**; still >90% of global mobile |
| 3G | CDMA-based | Data-capable |
| **4G** | **LTE** | Uses **OFDMA** |
| **5G** | — | **Gigabit speeds and very low latency** |

**Multiplexing methods worth understanding:**
- **TDMA (Time Division Multiple Access)** — one channel divided into **time slots**. Three conversations interleave; each gets every third slot. Because data transmission is so much faster than voice, the receiving circuits reassemble it into continuous real-time speech with no audible gaps.
- **CDMA (Code Division Multiple Access)** — each phone generates a **pseudo-random code** at connection time and mixes it into the data. Other phones hear the transmission but cannot decode it without the code. Allows more simultaneous connections than TDMA.

⚠️ **Generations are generally not backward compatible** with each other — different frequencies and different encoding. A tower may support several because it contains multiple transmitters, but the standards themselves don't interoperate.

📌 **Why 5G latency matters:** the transcript's framing is good — for remote operation (drones, remote equipment), latency is the difference between turning left and hitting a tree. Bandwidth isn't the only metric.

### SSID and guest networks

**SSID (Service Set Identifier)** — the network name clients search for and see in a list.

⚠️ **Hiding the SSID is weak security.** Freely available software can force the AP to reveal it. It raises the bar for a casual user, not for an attacker. Treat it as obscurity, not security.

**Guest network** — its own **virtual SSID**, isolated from the internal network. Provides internet access without exposing internal resources. 📌 This is the correct answer whenever a scenario involves visitors, contractors, or personal devices needing connectivity.

### Wireless security protocols

📌 The evolution, and why each step happened:

| Protocol | Encryption | Status |
|---|---|---|
| **WEP** | RC4, static key, weak IV | ❌ **Broken.** Crackable in minutes. Never use |
| **WPA** | RC4 + **TKIP** | ❌ Deprecated. Interim fix for WEP |
| **WPA2** | **AES-CCMP** | ✅ Still widely used and still considered secure, though vulnerable to specific attacks (e.g. KRACK) |
| **WPA3** | AES + **SAE** | ✅ **Most secure.** Adoption slowed by compatibility |

📌 ⚠️ **The WPA2 → WPA3 distinction is the highest-value fact in this section, and it's about *authentication*, not just encryption:**

- **WPA2 uses a Pre-Shared Key (PSK).** One code, typed into the AP, used by **every client**. ⚠️ **If the code is cracked, everybody is vulnerable** — all sessions, retroactively.
- **WPA3 uses SAE (Simultaneous Authentication of Equals)**, also called the **Dragonfly protocol**. Each device and the AP **negotiate their own separate key**. There is no shared secret between clients. **Each channel is independent**, so compromising one session does not compromise others.

**Why WPA3 isn't universal yet:** it is **not backward compatible with WPA2**, because the authentication methods differ fundamentally. WPA2 devices cannot connect to a WPA3-only network. Some devices can be firmware-upgraded; many cannot, and must be replaced.

**Enterprise vs Personal:**

| | **Personal (PSK / SAE)** | **Enterprise (802.1X)** |
|---|---|---|
| Credentials | One shared passphrase | **Per-user** credentials |
| Backend | None | **RADIUS server** |
| Framework | — | **EAP** |
| Revoking access | Change the key for everyone | **Disable one user** |

📌 **802.1X / EAP / RADIUS is the answer** whenever a scenario mentions per-user wireless authentication, centralized credentials, or the need to revoke one employee's access without disrupting everyone.

### Antennas

| Type | Radiation pattern | Use |
|---|---|---|
| **Omnidirectional** | 360° horizontally — a doughnut shape | 📌 **The most common.** General coverage from a central point; standard indoor APs |
| **Directional** (Yagi, parabolic/dish) | Focused beam | Point-to-point links, long distance, covering a specific area, or reaching a distant building |
| **Patch / panel** | Hemispherical, one direction | Wall-mounted coverage of a room or corridor from the edge |

📌 **The design principle:** directional antennas trade coverage area for **range and gain**. Same transmit power, focused instead of spread. If a scenario needs to reach a warehouse 500 m away, the answer is directional.

### Access point types

| | **Autonomous (fat/thick) AP** | **Lightweight (thin) AP** |
|---|---|---|
| Intelligence | **Self-contained** — full config on the device | Config lives on the **Wireless LAN Controller** |
| Management | **Individually, manually** | **Centrally**, from the WLC |
| Scale | ⚠️ **Small networks.** Building a workgroup of several is difficult because each must be edited separately | **Large corporate networks** — one controller manages many APs |
| Deployment | Often combined AP + switch in one independent device | Ceiling-mounted, PoE, cabled back to a switch |

📌 **The scaling argument is the exam point.** Autonomous APs *can* be grouped, but manual per-device configuration makes consistency painful and error-prone as you add units. A WLC gives you one place to push SSIDs, security policy, channel plans, and power settings — plus features that need a global view, like coordinated channel assignment and roaming.

### Site survey and coverage

Concepts that appear in both configuration and troubleshooting questions:

- **Site survey** — measure signal strength and interference before deployment; produce a **heat map**.
- **RSSI (Received Signal Strength Indicator)** — how strong the received signal is. Closer to 0 is better; **−70 dBm** is a common usable threshold.
- **SNR (Signal-to-Noise Ratio)** — signal strength relative to background noise. ⚠️ **A strong signal in a noisy environment still performs badly** — this is why RSSI alone doesn't tell the story.
- **EIRP** — effective radiated power, the regulated output limit.
- **Channel overlap / co-channel interference** — adjacent APs on the same or overlapping channels degrading each other.
- **DFS (Dynamic Frequency Selection)** — required on certain 5 GHz channels to avoid interfering with radar; an AP must vacate the channel if radar is detected.

### 🔧 LAB 2.3 — Wireless Deployment and Interference *(call TORA)*
Build a multi-AP wireless network in Packet Tracer with a WLC managing lightweight APs, separate corporate and guest SSIDs with VLAN separation, WPA2-Enterprise backed by a RADIUS server, and a 1/6/11 channel plan. Break/fix: two APs sharing a channel, a guest SSID with a route into the internal VLAN, a client stuck on 2.4 GHz dragging the network down, and an evil twin introduced alongside the legitimate SSID.

---
## 2.4 Physical Installations and Specialized Devices

*Source: Day 17 — Physical Installations; Day 9 — Network Implementations*

### Planning a physical installation

**Stage one is assessment.** Map the area where the network will be installed and ask:
- Are all client connections **within the proper distance** of the equipment room?
- What obstacles — concrete walls, fire breaks — sit between the user and the closet?

**Cabling vocabulary you need:**

| Term | Meaning |
|---|---|
| **Run** | The cable routed from the closet through the ceiling |
| **Drop** | Where the run comes down the wall to a connector |
| **Raceway** | 📌 A plastic covering adhered to the wall, used when the wall is solid and the cable **must be mounted on the outside** rather than run inside it |
| **Poles** | Used to bring a drop to a workstation where there is no adjacent wall |

📌 ⚠️ **The TIA/EIA-568 / 569 distance budget — memorize all three numbers:**

| Segment | Max length |
|---|---|
| **Equipment room → wall outlet** (the horizontal run) | **90 meters** |
| **Wall outlet → end computer** (patch cable) | **6 meters** |
| **Patch panel → equipment in the rack** | **3 meters** |

**90 + 6 + 3 = 99**, which is how the familiar **100-meter Ethernet limit** is actually budgeted in practice. This is a much better answer than "100 meters" if a question gives you the components separately — and questions do.

⚠️ **568 vs 569:** apart from the wiring color pattern, the standards are essentially the same and both define things like maximum cable length.

### Equipment rooms, racks, and hardware

| Item | Purpose |
|---|---|
| **MDF (Main Distribution Frame)** | The primary equipment room — where the main termination and core equipment live |
| **IDF (Intermediate Distribution Frame)** | Satellite closets serving a floor or wing, cabled back to the MDF |
| **Rack units (U)** | The vertical measurement of rack-mounted equipment; 1U ≈ 1.75 inches |
| **Patch panel** | Termination point for horizontal runs (see 1.5) |
| **PDU (Power Distribution Unit)** | Distributes power within the rack |
| **UPS** | Battery backup and power conditioning (see 1.5) |

📌 The MDF/IDF hierarchy exists **because of the 90-meter limit.** If users are farther than that from the MDF, you place an IDF closer to them. That's the whole design logic, and it connects the distance number to the room layout.

### Environmental factors

**The core fact:** all electronic devices **generate heat**, so keeping temperature constant around them is mandatory.

⚠️ **Scale changes the problem.** In an office with computers spread across a large area, the heat generated doesn't meaningfully warm the room. In a **data center**, many devices are concentrated in a small area — so **planning that room to dissipate heat is imperative**.

**HVAC (Heating, Ventilation, and Air Conditioning):**

📌 Two exam-relevant points the transcript makes well:

1. **Fire system integration.** The air an HVAC system circulates **feeds a fire**. In a data center fire, you do not want to keep blowing air onto it. HVAC systems therefore **detect fire and stop ventilation** so they don't make it worse.
2. **Keep the data center HVAC separate from the building HVAC.** Most office buildings already have HVAC for the people working there. The data center needs its own, so that problems with the main building system don't take down the data center's cooling.

**Other environmental controls:**
- **Humidity** — ⚠️ **too low → electrostatic discharge; too high → condensation and corrosion.** Both directions are dangerous, and questions often test that you know it's a *range*, not a maximum.
- **Airflow management** — hot aisle / cold aisle containment so exhaust from one row doesn't become intake for the next.
- **Fire suppression** — clean-agent systems rather than water in equipment areas.

🔗 **A+ crossover:** ESD precautions, proper grounding, and antistatic practice all carry straight over. Same physics, larger scale.

### Legacy interconnection devices

| Device | Layer | Behavior |
|---|---|---|
| **Hub** | 1 | 📌 **"Just an amplifier."** No forwarding intelligence. Repeats every frame out every port. **One collision domain, one broadcast domain.** Obsolete |
| **Bridge** | 2 | Software-based, few ports. Forwards on MAC address. **Segments collision domains.** Essentially the ancestor of the switch |
| **Switch** | 2 (or 3) | Hardware-based, many ports. **Each port is its own collision domain.** See 1.2 |
| **Router** | 3 | **Separates broadcast domains.** See 1.2 |

📌 ⚠️ **The collision domain / broadcast domain table is a reliable exam question:**

| Device | Collision domains | Broadcast domains |
|---|---|---|
| Hub | **1** (all ports) | 1 |
| Switch | **One per port** | **1** (unless VLANs) |
| Router | One per interface | **One per interface** |

**A switch with VLANs creates one broadcast domain per VLAN.** That's the connection between this table and section 2.2.

### VoIP — Voice over IP

Carrying voice conversations over the data network rather than a separate telephone system.

**Requirements and consequences:**
- Voice is **delay-intolerant** — needs QoS (see 1.2) and typically a **voice VLAN** (see 2.2)
- Often powered by **PoE** (see 2.2), so phones need no separate power
- **SIP** handles signaling (ports 5060/5061); RTP carries the media
- Replaces the traditional **PBX**

⚠️ **Jitter is the specific enemy of voice** — variation in packet arrival time, not raw latency. Symptoms: choppy audio, echo, dropouts. A network with excellent average latency but high jitter delivers terrible calls.

### IoT — Internet of Things

Everyday devices with network connectivity generating large volumes of data. Examples: smart thermostats, cameras, sensors, appliances, medical and industrial devices.

⚠️ 📌 **IoT is a security problem, and that's how it's tested.** These devices commonly ship with default credentials, receive infrequent or no patches, and have limited or no built-in security. **The correct architectural answer is almost always segmentation** — put IoT on its own VLAN or network segment with tightly restricted access to everything else.

### SCADA and ICS

**SCADA (Supervisory Control and Data Acquisition)** gathers and analyzes data **in real time** to monitor equipment and manage operations in a plant or factory.

📌 It's related to IoT — many devices generating a lot of data — but the real challenge is **turning raw data into useful information**.

**What SCADA does:**
- Control industrial processes **locally or remotely** across many locations
- Monitor, gather, and process sensor data in real time
- **Directly interact** with monitored devices — pumps, motors, control valves — through **HMI (Human Machine Interface)** software
- Log collected data to a file or database for later analysis

⚠️ **The security framing that matters:** industrial control systems were designed for **isolated networks** and often run legacy protocols with no authentication or encryption. Connecting them to corporate networks or the internet — for the convenience of remote monitoring — is where the risk enters. **Air-gapping and segmentation** are the standard answers.

### 🔧 LAB 2.4 — Physical Design and Specialized Segments *(call TORA)*
Design a two-floor building layout honoring the 90/6/3 distance budget, placing MDF and IDF appropriately and justifying each. Build it in Packet Tracer with VoIP phones on a PoE switch with a voice VLAN, an isolated IoT segment, and a segmented SCADA/ICS network. Break/fix: a horizontal run exceeding 90 m producing intermittent errors, a PoE budget exceeded so an AP won't boot, an IoT device with a route into the corporate VLAN, and a VoIP call degraded by missing QoS marking.

---
# PART 3 — Network Operations (Domain 3.0, 19%)

## 3.1 Network Documentation, Life Cycle, and Configuration Management

*Source: Day 18 — Organizational Processes & Procedures; Day 14 — Network Operations*

This section feels like the least technical material on the exam. It is also where a lot of easy points live, because the answers are consistent and the vocabulary is precise.

### IPAM — IP Address Management

**A software tool for managing IPv4 and IPv6 infrastructure administration and monitoring, by centrally managing your DHCP and DNS servers.**

📌 **The problem it solves.** DHCP and DNS each have their own management interfaces, and those work fine — for one server. The difficulty is **managing multiple DHCP and DNS servers across a large organization**. With VLANs in play, address scopes end up scattered, and tracking which subnet belongs to which VLAN across multiple servers becomes a daunting task.

**What IPAM gives you:**
- **A single interface** for the entire IP address space, both dynamic and static
- Customizable views — by server, by scope, or by subnet
- **Resource pool monitoring** — how many addresses are assigned and how much of the pool remains
- **Alerts** when a pool crosses a utilization threshold

⚠️ Scope exhaustion is a silent failure that surfaces as APIPA addresses on user machines (see 3.4). IPAM's utilization alerting is specifically what prevents that.

### Asset management and inventory

**Asset inventory is the process of identifying every technology asset the organization owns** and tracking configuration changes throughout each asset's life cycle.

📌 **Why it's a prerequisite, not paperwork:** you cannot secure, patch, license, or replace what you don't know you have. The zero trust discussion in 1.8 makes the same point — inventory is step one, because you can't classify devices as managed or unmanaged until you know they exist.

**What to track:** device identity and serial numbers, location, owner, configuration, warranty and support status, and lifecycle stage.

### Life cycle management

**Key milestones:** purchase/installation → useful life → decommissioning → **end of life** → **end of support**.

📌 ⚠️ **EOL vs EOS — a precise distinction the exam tests:**

| | **EOL (End of Life)** | **EOS (End of Support)** |
|---|---|---|
| Meaning | The product is **no longer sold** | **Support has ended** — no more updates or patches |
| Updates | ⚠️ **Limited updates still available** | ❌ **No updates at all** |
| Timing | Comes first | Can be **2 years or more after** EOL |

📌 **The security consequence:** at EOL a product receives limited updates; at EOS it receives none. **A device past end of support will never be patched again**, so every vulnerability discovered from that point forward is permanent. That is the argument for replacement, and it's the reasoning an exam question wants you to reproduce.

### Change management

**The planning, testing, and approving of changes.**

📌 **Why it exists:** changes cause unexpected results. The transcript's example is deliberately mundane and therefore convincing — swapping in an **unsupported or undocumented network card** can disrupt the network or take it down entirely.

**Objectives:**
- **Minimize disruption during the change** — the business keeps running while the change is made
- **Create and implement standardized procedures**

**The change management process:**

| Step | Content |
|---|---|
| **Request** | Who wants what, and why |
| **Impact analysis** | What breaks if this goes wrong; who is affected |
| **Approval** | Typically a **CAB (Change Advisory Board)** for significant changes |
| **Testing** | Validate in a non-production environment first |
| **Scheduling** | Maintenance window, communicated in advance |
| **Implementation** | Execute the documented plan |
| **Rollback plan** | ⚠️ **Defined before the change begins**, not improvised during it |
| **Documentation** | Update diagrams, configs, and the CMDB |

⚠️ 📌 **If an exam scenario describes an outage caused by an undocumented change, the answer is almost always a change management failure** — not a technical one. Look for the missing approval, the absent rollback plan, or the documentation nobody updated.

### Incident response

**Responding to incidents that threaten the security of the network or its information.** These responses are inherently **reactionary** — something happens, the team responds. The goal of planning is to decide **how you will respond before the incident occurs**.

**Phases:**

| Phase | Activity |
|---|---|
| **Preparation** | Plans, tooling, training, contact lists |
| **Detection & analysis** | Identify that something happened and characterize it |
| **Containment** | Stop the spread |
| **Eradication** | Remove the cause |
| **Recovery** | Restore normal service, monitor for recurrence |
| **Lessons learned** | Post-incident review feeding back into preparation |

⚠️ Connect this to the elasticity warning in 1.3: in a cloud environment, a compromised VM may be **destroyed automatically before you can investigate it**. Incident response planning must account for evidence preservation in ephemeral infrastructure.

### Wireless site surveys

📌 Three types, and the distinction is precise:

| Type | What it measures | Connected to the AP? |
|---|---|---|
| **Passive** | Existing AP **signal strength, interference, and coverage** — the signal itself, not the data in it. Produces the overall RF picture: strong, weak, reflections | ❌ **No** |
| **Active** | **Network traffic patterns**, which APs are busiest, **throughput and packet loss**, physical data rate, frequencies in use. "We're receiving a signal, but are we actually getting the data through?" | ✅ **Yes** |
| **Predictive** | Modeled in software from floor plans and materials, before anything is installed | N/A — nothing built yet |

⚠️ **The key insight:** a passive survey can show excellent signal strength while an active survey reveals that data isn't actually getting through — because of retransmissions caused by reflections or interference from other devices. **Signal strength alone doesn't tell you the network works**, which is the same point made about RSSI vs SNR in section 2.3.

### Organizational documents and agreements

| Document | Purpose |
|---|---|
| **NDA (Non-Disclosure Agreement)** | Binds parties — two companies or two individuals — not to disclose confidential information |
| **SLA (Service Level Agreement)** | Defines the **service level committed**, including availability targets and penalties |
| **MOU (Memorandum of Understanding)** | Statement of intent between parties; less binding than a contract |
| **MSA (Master Service Agreement)** | Umbrella terms governing an ongoing relationship |
| **SOW (Statement of Work)** | The specific deliverables, timeline, and scope for a particular engagement |
| **AUP (Acceptable Use Policy)** | What users may and may not do with organizational resources |
| **BYOD policy** | Rules for personal devices on the corporate network |

### Network documentation

| Document | Contents |
|---|---|
| **Physical network diagram** | Actual cabling, ports, rack layout, device locations |
| **Logical network diagram** | IP addressing, VLANs, routing, traffic flow |
| **Rack diagram** | Elevation showing what occupies each U |
| **Wiring / cable map** | Run and drop identifiers, patch panel port mapping |
| **IDF/MDF documentation** | What lives in each closet |
| **Baseline configuration** | The known-good standard config for a device class |
| **Asset inventory / CMDB** | Everything you own and its state |
| **Site survey report** | Wireless coverage and RF characteristics |
| **Audit and assessment reports** | Findings and remediation status |

📌 **The hybrid topology warning from section 1.6 applies here:** complex networks are only manageable if they're documented. Documentation isn't a deliverable at the end of a project — it's what makes troubleshooting possible six months later when the person who built it has left.

⚠️ **Labeling** is documentation too. Labeled cables, ports, and racks convert a two-hour trace into a two-minute one.

### Security policies

Policies vary by organization, but the standard set:

| Policy | Covers |
|---|---|
| **Password policy** | Length, complexity, rotation, reuse, lockout |
| **Acceptable use** | Permitted use of systems and network |
| **Data loss prevention (DLP)** | Preventing sensitive data from leaving |
| **Remote access** | VPN requirements, MFA, device standards |
| **BYOD** | Personal device requirements and access limits |
| **Onboarding / offboarding** | ⚠️ Account provisioning and — critically — **deprovisioning** |
| **Incident response** | Roles, escalation, communication |
| **Data classification and retention** | What data is sensitive and how long it's kept |

📌 ⚠️ **Offboarding is the one that fails in practice.** Orphaned accounts belonging to departed employees are a persistent, well-documented attack vector. If a scenario mentions a former employee retaining access, the failure is an offboarding process gap, not a technical control.

### On-premises vs cloud management models

| | **On-premises** | **Cloud-based** |
|---|---|---|
| Infrastructure | Owned and operated in-house | Provider-operated |
| Control | Complete | Shared responsibility |
| Cost model | **Capital expenditure** up front | **Operational expenditure**, pay as you use |
| Scaling | Buy hardware | Elastic (see 1.3) |
| Suits | Large campuses, regulated data | Distributed organizations, variable demand |

📌 The **shared responsibility model** is the concept to carry away: in cloud, the provider secures *the cloud*, and you secure *what you put in it*. Where that line falls depends on the service model — it moves as you go IaaS → PaaS → SaaS (see 1.3).

### 🔧 LAB 3.1 — Documentation and Change Simulation *(call TORA)*
Rather than a pure build, this is a documentation exercise on a Packet Tracer topology: produce physical and logical diagrams, an addressing plan, and a rack elevation for a network you've built. Then execute a change through a full change management workflow — including a deliberately failed change requiring rollback — and document the incident.

---
## 3.2 Network Monitoring and Performance

*Source: Day 14 — Network Operations; Day 16 — Network Monitoring & DR Concepts*

### What monitoring is for

**Network monitoring is the continual observation of the state of the network and its data.** It lets IT staff assess patterns, spot developing problems before users report them, and make informed capacity decisions.

📌 The core value proposition: monitoring converts **reactive** troubleshooting into **proactive** management. You find the failing link before the help desk phone rings.

### Factors affecting network performance

Things that degrade performance, which you should be able to name in a scenario:

| Factor | Effect |
|---|---|
| **Bandwidth saturation** | Link at capacity; everything queues |
| **Latency** | Delay in transit |
| **Jitter** | **Variation** in latency — kills voice and video |
| **Packet loss** | Retransmissions; catastrophic for real-time traffic |
| **Duplex mismatch** | Collapsed throughput with a link that looks "up" (see 2.2) |
| **Broadcast storms** | Layer 2 loop with no STP (see 2.2) |
| **Device resource exhaustion** | CPU or memory on the switch/router itself |
| **MTU mismatch** | Fragmentation or black-holed large packets (see 2.2) |
| **Environmental** | Heat causing hardware instability (see 2.4) |

### SNMP

Identifies and monitors devices on the network. Ports **161** (polling) and **162** (traps). See 1.4.

| Component | Role |
|---|---|
| **Manager / NMS** | The central monitoring station that polls agents |
| **Agent** | Software on the managed device that responds |
| **MIB** | **Management Information Base** — the structured database of what can be queried |
| **OID** | **Object Identifier** — the address of a specific value inside the MIB |
| **Trap** | 📌 **Unsolicited** alert pushed from device to manager |
| **Inform** | Like a trap, but **acknowledged** so the sender knows it arrived |

📌 ⚠️ **Polling vs traps is the design trade-off:** polling is regular and predictable but adds constant background traffic and may miss an event between poll intervals. Traps are immediate and efficient but **unacknowledged in SNMP** — a lost trap is simply lost, which is why informs exist.

⚠️ **SNMPv1 and v2c transmit community strings in cleartext.** Only **SNMPv3** adds authentication and encryption. Any hardening question resolves to v3, and changing default community strings ("public"/"private") is a basic hardening step.

### Log files

Logs provide a record of activity for troubleshooting, security investigation, and compliance.

| Log type | Contains |
|---|---|
| **System** | OS and hardware events |
| **Application** | Software-specific events |
| **Security / audit** | Logons, privilege use, policy changes |
| **Traffic / flow** | Connection records |

**Syslog** (port **514**, UDP) is the standard for centralized log collection.

📌 **Syslog severity levels — 0 is most severe:**

| Level | Name |
|---|---|
| 0 | **Emergency** |
| 1 | Alert |
| 2 | Critical |
| 3 | Error |
| 4 | Warning |
| 5 | Notice |
| 6 | Informational |
| 7 | **Debug** |

⚠️ **Debug (7) is the most verbose, not the most severe.** Leaving a device at debug level in production can generate enough logging to affect device performance. Mnemonic for the order: **Every Awesome Cisco Engineer Will Need Ice cream Daily.**

📌 **Centralize logs.** Logs stored only on the device are lost if the device fails — or is wiped by an attacker. A central **SIEM** or syslog server preserves evidence and enables correlation across devices. This is also why **NTP matters** (see 3.4): correlation is impossible without synchronized time.

### Interface monitoring and error counters

Interfaces are where everything actually happens, and their counters are the highest-value diagnostic data on the network.

📌 **The error table — learn what each error *implies*, not just what it is:**

| Error | Meaning | Usual cause |
|---|---|---|
| **FCS / CRC errors** | The **Frame Check Sequence** applied by the sender doesn't match the **cyclic redundancy check** computed by the receiver — the frame is corrupt and is **discarded, requiring retransmission** | Bad cable, EMI, failing NIC, **duplex mismatch** |
| **Runts** | Frames **smaller** than 64 bytes | Collisions, duplex mismatch |
| **Giants / jumbo** | Frames **larger** than the MTU | MTU mismatch, misconfiguration |
| **Late collisions** | Collision detected **after** the first 64 bytes | 📌 **Almost always duplex mismatch** or a cable run exceeding the distance limit |
| **Drops / discards** | Frames dropped due to congestion or full buffers | Oversubscription, bandwidth saturation |
| **Input/output errors** | Aggregate error counter | Investigate the specific sub-counters |
| **Interface resets / flapping** | Link repeatedly up and down | Failing hardware, marginal cable, power issue |

⚠️ **An error counter that is high but *static* reflects a past problem. A counter that is *incrementing* reflects a live one.** Always check the counters twice, a minute apart. This distinction separates people who read counters from people who understand them.

**Interface utilization** — sustained high utilization means you need more capacity or better traffic management; it is not itself an error.

### Baselines

📌 **A baseline is a recorded set of performance metrics captured during normal operation.**

**Why they matter:** without a baseline, "the network is slow" is unfalsifiable. With one, you can say the link that normally runs at 30% is now at 85%, and *that* is actionable.

**Uses:**
- Detect deviations from normal
- Justify capacity planning and budget with evidence
- Validate that a change improved things
- Support anomaly-based detection (see the IDS discussion in 1.2)

⚠️ **Baselines must be re-taken after significant changes.** A baseline from before you added 200 users or migrated to the cloud is worse than no baseline, because it produces confident wrong conclusions.

### NetFlow

A **Cisco-developed network protocol** for collecting **traffic flow** information.

📌 **The distinction the exam wants:** SNMP tells you **how much** traffic an interface carried. **NetFlow tells you what that traffic actually was** — who talked to whom, on which ports, for how long, and how much. Flow data answers "why is the link saturated," which SNMP alone cannot.

**A flow is identified by:** source IP, destination IP, source port, destination port, protocol, interface, and type of service.

**Uses:** bandwidth analysis, identifying top talkers, security anomaly detection, billing and chargeback, capacity planning.

⚠️ **NetFlow is metadata, not packet capture.** It records *that* a conversation happened and its characteristics; it does **not** contain the payload. That makes it far more storage-efficient than full packet capture, and it's the right answer when a scenario needs long-term traffic visibility without the storage cost. **sFlow** and **IPFIX** are the vendor-neutral equivalents.

### Uptime and availability

**Availability** is the amount of time a network or resource is operational and accessible.

📌 **The nines table — memorize the downtime figures:**

| Availability | Downtime per year | Downtime per month |
|---|---|---|
| 99% ("two nines") | ~3.65 days | ~7.2 hours |
| 99.9% ("three nines") | ~8.76 hours | ~43 minutes |
| **99.99% ("four nines")** | **~52.6 minutes** | ~4.3 minutes |
| 99.999% ("five nines") | **~5.26 minutes** | ~26 seconds |

⚠️ Each additional nine costs dramatically more than the last. "Five nines" is a serious engineering and financial commitment, not a marketing phrase. **SLAs** codify the agreed availability target and the penalties for missing it.

### Monitoring solutions

Network monitoring applications provide an overview of operations: device discovery and inventory, availability and performance polling, alerting and thresholds, dashboards and reporting, and topology mapping.

📌 **Agent-based vs agentless:** agent-based gives deeper visibility into the host but requires software deployment and maintenance on every device. Agentless (typically SNMP or WMI) deploys faster and touches nothing, but sees less. The trade-off is depth vs deployment cost.

### 🔧 LAB 3.2 — Monitoring and Baseline Establishment *(call TORA)*
Configure SNMP with a monitoring server, set up syslog forwarding from all devices with correct severity levels, synchronize time with NTP so log correlation works, and capture a performance baseline under normal load. Then induce failures — a duplex mismatch, a saturated link, a flapping interface — and identify each one purely from the counters and logs, without looking at the configuration.

---
## 3.3 Disaster Recovery and High Availability

*Source: Day 13 — Disaster Recovery & High Availability; Day 16 — Network Monitoring & DR Concepts*

### The vocabulary, precisely

⚠️ These four metrics are routinely confused, and the exam exploits that. Learn them as two pairs.

**Pair 1 — measuring reliability and repair:**

| Metric | Full name | Measures |
|---|---|---|
| **MTBF** | **Mean Time Between Failures** | The **average time until a system or component fails.** Indicates **reliability** |
| **MTTR** | **Mean Time To Repair/Recovery** | The **average time to restore** a failed system |

📌 **MTBF calculation: total operating time ÷ number of failures.**
*Worked example from the course:* a system runs 1,000 hours and fails twice → 1000 ÷ 2 = **500 hours MTBF**. The same system failing five times → 1000 ÷ 5 = **100 hours**, indicating a **less reliable** system.

📌 **Higher MTBF = more reliable. Lower MTTR = faster recovery.** They move in opposite directions and both are good.

⚠️ **What MTBF is not.** It is **not a guaranteed lifetime.** An individual unit may fail well before or long after the MTBF figure. It's an average across many units. Also note the calculation's limitations: it doesn't account for *when* failures occur (a system near end-of-life fails more often than a new one), and external events — a fire, a power surge — cause failures that say nothing about the product's inherent reliability.

**Factors affecting MTBF:** the operating environment, quality of materials, and **ongoing preventative maintenance**.

📌 The preventative maintenance example is a good one: computers have shorter lifetimes in **higher-temperature environments**, and **dust increases heat retention**. Dust should be removed on a regular schedule, with frequency determined by how dusty the environment actually is. This connects directly to the HVAC discussion in 2.4.

**Pair 2 — defining recovery objectives (these are decisions, not measurements):**

| Metric | Full name | Answers |
|---|---|---|
| **RPO** | **Recovery Point Objective** | **How much DATA can we afford to lose?** Measured backward from the incident |
| **RTO** | **Recovery Time Objective** | **How long can we afford to be DOWN?** Measured forward from the incident |

📌 **The memory hook:** **RPO = Point in time = data loss tolerance.** **RTO = Time to restore = downtime tolerance.**

⚠️ **RPO drives backup frequency.** An RPO of one hour means you must back up at least hourly — anything less and you cannot meet it. **RTO drives infrastructure investment** — a four-hour RTO and a four-week RTO buy completely different disaster recovery sites.

### Disaster recovery sites

**A DR site is another location where the organization can continue to operate if the current location is no longer usable** — after a fire, hurricane, or flood. Without a backup location and backups of critical information, a business can simply **cease to exist**.

📌 **The three site types — this table is guaranteed exam content:**

| Site | Hardware | Data | Time to operational | Cost |
|---|---|---|---|---|
| **Cold** | ❌ Not installed — **just a building** | Exists in backup; must be copied after equipment is installed and configured | **Days to weeks** | **Cheapest** |
| **Warm** | ✅ In place, partially or fully configured | Restored from backup, then tested | **Hours to days** | Middle |
| **Hot** | ✅ Fully installed and running | **Continuously replicated / current** | **Minutes** — near-immediate | **Most expensive** |

⚠️ **The trade-off is cost versus recovery time, and it maps directly onto RTO.** A cold site is cheapest but the days or weeks required may be **completely unacceptable** depending on the organization. If a scenario states an RTO measured in minutes, only a **hot site** satisfies it — cost is not the deciding factor, the requirement is.

**Cloud DR** has largely changed this calculus, letting organizations maintain warm or hot capability without owning a second facility. This connects to the elasticity discussion in 1.3.

### Disaster recovery testing

**DR testing evaluates the plan to determine whether it actually works.** A plan that has never been tested is an assumption, not a capability.

📌 **Testing methods, from least to most disruptive:**

| Method | What happens |
|---|---|
| **Tabletop exercise** | Participants talk through the plan in a room. No systems touched. Cheapest; finds gaps in documentation and roles |
| **Walkthrough / structured review** | Step-by-step review of procedures with the responsible teams |
| **Simulation** | A realistic scenario is enacted without affecting production |
| **Parallel test** | Recovery systems are brought up **alongside** production; production keeps running |
| **Full interruption / failover test** | Production is actually failed over to the DR site. ⚠️ Most realistic, highest risk, and the only one that proves the plan truly works |

📌 **The most common finding in DR testing is not that the technology failed — it's that documentation was stale, contact lists were wrong, or nobody knew who had authority to declare a disaster.** That's why tabletop exercises are valuable despite touching no systems.

### High availability

**High availability means resources are available nearly full-time** — minimizing both planned and unplanned downtime.

📌 **The governing principle: eliminate single points of failure.** For every component in the path, ask what happens when it fails. If the answer is "everything stops," that's an SPOF.

**HA solutions across the stack:**

| Layer | Solution |
|---|---|
| **Gateway** | **FHRP** — HSRP, VRRP, GLBP (see 2.1) |
| **Link** | **Link aggregation / LACP**, redundant uplinks, STP alternate paths |
| **Interface** | **NIC teaming** |
| **Server** | **Clustering**, load balancing |
| **Storage** | **RAID**, SAN replication |
| **Power** | **UPS**, generators, dual PSUs, **dual power feeds** |
| **Site** | Hot/warm DR sites, geographic distribution |

### Redundancy vs clustering

⚠️ Related but distinct, and the exam separates them.

| | **Redundancy** | **Clustering** |
|---|---|---|
| Concept | A **duplicate component** ready to take over | **Multiple systems working together as one logical unit** |
| Typical state | Standby, often idle | **Active participants** |
| Adds capacity? | Usually no | **Yes** — nodes share the workload |
| Failure behavior | Failover to the spare | Remaining nodes absorb the load |

📌 Clustering delivers **both** availability and scalability; simple redundancy delivers availability only. That's why clustering costs more and is more complex.

### NIC teaming

**Combines multiple physical network adapters into one logical interface.**

**Benefits:**
- **Fault tolerance** — if one NIC or its cable or its switch port fails, traffic continues on the others
- **Increased throughput** — aggregate bandwidth across members (depending on mode)
- **Load balancing** across the member adapters

📌 **The real value is the failure domain it covers.** Team two NICs into **two different switches** and you survive the loss of an entire switch, not just a cable. Teaming both NICs into the same switch protects against cable and port failure but leaves the switch as a single point of failure. That design distinction is exactly what a scenario question tests.

Related: **LACP / 802.3ad** (see 2.1) is the standard for negotiating aggregated links on the switch side.

### Load balancing for availability

*(Full treatment in section 1.2.)* In the HA context, the load balancer's contribution is that a **back-end server failure is invisible to the user** — the request is seamlessly served by another server holding the same content, because the user was connected to the load balancer, not to the individual server.

### Facilities and infrastructure support

A significant component of any HA or DR plan, and easy to overlook because it isn't "networking."

| Element | Consideration |
|---|---|
| **Power** | UPS for graceful shutdown and ride-through; **generators** for extended outages; dual feeds from separate utility circuits; **PDUs** in racks |
| **Cooling** | HVAC sized for the heat load; redundant units; separate from building HVAC (see 2.4) |
| **Fire suppression** | Clean-agent systems; **HVAC integration to stop feeding air to a fire** (see 2.4) |
| **Environmental monitoring** | Temperature and humidity sensors with alerting |
| **Physical security** | Covered in Part 4 |

⚠️ **A UPS does not make a system highly available on its own.** It buys you time for a graceful shutdown (see 1.5). Extended operation requires a **generator**, and generators require fuel, testing, and transfer switches that themselves need maintenance. "We have a UPS" is not a continuity plan.

### Backups

| Type | What it copies | Restore complexity | Backup speed |
|---|---|---|---|
| **Full** | Everything | **Simplest** — one set | Slowest |
| **Incremental** | Changes since the **last backup of any type** | ⚠️ Needs the full **plus every** incremental since | **Fastest** |
| **Differential** | Changes since the **last full** | Needs the full **plus the latest** differential only | Grows over time |

📌 **The 3-2-1 rule:** **3** copies of the data, on **2** different media types, with **1** stored **off-site**.

⚠️ **An untested backup is not a backup.** Restore testing belongs in the DR testing cycle above. The failure mode organizations actually experience is discovering during an incident that the backups have been silently failing for months.

### 🔧 LAB 3.3 — Redundancy and Failover *(call TORA)*
Build a topology with dual routers running FHRP, redundant switch uplinks under STP, NIC-teamed servers connected to two different switches, and a load-balanced server pair. Prove each layer of redundancy by failing it while a continuous ping runs, and measure actual failover time against a stated RTO. Break/fix: FHRP configured but both routers claiming active, a NIC team homed to a single switch, and STP blocking the wrong link after a root bridge change.

---
## 3.4 DHCP, DNS, and Time Protocols

*Source: Day 14 — Network Management & IP Services*

### DHCP — dynamic addressing

Client systems don't have to be manually configured; they request configuration at startup.

**What DHCP delivers:** IP address, subnet mask, default gateway, DNS servers, and optionally NTP servers, domain name, and vendor-specific options.

**DORA** — see section 1.4 for the exchange. Key terms:

| Term | Meaning |
|---|---|
| **Scope** | The pool of addresses a server can hand out for a subnet |
| **Lease** | How long a client may keep an address before renewing |
| **Reservation** | 📌 A **specific IP tied to a specific MAC**, so a device always gets the same address while still using DHCP |
| **Exclusion** | Addresses inside the scope that DHCP must **not** hand out (e.g. static server addresses) |
| **Relay agent / IP helper** | Forwards DHCP broadcasts across a router to a server on another subnet |

📌 ⚠️ **Reservation vs static assignment.** A reservation is managed centrally at the DHCP server; a static address is configured on the device itself. For printers and servers, **reservations are usually preferred** because you keep central visibility and control. If a question asks how to guarantee a consistent address *without* manually configuring each device, the answer is reservation.

**The classic DHCP failure modes:**

| Symptom | Cause |
|---|---|
| **169.254.x.x (APIPA)** on one subnet, others fine | Missing **IP helper / relay** on that subnet's router |
| APIPA everywhere | DHCP server down, or scope exhausted |
| Duplicate IP conflicts | Static addresses inside the scope with **no exclusion** |
| Client gets an address on the wrong subnet | VLAN assignment or relay misconfiguration |
| Address works, but no internet | Scope handing out a wrong gateway or DNS server |

### DNS — name resolution

Maps human-readable names to IP addresses. Runs on **port 53** (UDP for queries, TCP for zone transfers).

**The resolution order** — worth knowing because troubleshooting follows it:
1. Local **cache**
2. **HOSTS file** ⚠️ — a locally modified HOSTS file overrides DNS entirely and is a classic malware trick *and* a classic "why does this one machine resolve wrong?" answer
3. Configured **DNS server**
4. Recursive lookup: root → TLD → authoritative

**Record types — memorize this table:**

| Record | Purpose |
|---|---|
| **A** | Name → **IPv4** address |
| **AAAA** | Name → **IPv6** address |
| **CNAME** | Alias — one name pointing to another name |
| **MX** | **Mail exchange** — where to deliver email for the domain |
| **NS** | **Name server** authoritative for the zone |
| **PTR** | **Reverse lookup** — IP → name |
| **SOA** | **Start of Authority** — zone metadata, serial number, refresh timers |
| **SRV** | **Service** location — host and port for a specific service |
| **TXT** | Arbitrary text; used for **SPF, DKIM, DMARC** and domain verification |
| **DNAME** | Redirects an entire subtree of names, where CNAME redirects a single name |

**Zone concepts:**
- **Forward lookup zone** — name to IP. **Reverse lookup zone** — IP to name (PTR records).
- **Primary / secondary** — the authoritative writable copy vs read-only replicas.
- **Zone transfer** — replication between servers. ⚠️ Uses **TCP**, and should be **restricted to authorized secondaries** — an open zone transfer hands an attacker your entire network map.
- **Internal vs external DNS (split-brain)** — different answers for internal and external clients, so internal hostnames aren't exposed publicly.

⚠️ 📌 **The signature DNS symptom: `ping 8.8.8.8` succeeds but `ping google.com` fails.** Connectivity is fine at Layers 1–3; name resolution is broken. Check DNS server settings, `nslookup`/`dig`, the HOSTS file, and DNS cache (`ipconfig /flushdns`).

### NTP and time synchronization

**NTP** (port **123**, UDP) synchronizes clocks across the network.

**Stratum levels:** Stratum 0 is a reference clock (atomic, GPS); Stratum 1 is directly attached to one; each subsequent stratum is one hop further from the source. Lower stratum = more authoritative.

📌 **Why time matters more than it appears:**
- **Kerberos authentication fails** on clock skew beyond a small tolerance (typically 5 minutes)
- **Certificate validation** depends on accurate time — a wrong clock makes valid certs look expired or not-yet-valid
- **Log correlation** across devices is impossible without synchronized timestamps, which breaks incident investigation
- Scheduled tasks and backups fire at the wrong time

**Related protocols:**
- **PTP (Precision Time Protocol)** — sub-microsecond accuracy for environments where NTP isn't precise enough (financial trading, industrial control)
- **NTS (Network Time Security)** — adds authentication and integrity to NTP, protecting against an attacker feeding you false time

### 🔧 LAB 3.4 — Addressing and Name Services End to End *(call TORA)*
Build a routed multi-VLAN network with a central DHCP server serving every subnet via IP helper addresses, a DNS server carrying A, AAAA, CNAME, MX and PTR records, and NTP synchronisation across all devices. Break/fix: a missing IP helper causing APIPA on one VLAN only, a scope with no exclusions producing address conflicts, a stale DNS record, and clock skew breaking authentication.

---
## 3.5 VPNs and Remote Access

*Source: Day 14 — Network Management & IP Services*

### VPN types

| | **Site-to-site** | **Client-to-site (remote access)** |
|---|---|---|
| Connects | **Two networks** that are physically separated | **A single device** to a VPN server |
| Endpoints | Gateway devices at each site | Client software on the user's device |
| Transparency | Users don't know it's there | User initiates the connection |
| Typical use | Branch office to head office | Remote worker to corporate network |

**Split tunnel vs full tunnel:**

| | **Full tunnel** | **Split tunnel** |
|---|---|---|
| Traffic through the VPN | **All of it** | Only corporate-bound traffic |
| Internet traffic | Routed via corporate, inspected | Goes direct |
| Security | **Higher** — everything is inspected | Lower — direct paths are uninspected |
| Performance / bandwidth cost | Worse — this is the **backhaul** problem from 1.8 | Better |

📌 The split vs full tunnel decision is exactly the tension SD-WAN and SASE were designed to resolve: you want the direct path *and* the policy enforcement.

### Connecting to network devices for configuration

| Method | Description | Security |
|---|---|---|
| **Console (serial)** | Direct physical cable to the device's console port | 📌 Requires **physical access**; works when the network is down |
| **Telnet** | Remote CLI over the network, port 23 | ❌ **Cleartext, including credentials.** Never use in production |
| **SSH** | Encrypted remote CLI, port 22 | ✅ **The standard** |
| **HTTP/HTTPS (web GUI)** | Browser-based management | Use HTTPS only |
| **API** | Programmatic access | Underpins automation and SDN |

### In-band vs out-of-band management

📌 This distinction is a reliable exam question.

| | **In-band** | **Out-of-band** |
|---|---|---|
| Path | Over the **production network** | Over a **separate, dedicated** path |
| Examples | SSH across the LAN, web GUI | Console cable, dedicated management port, cellular modem, terminal server |
| Cost | None additional | Additional infrastructure |
| ⚠️ **Critical weakness / strength** | **If the network is down, you can't manage the device that would fix it** | **Works even when the production network is completely down** |

📌 The whole justification for out-of-band is that catch-22: the device you need to reconfigure is unreachable precisely because it is misconfigured. Out-of-band management is what lets you fix a router remotely after you've accidentally shut down its uplink.

### Jump servers

A **jump server** (jump host, jump box) is an intermediary system that sits between a user and the sensitive systems they need to reach.

**How it works:** administrators connect to the jump server first, then from there to internal devices. Direct access from user workstations to sensitive systems is **blocked**.

📌 **Why it's valuable:**
- **Single hardened, monitored, audited chokepoint** for administrative access
- Reduces the attack surface — internal management interfaces are never directly exposed
- All administrative sessions can be **logged and recorded** in one place
- Enforces MFA and strong authentication at one controlled point

⚠️ **The corresponding risk:** the jump server becomes a **high-value target and a single point of failure**. Compromise it and you've compromised the path to everything behind it. It must be among the most hardened, most monitored systems you own.

### 🔧 LAB 3.5 — Remote Access and Management Paths *(call TORA)*
Configure a site-to-site VPN between head office and a branch, then add client-to-site remote access. Compare split and full tunnel behaviour by tracing where internet-bound traffic actually goes. Harden device access to SSH only with Telnet disabled, place a jump server as the sole administrative path, and prove out-of-band recovery by shutting down a router's management interface and restoring it over console.

---
# PART 4 — Network Security (Domain 4.0, 14%)

*Source: Day 15 — Network Security Concepts & Solutions; Day 15 — Physical Security & Network Hardening*

⚠️ **This is the domain with the thinnest transcript coverage relative to its exam weight.** The material below is complete for what the course covers, but supplement it — particularly on attack types and cryptographic concepts.

## 4.1 Security Concepts, Authentication, and Segmentation Enforcement

### The CIA triad

| Principle | Meaning | Protected by |
|---|---|---|
| **Confidentiality** | Only authorized parties can read the data | Encryption, access control |
| **Integrity** | Data hasn't been altered | Hashing, digital signatures, checksums |
| **Availability** | Authorized users can access it when needed | Redundancy, HA, DDoS mitigation, backups |

📌 Match a control to the leg it protects. Encryption protects confidentiality, **not** integrity — hashing does that.

### Risk vocabulary

📌 Precise definitions; the exam tests them as definitions.

| Term | Definition |
|---|---|
| **Risk** | The **possibility of an adverse event** occurring |
| **Threat** | The potential cause of an unwanted incident |
| **Vulnerability** | A **weakness** that a threat can exploit |
| **Exploit** | The method of taking advantage of a vulnerability |
| **Impact** | The consequence if it happens |

**Risk = Threat × Vulnerability × Impact.** A threat with no matching vulnerability presents no risk.

**Risk responses:**

| Response | Meaning |
|---|---|
| **Avoid** | Stop doing the risky activity |
| **Mitigate** | Reduce likelihood or impact with controls |
| **Transfer** | Shift it — insurance, or a third-party provider |
| **Accept** | Acknowledge and take no further action |

### Encryption

Encryption converts readable data into an unreadable form so only authorized parties can access it.

| | **Symmetric** | **Asymmetric** |
|---|---|---|
| Keys | **One shared key** for encrypt and decrypt | **Key pair** — public and private |
| Speed | **Fast** | Slow |
| Problem | **Key distribution** — how do you share the key securely? | Solves key distribution |
| Examples | **AES**, 3DES, **DES** (broken) | **RSA**, **ECC**, Diffie-Hellman |

📌 **How TLS actually uses both:** asymmetric cryptography is used to **exchange** a symmetric session key; the bulk data is then encrypted **symmetrically** because it's far faster. This hybrid model is worth understanding rather than memorizing — it explains why both types exist.

**Data states:**
- **At rest** — stored. Protected by full-disk or file-level encryption.
- **In transit** — moving. Protected by TLS, IPsec, VPN.
- **In use** — in memory. Hardest to protect.

**Hashing** is **one-way** — it produces a fixed-length digest that cannot be reversed. Used for **integrity verification** and password storage, not confidentiality. Examples: SHA-256, MD5 (⚠️ broken, collision-prone).

**PKI concepts:** a **certificate** binds a public key to an identity, signed by a **Certificate Authority**. **Self-signed** certificates provide encryption but not third-party-verified identity — which is why browsers warn about them.

### Honeypots and honeynets

📌 **A honeypot is a virtual trap intended to entice potential attackers.** It is a system **deliberately left compromised** — anything from a server to a router to a client computer.

**Why deploy one:**
- Understand attacker behavior and the techniques currently in use
- Aid investigation of security breaches
- Collect intelligence on intruder behavior
- 📌 **Use that intelligence to tune automated IDS/IPS and eliminate false positives** — this connects directly to the anomaly-based detection tuning discussed in 1.2

**Deployment types:**

| Type | Behavior |
|---|---|
| **Pure** | Full system; interaction is **recorded for later analysis** |
| **Low interaction** | Automatically records activity from **botnets and worms** — automated threats, no human interaction |
| **High interaction** | **Acts like a real production system.** Intent is for a human to actually compromise it so their actions can be monitored |

⚠️ **High-interaction honeypots require more maintenance and higher expertise**, because you must ensure the attacker doesn't use the honeypot as a pivot into the real network. A badly run honeypot is a liability, not an asset.

**A honeynet** is a network of honeypots — a more convincing environment.

### Compliance

Being compliant means **adhering to standards created by industry and following industry best practice**.

| Framework | Applies to |
|---|---|
| **PCI DSS** | Payment card data |
| **HIPAA** | Healthcare information (US) |
| **GDPR** | Personal data of EU residents |
| **SOX** | Financial reporting (US public companies) |

📌 Compliance is a **floor, not a ceiling** — meeting a standard is not the same as being secure. But failing one carries legal and financial penalties independent of whether a breach occurs.

⚠️ Connect this to multitenancy in 1.3: regulated data on shared cloud infrastructure raises compliance questions that private or hybrid deployment avoids.

### Network segmentation

**The process of isolating network devices from one another**, with each segment operating as its own network.

**Why:**
- **Contains breaches** — an attacker who compromises one segment cannot move laterally into others
- **Reduces broadcast traffic** and improves performance
- **Simplifies compliance scope** — isolate cardholder data and only that segment falls under PCI
- **Enforces least privilege** at the network level

**Methods:** VLANs (2.1), subnets and routing with ACLs, physical separation/air gap, **microsegmentation** (see 1.6), and DMZ/screened subnet (see 1.2).

📌 **Segmentation is the standard answer** for IoT (2.4), SCADA/ICS (2.4), guest networks (2.3), and east-west lateral movement (1.6). When a scenario involves untrusted or unpatchable devices needing network access, segment them.

### Network access control

**Port security.** Restricts **ingress traffic** on a switch port by limiting which **MAC addresses** may connect. The switch compares the MAC of each incoming frame against its allowed list; a mismatch triggers a **violation**.

📌 **Two violation triggers to know:**
1. **Maximum MAC count exceeded** — the port is configured to allow a limited number of addresses (learned dynamically or configured statically). If the limit is 20 and traffic from a 21st MAC arrives, violation.
2. ⚠️ **Move violation** — a MAC learned on one port appears on **another port in the same VLAN**. It looks like the system moved to a port it wasn't authorized for.

**Violation modes** (see 2.2): protect (discard silently), restrict (discard and log), **shutdown** (err-disable the port — the default).

**802.1X.** Port-based network access control requiring **authentication before the port is opened**.

| Component | Role |
|---|---|
| **Supplicant** | The client device requesting access |
| **Authenticator** | The switch or AP controlling the port |
| **Authentication server** | **RADIUS**, which makes the decision |

**EAP** is the framework carrying the authentication exchange (PEAP, EAP-TLS, EAP-TTLS).

📌 ⚠️ **802.1X is fundamentally stronger than MAC filtering or port security**, because it authenticates an **identity** rather than a **hardware address**. MAC addresses are trivially spoofed; credentials and certificates are not.

**MAC filtering.** Allow or deny based on MAC address. ⚠️ **Weak security** — MAC addresses are transmitted in cleartext in every frame and can be cloned in seconds. Treat it as an inventory convenience, not a control.

**RADIUS vs TACACS+:**

| | **RADIUS** | **TACACS+** |
|---|---|---|
| Standard | **Open** | **Cisco-proprietary** |
| Transport | UDP | **TCP** |
| Encryption | **Password only** | **Entire payload** |
| AAA | Combines authentication and authorization | **Separates** all three |
| Typical use | Network access, wireless, VPN | **Device administration** |

📌 **The discriminator: TACACS+ encrypts the whole payload and separates AAA functions**, which is why it's preferred for administrative access to network devices.

### Access control models

| Model | Basis |
|---|---|
| **RBAC (Role-Based)** | Permissions attached to **roles**; users inherit via role membership |
| **MAC (Mandatory)** | System-enforced labels and clearances; users cannot change permissions |
| **DAC (Discretionary)** | The data **owner** decides who gets access |
| **ABAC (Attribute-Based)** | Decisions from attributes — user, device, location, time |

📌 **Least privilege** and **separation of duties** are the governing principles, and they run through the zero trust discussion in 1.8.

### ACLs, URL filtering, and content filtering

**ACLs (Access Control Lists)** grant or deny traffic based on criteria — source/destination IP, protocol, port.

📌 **Two rules that decide most ACL questions:**
1. **Processed top to bottom; first match wins.** Order matters enormously — a permissive rule above a restrictive one makes the restrictive one dead code.
2. **Implicit deny at the end.** Anything not explicitly permitted is denied.

**URL filtering** — allow/deny by web address (see the proxy discussion in 1.2).
**Content filtering** — inspect and filter by content category or type, including scanning for malware and for sensitive data leaving the organization.

### 🔧 LAB 4.1 — Segmentation and Access Control *(call TORA)*
Build a flat network and segment it properly: separate VLANs for corporate, guest, IoT and management, with a Layer 3 device applying inter-VLAN ACLs. Add 802.1X with a RADIUS server so ports authenticate identities rather than MAC addresses. Break/fix: an ACL whose rule order silently permits traffic it was written to block, and a segment that reaches the management VLAN because of a missing implicit-deny assumption.

---
## 4.2 Common Network Attacks

*New section. The N10-009 objectives dedicate 4.2 entirely to attack types, and the Day-format transcripts covered them only in passing. Written to close that gap.*

⚠️ This objective is **pure recall under pressure**. The exam gives you a symptom or a scenario and asks which attack it is. Learn each one by its **distinguishing signature** — the detail that rules the others out.

### Denial of Service

**DoS** makes a resource unavailable to legitimate users by exhausting something finite: bandwidth, connection state, CPU, or memory.

| Variant | Mechanism |
|---|---|
| **DoS** | A single source overwhelms a target |
| **DDoS** | 📌 **Many** compromised hosts — a **botnet** — attack at once. Harder to block because there is no single source IP to filter |
| **Amplification / reflection** | Attacker sends small spoofed requests to third-party servers, which send **large** replies to the victim. DNS and NTP are classic amplifiers |
| **Friendly / unintentional DoS** | No attacker at all — a link saturated by a legitimate traffic spike, or a misconfiguration causing a loop |

📌 **The amplification insight worth understanding:** the attacker spoofs the *victim's* address as the source, so replies go to the victim. A small query producing a large answer means the attacker multiplies their own bandwidth many times over.

⚠️ **Friendly DoS is a real exam answer.** If a scenario describes an outage with no evidence of malice — a backup job saturating a WAN link, or a broadcast storm from a switching loop — the answer is unintentional, not an attack.

**Mitigation:** upstream filtering and scrubbing services, rate limiting, anycast distribution (see 1.7), and eliminating the loops that cause the friendly variety.

### VLAN hopping

Reaching a VLAN you were never assigned to. Two methods, and the exam distinguishes them:

| Method | How it works | Prevention |
|---|---|---|
| **Switch spoofing** | The attacker's device **pretends to be a switch** and negotiates a trunk, which then carries every VLAN | 📌 **Disable automatic trunk negotiation.** Set access ports explicitly to access mode |
| **Double tagging** | The frame is given **two 802.1Q tags**. The first switch strips the outer tag and forwards it; the second switch acts on the inner tag and delivers it into the target VLAN | 📌 **Change the native VLAN** to an unused one and never carry user traffic on it |

⚠️ 📌 **Double tagging exploits the native VLAN directly** — this is exactly why section 2.2 insists the native VLAN must match on both trunk ends and should be an unused VLAN. It is also **one-way**: the attacker can send into the target VLAN but receives nothing back.

### MAC flooding

The attacker floods a switch with frames carrying **thousands of bogus source MAC addresses**, filling the finite MAC address table.

📌 **What happens next is the whole point.** Once the table is full, the switch can no longer learn or store legitimate entries. Unable to look up a destination, it **floods frames out every port** — reverting to hub-like behaviour (see 2.4). The attacker now sees traffic intended for other hosts.

**This is an availability attack that becomes a confidentiality attack.** That progression is the exam's favourite thing about it.

**Mitigation:** **port security** with a MAC limit per port (see 4.1) — the control is a direct answer to this attack.

### ARP poisoning and ARP spoofing

ARP has **no authentication** (see 2.2). Any device can answer for any IP address.

**The attack:** the attacker sends unsolicited ARP replies claiming that the **default gateway's IP** belongs to the **attacker's MAC**. Victims update their ARP caches and begin sending all off-subnet traffic to the attacker, who forwards it on — becoming an **on-path attacker**.

📌 **Detection signature:** two different IP addresses resolving to the **same MAC**, or a gateway MAC that changes unexpectedly. `arp -a` shows it.

⚠️ **On-path attack** is the current term for what older material calls **man-in-the-middle**. Both may appear; they mean the same thing.

**Mitigation:** **Dynamic ARP Inspection (DAI)**, DHCP snooping, static ARP entries for critical hosts, and encryption so intercepted traffic is unreadable.

### DNS poisoning and spoofing

Corrupting name resolution so a legitimate name resolves to an attacker's address.

| Where it happens | Mechanism |
|---|---|
| **Local HOSTS file** | 📌 Modified on the host. Overrides DNS entirely — see 3.4 |
| **Resolver cache poisoning** | Forged responses injected into a caching server, affecting **everyone** who uses it |
| **Rogue DNS server** | Clients handed a malicious DNS server, often via a rogue DHCP server |

⚠️ **The signature symptom:** the address bar shows the correct name, but the site is wrong — or the certificate warning fires because the attacker cannot produce a valid certificate for that name. **That certificate warning is the user's last line of defence**, which is why training people to click through it is so damaging.

**Mitigation:** **DNSSEC**, restricting recursion, securing zone transfers (see 3.4), and HTTPS with proper certificate validation.

### Rogue services

Unauthorised services offering legitimate-looking functions on the network.

| Rogue service | Effect | Detection |
|---|---|---|
| **Rogue DHCP server** | Hands out wrong gateway and DNS, redirecting traffic through the attacker | 📌 Clients receive addressing from an unexpected server or an unexpected subnet |
| **Rogue access point** | An unauthorised AP on the corporate network. ⚠️ **Often an employee, not an attacker** (see 1.2) | Wireless scanning, WLC detection |
| **Evil twin** | An AP broadcasting a **legitimate SSID** to lure clients | Two identical SSIDs, unexpected signal strength |

**Mitigation for rogue DHCP: DHCP snooping**, which permits DHCP server responses only from trusted ports. 📌 That is the specific named control, and it is the expected answer.

### Social engineering

Manipulating **people** rather than technology. 📌 The exam treats this as its own attack category because no technical control fully prevents it.

| Attack | Definition |
|---|---|
| **Phishing** | Fraudulent messages at scale seeking credentials or action |
| **Spear phishing** | Phishing **targeted** at a specific person using researched detail |
| **Whaling** | Spear phishing aimed at **executives** |
| **Vishing** | Voice phishing, by phone |
| **Smishing** | Phishing by **SMS** |
| **Pretexting** | Inventing a scenario to establish false legitimacy |
| **Tailgating / piggybacking** | Following an authorised person through a controlled door (see 4.3) |
| **Shoulder surfing** | Observing credentials being entered |
| **Dumpster diving** | Recovering sensitive material from discarded waste |
| **Watering hole** | Compromising a site the target group is known to visit |

📌 **The principles attackers exploit:** authority, urgency, scarcity, familiarity, trust, and intimidation. If a scenario emphasises **time pressure** plus an **authority claim**, it is social engineering regardless of the delivery method.

**Mitigation:** user training, verification procedures for unusual requests, and MFA so a stolen password alone is insufficient.

### Malware

| Type | Distinguishing behaviour |
|---|---|
| **Virus** | Attaches to a file and requires **user action** to execute |
| **Worm** | 📌 **Self-replicating across the network with no user interaction** — which is why worms spread so fast |
| **Trojan** | Disguised as legitimate software |
| **Ransomware** | Encrypts data and demands payment |
| **Spyware / keylogger** | Covertly gathers information |
| **Rootkit** | Hides at a deep level, often kernel or firmware, to evade detection |
| **Botnet client** | Enrols the host into a network of remotely controlled machines |
| **Logic bomb** | Dormant until a trigger condition, such as a date or an event |
| **Fileless malware** | Runs in memory using legitimate system tools, leaving little on disk |

⚠️ 📌 **Virus versus worm is the single most tested malware distinction.** A virus needs a user to open something; a **worm needs nothing**. If a scenario describes rapid spread across a network with no user action, it is a worm.

📌 **Ransomware is where backups become a security control, not just an operations one.** The 3-2-1 rule and an **offline or immutable** copy are what defeat it — see 3.3. An attacker who can encrypt your backups has defeated the backup strategy entirely.

### Other attacks worth knowing

| Attack | Signature |
|---|---|
| **On-path (MITM)** | Attacker positioned between two parties, relaying and possibly altering traffic |
| **Deauthentication** | Forged 802.11 management frames disconnect wireless clients — often a precursor to an evil twin |
| **Brute force / password spraying** | Guessing credentials. Spraying tries **one common password across many accounts** to avoid lockout |
| **Credential stuffing** | Reusing credentials leaked from another breach |
| **DNS tunnelling** | Exfiltrating data inside DNS queries, which firewalls often permit unexamined |
| **Spoofing** | Forging a source address — IP, MAC, or email |
| **Insider threat** | Authorised access misused. ⚠️ Perimeter controls never see it — connects to east-west visibility in 1.6 |

### Attack → control quick reference

📌 **Learn this table in the control direction too.** The exam asks both "what attack is this?" and "which control prevents it?"

| Attack | Primary control |
|---|---|
| MAC flooding | **Port security** |
| ARP poisoning | **Dynamic ARP Inspection** |
| Rogue DHCP | **DHCP snooping** |
| VLAN hopping (spoofing) | **Disable trunk negotiation** |
| VLAN hopping (double tag) | **Unused native VLAN** |
| DNS poisoning | **DNSSEC** |
| Evil twin | **802.1X / WPA3, certificate validation** |
| Deauthentication | **802.11w management frame protection** |
| Social engineering | **Training and MFA** |
| Ransomware | **Offline, tested backups** |
| DDoS | **Upstream scrubbing, rate limiting** |

### 🔧 LAB 4.2 — Attack and Defence *(call TORA)*
Packet Tracer supports several of these directly. Build a network and demonstrate MAC flooding filling the CAM table and triggering flooding, then stop it with port security. Introduce a rogue DHCP server and watch clients take bad addressing, then defeat it with DHCP snooping. Create a VLAN hopping scenario via an unused native VLAN, and stage an evil twin alongside a legitimate SSID. Each stage is build it, break it, then defend it.

---
## 4.3 Device Security and Security Rules

### Physical security controls

| Control | Purpose |
|---|---|
| **Fencing / bollards** | Perimeter deterrence and vehicle barriers |
| **Locks** | Physical, electronic, biometric |
| **Access badges / key fobs / smart cards** | Controlled entry with an audit trail |
| **Mantrap / access control vestibule** | 📌 Two interlocking doors preventing **tailgating** — only one person passes at a time |
| **Security guards** | Judgment that automated systems lack |
| **Cameras / CCTV** | ⚠️ **Detective**, not preventative — records but doesn't stop |
| **Motion detection and sensors** | Detect presence in restricted areas |
| **Asset tags / RFID** | Track equipment movement |
| **Lighting and signage** | Deterrence |

📌 ⚠️ **Classify controls correctly — the exam asks:**
- **Deterrent** — discourages (signage, lighting, visible cameras)
- **Preventative** — stops (locks, mantraps, guards)
- **Detective** — identifies after the fact (cameras, logs, alarms)
- **Corrective** — restores (backups, DR sites)

**Tailgating / piggybacking** is the specific threat a mantrap addresses: an unauthorized person following an authorized one through a controlled door.

### Geofencing

**Defining geographical boundaries** monitored by **GPS satellites, RFID, cellular service, or Wi-Fi**, triggering an alert when a monitored device **enters or exits** the boundary. Boundaries are typically drawn in a **web interface overlaid on a map or satellite imagery**.

📌 **Where it's actually used.** As the transcript notes, "geo" implies geography, so this isn't usually how you harden an *internal* network — it's more often used to **harden the services you offer**. Examples: restricting an application so it only functions within a facility, or blocking authentication attempts originating from countries where you have no operations.

⚠️ **Virtual barriers** — a design consideration covering the **level of participation required** from the person or device being monitored. Some implementations require an app or agent; others work passively. That difference determines what you can actually enforce.

**Hardening** is reducing attack surface by removing or securing everything that isn't required.

### Default credentials

📌 **The first and most important step, always.** Devices ship with published default usernames and passwords that are freely searchable. Changing them is the single highest-value hardening action.

⚠️ **Establish a secure connection first.** Changing a password over **Telnet** transmits the new password in cleartext — you've just handed an eavesdropper the credential you were trying to protect. **Use SSH or console access.**

### Password strength

Passwords remain one of the weakest links.

| Factor | Guidance |
|---|---|
| **Length** | 📌 **The most important factor** — length beats complexity |
| **Complexity** | Mixed character types |
| **Uniqueness** | No reuse across systems |
| **Passphrases** | Long and memorable beats short and cryptic |
| **MFA** | ⚠️ **The strongest single improvement** — a stolen password alone becomes insufficient |
| **Password managers** | Enable unique, long credentials per system |
| **Account lockout** | Blunts brute force |

**MFA factors:** something you **know** (password), **have** (token, phone), **are** (biometric). 📌 True MFA requires factors from **different categories** — two passwords is not MFA.

### Disabling unused ports

📌 Applies to **both** meanings of "port":

- **Physical switch ports** — an enabled unused port in a lobby or conference room is an open door onto the network. Shut them down administratively, or place them in an unused VLAN (a "black hole" VLAN).
- **Logical service ports** — every open TCP/UDP port is a service listening, and every listening service is potential attack surface. Disable services you don't use.

⚠️ **The principle behind both: if it isn't needed, it shouldn't be running or reachable.**

### Firewall rules

**Components of a rule:** source, destination, service/port, action, direction, and logging.

**Actions:**

| Action | Behavior | Sender sees |
|---|---|---|
| **Allow / Permit** | Traffic passes | Success |
| **Deny / Drop** | **Silently discarded** | **Timeout** — no response |
| **Reject** | Discarded **with notification** | Immediate refusal (RST or ICMP unreachable) |
| **Log** | Records the match | — |

📌 ⚠️ **Drop vs reject is a real design decision, not trivia.** Dropping reveals nothing to a scanner and slows reconnaissance, but produces confusing timeouts for legitimate users. Rejecting gives fast, clear failures for legitimate traffic but confirms to an attacker that a host exists. External-facing rules typically drop; internal rules often reject.

**Rule ordering** follows the ACL rules above: **top-down, first match wins, implicit deny at the end.**

### Wireless hardening

Beyond WPA3/WPA2 and 802.1X (see 2.3):

- **Transmit power tuning** — 📌 reduce AP power so the signal doesn't extend past your walls into the parking lot. More power is not better; it extends your attack surface geographically.
- **Disable WPS** — ⚠️ the PIN mechanism is brute-forceable and should be off.
- **Change default SSID names** — defaults reveal the vendor and model, telling an attacker which vulnerabilities to try.
- **Guest network isolation** — client isolation so guests can't reach each other or internal resources.
- **Rogue AP detection** — see 1.2. Wireless scanning and WLC-based detection.
- **Disable unused radios and bands.**

### IoT security

⚠️ IoT concerns, restated from 2.4 in security terms: default credentials, infrequent or absent patching, weak or no built-in security, and long deployment lifetimes on unsupported firmware.

📌 **Controls:** segment onto a dedicated VLAN, restrict outbound as well as inbound traffic, change defaults, disable UPnP, monitor for anomalous behavior, and inventory ruthlessly — you cannot secure devices you don't know are connected.

### Remote access security

| Protocol | Port | Security |
|---|---|---|
| **SSH** | 22 | ✅ Encrypted. The standard for CLI |
| **RDP** | 3389 | Microsoft's GUI remote access. ⚠️ **Never expose directly to the internet** — put it behind a VPN or jump server |
| **VNC** | 5900 | Cross-platform GUI; ⚠️ often unencrypted by default |
| **Telnet** | 23 | ❌ Cleartext. Disable it |
| **VPN** | Varies | Encrypted tunnel (see 1.2, 3.1) |

📌 **RDP and VNC exposed to the internet are among the most reliably exploited entry points in real breaches.** The answer in any scenario is: **VPN first, or a jump server (see 3.5), then RDP internally.**

**Remote access authentication:** RADIUS, TACACS+, LDAP/Active Directory integration, SSO, and MFA.

### 🔧 LAB 4.3 — Device Hardening *(call TORA)*
Take a deliberately insecure Packet Tracer network — default credentials, Telnet enabled, no port security, flat VLAN, open guest wireless — and harden it systematically: SSH-only management, port security with all three violation modes, 802.1X with RADIUS, segmented IoT and guest VLANs, ACLs demonstrating first-match-wins and implicit deny, and a DMZ. Break/fix: an ACL with rules in the wrong order silently permitting blocked traffic, a port security move violation, and an over-powered AP leaking signal beyond the building.

---
# PART 5 — Network Troubleshooting and Tools (Domain 5.0, 24%)

**The heaviest domain on the exam.** It is applied rather than recall, which is why people underprepare for it. Work the scenarios.

## 5.1 The Troubleshooting Methodology

*Source: Day 16 — Troubleshooting Methodologies & Approaches*

📌 **Memorize the seven steps in order. The exam asks "what is the NEXT step" constantly, and the answer is always positional — it depends only on where in the sequence the scenario has stopped.**

| # | Step |
|---|---|
| **1** | **Identify the problem** |
| **2** | **Establish a theory of probable cause** |
| **3** | **Test the theory** to determine the cause |
| **4** | **Establish a plan of action** and identify potential effects |
| **5** | **Implement the solution** or escalate |
| **6** | **Verify full system functionality** and implement preventative measures |
| **7** | **Document findings, actions, and outcomes** |

⚠️ **The two most common exam mistakes:** jumping from step 2 straight to step 5 (implementing before testing), and forgetting that **documentation is a required step**, not optional cleanup.

### Step 1 — Identify the problem

**The opening questions:**
- Did the device **ever** work, or has it never worked since it came out of the box?
- If it worked, **when did it last work**?
- **Has anything changed** between then and now?

📌 You must **fully understand the problem before applying any solution.** "No internet access" is a report, not a problem — in a large environment there could be many reasons for it.

**Gathering information:**
- **Use tools.** `ipconfig` may reveal the user has no valid IP. `ping` verifies whether the gateway or DNS server is reachable.
- **Determine scope.** Question other users — is this one person or many? ⚠️ **Scope is the single most valuable early data point**, because it immediately eliminates entire categories of cause.
- **Assess device state on arrival.** Is the device otherwise functioning? Are applications frozen? Is there visible physical damage to the system or its adapter?
- **Establish the prior state.** Did it work earlier today and stop recently, or has there been no access since power-on?

**Duplicate the problem, and document the attempt.** If the affected user is on wireless, connect your own device to the same wireless network and see whether you also lose access. **Document the result either way** — knowing which actions succeeded matters as much as knowing which failed. This phase often surfaces additional issues.

⚠️ **Question users carefully.** Users may lack technical vocabulary and may not know how to describe what happened. **Assess on your own first, then talk to them** to build an accurate picture — what behaviors they observed, which applications were in use, and whether the application is new to them (which might reveal the "problem" is simply not knowing how to use a feature).

**Identify specific symptoms.** What was actually happening when the issue arose? What effects is it having on the device and on the network?

**Determine whether anything changed.** New hardware or software? Updates applied? 📌 **Does the timing line up?** If an update ran overnight and every user who received it has problems the next morning, the update is very likely the cause.

**Approach each problem individually.** Isolate and address one at a time. ⚠️ **Do not jump to conclusions or start from the biggest picture.** Stay focused on the specific problem, then expand scope only as necessary. If two users have no internet, don't conclude that all internet has failed organization-wide — determine the next step instead.

### Step 2 — Establish a theory of probable cause

📌 **The tire analogy is the best framing in the whole course.** Low tire pressure: you can add air, and the problem appears solved. But if the root cause is a **nail in the tire**, adding air treats only the symptom. The permanent fix is removing the nail and patching or replacing the tire.

⚠️ **If you don't reach the root cause, the symptoms will reappear.** You may even stumble onto a resolution accidentally — but those are temporary fixes.

**The method:** list **all** potential causes, then **prioritize by likelihood**. This lets you eliminate possibilities while focusing on the probable cause, which often presents the easiest solution.

📌 **The prioritization example is worth internalizing.** Internet access is lost. It could be a failed DNS server or a failed default gateway. But **most clients are configured with two DNS servers and one default gateway** — so it is far more likely that a **single gateway failed** than that **both** DNS servers failed simultaneously. Probability, not just possibility.

**Start with the obvious:**
- Is there **power** to all components?
- Was a **change** implemented by a user, an administrator, or an automated update?
- **Has anyone tried rebooting?**

⚠️ "The easiest solution is often the right one, but that is by no means a rule." Simple questions are a **starting point**, not the whole method.

**Top-down vs bottom-up (OSI layers):**

| Approach | Use when | Example |
|---|---|---|
| **Top-down** | The device clearly has network connectivity | 📌 Can reach files, printers, and internal resources but not the internet → **not a cable problem**. Start at the top with DNS |
| **Bottom-up** | The device has no connectivity at all | A single user can't get on the network at all → start with the **NIC and Ethernet cable** |
| **Divide and conquer** | The cause could be anywhere | Start in the middle (Layer 3/4) and work outward in whichever direction the evidence points |

📌 **The diagnostic that decides it:** if you can reach an internet site **by IP address** but not **by name**, that is almost certainly **DNS** — and DNS lives at the top of the stack. Top-down resolves it fastest.

**Categorize causes** as unlikely / likely / most likely, and pursue the most likely first. In the example above, "connects to the network but not the internet" **eliminates the physical layer entirely**, while a **failed default gateway at Layer 3** becomes a strong candidate.

**Divide and conquer as a team.** Assign specific candidate causes to specific people or teams so theories can be investigated and tested in parallel, then coordinate findings.

### Step 3 — Test the theory

**A theory must be validated.** If you believe a faulty cable is the cause, the theory is: replace the cable and the issue resolves.

⚠️ 📌 **Do not install a new cable and walk away assuming it worked. Test connectivity before moving on.** If the user still can't connect, your theory was **just disproved** — which is useful information, not a failure.

**When a theory is disproved:** formulate a new one and test it. ⚠️ **Do not formulate theory after theory without testing any of them.** Test each in sequence, because what you learn from each test narrows which remaining theories are plausible.

**Continue until you run out of testable theories.** 📌 Note carefully what that means: **it usually reflects the limits of your job responsibilities, not the limits of your knowledge or skill.**

**Support tiers.** Tier 1, 2, 3 placement depends on experience, training, and certifications. A new hire with fundamental training will start at the lowest tier and move up. When you hit the limit of what your tier is permitted to do and the issue remains, **escalate**.

*Example continuing the cable scenario:* if the new cable didn't help, maybe the switch is down — which would mean multiple users affected, so that's a testable theory. But a low-tier responder may not have access to the networking equipment, so the issue must be escalated to a tier that does.

📌 **Even when you can't resolve it, the step-by-step approach has value:** you've eliminated theories through the tests you *were* able to run, so **the escalation target doesn't start from scratch.**

### Step 4 — Establish a plan of action and identify potential effects

Once you've zeroed in on the problem, a solution must be implemented — but **success isn't guaranteed**, so the plan should outline what to do **if the solution fails**.

📌 **The switch replacement example is exactly the kind of thinking the exam rewards.** A faulty switch seems simple: replace it. But you **cannot assume** that users plugged into the failed switch can simply be reconnected to a different switch — that could place them **in a different VLAN**, severely impacting their ability to work by losing connectivity to required services, resource access, and security or management policies.

**Plan considerations:**
- What if the replacement isn't on hand?
- If you relocate users as a short-term fix, do those switches need **VLAN reconfiguration** so users reach the resources they need **without violating security policy**?
- **Write out a step-by-step plan** for complex solutions so each step's repercussions can be considered individually.
- What is the user impact of each option — **disconnected for a period** vs **connected but to the wrong network**?

⚠️ **The trade-off between "down" and "up but wrong" is a real decision, and often "down" is the safer choice.** A user on the wrong VLAN may be a security violation.

**If the solution fails:** return to the plan, consider other options — and evaluate *their* side effects too, which will differ from the original plan's. You may repeat this several times, retracing steps to find what was missed.

### Step 5 — Implement the solution or escalate

⚠️ **Verify you have the authority.** You might have correctly identified the problem, the solution, and the effects — and still **lack the permission or ability** to implement it. Authority and skillset are separate questions, and either one can force escalation.

**When escalating, include everything:**
- All facts and documentation from your investigation **and your teammates'**
- **Every step already completed**, so the receiving party knows where to start
- Which theories were already **disproved**

📌 **This is the point of documentation during troubleshooting** — so nobody redoes completed work.

**Escalation procedure:** 📌 **begin with the closest help.** Talk to colleagues, notify your immediate supervisor. ⚠️ **Do not go straight to the top.** Organizations with advanced structures have a chain of command specifically so every issue is handled efficiently and everyone knows what everyone else has done.

⚠️ Note the reality check: **even a highly skilled person new to an environment is unlikely to be given authority to correct every problem**, simply because they lack experience with *that* environment. And in a small organization you may **be** the entire hierarchy, in which case escalation isn't an option at all.

**Acting beyond your authorization level can have consequences.** Stay within your tier.

### Step 6 — Verify full system functionality and implement preventative measures

**Verify the issue is actually resolved** — and also that **no new issues have arisen from your troubleshooting**, particularly if you applied a temporary fix.

**Preventative measures** depend on what the problem was:

| Problem type | Prevention |
|---|---|
| Virus found, no antivirus installed | Install AV, **schedule definition updates and regular scans** |
| User error or unfamiliarity | **Additional user training** |
| Hardware failure | ⚠️ Often **cannot be prevented** — only responded to. Mitigate with **redundancy** |
| User misconfiguration | **Policies restricting device and application configuration changes** |

📌 **Fault tolerance as prevention.** Servers can carry redundant components — **RAID** lets a server keep functioning through a drive failure with minimal downtime and no data loss depending on configuration. The approach extends across the environment.

⚠️ **The redundancy trade-off, stated honestly:** more redundancy means **higher cost, more administrative overhead, and greater complexity**. It buys reliability, and you pay for it.

📌 **Restrictive policies as prevention.** Administrators can enforce that anti-malware is installed, scanning, and updating — **and cannot be disabled or uninstalled by the user.** Removing access to the settings that cause problems prevents the problems from occurring at all.

**No environment is 100% problem-free**, but proactive measures mean fewer issues and less disruption.

### Step 7 — Document findings, actions, and outcomes

**Update existing documentation** if the problem has been seen before; **start new documentation** if it hasn't.

📌 **You are building a knowledge base.** Next time the problem occurs, a technician consults what was done previously and goes straight to the solution instead of repeating the entire process.

⚠️ **Caveat worth knowing:** the same type of problem can occur under **different circumstances**, so the same fix isn't guaranteed to work. But usually, if problem A was corrected by solution A, expect a successful resolution.

**What the documentation must record:**

| Field | Why |
|---|---|
| **Detailed description of the initial problem** | The starting point |
| **Date and time the report was received** | Correlation with changes and logs |
| **Who reported it** | Follow-up |
| **Scope** — one user or widespread | Immediately orients the next responder |
| **Which technician responded** | So they can be contacted later |
| **Whether it was escalated** | Chain of custody |
| **Symptoms reported** | Pattern matching |
| **Corrective actions taken and the outcome of each** | 📌 **Including the ones that did not work** |

📌 ⚠️ **Recording failed actions is the detail people skip and the exam rewards.** A future technician seeing which actions were unsuccessful doesn't waste time repeating them. That is half the value of the knowledge base.

**Where to record it:** dedicated software, a database, or an internal site in robust environments; **at minimum a journal** in less formal ones. The method matters less than the thoroughness.

### 🔧 LAB 5.1 — Methodology Drill *(call TORA)*
A set of Packet Tracer scenarios, each with a single planted fault and no hints, worked strictly through all seven steps with written documentation for each. Includes at least one scenario where the first theory is wrong and must be discarded, and one requiring simulated escalation.

---
## 5.2 Cable, Interface, and Hardware Issues

*Source: Day 12 — Troubleshooting Network Issues*

### Wired connectivity issues

**Crosstalk.** 📌 **The signal on one wire being picked up by another wire**, causing interference.

⚠️ **The definition is more specific than most people assume.** Crosstalk refers to **the individual wires inside a single cable** — not two separate Ethernet cables run next to each other or tie-wrapped together. An Ethernet cable has eight internal wires twisted into four pairs; crosstalk is signal jumping between *those*.

**Causes:**
- Protective coating worn away, **often very close to the connector**
- **Too much copper exposed during crimping** — a workmanship defect
- Wires run very close together or tied together, then damaged
- **An animal gnawing away the protective coating**
- **A strong heat source melting it**

**Symptoms:** intermittent connectivity, a **high rate of collisions**, **malformed packets**, or complete loss of connectivity.

⚠️ **This condition is not always easy to spot** visually — the damage may be inside the jacket or under the connector boot. A cable **certifier** (see 5.5) will catch what the eye won't.

**Duplex mismatch.** See 2.1 for the mechanism. Symptoms: the link is **up** but throughput is terrible, with **late collisions, CRC/FCS errors, and runts** climbing on the interface. Almost all modern communication is full duplex, so a half-duplex end is usually a misconfiguration.

**Other wired issues:**

| Issue | Symptom | Cause |
|---|---|---|
| **Attenuation** | Signal degrades over distance | Run exceeds the **90 m** horizontal limit (see 2.4) |
| **EMI** | Intermittent errors | Cable near power sources, UPS batteries, motors (see 1.5) |
| **Bad connector / crimp** | No link or intermittent link | Poor termination |
| **Wrong cable type** | No link between two like devices | Straight-through where crossover is needed (see 1.5) |
| **Damaged cable** | Errors, no link | Physical damage; locate with **TDR** |
| **Port disabled** | No link, no light | Administratively shut down, or **err-disabled** by port security (see 4.1) |

### Hardware failure and unresponsive services

| Symptom | Investigate |
|---|---|
| Device completely unresponsive | Power, PSU, **PoE budget** (2.1) |
| Intermittent reboots | Power quality, overheating (see 2.4 and MTBF factors in 3.3) |
| Interface flapping | Failing NIC or transceiver, marginal cable |
| Service down but device up | The service process itself — check logs (3.2) |
| Gradual degradation | Resource exhaustion — CPU, memory, buffers |
| Multiple simultaneous failures | ⚠️ Look for a **common upstream cause** — power, cooling, or a shared uplink — rather than treating each as separate |

📌 **When several things fail at once, resist the urge to troubleshoot them individually.** Step 1 of the methodology tells you to determine **scope** first; a widespread simultaneous failure almost always has one shared cause.

### 🔧 LAB 5.2 — Physical Layer Fault Isolation *(call TORA)*
Plant a series of physical-layer faults in one topology: a damaged run producing CRC errors, a duplex mismatch generating late collisions, an administratively shut port, an err-disabled port from a port security violation, and a run exceeding the 90 m limit. Diagnose each from interface counters alone, without inspecting the configuration.

---
## 5.3 Switching, Routing, and IP Issues

*Source: Day 12 — Troubleshooting Network Issues*

### Duplicate addresses

**Duplicate IP address** — the same IP assigned to two or more interfaces in the same network. Result: **one or both devices may have their interfaces disabled**, or at minimum both encounter connectivity issues.

📌 **The cause is almost always manual configuration error.** Someone didn't realize an address was already in use.

⚠️ **Two specific scenarios the transcript calls out — both are exam-realistic:**

1. **Static onto static.** In an environment where most systems use DHCP and only a few are static, someone assigns a static address that's already taken. Often just a **typo**.
2. **DHCP scope overlapping a static address.** 📌 You configure a scope of **192.168.1.100 – 192.168.1.200**, not realizing **192.168.1.150 was statically assigned** to another system. **The scope must exclude any statically assigned values.** (See exclusions in 3.4.)

**Duplicate MAC address** — rare from manufacturing (see 1.1), so it usually indicates **MAC spoofing** or a misconfigured virtual machine. Symptoms: erratic switching behavior, traffic reaching the wrong host, port security **move violations** (see 4.1).

**Detection:** `arp -a` showing one MAC for two IPs or one IP flipping between MACs; OS duplicate-address-detected warnings; switch logs.

### DHCP issues

| Symptom | Likely cause |
|---|---|
| **169.254.x.x (APIPA)** | DHCP server unreachable — see the full breakdown in 1.7 and 3.1 |
| APIPA on **one subnet only** | 📌 **Missing IP helper / relay agent** on that subnet's router |
| Some clients get addresses, others don't | **Scope exhaustion** |
| Address conflicts | Static addresses inside the scope with **no exclusion** |
| Client on the wrong subnet | VLAN or relay misconfiguration |
| Address obtained but no connectivity | Scope handing out a wrong **gateway** or **DNS** server |

**Lease time issues.** 📌 A **lease** is how long a client may keep an address.

⚠️ **Lease length is a genuine trade-off:**
- **Too short** → excessive renewal traffic and DHCP server load, and clients may lose addressing during a brief server outage.
- **Too long** → 📌 **addresses stay reserved for devices that have left**, exhausting the pool. This is the specific failure in high-turnover environments — guest wireless, conference rooms, hot-desking — where a 7-day lease on a network that sees hundreds of transient devices will run the scope dry.

**Fixes:** shorten leases in transient environments, lengthen them in stable ones, and reconcile the scope.

### DNS issues

📌 **The signature test: `ping 8.8.8.8` works, `ping google.com` fails.** Layers 1–3 are proven good; the failure is name resolution.

| Symptom | Cause |
|---|---|
| Name resolution fails entirely | Wrong or unreachable DNS server configured |
| One machine resolves wrong, others fine | ⚠️ **Modified HOSTS file** (see 3.4) — a classic malware technique |
| Stale results after a change | Cached record — `ipconfig /flushdns` |
| Internal names fail, external work | Internal DNS server or split-brain misconfiguration |
| Intermittent resolution | One of two configured DNS servers has failed |

**Tools:** `nslookup` and `dig` to query a specific server directly and see which one answered.

### Open and blocked ports

| Symptom | Diagnosis |
|---|---|
| **Connection times out** | 📌 Traffic **silently dropped** — usually a firewall (see the drop vs reject discussion in 4.3) |
| **Connection refused / immediate RST** | Port **closed** — nothing is listening, or the firewall is set to **reject** |
| Works internally, fails externally | Firewall or ACL between the segments |
| Works for some users only | ACL scoped by source, or a rule-order problem (see 4.1) |

📌 **Timeout vs refused is real diagnostic information, not noise.** A timeout suggests something is silently discarding traffic in the path. An immediate refusal means the packet reached a host that actively said no. They point at different places.

**Verification:** port scan (5.2) to see what's actually listening, `netstat` on the host, and firewall/ACL review remembering **first match wins and implicit deny**.

### 🔧 LAB 5.3 — Addressing and Path Faults *(call TORA)*
Break addressing and routing in sequence: a DHCP scope overlapping a static address, a missing IP helper causing APIPA on one VLAN, a stale static route overriding OSPF, a native VLAN mismatch leaking traffic between VLANs, and an ACL blocking a port the application needs. Work each one through the seven-step methodology with written documentation.

---
## 5.4 Performance and Wireless Issues

*Source: Day 12 — Troubleshooting Network Issues*


### Performance issues

Performance complaints are the hardest troubleshooting calls because nothing is *broken*. The link is up, the service responds, and the user is still right that it is bad.

📌 **Separate the four measures before doing anything else.** They have different causes and different fixes, and conflating them is why these calls drag on.

| Measure | What it is | Feels like | Usual cause |
|---|---|---|---|
| **Bandwidth** | Capacity of the link | Large transfers crawl | Saturation, undersized link, a top talker |
| **Throughput** | What you actually achieve | Slower than the link should allow | Duplex mismatch, retransmissions, MTU problems, device CPU |
| **Latency** | Delay in transit | Everything feels sluggish | Distance, hop count, queuing, backhaul (see 1.8) |
| **Jitter** | **Variation** in latency | Choppy voice and video | Congestion, inconsistent queuing, no QoS |

⚠️ **A link can have plenty of bandwidth and still deliver terrible throughput.** That gap is the diagnosis, not a contradiction — check duplex, errors, and MTU before assuming you need a bigger link.

📌 **Jitter is the one people miss.** Average latency can look excellent while calls are unusable, because voice cares about *consistency* of arrival, not average speed. If a scenario reports good ping times and bad call quality, the answer is jitter.

**Working a performance complaint:**

1. **Compare against the baseline** (see 3.2). Without one, "slow" is unfalsifiable
2. **Determine scope** — one user, one segment, or everyone. This eliminates most causes immediately
3. **Check interface counters** for errors and discards before looking anywhere else
4. **Check utilisation** on the path, and use **NetFlow** to find *what* is consuming it (see 3.2)
5. **Check device resources** — a switch or router at high CPU degrades everything passing through it
6. **Check for a duplex mismatch** on any link in the path

**Common causes and their fixes:**

| Cause | Fix |
|---|---|
| Link saturation | More capacity, or **QoS** to protect what matters (see 1.2) |
| **Bottleneck** at one hop | Identify with hop-by-hop testing; upgrade that segment |
| Duplex mismatch | Match settings both ends (see 2.2) |
| Device resource exhaustion | Reduce load or replace the device |
| **Backhaul / inefficient path** | Direct routing to the resource (see 1.8) |
| Missing QoS | Mark and prioritise delay-intolerant traffic |
| Oversubscription | Rebalance load, add uplinks, aggregate links (see 2.1) |

⚠️ **Resist replacing hardware first.** It is the expensive guess, and duplex mismatches and missing QoS are far more common than undersized equipment.


### Wireless issues

**Speed and distance limitations.** 📌 Governed by the frequency trade-off in 2.3 — higher frequency means more throughput but less range and worse wall penetration.

| Issue | Symptom | Fix |
|---|---|---|
| **Distance / weak signal** | Low RSSI, slow speeds, drops at the edge | Reposition or add APs; consider **directional antennas** (2.3) |
| **Channel overlap** | Slow despite strong signal | 📌 Enforce **1/6/11** on 2.4 GHz (2.3) |
| **Interference** | Intermittent, worse at certain times | Microwaves, Bluetooth, cordless phones; **spectrum analyzer** to identify |
| **Incorrect antenna type or placement** | Coverage doesn't match the space | Match antenna pattern to the area (2.3) |
| **AP power too high** | Coverage bleeds outside the building; clients cling to a distant AP instead of roaming | Reduce transmit power (4.4) |
| **AP power too low** | Dead zones | Increase power or add APs |
| **Client capability mismatch** | One old device slows the whole network | Segregate legacy clients (2.3) |
| **Wrong security type or passphrase** | Client can't associate | Verify WPA2/WPA3 settings (2.3) |
| **Roaming problems** | Drops when moving between APs | Overlapping coverage and consistent SSID/security config |

📌 **The distinction that resolves most wireless complaints:** a **strong signal is not the same as good throughput.** A client can show full bars and still perform badly because of channel congestion, interference, or retransmissions. That's the passive-vs-active site survey point from 3.1 and the RSSI-vs-SNR point from 2.3, arriving as a real symptom.

### Certificate issues

**SSL/TLS** protects information in transit with encrypted communications — most visibly between web servers and browsers for banking and shopping, but also used internally to secure a corporate network.

📌 **Certificate problems the transcript names:**

| Problem | Detail |
|---|---|
| **Name mismatch (SNI)** | 📌 **Server Name Indication** mismatch — the server was renamed and now **the server's name and the name on its certificate don't match. This invalidates the certificate entirely** |
| **Deleted certificate** | Mistakenly removed |
| **Renewal failure** | Problem contacting the **issuing trusted root CA** when attempting to renew |
| **Expired certificate** | Validity period lapsed |
| **Wrong certificate type** | The wrong kind installed on a client device |
| **Failed installation** | Problem during install |

⚠️ **Add to that list:** an **untrusted root CA** (self-signed or an internal CA not in the client's trust store) and **incorrect system time**, which makes a valid certificate appear expired or not-yet-valid — which is exactly why **NTP matters** (see 3.4).

**Tools:** **SSL Labs** for checking publicly accessible web servers; browser certificate inspection; `openssl s_client` for direct examination.

### 🔧 LAB 5.4 — Performance and Wireless Degradation *(call TORA)*
Build a wireless network with overlapping channels and measure the throughput cost, then fix the channel plan and measure again. Saturate a link and observe the effect on a VoIP call with and without QoS marking. Break/fix: an AP at excessive transmit power causing clients to cling instead of roam, a legacy client dragging down a modern network, and a certificate name mismatch after a server rename.

---
## 5.5 Software, Command Line, and Hardware Tools

*Source: Day 12 — Troubleshooting Network Issues*

### Command-line tools

📌 This is the highest-yield table in Domain 5. Learn **what each tool proves**, not just what it does.

| Command | Purpose | Proves |
|---|---|---|
| **`ping`** | Tests reachability using **ICMP** | Layer 3 connectivity between two hosts |
| **`ping 127.0.0.1`** | Pings the **loopback** | 📌 **TCP/IP is correctly installed and bound to the adapter** |
| **`ipconfig`** (Win) / **`ifconfig`**, **`ip`** (Linux) | Displays IP configuration | Whether the host has a valid address, mask, gateway, DNS |
| **`tracert`** (Win) / **`traceroute`** (Linux) | Maps the path hop by hop using **TTL expiry** | **Where** along the path traffic stops |
| **`nslookup`** / **`dig`** | Queries DNS directly | Whether name resolution works and which server answered |
| **`netstat`** | Shows active connections and listening ports | What the host is actually talking to |
| **`arp -a`** | Displays the ARP cache | IP↔MAC mappings; detects duplicates and spoofing |
| **`route print`** / **`ip route`** | Displays the routing table | Whether the host knows where to send traffic |
| **`nmap`** | Port scanning and host discovery | Which ports are open on which hosts |
| **`tcpdump`** | CLI packet capture | The actual traffic on the wire |
| **`hostname`** | The system's name | Identity in a script or remote session |

### Ping, in the depth the exam expects

**Ping** stands for **Packet Internet Groper** and uses **ICMP** as its transport. It answers: can my system see yours, and can yours see me?

📌 **The loopback address 127.0.0.1 is the same on every Windows system.** It is reserved and effectively bound to every adapter. **If you have connectivity issues, ping it first** — successful replies rule out your own adapter as the cause. `ping localhost` resolves to the same address by default.

📌 **The outward-expansion sequence — this is the diagnostic pattern to internalize:**

| Step | Target | If it fails |
|---|---|---|
| 1 | **127.0.0.1** (loopback) | TCP/IP stack or adapter problem |
| 2 | **Own IP address** | Local NIC configuration |
| 3 | **Default gateway** | Local segment — cable, switch, VLAN, or gateway itself |
| 4 | **Host on another subnet** | Routing |
| 5 | **Public IP (e.g. 8.8.8.8)** | Internet path or edge device |
| 6 | **Public name (e.g. google.com)** | 📌 **DNS** — everything below this layer already works |

⚠️ **Internet pings often fail harmlessly.** Many internet routers **discard ICMP** to avoid being pinged constantly. A failed ping to an external host is not proof of a problem. And once you're out on the internet, there isn't much more you can troubleshoot anyway — ping's real value is measuring connectivity **within** your organization.

### Packet sniffers / protocol analyzers

**Intercept and log network traffic** for analysis. Wireshark is the reference implementation (see the OSI decode walkthrough in 1.1).

**Uses:** diagnosing protocol-level failures, seeing whether a request was ever sent or answered, identifying malformed traffic, spotting broadcast storms, and confirming which layer a failure actually occurs at.

⚠️ **Capturing traffic may require legal authorization and a policy basis.** It can expose credentials and personal data. Capture with permission and a defined purpose.

📌 Modern switched networks deliver frames only to the destination port, so a sniffer sees only its own traffic and broadcasts unless you configure **port mirroring / SPAN** or use a network TAP.

### Port scanners

**Identify which ports are open or listening.**

**Legitimate uses:** verifying that hardening actually closed what you meant to close, discovering unauthorized services, auditing before and after change. ⚠️ **Scanning networks you don't own or lack authorization to test is unlawful in many jurisdictions.**

📌 A port scan is also the fastest way to answer "is the service even listening?" before you go looking for a firewall rule.

### Wi-Fi analyzers

Software on a laptop, phone, or tablet that surveys the RF environment.

**Reveals:** nearby SSIDs and their channels, **signal strength (RSSI)**, **channel overlap and congestion**, interference sources, and coverage dead zones.

📌 This is the practical instrument behind the site survey concepts in 3.1 and the channel planning in 2.3. If a scenario involves slow or unstable wireless in a specific area, a Wi-Fi analyzer is the tool.

### Hardware tools

| Tool | Purpose |
|---|---|
| **Cable tester** | Continuity and correct pinout — is the cable wired properly end to end |
| **Cable certifier** | Tests to a performance standard (Cat 6 at rated speed), not just continuity |
| **Toner and probe (fox and hound)** | Trace and identify a specific cable in a bundle or at a patch panel |
| **Loopback plug** | Tests a port by looping transmit to receive |
| **TDR / OTDR** | **Time Domain Reflectometer** (copper) / **Optical** TDR (fiber) — 📌 locates a break **and reports the distance to it** |
| **Light meter / optical power meter** | Measures optical signal strength on fiber |
| **Multimeter** | Voltage, continuity, resistance |
| **Punchdown tool** | Terminates wires onto a patch panel or block (see 1.5) |
| **Crimper** | Attaches connectors to bulk cable (see 1.5) |
| **Spectrum analyzer** | Identifies RF interference including non-Wi-Fi sources |

📌 ⚠️ **Cable tester vs certifier is a distinction the exam makes.** A tester says "the wires connect correctly." A **certifier** says "this run meets Cat 6 specification at its rated speed over its length." A cable can pass a tester and still fail to carry gigabit reliably.

📌 **TDR reports distance to fault**, which is what makes it valuable — you don't replace the run, you go to the spot.

### 🔧 LAB 5.5 — Tool Selection Drill *(call TORA)*
A scenario set where the task is not to fix the fault but to **name the correct tool and justify it** — then use it in Packet Tracer where supported. Includes cases designed to distinguish tester vs certifier, ping vs traceroute, and sniffer vs port scanner.

---
# APPENDICES

## Appendix A — Port and Protocol Drill Sheet

Cover the right column. Work down. Then cover the left and work up. **Both directions.**

| Port | Protocol | TCP/UDP |
|---|---|---|
| 20 | FTP data | TCP |
| 21 | FTP control | TCP |
| 22 | SSH / SFTP / SCP | TCP |
| 23 | Telnet | TCP |
| 25 | SMTP | TCP |
| 53 | DNS | TCP + UDP |
| 67 | DHCP server | UDP |
| 68 | DHCP client | UDP |
| 69 | TFTP | UDP |
| 80 | HTTP | TCP |
| 110 | POP3 | TCP |
| 123 | NTP | UDP |
| 143 | IMAP | TCP |
| 161 | SNMP query | UDP |
| 162 | SNMP trap | UDP |
| 389 | LDAP | TCP |
| 443 | HTTPS | TCP |
| 445 | SMB | TCP |
| 514 | Syslog | UDP |
| 587 | SMTP submission | TCP |
| 636 | LDAPS | TCP |
| 989/990 | FTPS | TCP |
| 993 | IMAPS | TCP |
| 995 | POP3S | TCP |
| 1433 | MS SQL | TCP |
| 3306 | MySQL | TCP |
| 3389 | RDP | TCP |
| 5060/5061 | SIP | TCP/UDP |

**Secure/insecure pairs — recite these as pairs:**
80→443 · 21→22 (SFTP) · 23→22 · 25→587 · 110→995 · 143→993 · 389→636

---

## Appendix B — Subnetting Drill Sheet

### The three tables to know cold

**Mask octet values:** 0 · 128 · 192 · 224 · 240 · 248 · 252 · 254 · 255

**Powers of two:** 1 · 2 · 4 · 8 · 16 · 32 · 64 · 128 · 256 · 512 · 1024 · 2048 · 4096

**CIDR → usable hosts:**

| /24 | /25 | /26 | /27 | /28 | /29 | /30 |
|---|---|---|---|---|---|---|
| 254 | 126 | 62 | 30 | 14 | 6 | **2** |

### The magic number method

1. Find the interesting octet (mask is neither 255 nor 0)
2. **Magic number = 256 − mask value**
3. Subnets start at multiples of the magic number
4. Network = the multiple at or below the host address
5. Broadcast = next network − 1
6. Usable = network+1 to broadcast−1

### Practice set — work these until each takes under 30 seconds

| # | Given | Find network, broadcast, first, last, host count |
|---|---|---|
| 1 | 192.168.1.77/26 | |
| 2 | 10.0.5.130/25 | |
| 3 | 172.16.40.200/27 | |
| 4 | 192.168.10.35/28 | |
| 5 | 10.1.1.9/30 | |
| 6 | 172.20.130.55/20 | |
| 7 | 192.168.100.190/29 | |
| 8 | 10.10.10.10/22 | |

**Answers:**

| # | Network | Broadcast | Usable range | Hosts |
|---|---|---|---|---|
| 1 | 192.168.1.64 | 192.168.1.127 | .65 – .126 | 62 |
| 2 | 10.0.5.128 | 10.0.5.255 | .129 – .254 | 126 |
| 3 | 172.16.40.192 | 172.16.40.223 | .193 – .222 | 30 |
| 4 | 192.168.10.32 | 192.168.10.47 | .33 – .46 | 14 |
| 5 | 10.1.1.8 | 10.1.1.11 | .9 – .10 | 2 |
| 6 | 172.20.128.0 | 172.20.143.255 | 172.20.128.1 – 172.20.143.254 | 4094 |
| 7 | 192.168.100.184 | 192.168.100.191 | .185 – .190 | 6 |
| 8 | 10.10.8.0 | 10.10.11.255 | 10.10.8.1 – 10.10.11.254 | 1022 |

### VLSM practice

Given **192.168.50.0/24**, allocate for: 100 hosts, 50 hosts, 20 hosts, 10 hosts, and two point-to-point links.

**Answer (largest first):**

| Need | Subnet | Mask | Usable |
|---|---|---|---|
| 100 | 192.168.50.0/25 | 255.255.255.128 | .1 – .126 |
| 50 | 192.168.50.128/26 | 255.255.255.192 | .129 – .190 |
| 20 | 192.168.50.192/27 | 255.255.255.224 | .193 – .222 |
| 10 | 192.168.50.224/28 | 255.255.255.240 | .225 – .238 |
| 2 | 192.168.50.240/30 | 255.255.255.252 | .241 – .242 |
| 2 | 192.168.50.244/30 | 255.255.255.252 | .245 – .246 |

---

## Appendix C — Command Reference

### Windows

```
ipconfig                    Basic IP configuration
ipconfig /all               Full detail: MAC, DHCP server, lease, DNS
ipconfig /release           Release the DHCP lease
ipconfig /renew             Request a new lease
ipconfig /flushdns          Clear the DNS resolver cache
ipconfig /displaydns        Show cached DNS entries
ping <target>               ICMP reachability
ping -t <target>            Continuous ping
ping -f -l 1472 <target>    Test path MTU (DF bit set)
tracert <target>            Trace the path hop by hop
pathping <target>           Trace plus per-hop loss statistics
nslookup <name>             DNS query
nslookup <name> <server>    Query a specific DNS server
netstat -an                 All connections and listening ports
netstat -b                  Show the owning executable
arp -a                      Display the ARP cache
arp -d                      Clear the ARP cache
route print                 Display the routing table
nbtstat -n                  NetBIOS names
hostname                    This system's name
telnet <host> <port>        Crude port reachability test
```

### Linux / macOS

```
ip addr / ifconfig          Interface configuration
ip route / route -n         Routing table
ping <target>               ICMP reachability
traceroute <target>         Path trace
mtr <target>                Continuous traceroute with statistics
dig <name>                  DNS query (preferred over nslookup)
dig @<server> <name>        Query a specific server
host <name>                 Simple DNS lookup
ss -tuln / netstat -tuln    Listening ports
arp -n / ip neigh           ARP cache
tcpdump -i <iface>          Packet capture
nmap <target>               Port scan
ethtool <iface>             Interface speed, duplex, link status
```

### Cisco IOS — Packet Tracer essentials

```
enable                                  Privileged EXEC
configure terminal                      Global config
hostname <name>                         Set device name

show running-config                     Active configuration
show startup-config                     Saved configuration
copy running-config startup-config      Save
show ip interface brief                 All interfaces, IPs, status  ← use constantly
show interfaces <int>                   Detail including ERROR COUNTERS
show mac address-table                  Learned MACs per port
show vlan brief                         VLAN assignments
show interfaces trunk                   Trunk status and native VLAN
show ip route                           Routing table
show cdp neighbors                      Directly connected Cisco devices
show spanning-tree                      STP roles, states, root bridge
show port-security                      Port security status and violations

interface <int>                         Enter interface config
 ip address <ip> <mask>                 Assign address
 no shutdown                            Enable the interface
 switchport mode access                 Access port
 switchport access vlan <id>            Assign VLAN
 switchport mode trunk                  Trunk port
 switchport trunk native vlan <id>      Set native VLAN
 switchport port-security               Enable port security
 switchport port-security maximum <n>   MAC limit
 switchport port-security violation shutdown|restrict|protect
 speed <10|100|1000> / duplex <full|half|auto>

vlan <id> / name <name>                 Create and name a VLAN

interface <int>.<subif>                 Subinterface (router-on-a-stick)
 encapsulation dot1Q <vlan-id>          Tag the subinterface
 ip address <ip> <mask>

ip route <net> <mask> <next-hop>        Static route
router ospf <pid> / network <net> <wildcard> area <n>
router rip / version 2 / network <net>

line vty 0 4 / transport input ssh / login local
ip domain-name <name> / crypto key generate rsa
```

📌 **`show ip interface brief` and `show interfaces <int>` are the two commands you will use most.** The first tells you what's up; the second tells you *why* it's misbehaving, via the error counters from section 3.2.

---

## Appendix D — Acronym Master List

**Addressing & routing:** APIPA · ARP · BGP · CIDR · DHCP · DNS · EIGRP · EUI · FHRP · GLBP · HSRP · IPAM · NAT · NDP · OSPF · PAT · RIP · SLAAC · VIP · VLSM · VRRP

**Switching:** CSMA/CA · CSMA/CD · LACP · LAG · MAC · MSTP · MTU · OUI · PoE · RSTP · STP · SVI · VLAN · VTP · VXLAN

**Media:** APC · CWDM · DAC · DWDM · EMI · GBIC · LC · MMF · MT-RJ · OM · OS · QSFP · SC · SFP · SMF · ST · STP (shielded twisted pair) · TIA/EIA · UPC · UTP

**Protocols & ports:** FTP · FTPS · HTTP · HTTPS · ICMP · IMAP · LDAP · LDAPS · NTP · NTS · POP3 · PTP · RDP · SCP · SFTP · SIP · SMB · SMTP · SNMP · SSH · TCP · TFTP · TLS · UDP · VNC

**Security:** AAA · ACL · AES · CASB · CIA · DLP · DMZ · EAP · FWaaS · HIDS · IAM · IDS · IPS · MFA · NAC · NGFW · NIDS · PKI · PSK · RADIUS · RBAC · RC4 · RSA · SAE · SASE · SIEM · SWG · TACACS+ · TKIP · WEP · WPA · WPA2 · WPA3 · ZTA · ZTNA

**Operations & DR:** BYOD · CAB · CMDB · EOL · EOS · HVAC · IDF · MDF · MOU · MSA · MTBF · MTTR · NDA · NOC · PDU · RAID · RPO · RTO · SLA · SOW · UPS

**Architecture & cloud:** CDN · IaaS · IaC · NAS · NFV · NSG · PaaS · QoS · SAN · SaaS · SD-WAN · SDN · VM · VPC · VPN

**Diagnostics:** CRC · FCS · MIB · OID · OTDR · RSSI · SNI · SNR · TDR · TTL

---

## Appendix E — Study Plan

### Weekly rhythm

| Day | Focus |
|---|---|
| Mon | New domain content — read one section |
| Tue | Lab that section (call **TORA**) |
| Wed | New content |
| Thu | Lab + break/fix |
| Fri | Review the week's ⚠️ and 📌 boxes only |
| Sat | Full-length practice questions |
| Sun | Rest, or light drill only |

### Daily non-negotiables — 15 minutes, every day

1. **Ports** — Appendix A, both directions
2. **Subnetting** — three problems from Appendix B, timed
3. **One symptom → cause** row from the master table in Appendix F

📌 These three compound. Doing them daily for six weeks beats cramming them in the final week, because all three are recall under time pressure — exactly what the exam tests.

### Domain priority given the weights

| Priority | Domain | Why |
|---|---|---|
| 1 | **5.0 Troubleshooting (24%)** | Heaviest, applied, most commonly underprepared |
| 2 | **1.0 Concepts (23%)** | Heaviest recall load; everything else builds on it |
| 3 | **2.0 Implementation (20%)** | Most PBQ-relevant |
| 4 | **3.0 Operations (19%)** | Easy points, precise vocabulary |
| 5 | **4.0 Security (14%)** | Lightest weight. Section 4.2 attacks was written from scratch — drill it hard, it is pure recall |

### Readiness checklist

Before booking the exam, you should be able to:

- [ ] Recite the OSI layers both directions and place any technology at its layer
- [ ] Subnet any address to any prefix in under 30 seconds without a calculator
- [ ] Design a VLSM scheme largest-first without prompting
- [ ] Name all standard ports cold, in both directions
- [ ] State the 7 troubleshooting steps in order and identify "the next step" from any scenario
- [ ] Explain why a 169.254 address appears and list four causes
- [ ] Distinguish IDS/IPS, NAS/SAN, RPO/RTO, MTBF/MTTR, cold/warm/hot, shaping/policing, HSRP/GLBP
- [ ] Name the attack from its signature, and the control that stops it, in both directions (4.2)
- [ ] Separate bandwidth, throughput, latency and jitter, and say what causes each (5.4)
- [ ] Explain duplex mismatch, its symptoms, and where you'd see evidence
- [ ] Explain why Layer 2 loops need STP but Layer 3 loops don't
- [ ] Configure VLANs, trunks, inter-VLAN routing, and port security from memory in Packet Tracer
- [ ] Diagnose at least eight distinct planted faults from symptoms alone

---

## Corrections to the source transcripts

Three factual errors in the course material, flagged where they appear and collected here:

| Location | Transcript says | Correct |
|---|---|---|
| Day 4 — TTL | IP TTL default is **16 hops** | **16 is RIP's infinity metric.** IP TTL defaults are 64 (Linux/macOS), 128 (Windows), 255 (many network devices) |
| Day 7 — private ranges | 172.16.0.0 uses a **/16**, 192.168.0.0 uses a **/24** | Those are the *classful defaults for individual networks* inside each block. The **RFC 1918 blocks** are **10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16** |
| Day 11 — IPv6 | Default IPv6 subnet mask is **/32** | **/64** is the standard LAN prefix. A /32 is an ISP-scale allocation |

📌 Knowing where your source material is wrong is itself a form of mastery. If an exam question hinges on any of these three, trust this table.

---

*End of guide. Call **TORA** to expand any 🔧 lab stub into a full Packet Tracer 9.0.1 build. Call **GUM!GUM!** to brainstorm with multiple-choice options.*
## Appendix F — Master Symptom Reference



📌 **Study this table until it's reflexive. It converts most Domain 5 questions into a lookup.**

| Symptom | Most likely cause | First check |
|---|---|---|
| **169.254.x.x address** | DHCP unreachable | IP helper, scope, server, VLAN |
| **Ping IP works, ping name fails** | **DNS** | DNS server setting, HOSTS file, flush cache |
| **Can reach local, not remote** | **Default gateway** | Gateway address, router status |
| **No link light** | **Layer 1** | Cable, port state, NIC |
| **Link up, terrible throughput, late collisions** | **Duplex mismatch** | Interface settings both ends |
| **Ping works, large transfers fail** | **MTU mismatch** | Path MTU with `ping -f -l` |
| **Network intermittently unusable, broadcasts flooding** | **Switching loop** | STP status, redundant links |
| **Two hosts fighting, interfaces disabling** | **Duplicate IP** | Static vs DHCP scope overlap |
| **Port shut down after a device was plugged in** | **Port security violation** | Violation mode, err-disable state |
| **Certificate warning in browser** | Expired, name mismatch, or untrusted CA | Cert validity, SNI name, system clock |
| **Connection times out** | Firewall **dropping** | ACL/firewall rules and order |
| **Connection refused immediately** | Nothing listening, or **reject** rule | Service status, port scan |
| **Wireless slow with full signal bars** | **Channel congestion / interference** | Wi-Fi analyzer, channel plan |
| **Users on one VLAN only affected** | VLAN, trunk, or subnet-specific service | Trunk config, native VLAN, helper address |
| **Everything broke after last night** | **Change** | Change log, update history |

---
## Appendix G — Cross-Reference to Professor Messer's Course Notes

This maps every section of this guide to the corresponding topic and page in **Professor Messer's CompTIA N10-009 Network+ Course Notes, version 1.5** (© 2024 Messer Studios, LLC), so you can read both together.

⚠️ **This is an index, not a substitute.** No content from those notes appears in this guide — they are copyrighted and separately purchased. Use this table to find the right page in your own copy.

📌 Where a page range is listed, Messer splits the objective across several titled topics. Where this guide's section has **no page listed**, that material is organised differently between the two, so check the neighbouring objective.

### Domain 1 — Networking Concepts

| This guide | Messer topic(s) | Page |
|---|---|---|
| 1.1 The OSI Reference Model | Understanding the OSI Model · Networking Devices | 1 |
| 1.2 Networking Appliances, Applications, and Functions | Networking Functions | 3 |
| 1.3 Cloud Computing Concepts and Connectivity | Designing the Cloud · Cloud Models | 4–5 |
| 1.4 Ports, Protocols, and Services | Introduction to IP · Common Ports · Other Useful Protocols · Network Communication | 6–11 |
| 1.5 Transmission Media, Connectors, and Ethernet Standards | Ethernet Standards · Optical Fiber · Copper Cabling · Network Transceivers · Fiber Connectors | 12–16 |
| 1.6 Topologies, Architectures, and Traffic Flow | Network Topologies · Network Architecture | 17–18 |
| 1.7 IPv4 Addressing, Subnetting, and IPv6 | Binary Math · IPv4 Addressing · Classful Subnetting · IPv4 Subnet Masks · Calculating Subnets and Hosts · Magic Number Subnetting · Seven Second Subnetting | 19–21 |
| 1.8 Modern Network Environments | Software Defined Networking · Virtual Extensible LAN · Zero Trust · Infrastructure as Code · IPv6 Addressing | 22–25 |

📌 Messer places **IPv6 addressing at 1.8** and wireless networking at **1.5** (page 11). This guide keeps IPv6 with the rest of addressing in 1.7 and wireless in 2.3, because they drill better that way. The exam accepts either — the content is what matters.

### Domain 2 — Infrastructure

| This guide | Messer topic(s) | Page |
|---|---|---|
| 2.1 Routing Technologies and Bandwidth Management | Dynamic Routing · Routing Technologies · Network Address Translation | 26–28 |
| 2.2 Ethernet Switching Features | VLANs and Trunking · Interface Configurations · Spanning Tree Protocol | 29–31 |
| 2.3 Wireless Technologies | Wireless Technologies · Wireless Networking · Network Types · Wireless Encryption | 31–34 |
| 2.4 Physical Installations and Specialized Devices | Installing Networks · Power · Environmental Factors | 34–36 |

### Domain 3 — Network Operations

| This guide | Messer topic(s) | Page |
|---|---|---|
| 3.1 Network Documentation, Life Cycle, and Configuration Management | Network Documentation · Life Cycle Management · Configuration Management | 36–38 |
| 3.2 Network Monitoring and Performance | SNMP · Logs and Monitoring · Network Solutions | 38–40 |
| 3.3 Disaster Recovery and High Availability | Disaster Recovery · Network Redundancy | 40–41 |
| 3.4 DHCP, DNS, and Time Protocols | DHCP · Configuring DHCP · IPv6 and SLAAC · An Overview of DNS · DNS Records · Time Protocols | 41–47 |
| 3.5 VPNs and Remote Access | VPNs · Remote Access | 48–49 |

### Domain 4 — Network Security

| This guide | Messer topic(s) | Page |
|---|---|---|
| 4.1 Security Concepts, Authentication, and Segmentation Enforcement | Security Concepts · Authentication · Security Technologies · Regulatory Compliance · Segmentation Enforcement | 50–54 |
| 4.2 Common Network Attacks | Denial of Service · VLAN Hopping · MAC Flooding · ARP and DNS Poisoning · Rogue Services · Social Engineering · Malware | 54–58 |
| 4.3 Device Security and Security Rules | Device Security · Security Rules | 58–60 |

📌 **Domain 4 is where reading both is most worthwhile.** Section 4.2 here was written from scratch because the original transcripts barely covered attacks, so cross-checking against pages 54–58 is a genuine second source rather than a restatement.

### Domain 5 — Network Troubleshooting and Tools

| This guide | Messer topic(s) | Page |
|---|---|---|
| 5.1 The Troubleshooting Methodology | Network Troubleshooting Methodology | 61 |
| 5.2 Cable, Interface, and Hardware Issues | Cable Issues · Interface Issues · Hardware Issues | 62–65 |
| 5.3 Switching, Routing, and IP Issues | Switching Issues · Routing and IP Issues | 65–66 |
| 5.4 Performance and Wireless Issues | Performance Issues · Wireless Issues | 67 |
| 5.5 Software, Command Line, and Hardware Tools | Software Tools · Command Line Tools · Hardware Tools · Basic Network Device Commands | 68–70 |

### Free video companion

Messer's **video series is free** at professormesser.com, separate from the paid notes. The `messer-domain-1.md` file in the project holds direct links to the Domain 1 videos, ordered by objective. They follow the same numbering as the table above, so a section here maps to a video by objective number.

📌 **A study loop that works:** read the section here → watch the matching video → read the matching pages in your notes → then drill the section's cards and quiz in the interactive guide. Three explanations of the same idea from three angles, then immediate retrieval practice.

---
