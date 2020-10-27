import requests
from pprint import pprint
import os
def inquiry_url(TOKEN):
    HEADERS = {"Authorization": f"OAuth {TOKEN}"}
    response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                            params={"path": '/text.txt'},
                            headers=HEADERS
                            )
    return response.json()




def file_upload(name_file):
    file_patch= os.path.join(os.getcwd(),name_file)
    with open(file_patch,'rb') as f:
        resp = requests.put(inquiry_url("*****"),
                            files = {'file':f})
    return 'Вернуть ответ об успешной загрузке'
print(file_upload("yandexdisk.txt"))