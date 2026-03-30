#  Network Automation Journey

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![ArubaOS-CX](https://img.shields.io/badge/Aruba-AOS--CX-FF8300.svg)
![NetDevOps](https://img.shields.io/badge/NetDevOps-Automation-success.svg)

Welcome to my Network Automation repository! This project serves as a practical, hands-on lab environment documenting the transition from traditional CLI-based NOC engineering to modern infrastructure-as-code (IaC) and API-driven automation. 

The primary testing environment utilizes **EVE-NG** running **Aruba AOS-CX** virtual switches.

## 📂 Repository Architecture

```text
NETWORK-AUTOMATION/
├── Automation - Python/
│   ├── .venv/                           # Local Python Virtual Environment (Git Ignored)
│   ├── Day-1/
│   │   └── auth.test.py                 # Aruba CX REST API authentication & session handling
│   └── Day-2/
│       └── Telent/
│           ├── .gitignore               # Ignores local venv binaries
│           └── telent.py                # Legacy CLI automation script via telnetlib
│
├── Automation - YAML/                   # Ansible & YAML based declarative automation
│   ├── Day-1 - Discovery & Telemetry/   # Playbooks for state gathering
│   ├── Day-2 - Configuration & Idempotency/ # Playbooks for pushing config changes
│   ├── ansible.cfg                      # Main Ansible configuration file
│   └── hosts                            # Ansible inventory file
│
└── README.md                            # Project documentation
