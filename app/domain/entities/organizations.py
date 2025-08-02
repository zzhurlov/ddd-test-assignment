from dataclasses import dataclass, field

from app.domain.entities.activities import Activity
from app.domain.entities.base import BaseEntity
from app.domain.entities.buildings import Building
from app.domain.values.organizations import OrganizationTitle, PhoneNumber


@dataclass
class Organization(BaseEntity):
    title: OrganizationTitle
    phone_numbers: list[PhoneNumber] = field(
        default_factory=list,
        kw_only=True,
    )
    building: Building
    activity: Activity
