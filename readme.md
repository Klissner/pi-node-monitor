
> 📌 **Hinweis / Note:** Dokument in DE und EN verfügbar / Document available in DE and EN.

---

## 🇩🇪 Deutsche Fassung

Ein leichtgewichtiges, webbasiertes HUD-Dashboard zur Echtzeit-Überwachung einer Pi-Network Node. Das Design ist im modernen Cyberpunk-/HUD-Stil gehalten (basierend auf Tailwind CSS) und bietet eine übersichtliche Matrix aller kritischen Konsens- und Systemdaten des Stellar/Pi Consensus Protocols (SCP).

In dieser ersten Beta-Version wird primär die Überwachung einer **Single Node** unterstützt. Da das System jedoch vollständig containerisiert und über Umgebungsvariablen gesteuert wird, kann der Container problemlos **mehrfach gestartet werden**, um mehrere Nodes parallel auf unterschiedlichen Ports zu überwachen.

Dokumentation
https://www.klissner.uk/de/pi-node-monitor-beta-0-01-offizielle-web-seite/

---

### 🚀 Features & Funktionsumfang
* **Live-Status-Überwachung:** Direktes Feedback, ob die Node im Netzwerk `SYNCED`, `NOMINATE`, `PREPARE` oder `OFFLINE` ist.
* **Dynamische Block-Anzeige:** Vergleicht die aktuelle Blockhöhe deiner Node mit den Gesamtblöcken des Netzwerks, inklusive Berechnung der Zeitdifferenz (Letzter Block vor X Sekunden).
* **Quorum- & Konsens-Matrix:** Echtzeit-Einsicht in die Quorum-Gruppe, ausfalltolerante Knoten (Fault Tolerance), Peers, und Verbindungsverzögerung (Lag in ms).
* **Ertrags-Index (KPI):** Ein mathematischer Schätzwert der Node-Effizienz für den Pi-Mining-Bonus basierend auf Synchronität und Latenz.
* **Sicherheits-Schnittmenge:** Automatische Validierung, ob die Quorum-Schnittmenge (`intersection`) im Netzwerk mathematisch sicher geschützt ist (`SECURE_OK`).
* **Mehrsprachigkeit:** Nahtloser Wechsel zwischen Deutsch (DE) und Englisch (EN) direkt im UI.
* **Persistenz & Flexibilität:** Einstellungen können temporär im UI überschrieben werden; Standardwerte werden sicher über die `.env`-Datei geladen.

---

### 💻 Systemanforderungen

* **Betriebssystem & Laufzeitumgebung:**
  * **Linux:** Docker CE (Community Edition) & Docker Compose v2.
  * **Windows:** Windows Subsystem for Linux (WSL 2) mit Docker Desktop.
* **Pi-Node Kompatibilität:**
  * Pi-Node **v24.1.0** (oder höher), ausgeführt innerhalb von Docker (entweder über die offizielle Pi-App oder eine eigenständige Linux-Node-Konfiguration).
* **Netzwerk:**
  * Netzwerkzugriff über IP auf die API der Pi-Node (Lokal auf demselben Host, via LAN oder über WAN/VPN).
  * Der Standard-API-Port der Pi-Node (`11626`) muss für den Monitor-Container erreichbar sein.

---

### 📦 Unterstützte Architekturen (Docker Images)

Das Docker-Setup unterstützt Multi-Architektur-Builds und läuft nativ auf folgenden Plattformen:
* **X86_64 / AMD64:** Für klassische Server, Desktop-PCs, Legion-Systeme oder VM-Umgebungen.
* **ARM64 / ARMv8:** Optimiert für Single-Board-Computer wie den Raspberry Pi (4/5), Synology NAS oder Apple Silicon (M-Series MacBooks).

### Images
ghcr.io/Klissner/pi-node-monitor:beta-0.01-amd64
ghcr.io/Klissner/pi-node-monitor:beta-0.01-arm64

---

### ⚙️ Konfiguration & Installation

Die gesamte Konfiguration wird über eine zentrale `.env`-Datei gesteuert, die von Docker Compose eingelesen und als Umgebungsvariable an die Flask-App übergeben wird.

#### 1. `docker-compose.yml`
Erstelle eine Datei namens `docker-compose.yml` in deinem Projektverzeichnis:

