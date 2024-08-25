"""Module "enums".

File:
    enums.py

About:
    File describing enums describing the data types
    of SQLAlchemy table columns.
"""

from enum import Enum


class PeerMark(Enum):
    """Description of peer mark types.

    :param CHAT: Value `str`(`CHAT`)
    :param LOG: Value `str`(`LOG`)
    """

    CHAT = "CHAT"
    LOG = "LOG"


class UserPermission(Enum):
    """Description of user access lvls.

    :param user: Value `int`(`0`)
    :param moderator: Value `int`(`1`)
    :param administrator: Value `int`(`2`)
    """

    user = 0
    moderator = 1
    administrator = 2


class SettingStatus(Enum):
    """Description of setting status.

    :param inactive: Value `bool`(`False`)
    :param active: Value `bool`(`True`)
    """

    inactive = False
    active = True


class SettingDestination(Enum):
    """Description of setting destinations.

    :param filter: Value `str`(`filter`)
    :param system: Value `str`(`system`)
    """

    filter = "filter"
    system = "system"


class LinkType(Enum):
    """Description of link types.

    :param domain: Value `str`(`domain`)
    :param url: Value `str`(`link`)
    """

    domain = "domain"
    link = "link"


class LinkStatus(Enum):
    """Description of link status.

    :param forbidden: Value `str`(`forbidden`)
    :param allowed: Value `str`(`allowed`)
    """

    forbidden = "forbidden"
    allowed = "allowed"


class StaffRole(Enum):
    """Description of user staff roles.

    :param ADM: Value `str`(`ADM`)
    :param TECH: Value `str`(`TECH`)
    :param SYS: Value `str`(`SYS`)
    """

    TECH = "TECH"
    # Below are the legacy attributes
    ADM = "ADM"
    SYS = "SYS"
