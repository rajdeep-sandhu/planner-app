# duckdb_factory.py
import duckdb


class DuckDBFactory:
    """
    DuckDB Factory.
    """

    def __init__(self, database: str = ":memory:") -> None:
        """DuckDBFactory Constructor."""
        self._database: str = database

    def create_connection(self) -> duckdb.DuckDBPyConnection:
        """Create a DuckDB connection."""
        return duckdb.connect(self._database)
