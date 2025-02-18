import datetime

SECRET_KEY = "jdnadndoknoajmdsgk"

ALGORITHM_ENCRYPTION_TOKEN = "HS256"

DATATIME_NOW = datetime.datetime.now(datetime.timezone.utc)

LIFE_ACCESS_TOKEN = DATATIME_NOW + datetime.timedelta(minutes=15)
LIFE_REFRESH_TOKEN = DATATIME_NOW + datetime.timedelta(days=7)

DATABASE_URL = "postgresql+asyncpg://admin:admin@localhost:5432/crm"