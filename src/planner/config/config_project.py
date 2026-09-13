# config_project.py

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class ConfigProject:
    """Project level config."""
    project_root: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2])
