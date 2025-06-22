import os
from dotenv import load_dotenv

load_dotenv(override=True)
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
domain_name = os.getenv("DOMAIN_NAME")