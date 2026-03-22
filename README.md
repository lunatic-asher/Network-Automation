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
This project utilizes a **Global Inventory Architecture**. Instead of maintaining separate credential files for every lab, a single source of truth is kept at the root directory.

```text
Netwrok-Automation/
├── ansible.cfg          # Global Ansible settings (timeouts, strict host checking)
├── hosts                # Global inventory file (IPs, credentials, OS variables)
├── README.md            # Project documentation
├── Day-1 - Connecting/  # Discovery and telemetry playbooks
│   ├── aruba_playbook.yml
│   └── juniper_playbook.yml
└── Day-2/               # State changes and configuration management
    └── juniper_config_playbook.yml