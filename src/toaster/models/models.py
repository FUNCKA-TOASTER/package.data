"""Module "BaseModel".

File:
    models.py

About:
    File describing SQLAlchemy table models.
"""

from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy.dialects.mysql import (
    TINYINT,
    BIGINT,
    INTEGER,
    VARCHAR,
    DATETIME,
)
from toaster.enums import (
    PeerMark,
    UserPermission,
    SettingDestination,
    SettingStatus,
    LinkStatus,
    LinkType,
    StaffRole,
)
from .annotations import UUID, BPID


BaseModel = declarative_base()


class Peer(BaseModel):
    """Peer SQLA model

    Columns:
        id
        name
        mark
    """

    __tablename__ = "peers"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(VARCHAR(255))
    mark: Mapped[PeerMark]


class Permission(BaseModel):
    """Permission SQLA model

    Columns:
        bpid
        uuid
        permission
    """

    __tablename__ = "permissions"

    bpid: Mapped[BPID]
    uuid: Mapped[UUID]
    permission: Mapped[UserPermission]


class Warn(BaseModel):
    """Warn SQLA model

    Columns:
        bpid
        uuid
        points
        expired
    """

    __tablename__ = "warns"

    bpid: Mapped[BPID]
    uuid: Mapped[UUID]
    points: Mapped[int] = mapped_column(TINYINT(10))
    expired: Mapped[datetime] = mapped_column(DATETIME)


class Session(BaseModel):
    """Session SQLA model

    Columns:
        bpid
        cmid
        expired
    """

    __tablename__ = "sessions"

    bpid: Mapped[BPID]
    cmid: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    expired: Mapped[datetime] = mapped_column(DATETIME)


class Queue(BaseModel):
    """Queue SQLA model

    Columns:
        bpid
        uuid
        expired
    """

    __tablename__ = "queue"

    bpid: Mapped[BPID]
    uuid: Mapped[UUID]
    expired: Mapped[datetime] = mapped_column(DATETIME)


# Таблицы настроект узлов
class Setting(BaseModel):
    """Setting SQLA model

    Columns:
        bpid
        name
        status
        destination
        points
    """

    __tablename__ = "settings"

    bpid: Mapped[BPID]
    name: Mapped[str] = mapped_column(VARCHAR(30), primary_key=True)
    status: Mapped[SettingStatus]
    destination: Mapped[SettingDestination]
    points: Mapped[int] = mapped_column(TINYINT(10))


class Curse(BaseModel):
    """Cursed SQLA model

    Columns:
        bpid
        word
    """

    __tablename__ = "cursed"

    bpid: Mapped[BPID]
    word: Mapped[str] = mapped_column(VARCHAR(40), primary_key=True)


class Delay(BaseModel):
    """Delay SQLA model

    Columns:
        bpid
        setting
        delay
    """

    __tablename__ = "delays"

    bpid: Mapped[BPID]
    setting: Mapped[str] = mapped_column(VARCHAR(30), primary_key=True)
    delay: Mapped[int] = mapped_column(INTEGER)


class Link(BaseModel):
    """Link SQLA model

    Columns:
        bpid
        type
        pattern
        status
    """

    __tablename__ = "links"

    bpid: Mapped[BPID]
    type: Mapped[LinkType] = mapped_column(primary_key=True)
    pattern: Mapped[str] = mapped_column(VARCHAR(255), primary_key=True)
    status: Mapped[LinkStatus]


class Staff(BaseModel):
    """Staff SQLA model

    Columns:
        uuid
        role
    """

    __tablename__ = "staff"

    uuid: Mapped[UUID]
    role: Mapped[StaffRole]
