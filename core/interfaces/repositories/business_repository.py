from abc import ABC, abstractmethod
from typing import List

from core.entities.business import Business


class BusinessRepository(ABC):
    @abstractmethod
    def list(self) -> List[Business]:
        raise NotImplementedError
