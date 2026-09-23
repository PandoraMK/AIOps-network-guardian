# AIOps Autonomous Network Guardian & Predictive Simulation

An end-to-end AIOps (Artificial Intelligence for IT Operations) framework designed to transition telecommunications Network Operations Centers (NOCs) from reactive firefighting to proactive, automated self-healing. 

Developed entirely within a structured Jupyter Notebook environment, this project simulates high-frequency cellular tower telemetry by incorporating real-world operational stressors such as power grid instability, thermal overheating, and regulatory drop-rate compliance in order to forecast failures one hour in advance and execute closed-loop remediation playbooks.

---

## Architecture & Workflow

The system is organized into four logical, sequential phases:

### 1. Multivariate Telemetry Simulation (`simulation.py` / Notebook Part 1)
* Generates high-resolution 30-day operational telemetry across multiple regional base stations.
* Tracks core performance indicators including **CPU load, PRB resource utilization, cabinet temperature, core latency, Mean Opinion Score (MOS), power grid stability, and ICASA drop-rate compliance**.
* Injects realistic, continuous failure episodes (e.g., thermal spikes and grid outages) to replicate genuine field conditions.

### 2. Time-Series Feature Engineering & Machine Learning (`model.py` / Notebook Part 2)
* Engineers temporal **lag features** (`Temp_Lag_1`, `Temp_Lag_2`, `Health_Lag_1`, `CPU_Lag_1`) to capture operational momentum and trends before a failure occurs.
* Trains a **Random Forest Classifier** with optimized balanced class weighting to handle class imbalance and eliminate alert fatigue.
* Establishes a **1-hour predictive horizon** (`Future_Anomaly`), allowing engineers to act *before* service degradation impacts customers.

### 3. Closed-Loop Automation Playbooks (`playbooks.py` / Notebook Part 3)
* Automatically scans network inference outputs and isolates the exact root cause of a predicted failure.
* Dispatches targeted self-healing scripts:
  * **Power Playbook:** Engages backup lithium battery reserves and dispatches diesel generators upon grid failure.
  * **Thermal Playbook:** Overrides cabinet HVAC systems to maximum cooling capacity during severe temperature spikes.
  * **Traffic Playbook:** Executes Software-Defined Networking (SDN) load balancing to offload congested PRB resources to adjacent towers.

### 4. NOC Operations Dashboard (Power BI)
* Connects the pipeline data to an interactive analytics dashboard featuring macro executive KPIs, spatial tower health mapping, predictive degradation trend lines, and a live audit log of automated interventions.

---

## Performance & Results

* **Prediction Horizon:** 1 Hour ahead of critical failure
* **Precision:** `1.00` (Zero false alarms, effectively eliminating alert fatigue)
* **Recall:** `0.81` (Captures over 80% of impending critical crisis episodes)
* **Overall Accuracy:** `98.6%` across rigorous multivariate stress-test datasets.

---

## Tech Stack

* **Language & Environment:** Python 3.x, Jupyter Notebook (VS Code)
* **Data Processing & ML:** Pandas, NumPy, Scikit-Learn (Random Forest)
* **BI & Visualization:** Power BI (DAX measures, Power Query, custom conditional formatting)
* **Methodologies:** Multivariate Time-Series Analysis, Supervised Classification, Closed-Loop System Automation

---

## Getting Started

Clone the repository:
   ```bash
   git clone [https://github.com/your-username/aiops-network-guardian.git](https://github.com/your-username/aiops-network-guardian.git)
