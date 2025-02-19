import pyautogui
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()

SENHA_NOTION = os.getenv("SENHA_NOTION")
SENHA_GOOGLE = os.getenv("SENHA_GOOGLE")