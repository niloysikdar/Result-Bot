import requests
import time
import os
from dotenv import load_dotenv
from check_result import check_result

load_dotenv()
webhook_url = os.getenv("WEBHOOK_URL")

while (True):
    result, url = check_result("CSE_SEM3_19101104001")
    if (result):
        data = {"content": "Hey @everyone, the results for SEM3 are available now. \nYou can also request the results by messaging : !result <department>_SEM<sem_number>_<roll_number> \nExample: !result CSE_SEM3_19101104001"}
        response = requests.post(webhook_url, json=data)
        break
    time.sleep(60)
