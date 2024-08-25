import os
from funcka_bots.credentials import AlchemyCredentials, AlchemySetup

SQL_ALCHEMY_SETUP = AlchemySetup(
    dialect="mysql",
    driver="pymysql",
    database=os.getenv("DATABASE"),
)

SQL_ALCHEMY_CREDS = AlchemyCredentials(
    host=os.getenv("SQL_HOST"),
    port=int(os.getenv("SQL_PORT")),
    user=os.getenv("SQL_USER"),
    pswd=os.getenv("SQL_PSWD"),
)
