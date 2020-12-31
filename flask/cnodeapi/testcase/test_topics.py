import requests
import business.common as common

base_url = 'http://49.233.108.117:3000/api/v1'


def test_topic_index_page():
    query_params = {
        'page': 1,
        'tab': 'ask',
        'limit': 1,
        'mdrender': 'false'
    }
    r = requests.get(base_url + '/topics', params=query_params)
    assert r.status_code == 200
    assert r.json()['success'] == True
    data = r.json()['data']
    assert len(data) == query_params['limit']
    for topic in data:
        assert topic['tab'] == query_params['tab']


def test_create_topic():
    topic_data = {
        'accesstoken': common.get_token(),
        'title': 'aaaaaaaaa',
        'tab': 'ask',
        'content': '11111111111'
    }
    r = common.create_topic(topic_data)
    assert r.status_code == 200
    assert r.json()['success'] == True
    r2 = common.create_topic(topic_data)
    assert r.json()['topic_id'] != r2.json()['topic_id']


def test_topic_update():
    topic_data = {
        'accesstoken': common.get_token(),
        'title': 'aaaaaaaaa',
        'tab': 'ask',
        'content': '11111111111'
    }
    r = common.create_topic(topic_data)
    id = r.json()['topic_id']
    update_topic_data = {
        'accesstoken': common.get_token(),
        'topic_id': id,
        'title': 'aaaaaaaa111111111111',
        'tab': 'ask',
        'content': '11111111111aaaaaaaaaaaaa'
    }
    r = requests.post(base_url + '/topic/update', update_topic_data)
    assert r.json() == id
    r_detail = common.topic_detail(id)
    assert r_detail.json()['data']['id'] == id
    assert r_detail.json()['data']['tab'] == update_topic_data['tab']
    assert r_detail.json()['data']['title'] == update_topic_data['title']
    assert update_topic_data['content'] in r_detail.json()['data']['content']


if __name__ == '__main__':
    test_topic_index_page()
