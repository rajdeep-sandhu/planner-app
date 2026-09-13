# config_lists.py
from pathlib import Path


class ConfigLists:
    """Set up configuration lists."""

    def __init__(self):
        """ConfigLists constructor."""
        self.config_lists: dict = {}
        self.gammon_plan_workbook: Path = (
            Path(__file__).parent / "dev_data" / "Gammon_Plan_XL_V3_DEMO_WIP.xlsm"
        )
