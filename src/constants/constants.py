import os
from datetime import datetime
from dataclasses import dataclass

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

@dataclass
class EnvironmentVariables:
    mongo_db_url = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariables()