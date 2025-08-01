from dataclasses import dataclass, field
from uuid import uuid4

from app.domain.values.buildings import Address, GeoPoint


@dataclass
class Building:
    oid: str = field(
        default_factory=str(uuid4()),
        kw_only=True,
    )
    address: Address
    location: GeoPoint
