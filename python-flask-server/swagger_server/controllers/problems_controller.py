import connexion
from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import json
from flask import jsonify
from flask_api import status
from firebase import firebase

def add_problem(problem):
    """
    Creates a new problem and returns a problemID
    
    :param problem: Problem object that needs to be updated.
    :type problem: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        problem = Problem.from_dict(connexion.request.get_json())
        #get and update the largest id
        largest_id = -1
        Firebase = firebase.FirebaseApplication('https://team1robotsim.firebaseio.com/', None)
        result = Firebase.get('/maxNum', None)
        if result is not None:
          largest_id = result
        problem_id = largest_id + 1
        
        Firebase.put('/', 'maxNum', problem_id)
      
        result = Firebase.put('/problems', 'id_' + str(problem_id), problem )
      
        return jsonify(problem_id), status.HTTP_201_CREATED
    else:
        return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE


def get_problems():
    """
    Problems
    Returns a list of all of the Problems generated. This can be an empty list. 

    :rtype: List[Problem]
    """
    Firebase = firebase.FirebaseApplication('https://team1robotsim.firebaseio.com/', None)
    result = Firebase.get('/problems', None)
    if result is None:
        return jsonify({})
    else:
        return jsonify(result)
