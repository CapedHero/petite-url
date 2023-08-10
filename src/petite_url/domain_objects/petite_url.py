from dataclasses import dataclass
from datetime import datetime


@dataclass
class PetiteURL:
    target_url: str
    petite_code: str
    created_at: datetime

    def __str__(self):
        return f"{self.petite_code} -> {self.target_url}"
