# autoplan.py

from datetime import date, datetime


class Autoplan:
    """
    Autoplans Production jobs from planning data.
    """

    def get_element_start(self, plan_date: date, sku: str, job_number: str) -> datetime:
        """
        Get the start time of the job element defined by job_number, sku and plan_date.
        """

        raise NotImplementedError
