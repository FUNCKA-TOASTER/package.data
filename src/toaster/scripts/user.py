"""Module "scripts".

File:
    user.py

About:
    File describing custom SQLA scripts associated
    with the user.
"""

from typing import Tuple, Optional
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from toaster.models import (
    Permission,
    Staff,
    Warn,
    Queue,
    Delay,
)
from toaster.enums import StaffRole, UserPermission
from toaster import TOASTER


WarnInfo = Tuple[int, datetime]


@TOASTER.script(auto_commit=False, debug=True)
def get_user_permission(
    session: Session, uuid: int, bpid: int, ignore_staff: bool = False
) -> UserPermission:
    if not ignore_staff:
        staff = session.get(Staff, {"uuid": uuid})
        if (staff is not None) and (StaffRole.TECH == staff.role):
            return UserPermission.administrator

    user = session.get(Permission, {"uuid": uuid, "bpid": bpid})
    return user.permission if user else UserPermission.user


@TOASTER.script(auto_commit=False, debug=True)
def set_user_permission(
    session: Session, lvl: UserPermission, uuid: int, bpid: int
) -> None:
    new_user = Permission(
        bpid=bpid,
        uuid=uuid,
        permission=lvl,
    )
    session.add(new_user)
    session.commit()


@TOASTER.script(auto_commit=False, debug=True)
def update_user_permission(
    session: Session, lvl: UserPermission, uuid: int, bpid: int
) -> None:
    user = session.get(Permission, {"uuid": uuid, "bpid": bpid})
    user.permission = lvl
    session.commit()


@TOASTER.script(auto_commit=False, debug=True)
def drop_user_permission(session: Session, uuid: int, bpid: int) -> None:
    user = session.get(Permission, {"uuid": uuid, "bpid": bpid})
    session.delete(user)
    session.commit()


@TOASTER.script(auto_commit=False, debug=True)
def get_user_warns(session: Session, uuid: int, bpid: int) -> Optional[WarnInfo]:
    warn = session.get(Warn, {"bpid": bpid, "uuid": uuid})
    return (warn.points, warn.expired) if warn else None


@TOASTER.script(auto_commit=False, debug=True)
def set_user_warns(session: Session, uuid: int, bpid: int, points: int) -> None:
    warn = session.get(Warn, {"bpid": bpid, "uuid": uuid})

    zone = "_zone"
    if points > 6:
        zone = "red" + zone
    elif points > 3:
        zone = "yellow" + zone
    else:
        zone = "green" + zone

    setting = session.get(Delay, {"bpid": bpid, "setting": zone})

    if warn is not None:
        if points <= 0 or points >= 10:
            session.delete(warn)
        else:
            warn.points = points
            warn.expired = datetime.now() + timedelta(days=setting.delay)
    else:
        new_warn = Warn(
            bpid=bpid,
            uuid=uuid,
            points=points,
            expired=datetime.now() + timedelta(days=setting.delay),
        )
        session.add(new_warn)

    session.commit()


@TOASTER.script(auto_commit=False, debug=True)
def get_user_queue_status(session: Session, uuid: int, bpid: int) -> Optional[datetime]:
    queue = session.get(Queue, {"bpid": bpid, "uuid": uuid})
    return queue.expired if queue else None


@TOASTER.script(auto_commit=False, debug=True)
def insert_user_to_queue(session: Session, uuid: int, bpid: int, setting: str) -> None:
    setting = session.get(Delay, {"bpid": bpid, "setting": setting})
    delay = setting.delay if setting else 0
    expired = datetime.now() + timedelta(minutes=delay)
    new_row = Queue(bpid=bpid, uuid=uuid, expired=expired)
    session.add(new_row)
    session.commit()
