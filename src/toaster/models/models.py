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

    :param BIGINT id: Peer ID.
    :param VARCHAR(255) name: The name of the peer.
    :param PeerMark mark: Peer mark.
    """

    __tablename__ = "peers"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(VARCHAR(255))
    mark: Mapped[PeerMark]


class Permission(BaseModel):
    """Permission SQLA model

    :param BPID bpid: Bot peer ID.
    :param UUID uuid: Unique user ID.
    :param UserPermission permission: User permission.
    """

    __tablename__ = "permissions"

    bpid: Mapped[BPID]
    uuid: Mapped[UUID]
    permission: Mapped[UserPermission]


class Warn(BaseModel):
    """Warn SQLA model

    :param BPID bpid: Bot peer ID.
    :param UUID uuid: Unique user ID.
    :param TINYINT(10) points: User warn points.
    :param DATETIME expired: Expiration date of warn points.
    """

    __tablename__ = "warns"

    bpid: Mapped[BPID]
    uuid: Mapped[UUID]
    points: Mapped[int] = mapped_column(TINYINT(10))
    expired: Mapped[datetime] = mapped_column(DATETIME)


class Session(BaseModel):
    """Session SQLA model

    :param BPID bpid: Bot peer ID.
    :param BIGINT cmid: Conversation message ID.
    :param DATETIME expired: Expiration date of session.
    """

    __tablename__ = "sessions"

    bpid: Mapped[BPID]
    cmid: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    expired: Mapped[datetime] = mapped_column(DATETIME)


class Queue(BaseModel):
    """Queue SQLA model

    :param BPID bpid: Bot peer ID.
    :param UUID uuid: Unique user ID.
    :param DATETIME expired: Expiration date of record.
    """

    __tablename__ = "queue"

    bpid: Mapped[BPID]
    uuid: Mapped[UUID]
    expired: Mapped[datetime] = mapped_column(DATETIME)


# Таблицы настроект узлов
class Setting(BaseModel):
    """Setting SQLA model

    :param BPID bpid: Bot peer ID.
    :param VARCHAR(30) name: Setting name.
    :param SettingStatus status: Setting status.
    :param SettingDestination destination: setting destination.
    :param TINYINT(10) points: Warn points for violation.
    """

    __tablename__ = "settings"

    bpid: Mapped[BPID]
    name: Mapped[str] = mapped_column(VARCHAR(30), primary_key=True)
    status: Mapped[SettingStatus]
    destination: Mapped[SettingDestination]
    points: Mapped[int] = mapped_column(TINYINT(10))


class Curse(BaseModel):
    """Cursed SQLA model

    :param BPID bpid: Bot peer ID.
    :param VARCHAR(40) word: Cursed word.
    """

    __tablename__ = "cursed"

    bpid: Mapped[BPID]
    word: Mapped[str] = mapped_column(VARCHAR(40), primary_key=True)


class Delay(BaseModel):
    """Delay SQLA model

    :param BPID bpid: Bot peer ID.
    :param VARCHAR(30) setting: Setting name.
    :param INTEGER delay: Time interval for this setting.
    """

    __tablename__ = "delays"

    bpid: Mapped[BPID]
    setting: Mapped[str] = mapped_column(VARCHAR(30), primary_key=True)
    delay: Mapped[int] = mapped_column(INTEGER)


class Link(BaseModel):
    """Link SQLA model

    :param BPID bpid: Bot peer ID.
    :param LinkType type: Link pattern type.
    :param VARCHAR(255) pattern: Link pattern.
    :param LinkStatus status: Link pattern status.
    """

    __tablename__ = "links"

    bpid: Mapped[BPID]
    type: Mapped[LinkType] = mapped_column(primary_key=True)
    pattern: Mapped[str] = mapped_column(VARCHAR(255), primary_key=True)
    status: Mapped[LinkStatus]


class Staff(BaseModel):
    """Staff SQLA model

    :param UUID uuid: Unique user ID.
    :param StaffRole role: User role.
    """

    __tablename__ = "staff"

    uuid: Mapped[UUID]
    role: Mapped[StaffRole]
