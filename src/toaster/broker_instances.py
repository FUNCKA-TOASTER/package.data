from funcka_bots.broker import Broker
from .config import BROKER_CREDENTIALS

if BROKER_CREDENTIALS:
    broker = Broker(creds=BROKER_CREDENTIALS)

else:
    broker = None