```yaml

services:
  pi-monitor:
    image: ghcr.io/klissner/pi-node-monitor:beta-0.01-amd64      # x86 systems
    # image: ghcr.io/klissner/pi-node-monitor:beta-0.01-arm64    # Raspberry Pi / Apple Silicon
    container_name: pi-monitor
    restart: unless-stopped
    ports:
      - "${MONITOR_PORT}:${MONITOR_PORT}"
    env_file:
      - .env
    volumes:
      - ./app-data:/app/data

```

#### 2. `.env` Datei

Erstelle eine `.env`-Datei im selben Verzeichnis wie die `docker-compose.yml` und passe die Werte an deine Umgebung an:

```env
# Port, auf dem das Dashboard erreichbar sein soll (Host & Container-intern match)
MONITOR_PORT=8080

# IP-Adresse der zu überwachenden Pi-Node (z.B. 127.0.0.1 oder die LAN-IP)
NODE_IP=127.0.0.1

# Interner API-Port der Pi-Node (Standard: 11626)
NODE_PORT=11626

# Aktualisierungsintervall des Dashboards in Sekunden
MONITOR_REFRESH=5

```

#### 3. Beschreibung der Konfigurations-Optionen

| Variable | Beschreibung | Standardwert |
| --- | --- | --- |
| `MONITOR_PORT` | Der Port, unter dem du das Dashboard im Browser aufrufst (z. B. `http://localhost:8080`). Muss mit der internen Flask-Konfiguration übereinstimmen. | `8080` |
| `NODE_IP` | Die IP-Adresse deiner Pi-Node. Läuft der Monitor auf demselben PC wie die Node, nutze `127.0.0.1`. | `127.0.0.1` |
| `NODE_PORT` | Der JSON-RPC / Info Port der Pi-Node Core Software. | `11626` |
| `MONITOR_REFRESH` | Intervall in Sekunden, in dem das Frontend neue Daten von der Node abfragt. | `5` |

---

### 🚀 Starten des Containers

Starte den Monitor anschließend im Hintergrund (Detached Mode):

```bash
docker compose up -d

```

Der Monitor ist danach über `http://<Deine-Host-IP>:8080` (bzw. dem von dir gewählten `MONITOR_PORT`) erreichbar.

---

### 🔒 Copyright & Lizenzhinweis

MIT License

Copyright (c) 2026 KSC | by Michael Klissner

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

### ☕ Spenden / Support

Wenn dir dieses Dashboard hilft und du die Weiterentwicklung unterstützen möchtest, freuen wir uns über eine Spende an die folgenden Adressen:

* **Pi-Wallet Adresse:**
```text
GCOQMXIRFWMNBV73GDPDYWL4BT7AUGWOPZWIZKPHB7WFRY5TNUFWAJRR

```


