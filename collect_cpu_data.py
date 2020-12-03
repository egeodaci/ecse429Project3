from multiprocessing import Process
import requests
import psutil
import os
import random
import string
import time

def random_title(length):
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for i in range(length))
    return name
apiURL = 'http://localhost:4567/'



def post_todo():
    apiURL = 'http://localhost:4567/'
    endpoint = 'todos'
    #result=[]
    #result2=[]
    start = time.time()
    p = psutil.Process(os.getpid())
    for i in range(10000):
        title=random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                      headers={'content-type': 'application/json'})
        #print(i)
        #print("CPU: ", psutil.cpu_percent())
        #print("CPU: ", psutil.cpu_percent(interval=None) / psutil.cpu_count())
        #print("CPU: ", p.cpu_percent() / psutil.cpu_count())
        #finish =  time.time() - start
        #result.append([p.cpu_percent(interval=0.001)])
        #result2.append([finish])
    endtime = time.time() - start
    print('Total runtime is ' , endtime , 'seconds')

    #plt.plot(result2,result)
    #plt.show()

def delete_todo():
    endpoint = 'todos'
    start = time.time()
    for i in range(10000):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.delete(apiURL + endpoint + '/' + new_id)
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')



def modify_todo():
    endpoint = 'todos'
    start = time.time()
    for i in range(10000):

        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.post(apiURL + endpoint + '/' + new_id, json={"title": 'New Title',
                                        "description": 'Project Description Changed'},
                                 headers={'content-type': 'application/json'})

    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')
def post_project():
    endpoint = 'projects'
    start = time.time()
    for i in range(10000):
        title=random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                      headers={'content-type': 'application/json'})
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')



def delete_project():
    endpoint = 'projects'
    start = time.time()

    for i in range(10000):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.delete(apiURL + endpoint + '/' + new_id)
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')


def modify_project():
    endpoint = 'projects'
    start = time.time()
    for i in range(10000):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.post(apiURL + endpoint + '/' + new_id, json={"title": 'New Title',
                                                    "description": 'Project Description Changed'},
                                 headers={'content-type': 'application/json'})
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')

def post_categories():
    endpoint = 'categories'
    start = time.time()
    for i in range(10000):
        title=random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                      headers={'content-type': 'application/json'})
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')


def delete_categories():
    endpoint = 'categories'
    start = time.time()

    for i in range(10000):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.delete(apiURL + endpoint + '/' + new_id)
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')

def modify_categories():
    endpoint = 'categories'
    start = time.time()
    for i in range(10000):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.post(apiURL + endpoint + '/' + new_id, json={"title": 'New Title',
                                        "description": 'Category Has been Changed'},
                                 headers={'content-type': 'application/json'})
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')

if __name__ == "__main__":
    p1 = Process(target=modify_project())
    p1.start()