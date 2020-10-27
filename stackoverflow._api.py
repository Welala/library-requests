import requests
from datetime import datetime
LINK_STACK = 'https://api.stackexchange.com/2.2/questions?fromdate=1603411200&order=desc&sort=activity&tagged=python&site=stackoverflow'
def output_questions(link):
    response = requests.get(link)
    return response.json()['items']


def output_titles(questions):
    all_titles = ''
    for title in questions:
        all_titles += f'Вопрос с заголовком {title["title"]}  был создан {datetime.fromtimestamp(title["creation_date"])} \n'
    return all_titles

print(output_titles(output_questions(LINK_STACK)))