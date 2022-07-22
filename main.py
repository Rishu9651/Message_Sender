
import requests

import json

def send_sms(number, message):
    url='https://www.fast2sms.com/dev/bulkV2'
    params={
        'authorization': 'RpGAcmztDh4XkrW32qJCY6uiZo0MQfLvdFOUIjTenxwsK5yN7BjkRQaLz1XU3TPw8Eu2rt7SBp4YNVFe',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number

    }
    response=requests.get(url,params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')

# send_sms("9651694997","this is text message.")