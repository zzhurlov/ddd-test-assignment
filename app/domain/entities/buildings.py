from dataclasses import dataclass

from app.domain.entities.base import BaseEntity
from app.domain.values.buildings import Address, GeoPoint


@dataclass
class Building(BaseEntity):
    address: Address
    location: GeoPoint
