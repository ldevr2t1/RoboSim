from nose.tools import assert_true
import requests
import json

def test_problems_post():
    """
    A 200 code is returned from a POST request to create a new problem
    """
    data = {"test": "test"}
    response = requests.post('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/',json=data)
    assert(response.ok)

def test_problems_get():
    """
    A 200 code is returned from a GET request for all problems
    """
    response = requests.get('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/')
    assert(response.ok)

def test_problems_get_by_id():
    """
    A 200 code is returned from a GET request for a valid problem id
    """
    data = {"test": "test"}
    response = requests.post('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/',json=data)

    response = requests.get('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/id=' + str(response.text).rstrip() + '/')
    assert(response.ok)

def test_problems_get_by_id_404():
    """
    A 404 code is returned from a GET request for an invalid problem id
    """
    response = requests.get('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/id=-1/')
    assert(response.status_code == 404)
    
def test_problems_put_update():
    """
    A 200 code is returned from a PUT update request for a valid problem id
    """
    data = {"test": "test"}
    response = requests.post('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/',json=data)

    data = {"new test": "new test"}
    response = requests.put('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/id=' + str(response.text).rstrip() + '/',json=data)
    assert(response.ok)

def test_problems_put_update_404_problem():
    """
    A 404 code is returned from a PUT update request for an invalid problem id
    """
    data = {"test": "test"}
    response = requests.put('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/id=-1/',json=data)
    assert(response.status_code == 404)

def test_problems_delete():
    """
    A 200 code is returned from a DELETE request for a valid problem id
    """
    data = {"test": "test"}
    response = requests.post('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/',json=data)

    response = requests.delete('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/id=' + str(response.text).rstrip() + '/')
    assert(response.ok)

def test_problems_delete_problem_404():
    """ 
    A 404 code is returned from a DELETE request for an invalid problem id
    """
    response = requests.delete('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/id=-1/')
    assert(response.status_code == 404)

def test_problems_multiple_operations():
    """ 
    We will run through a post, put, get, and then delete operation
	  The responses should be 200 200 200 200 400    
    """

    data = {"test": "test"}
    response = requests.post('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/',json=data)
    response_is_ok = response.ok
    
    id = str(response.text).rstrip()

    data = {"new test": "new test"}
    response = requests.put('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/id=' + id + '/',json=data)
    response_is_ok = response_is_ok and response.ok

    response = requests.get('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/id=' + id + '/')
    response_is_ok = response_is_ok and response.ok

    response = requests.delete('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/id=' + id + '/')
    response_is_ok = response_is_ok and response.ok

    response = requests.delete('http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/id=' + id + '/')
    response_is_ok = response_is_ok and (response.status_code == 404)

    assert(response_is_ok)