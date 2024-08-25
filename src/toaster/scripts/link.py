"""Module "scripts".

File:
    url.py

About:
    File describing custom SQLA scripts associated
    with the urls.
"""

from typing import Set
from sqlalchemy.orm import Session
from toaster.models import Link
from toaster.enums import LinkStatus, LinkType
from toaster import TOASTER


@TOASTER.script(auto_commit=False, debug=True)
def insert_pattern(
    session: Session, bpid: int, type: LinkType, status: LinkStatus, pattern: str
) -> None:
    new_pattern = Link(bpid=bpid, type=type, status=status, pattern=pattern)
    session.add(new_pattern)
    session.commit()


@TOASTER.script(auto_commit=False, debug=True)
def get_patterns(
    session: Session, bpid: int, type: LinkType, status: LinkStatus
) -> Set[str]:
    rows = (
        session.query(Link)
        .filter(
            Link.bpid == bpid,
            Link.type == type,
            Link.status == status,
        )
        .all()
    )
    return {row.pattern for row in rows}
