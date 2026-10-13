# 🌑 AetherRecon

**Advanced Modular Grey-Hat Research Framework**  
*Ethical • Authorized Use Only • No AI Dependencies*

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![No AI](https://img.shields.io/badge/AI-None-red.svg)]()

> **Disclaimer**: This tool is designed **exclusively for authorized security research, educational purposes, and defensive analysis** on systems and networks you own or have explicit written permission to test. Unauthorized use against any system is illegal and strictly prohibited. The authors assume no liability for misuse.

---

## ✨ What Makes AetherRecon Unique?

Most recon / OSINT / forensics tools are either too basic or too specialized. AetherRecon is a **unified research platform** with rare advanced features rarely found together:

| Feature | Description | Rarity |
|---------|-------------|--------|
| **Shadow Profile Correlation** | Multi-source public data timeline + relationship graph reconstruction | Very Rare |
| **Behavioral Baseline Engine** | Learns normal traffic patterns on *your* network and flags anomalies | Rare |
| **Deep Config Fingerprinting** | Scores risk of exposed services, headers, cloud misconfigs with remediation | Advanced |
| **Experimental Stego Lab** | Advanced LSB, DCT, and statistical steganography detection + extraction | Rare |
| **Evidence Chain Reporting** | Cryptographically chained reports (hash-linked) for forensic integrity | Unique |
| **Plugin Architecture** | Hot-load new modules without restarting | Production-grade |
| **Dual Interface** | Full-featured CLI (Rich + Textual) + modern Streamlit Web GUI | Complete |
| **Zero AI** | 100% local computation + public data sources only | Guaranteed |

---

## 🏗️ Architecture

```
AetherRecon/
├── core/               # Engine, auth, config, plugin loader, reporting
├── modules/
│   ├── osint/          # Passive OSINT & shadow profiling
│   ├── network/        # Authorized network analysis & baselining
│   ├── forensics/      # Local system & memory artifact analysis
│   ├── crypto/         # Crypto, hashing, steganography lab
│   └── config/         # Misconfiguration & exposure scanner
├── gui/                # Streamlit web interface
├── utils/              # Shared helpers
├── plugins/            # Drop-in plugins
├── reports/            # Generated reports
├── data/               # Wordlists, signatures, baselines
└── config/             # User configuration
```

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/sayan9168/AetherRecon.git
cd AetherRecon
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. CLI Mode

```bash
# Interactive help
python -m aetherrecon --help

# OSINT shadow profile
python -m aetherrecon osint shadow --target example.com --depth 2

# Authorized network baseline (requires confirmation)
python -m aetherrecon network baseline --interface eth0 --duration 300

# Local forensics scan
python -m aetherrecon forensics scan --path /home/user --recursive

# Crypto / Stego lab
python -m aetherrecon crypto stego-detect --image suspicious.png

# Launch full TUI
python -m aetherrecon tui
```

### 3. Web GUI

```bash
streamlit run gui/app.py
```

Open `http://localhost:8501`

---

## 📦 Modules Overview

### 1. OSINT / Shadow Profile
- Domain / IP / Username / Email passive enrichment
- Historical WHOIS, DNS, certificate transparency
- Cross-source correlation & timeline reconstruction
- Relationship graph export (GraphML / PNG)

### 2. Network Analysis (Authorized Only)
- Live interface monitoring
- Protocol anomaly detection
- Custom behavioral baseline learning
- Service fingerprinting with risk scoring
- **Mandatory authorization prompt** before any active scan

### 3. Local Forensics
- File integrity monitoring (FIM)
- Process & memory artifact extraction
- Timeline of file system events
- Hash-based evidence collection

### 4. Crypto & Steganography Lab
- Modern authenticated encryption helpers
- Multi-algorithm hash analysis
- Advanced steganography detection (LSB, statistical, chi-square)
- Secure wipe utilities

### 5. Config / Exposure Scanner
- Security headers analysis
- Common misconfiguration detection
- Public cloud bucket / exposed API checks (passive)
- Risk scoring + remediation suggestions

---

## 🔒 Ethical & Legal Notes

1. **Authorization is mandatory** for any active module (network scan, service probe, etc.).
2. The tool will **refuse** to run active features without explicit confirmation.
3. Only use against systems you own or have written permission to test.
4. Passive OSINT uses only publicly available information.
5. No exploitation payloads, no brute-force login attacks, no malware generation.

---

## 🧩 Extending with Plugins

Drop a Python file in `plugins/`:

```python
from core.plugin import PluginBase

class MyPlugin(PluginBase):
    name = "my_custom_module"
    description = "Does something unique"

    def run(self, **kwargs):
        # your logic
        return {"result": "ok"}
```

It will be auto-discovered.

---

## 📄 License

MIT License – see [LICENSE](LICENSE)

---

## ⚠️ Final Warning

**This is a research tool.**  
Misuse can result in criminal charges. Always stay on the right side of the law and ethics.

Built with ❤️ for legitimate security researchers by the community.

---

**Repository**: https://github.com/sayan9168/AetherRecon  
**Author**: Sayan the researcher (@sayan9168)
