import os
from app import app
# from test import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))