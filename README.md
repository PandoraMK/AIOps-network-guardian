# AIOps Autonomous Network Guardian & Predictive Simulation

An end-to-end AIOps framework designed to transition telecommunications Network Operations Centers (NOCs) from reactive firefighting to proactive, automated self-healing. Built with Python, Scikit-Learn, and Power BI, this system simulates high-frequency cellular tower telemetry—incorporating local operational realities such as grid instability and regulatory compliance—to forecast failures one hour in advance and execute automated remediation playbooks.

---

## Architecture & Core Components

1. **Multivariate Telemetry Simulation (`simulation.py`)**: 
   - Generates high-frequency operational data across multiple base stations.
   - Tracks CPU load, PRB resource utilization, cabinet temperature, core latency, Mean Opinion Score (MOS), power grid stability, and drop-rate compliance.
2. **Predictive Machine Learning Engine (`model.py`)**:
   - Leverages **Random Forest Classifiers** engineered with temporal lag features (`Temp_Lag`, `Health_Lag`, `CPU_Lag`) to capture operational momentum.
   - Solves class imbalance using optimized class weighting to eliminate alert fatigue.
3. **Closed-Loop Automation Playbooks (`playbooks.py`)**:
   - Automatically triages root causes upon a predicted failure flag (`Future_Anomaly = 1`).
   - Dispatches specific remediation workflows (e.g., battery/generator fallback for grid loss, maximum HVAC override for thermal spikes, and SDN load balancing for spectrum congestion).
4. **NOC Dashboard Interface (Power BI)**:
   - Visualizes macro-level KPIs, spatial tower health mapping, predictive degradation trends against critical safety thresholds, and live audit logs of automated interventions.

---

## Model Performance & Results
- **Prediction Horizon:** 1 Hour in advance
- **Precision:** `1.00` (Zero false alarms, eliminating NOC alert fatigue)
- **Recall:** `0.81` (Captures over 80% of impending critical crisis episodes)
- **Overall Accuracy:** `98.6%` on rigorous 30-day multivariate stress-test datasets.

---

## Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy, Scikit-Learn
- **BI & Analytics:** Power BI (DAX, Power Query)
- **Methodology:** Time-Series Feature Engineering, Supervised Classification, Closed-Loop Orchestration
