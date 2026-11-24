<div align="center">
  <h1>Alessio Devetti</h1>
  <p><strong>Systems & Network Administration • Smart Automation • Self-Hosted Infrastructure</strong></p>
  <p>Trieste, Italia • <a href="mailto:mail@joshuameta.it">mail@joshuameta.it</a> (PGP Signed)</p>
</div>

---

### Profilo

Studente ITS in Reti e Cybersecurity con esperienza pratica su ambienti Linux/Proxmox, Docker e configurazione di reti (VLAN, firewall stateful, WireGuard, DNS e Dual-Stack IPv4/IPv6 con Prefix Delegation). Porto competenze sistemistiche e di troubleshooting L2/L3 per supportare l'operatività di rete, con l'obiettivo di specializzarmi nel networking ISP e nel routing dinamico.

---

### Infrastruttura & Architettura

#### Rete & Sicurezza Perimetrale
* **Routing & Dual-Stack IPv6:** Gateway perimetrale basato su **OPNsense** con connettività FTTH in PPPoE (Aruba Fibra) e gestione Dual-Stack IPv4/IPv6 tramite **Prefix Delegation** su 3 interfacce e 3 sottoreti segmentate.
* **VPN & Hardening:** Server VPN **WireGuard** per l'accesso remoto cifrato e regole firewall granulari per l'isolamento dei flussi. Nodo `i2pd` su porta dedicata con policy restrittive perimetrali e firewall locale (`UFW`) che limita l'accesso SSH alla sola LAN (usato per il tunneling verso la console web).
* **Intrusion Prevention & DNS Cifrato:** Integrazione **CrowdSec** con parsing dei log di Nginx Proxy Manager e bouncer attivo direttamente su OPNsense. Risoluzione DNS affidata ad **AdGuard Home** con upstream **DNS-over-TLS (Mullvad)** per eliminare il traffico DNS in chiaro, esposto tramite dominio, porta e query path personalizzati contro le scansioni automatiche.

#### Virtualizzazione & Stack Servizi (Proxmox VE)
* **Storage & Hypervisor:** Nodo **Proxmox VE** con pool storage ridondato in configurazione RAID 5 (~60 TB utilizzabili), montato sui container **LXC** per la persistenza dei dati.
* **Isolamento dei Carichi:**
  * **LXC 1 (Isolated VPN Stack):** Ambiente Docker interamente instradato dietro tunnel **Gluetun VPN** con gestione automatica del port forwarding e interfacce web accessibili esclusivamente dalla rete locale.
  * **LXC 2 (Media Streaming):** Istanza dedicata a **Jellyfin** per lo streaming multimediale su rete locale/remota.
  * **LXC 3 (Core Self-Hosted Services):** Host Debian con stack Docker Compose per **Nginx Proxy Manager** (reverse proxy TLS), **Nextcloud**, **Collabora Online**, **Affine** e **BookOrbit**.

---

### Progetti di Rete & Infrastruttura

| Progetto | Ambito | Descrizione Tecnica |
| :--- | :--- | :--- |
| **Architettura Dual-Stack & Multi-Site VPN** | Networking / Security | Progettazione rete domestica con OPNsense, distribuzione prefissi IPv6 (SLAAC/DHCPv6-PD), regole firewall granulari e interconnessione remota via WireGuard. |
| **Nodo Floodfill I2P** | Overlay Networks | Deployment e tuning di un router `i2pd` ad alta banda isolato su Pi5 dedicato, ottimizzato per il routing cifrato sulla rete I2P. |
| **Mappatura & Diagnostica Topologia di Rete** | Network Analysis | Analisi passiva/attiva di sottoreti, tracciamento percorsi Dual-Stack e audit delle porte esposte in ambienti LAN/WAN. |

---

### Formazione

| Percorso di Studi | Istituto / Ente | Periodo | Avanzamento | Esito / Stato |
| :--- | :--- | :--- | :--- | :--- |
| **ITS Sicurezza delle Reti e dei Sistemi** | Accademia Nautica dell'Adriatico (Trieste) | Nov 2026 – Lug 2028 | `░░░░░░░░░░` 2% | In corso |
| **Diploma in Telecomunicazioni** | I.T.S. Alessandro Volta (Trieste) | 2020 – 2025 | `██████████` 100% | **90/100** |

#### Certificazioni & Corsi Specialistici

| Certificazione / Corso | Ente | Stato | Focus Tecnico |
| :--- | :--- | :--- | :--- |
| **IPv6 Certification** | Hurricane Electric (HE) | 🟡 In corso (livello Enthusiast)| Connettività IPv6 nativa, DNS AAAA/PTR, routing e server SMTP/web su IPv6 |
| **IPv6 Fundamentals / Advanced** | RIPE NCC Academy | 🔵 In programma | Piano di indirizzamento RIR, BGP su IPv6, policy di assegnazione e transizione |

---

### Stack Tecnologico

<p align="left">
  <img src="https://img.shields.io/badge/Linux-171717?style=flat-square&logo=linux&logoColor=white" />
  <img src="https://img.shields.io/badge/Debian-A81D33?style=flat-square&logo=debian&logoColor=white" />
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=flat-square&logo=proxmox&logoColor=white" />
  <img src="https://img.shields.io/badge/OPNsense-D94F00?style=flat-square&logo=opnsense&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/WireGuard-88171A?style=flat-square&logo=wireguard&logoColor=white" />
  <img src="https://img.shields.io/badge/CrowdSec-F55B3D?style=flat-square&logo=crowdsec&logoColor=white" />
  <img src="https://img.shields.io/badge/AdGuard%20Home-68BC71?style=flat-square&logo=adguard&logoColor=white" />
  <img src="https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white" />
  <img src="https://img.shields.io/badge/Home%20Assistant-41BDF5?style=flat-square&logo=homeassistant&logoColor=white" />
</p>

---