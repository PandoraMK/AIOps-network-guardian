import pandas as pd
import pytest
from src.features import create_temporal_lag_features
from src.playbooks import execute_remediation_playbook


def test_create_temporal_lag_features():
    raw_data = pd.DataFrame(
        {
            "cabinet_temp": [30.0, 32.0, 35.0, 40.0],
            "cpu_load": [0.2, 0.4, 0.6, 0.8],
            "health_score": [100, 95, 90, 80],
        }
    )

    transformed_df = create_temporal_lag_features(raw_data, lags=2)

    # 4 rows minus 2 lag shifts leaves 2 rows
    assert len(transformed_df) == 2
    # Verify exact lag values for row 0 (which was index 2 in original raw_data)
    assert transformed_df.loc[0, "Temp_Lag_1"] == 32.0
    assert transformed_df.loc[0, "Temp_Lag_2"] == 30.0
    assert transformed_df.loc[0, "CPU_Lag_1"] == 0.4
    assert transformed_df.loc[0, "Health_Lag_1"] == 95


def test_thermal_playbook_trigger():
    telemetry = {
        "cabinet_temp": 48.5,
        "grid_status": "ONLINE",
        "prb_utilization": 0.50,
    }
    result = execute_remediation_playbook(
        predicted_anomaly=True, telemetry=telemetry
    )

    assert result["status"] == "ACTION_TAKEN"
    assert result["playbook"] == "THERMAL_PLAYBOOK"
    assert result["action"] == "OVERRIDE_HVAC_MAX_COOLING"


def test_power_playbook_trigger():
    telemetry = {
        "cabinet_temp": 35.0,
        "grid_status": "OFFLINE",
        "prb_utilization": 0.40,
    }
    result = execute_remediation_playbook(
        predicted_anomaly=True, telemetry=telemetry
    )

    assert result["status"] == "ACTION_TAKEN"
    assert result["playbook"] == "POWER_PLAYBOOK"
    assert result["action"] == "ENGAGE_BATTERY_RESERVES_AND_GENERATOR"


def test_traffic_playbook_trigger():
    telemetry = {
        "cabinet_temp": 35.0,
        "grid_status": "ONLINE",
        "prb_utilization": 0.92,
    }
    result = execute_remediation_playbook(
        predicted_anomaly=True, telemetry=telemetry
    )

    assert result["status"] == "ACTION_TAKEN"
    assert result["playbook"] == "TRAFFIC_PLAYBOOK"
    assert result["action"] == "EXECUTE_SDN_LOAD_BALANCING"


def test_unknown_anomaly_trigger():
    telemetry = {
        "cabinet_temp": 35.0,
        "grid_status": "ONLINE",
        "prb_utilization": 0.50,
    }
    result = execute_remediation_playbook(
        predicted_anomaly=True, telemetry=telemetry
    )

    assert result["status"] == "UNKNOWN_ANOMALY"
    assert result["action"] == "DISPATCH_FIELD_ENGINEER"


def test_nominal_state():
    telemetry = {
        "cabinet_temp": 30.0,
        "grid_status": "ONLINE",
        "prb_utilization": 0.30,
    }
    result = execute_remediation_playbook(
        predicted_anomaly=False, telemetry=telemetry
    )

    assert result["status"] == "NOMINAL"
    assert result["action"] == "NO_ACTION_REQUIRED"
