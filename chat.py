"""

$ python3 chat.py 
{'predictions': [{'length': 10, 'tokens': ['<S1>', '你', '好', '啊', '</S1>', '<S2>', '你', '好', '哇', '</S2>', '</s>']}]}
# python3 chat.py 
{'predictions': [{'tokens': ['<S1>', '你', '好', '啊', '</S1>', '<S2>', '你', '好', '呀', '！', '</S2>', '</s>'], 'length': 11}]}
$ python3 chat.py 
{'predictions': [{'length': 10, 'tokens': ['<S1>', '你', '好', '啊', '</S1>', '<S2>', '不', '要', '脸', '</S2>', '</s>']}]}
$ python3 chat.py 
{'predictions': [{'tokens': ['<S1>', '你', '好', '啊', '</S1>', '<S2>', '你', '好', '啊', '</S2>', '<S1>', '我', '叫', '你', '一', '声', '你', '敢', '答', '应', '吗', '</S1>', '</s>'], 'length': 22}]}


"""

import re
import requests


def chat(text, SERVER_URL='http://localhost:8501/v1/models/chat:predict'):
    r = requests.post(SERVER_URL, json={
        'instances': [{
            'tokens': ['<S1>'] + list(text) + ['</S1>', '<S2>'],
            'length': len(text) + 3
        }]
    })
    return r.json()


if __name__ == '__main__':
    print(chat('你好啊'))

