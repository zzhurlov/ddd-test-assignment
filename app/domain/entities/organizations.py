from dataclasses import dataclass, field
from uuid import uuid4

from app.domain.values.organizations import PhoneNumber, Title


@dataclass
class Organization:
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    title: Title
    phone_number: PhoneNumber
