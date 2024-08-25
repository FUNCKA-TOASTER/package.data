import os
from funcka_bots.credentials import AlchemyCredentials, AlchemySetup

SQL_ALCHEMY_SETUP = AlchemySetup(
    dialect=os.getenv("alchemy_dialect"),
    driver=os.getenv("alchemy_driver"),
    database=os.getenv("alchemy_database"),
)

SQL_ALCHEMY_CREDS = AlchemyCredentials(
    host=os.getenv("sql_host"),
    port=int(os.getenv("sql_port")),
    user=os.getenv("sql_user"),
    pswd=os.getenv("sql_pswd"),
)
