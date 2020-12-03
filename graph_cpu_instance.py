from multiprocessing import Process
import requests
import psutil
import os
import random
import string
import time
import pytest
import matplotlib.pyplot as plt

def random_title(length):
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for i in range(length))
    return name
apiURL = 'http://localhost:4567/'



def post_todo():
    apiURL = 'http://localhost:4567/'
    endpoint = 'todos'
    result=[]
    result2=[]
    start = time.time()
    for i in range(10001):
        title=random_title(15)
        requests.post(apiURL + endpoint, json={"title": title},
                      headers={'content-type': 'application/json'})
        if i%500 == 0:
            print('Doing the post request at Todos' ,i , 'instances have been done')
            result.append([psutil.cpu_percent()])
            result2.append([i])
    plt.scatter(result2, result)
    plt.plot(result2, result)
    plt.ylim(0, 100)
    #plt.xticks(result2)
    plt.xlabel('Instances')
    plt.ylabel('Cpu use (%)')
    plt.title('Post request for Todo')
    plt.savefig('postTodoVideo.png')
    plt.show()

    endtime = time.time() - start
    print('Total runtime is ' , endtime , 'seconds')

    #plt.plot(result2,result)
    #plt.show()

def delete_todo():
    endpoint = 'todos'
    start = time.time()
    result=[]
    result2=[]
    for i in range(10001):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.delete(apiURL + endpoint + '/' + new_id)
        if i % 500 == 0:
            print('Doing the request' ,i , 'instances have been done')
            result.append([psutil.cpu_percent()])
            result2.append([i])
    plt.scatter(result2, result)
    plt.plot(result2, result)
    plt.ylim(0, 100)
    # plt.xticks(result2)
    plt.xlabel('Instances')
    plt.ylabel('Cpu use (%)')
    plt.title('Delete request for Todo')
    plt.savefig('deleteTodo.png')
    plt.show()
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')



def modify_todo():
    endpoint = 'todos'
    start = time.time()
    result = []
    result2 = []
    for i in range(10001):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.post(apiURL + endpoint + '/' + new_id, json={"title": 'New Title',
                                        "description": 'Project Description Changed'},
                                 headers={'content-type': 'application/json'})
        if i % 500 == 0:
            print('Doing the request', i, 'instances have been done')
            result.append([psutil.cpu_percent()])
            result2.append([i])
    plt.scatter(result2, result)
    plt.plot(result2, result)
    plt.ylim(0, 100)
    # plt.xticks(result2)
    plt.xlabel('Instances')
    plt.ylabel('Cpu use (%)')
    plt.title('Modify request for Todo')
    plt.savefig('modifyTodo.png')
    plt.show()
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')


def post_project():
    endpoint = 'projects'
    start = time.time()
    result = []
    result2 = []

    for i in range(10001):
        title=random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                      headers={'content-type': 'application/json'})
        if i % 500 == 0:
            print('Doing the request', i, 'instances have been done')
            result.append([psutil.cpu_percent()])
            result2.append([i])
    plt.scatter(result2, result)
    plt.plot(result2, result)
    plt.ylim(0, 100)
    # plt.xticks(result2)
    plt.xlabel('Instances')
    plt.ylabel('Cpu use (%)')
    plt.title('Post request for project')
    plt.savefig('postProjectInstance.png')
    plt.show()
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')




def delete_project():
    endpoint = 'projects'
    start = time.time()
    result = []
    result2 = []

    for i in range(10001):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.delete(apiURL + endpoint + '/' + new_id)
        if i % 500 == 0:
            print('Doing the request', i, 'instances have been done')
            result.append([psutil.cpu_percent()])
            result2.append([i])
    plt.scatter(result2, result)
    plt.plot(result2, result)
    plt.ylim(0, 100)
    # plt.xticks(result2)
    plt.xlabel('Instances')
    plt.ylabel('Cpu use (%)')
    plt.title('Delete request for project')
    plt.savefig('deleteProjectInstance.png')
    plt.show()
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')



def modify_project():
    endpoint = 'projects'
    start = time.time()
    result = []
    result2 = []
    for i in range(10001):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.post(apiURL + endpoint + '/' + new_id, json={"title": 'New Title',
                                                    "description": 'Project Description Changed'},
                                 headers={'content-type': 'application/json'})
        if i % 500 == 0:
            print('Doing the request', i, 'instances have been done')
            result.append([psutil.cpu_percent()])
            result2.append([i])
    plt.scatter(result2, result)
    plt.plot(result2, result)
    plt.ylim(0, 100)
    # plt.xticks(result2)
    plt.xlabel('Instances')
    plt.ylabel('Cpu use (%)')
    plt.title('Modify request for project')
    plt.savefig('modifyProjectInstance.png')
    plt.show()
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')


def post_categories():
    endpoint = 'categories'
    start = time.time()
    result = []
    result2 = []
    for i in range(10001):
        title=random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                      headers={'content-type': 'application/json'})
        if i % 500 == 0:
            print('Doing the request', i, 'instances have been done')
            result.append([psutil.cpu_percent()])
            result2.append([i])
    plt.scatter(result2, result)
    plt.plot(result2, result)
    plt.ylim(0, 100)
    # plt.xticks(result2)
    plt.xlabel('Instances')
    plt.ylabel('Cpu use (%)')
    plt.title('Post request for Category')
    plt.savefig('postCategoryInstance.png')
    plt.show()
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')



def delete_categories():
    endpoint = 'categories'
    start = time.time()
    result = []
    result2 = []

    for i in range(10001):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.delete(apiURL + endpoint + '/' + new_id)
        if i % 500 == 0:
            print('Doing the request', i, 'instances have been done')
            result.append([psutil.cpu_percent()])
            result2.append([i])
    plt.scatter(result2, result)
    plt.plot(result2, result)
    plt.ylim(0, 100)
    # plt.xticks(result2)
    plt.xlabel('Instances')
    plt.ylabel('Cpu use (%)')
    plt.title('Delete request for Category')
    plt.savefig('deleteCategoryInstance.png')
    plt.show()
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')


def modify_categories():
    endpoint = 'categories'
    start = time.time()
    result = []
    result2 = []
    for i in range(10001):
        title = random_title(15)
        response = requests.post(apiURL + endpoint, json={"title": title},
                                 headers={'content-type': 'application/json'})
        response_body = response.json()
        new_id = response_body["id"]
        requests.post(apiURL + endpoint + '/' + new_id, json={"title": 'New Title',
                                        "description": 'Category Has been Changed'},
                                 headers={'content-type': 'application/json'})
        if i % 500 == 0:
            print('Doing the request', i, 'instances have been done')
            result.append([psutil.cpu_percent()])
            result2.append([i])
    plt.scatter(result2, result)
    plt.plot(result2, result)
    plt.ylim(0, 100)
    # plt.xticks(result2)
    plt.xlabel('Instances')
    plt.ylabel('Cpu use (%)')
    plt.title('Modify request for Category')
    plt.savefig('modifyCategoryInstance.png')
    plt.show()
    endtime = time.time() - start
    print('Total runtime is ', endtime, 'seconds')


if __name__ == "__main__":
    p1 = Process(target=modify_categories())
    p1.start()