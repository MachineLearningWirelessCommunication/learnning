import requests

base_url = 'http://49.233.108.117:3000/api/v1 '


def create_topic(topic_data):
    # topic_data = {
    #     'accesstoken': '',
    #     'title': 'aaaaaaaaa',
    #     'tab': 'ask',
    #     'content': '11111111111'
    # }
    url = base_url + '/topics'
    r = requests.post(url=url, json=topic_data)
    return r


def get_token():
    return 'dsfsdfdsfsgdgfgfgfghfghdfsgg'


def topic_detail(id):
    url = base_url + 'topic' + id
    r = requests.get(url)
    return r


if __name__ == '__main__':
    topic_data = {
        'accesstoken': '',
        'title': 'aaaaaaaaa',
        'tab': 'ask',
        'content': '11111111111'
    }
    create_topic(topic_data)
