import os
from dotenv import load_dotenv, find_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

SECRET_KEY = os.getenv("SECRET_KEY")