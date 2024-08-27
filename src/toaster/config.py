import os
from funcka_bots.credentials import (
    AlchemyCredentials,
    AlchemySetup,
    RabbitMQCredentials,
)

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


BROKER_CREDENTIALS = RabbitMQCredentials(
    host=os.getenv("rabbitmq_host"),
    port=os.getenv("rabbitmq_port"),
    vhost=os.getenv("rabbitmq_vhost"),
    user=os.getenv("rabbitmq_user"),
    pswd=os.getenv("rabbitmq_pswd"),
)
