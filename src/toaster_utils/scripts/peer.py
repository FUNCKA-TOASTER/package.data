"""Module "scripts".

File:
    peer.py

About:
    File describing custom SQLA scripts associated
    with the peer.
"""

from typing import Optional, List
from sqlalchemy.orm import Session
from toaster.database import script
from toaster_utils.models import Peer
from toaster_utils.enums import PeerMark


@script(auto_commit=False, debug=True)
def get_peer_mark(session: Session, bpid: int) -> Optional[PeerMark]:
    peer = session.get(Peer, {"id": bpid})
    return peer.mark if peer else None


@script(auto_commit=False, debug=True)
def set_peer_mark(session: Session, mark: PeerMark, bpid: int, name: str) -> None:
    new_peer = Peer(
        id=bpid,
        name=name,
        mark=mark,
    )
    session.add(new_peer)
    session.commit()


@script(auto_commit=False, debug=True)
def update_peer_data(session: Session, bpid: int, name: str) -> None:
    peer = session.get(Peer, {"id": bpid})
    peer.name = name
    session.commit()


@script(auto_commit=False, debug=True)
def drop_peer_mark(session: Session, bpid: int) -> None:
    peer = session.get(Peer, {"id": bpid})
    session.delete(peer)
    session.commit()


@script(auto_commit=False, debug=True)
def get_log_peers(session: Session) -> List[int]:
    peers = session.query(Peer).filter(Peer.mark == PeerMark.LOG).all()
    return [peer.id for peer in peers]
