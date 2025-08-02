from dataclasses import dataclass, field
from uuid import uuid4

from app.domain.entities.activities import Activity
from app.domain.entities.buildings import Building
from app.domain.values.organizations import OrganizationTitle, PhoneNumber


@dataclass
class Organization:
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    title: OrganizationTitle
    phone_numbers: list[PhoneNumber]
    building: Building
    activity: Activity
