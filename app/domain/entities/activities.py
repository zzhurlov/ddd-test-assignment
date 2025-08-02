from dataclasses import dataclass, field
from uuid import uuid4

from app.domain.values.activities import ActivityTitle


@dataclass
class Activity:
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    title: ActivityTitle
