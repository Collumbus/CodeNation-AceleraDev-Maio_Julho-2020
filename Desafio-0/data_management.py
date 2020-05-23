import json
import requests

token = ''
params = {'token': token}


def get_data():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
    re = requests.get(url, params=params)
    data = json.loads(re.content)
    return data


def save_data(data):
    with open('Desafio-0/answer.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def post_file():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution'
    answer = {'answer': open('answer.json', 'rb')}
    re = requests.post(url, files=answer, params=params)
    print(re.status_code)
    print(re.text)
    print(re.raise_for_status())