* **Weitere Spendenlinks & YouTube Support:**
[📎 https://www.ksc-llp.uk/donateyoutube](https://www.google.com/search?q=https://www.ksc-llp.uk/donateyoutube)





## 🇬🇧 English Version

A lightweight, web-based HUD dashboard for real-time monitoring of a Pi-Network Node. The interface features a modern cyberpunk/HUD style (powered by Tailwind CSS) and provides a comprehensive matrix of all critical consensus and system metrics from the Stellar/Pi Consensus Protocol (SCP).

This initial beta release primarily supports monitoring a **single node**. However, since the setup is completely containerized and controlled via environment variables, you can easily **spin up multiple containers** to monitor several nodes simultaneously on different ports.

Documentation
https://www.klissner.uk/en/pi-node-monitor-beta-0-01-official-website/

---

### 🚀 Features

* **Live Status Monitoring:** Instant feedback on whether the node is `SYNCED`, `NOMINATE`, `PREPARE`, or `OFFLINE`.
* **Dynamic Block Display:** Compares your node's current block height against the network total, calculating the exact time delta (Last block X seconds ago).
* **Quorum & Consensus Matrix:** Real-time metrics regarding your quorum slice, fault tolerance (nodes allowed to fail), peer counts, and connection lag (in ms).
* **Incentive Index (KPI):** A mathematical estimation of your node's performance score for the Pi mining bonus, calculated based on sync status and latency.
* **Security Intersection Check:** Automatically validates if your quorum intersection is mathematically secured against ledger splits (`SECURE_OK`).
* **Multi-Language Support:** Seamlessly switch between German (DE) and English (EN) directly within the UI.
* **Persistence & Flexibility:** UI-overridden settings persist via sessions, while permanent defaults are securely loaded via the `.env` file.

---

### 💻 System Requirements

* **OS & Runtime Environment:**
* **Linux:** Docker CE (Community Edition) & Docker Compose v2.
* **Windows:** Windows Subsystem for Linux (WSL 2) with Docker Desktop.


* **Pi-Node Compatibility:**
* Pi-Node **v24.1.0** (or higher) running inside Docker (either via the official Pi App interface or a custom Linux node configuration).


* **Network Setup:**
* Network accessibility via IP to the Pi-Node API (Localhost, local LAN, or WAN/VPN routing).
* The default Pi-Node core API port (`11626`) must be accessible by the monitor container.



---

### 📦 Supported Architectures (Docker Images)

The Docker setup supports multi-architecture builds and runs natively on:

* **X86_64 / AMD64:** For typical servers, desktop PCs, home labs, or virtual machines.
* **ARM64 / ARMv8:** Optimized for single-board computers like the Raspberry Pi (4/5), Synology NAS, or Apple Silicon (M-Series MacBooks).

### Images
ghcr.io/Klissner/pi-node-monitor:beta-0.01-amd64
ghcr.io/Klissner/pi-node-monitor:beta-0.01-arm64

---

### ⚙️ Configuration & Installation

The entire runtime environment is controlled via a centralized `.env` file, which is parsed by Docker Compose and passed onto the Flask backend application.

#### 1. `docker-compose.yml`

Create a file named `docker-compose.yml` in your project root directory:

```yaml

services:
  pi-monitor:
    image: ghcr.io/klissner/pi-node-monitor:beta-0.01-amd64      # x86 systems
    # image: ghcr.io/klissner/pi-node-monitor:beta-0.01-arm64    # Raspberry Pi / Apple Silicon
    container_name: pi-monitor
    restart: unless-stopped
    ports:
      - "${MONITOR_PORT}:${MONITOR_PORT}"
    env_file:
      - .env
    volumes:
      - ./app-data:/app/data

```

#### 2. `.env` File

Create a `.env` file in the same directory as your `docker-compose.yml` and adjust the parameters for your network:

```env
# Port where the web dashboard will be exposed (Host & Container match)
MONITOR_PORT=8080

# IP address of the Pi-Node you want to monitor (e.g., 127.0.0.1 or your local LAN IP)
NODE_IP=127.0.0.1

# Internal API port of the Pi-Node core software (Default: 11626)
NODE_PORT=11626

# Dashboard refresh interval in seconds
MONITOR_REFRESH=5

```

#### 3. Configuration Options Glossary

| Variable | Description | Default Value |
| --- | --- | --- |
| `MONITOR_PORT` | The network port used to open the dashboard in your browser (e.g., `http://localhost:8080`). Must match the backend configuration. | `8080` |
| `NODE_IP` | The IP address belonging to the target Pi-Node. Use `127.0.0.1` if hosted on the same machine. | `127.0.0.1` |
| `NODE_PORT` | The JSON-RPC / Info port utilized by the underlying Pi-Node core. | `11626` |
| `MONITOR_REFRESH` | Interval in seconds defining how frequently the frontend requests fresh data from the node. | `5` |

---

### 🚀 Starting the Container

Launch the monitoring stack in the background (Detached Mode):

```bash
docker compose up -d

```

The dashboard will immediately be available at `http://<Your-Host-IP>:8080` (or whichever custom `MONITOR_PORT` you assigned).

---

### 🔒 Copyright & License

MIT License

Copyright (c) 2026 KSC | by Michael Klissner

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

### ☕ Support / Donations

If this dashboard helps you manage your node, feel free to support the project via:

* **Pi-Wallet Address:**
```text
GCOQMXIRFWMNBV73GDPDYWL4BT7AUGWOPZWIZKPHB7WFRY5TNUFWAJRR

```


* **External Links & YouTube Support:**
[📎 https://www.ksc-llp.uk/donateyoutube](https://www.google.com/search?q=https://www.ksc-llp.uk/donateyoutube)

```

```