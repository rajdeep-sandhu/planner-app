# config_lists.py
from pathlib import Path

import polars as pl


class ConfigLists:
    """Set up configuration lists."""

    def __init__(self):
        """ConfigLists constructor."""
        self.gammon_plan_workbook: Path = (
            Path(__file__).parent / "dev_data" / "Gammon_Plan_XL_V3_DEMO_WIP.xlsm"
        )
        self.lists: dict[str, list] = self._load_lists_from_excel()

    def _load_lists_from_excel(self) -> dict[str, list]:
        """
        Load lists from List worksheet of gammon_plan_workbook as DataFrame.
        
        Return:
        lists: dict of config lists.
        """
        lists_df: pl.DataFrame = pl.read_excel(
            self.gammon_plan_workbook, sheet_name="List"
        )

        lists: dict[str, list] = {
            column: lists_df[column].drop_nulls().to_list()
            for column in lists_df.columns
        }

        return lists
