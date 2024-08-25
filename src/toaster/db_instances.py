from funcka_bots.database import SyncDB, build_connection_uri
from .config import SQL_ALCHEMY_SETUP, SQL_ALCHEMY_CREDS

TOASTER = SyncDB(
    connection_uri=build_connection_uri(
        creds=SQL_ALCHEMY_CREDS,
        setup=SQL_ALCHEMY_SETUP,
    ),
    debug=False,
)
