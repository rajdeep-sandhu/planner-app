# duckdb_factory.py


class DuckDBFactory:
    """
    DuckDB Factory.
    """

    def __init__(self, database: str = ":memory") -> None:
        """
        DuckDBFactory Constructor.
        """
        self._database: str = database
