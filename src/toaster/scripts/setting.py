"""Module "scripts".

File:
    setting.py

About:
    File describing custom SQLA scripts associated
    with the settings.
"""

from typing import Dict, Optional
from sqlalchemy.orm import Session
from toaster.models import Setting
from toaster.enums import SettingDestination, SettingStatus
from toaster import TOASTER


@TOASTER.script(auto_commit=False, debug=True)
def get_destinated_settings_status(
    session: Session, destination: SettingDestination, bpid: int
) -> Dict[str, SettingStatus]:
    settings = (
        session.query(Setting)
        .filter(
            Setting.bpid == bpid,
            Setting.destination == destination,
        )
        .all()
    )
    result = {setting.name: setting.status for setting in settings}
    return result


@TOASTER.script(auto_commit=False, debug=True)
def get_setting_status(session: Session, bpid: int, name: str) -> SettingStatus:
    setting = session.get(Setting, {"bpid": bpid, "name": name})
    return setting.status if setting else SettingStatus.inactive


@TOASTER.script(auto_commit=False, debug=True)
def get_setting_points(session: Session, bpid: int, name: str) -> Optional[int]:
    setting = session.get(Setting, {"bpid": bpid, "name": name})
    return setting.points if setting else None


@TOASTER.script(auto_commit=False, debug=True)
def update_setting_points(session: Session, bpid: int, name: str, points: int) -> None:
    setting = session.get(Setting, {"bpid": bpid, "name": name})
    setting.points = points
    session.commit()


@TOASTER.script(auto_commit=False, debug=True)
def update_setting_status(
    session: Session, status: SettingStatus, bpid: int, name: str
) -> None:
    setting = session.get(Setting, {"bpid": bpid, "name": name})
    setting.status = status
    session.commit()
