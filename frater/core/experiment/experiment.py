from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Experiment:
    name: str = ''
    experiment_id: str = field(default_factory=lambda: str(uuid4()))
