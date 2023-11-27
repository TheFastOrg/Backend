from typing import List

from core.entities.business import Business
from core.interfaces.repositories.business_repository import BusinessRepository


class BusinessService:
    business_repository: BusinessRepository

    def __init__(self, business_repository: BusinessRepository):
        self.business_repository = business_repository

    def list(self) -> List[Business]:
        return self.business_repository.list()
