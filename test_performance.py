import requests
import psutil
import os
import random
import string
import time
import pytest

def random_title(length):
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for i in range(length))
    return name

apiURL = 'http://localhost:4567/'

def test_post_todo():
    endpoint = 'todos'

    for i in range(100):

        start = time.time()
        title=random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                      headers={'content-type': 'application/json'})
        #print("CPU: ", psutil.cpu_percent())
        assert response.status_code == 201

            #print("CPU: ", psutil.cpu_percent(interval=None) / psutil.cpu_count())
            #finish= time.time()
            #result.append([psutil.cpu_percent()])
            #result2.append([finish])


    #plt.plot(result2,result)
    #plt.show()


def test_delete_todo():
    endpoint = 'todos'

    for i in range(1):
        start = time.time()
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        assert response.status_code == 201
        response_body = response.json()
        new_id = response_body["id"]
        anotherresponse = requests.delete(apiURL + endpoint + '/' + new_id)
        assert anotherresponse.status_code == 200

def test_modify_todo():
    endpoint = 'todos'
    for i in range(1):
        start = time.time()
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        assert response.status_code == 201
        response_body = response.json()
        new_id = response_body["id"]
        anotherresponse = requests.post(apiURL + endpoint + '/' + new_id, json={"title": 'New Title',
                                                                                "description": 'Project Description Changed'},
                                 headers={'content-type': 'application/json'})
        assert anotherresponse.status_code == 200


def test_post_project():
    endpoint = 'projects'

    for i in range(1):
        start = time.time()
        title=random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                      headers={'content-type': 'application/json'})
        assert response.status_code == 201

def test_delete_project():
    endpoint = 'projects'

    for i in range(1):
        start = time.time()
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        assert response.status_code == 201
        response_body = response.json()
        new_id = response_body["id"]
        anotherresponse = requests.delete(apiURL + endpoint + '/' + new_id)
        assert anotherresponse.status_code == 200



def test_modify_project():
    endpoint = 'projects'
    for i in range(1):
        start = time.time()
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        assert response.status_code == 201
        response_body = response.json()
        new_id = response_body["id"]
        anotherresponse = requests.post(apiURL + endpoint + '/' + new_id, json={"title": 'New Title',
                                                                                "description": 'Project Description Changed'},
                                 headers={'content-type': 'application/json'})
        assert anotherresponse.status_code == 200

def test_post_categories():
    endpoint = 'categories'

    for i in range(1):
        start = time.time()
        title=random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                      headers={'content-type': 'application/json'})
        assert response.status_code == 201


def test_delete_categories():
    endpoint = 'categories'

    for i in range(1):
        start = time.time()
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        assert response.status_code == 201
        response_body = response.json()
        new_id = response_body["id"]
        anotherresponse = requests.delete(apiURL + endpoint + '/' + new_id)
        assert anotherresponse.status_code == 200

def test_modify_categories():
    endpoint = 'categories'
    for i in range(1):
        start = time.time()
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        assert response.status_code == 201
        response_body = response.json()
        new_id = response_body["id"]
        anotherresponse = requests.post(apiURL + endpoint + '/' + new_id, json={"title": 'New Title',
                                                                                "description": 'Category Has been Changed'},
                                 headers={'content-type': 'application/json'})
        assert anotherresponse.status_code == 200
