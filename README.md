# Multi-Vendor Network Automation Lab 🚀

This repository tracks my hands-on journey into Network Automation. It serves as a centralized, infrastructure-as-code (IaC) environment to provision, manage, and pull telemetry from a multi-vendor network topology using Ansible and EVE-NG.

## 🧰 Tech Stack & Environment
* **Orchestration:** Ansible Core (v2.17+)
* **Hypervisor:** EVE-NG (Bare Metal)
* **Vendors:** * Aruba (AOS-CX Virtual)
  * Juniper (vEX / Junos)
* **Connectivity:** A custom virtual NAT Bridge (Cloud 9) was engineered to isolate lab traffic from the physical ISP router while maintaining inbound/outbound connectivity.

---

## 📂 Repository Architecture

```text
NETWORK-AUTOMATION/
├── Automation - Python/
│   ├── .venv/                           # Primary Python Virtual Environment (Git Ignored)
│   ├── Day-1/
│   │   └── auth.test.py                 # Aruba CX REST API authentication & session handling
│   └── Day-2/
│       └── Telent/
│           ├── .gitignore               # Ignores local venv files
│           └── telent.py                # Legacy CLI automation script via telnetlib
│
├── Automation - YAML/                   # Ansible & YAML based declarative automation
│   ├── Day-1 - Discovery & Telemetry/   # Playbooks for state gathering
│   ├── Day-2 - Configuration & Idempotency/ # Playbooks for pushing config changes
│   ├── ansible.cfg                      # Main Ansible configuration file
│   └── hosts                            # Ansible inventory file
│
└── README.md                            # Project documentation