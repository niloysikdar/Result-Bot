import requests


def check_result(data):
    sem_no = data.split("_")[1][-1]
    url = f"https://jgec.ac.in/php/coe/results/{sem_no}/{data}.pdf"
    result = requests.get(url)
    if (result.status_code == 200):
        return True, url
    else:
        return False, url
