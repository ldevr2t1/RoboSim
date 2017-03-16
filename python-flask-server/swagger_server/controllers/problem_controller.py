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

def delete_problem(problem_id):
    """
    Delete Problem
    This removes the problem by the given ID
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: None
    """
    Firebase = firebase.FirebaseApplication('https://team1robotsim.firebaseio.com/', None)
    result = Firebase.get('/problems', 'id_' + str(problem_id))
    
    if result is None:
      return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    else:
      Firebase.delete('/problems', 'id_' + str(problem_id))
      return jsonify({"success":"Problem has been deleted"})


def get_problem(problem_id):
    """
    Problems
    Returns a specific problem 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Problem
    """
    Firebase = firebase.FirebaseApplication('https://team1robotsim.firebaseio.com/', None)
    result = Firebase.get('/problems', 'id_' + str(problem_id))
    if result is None:
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    else:
        return jsonify(result)


def update_problem(problem_id, problem):
    """
    Update the existing problem
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param problem: Problem object that needs to be updated.
    :type problem: dict | bytes

    :rtype: None
    """
    Firebase = firebase.FirebaseApplication('https://team1robotsim.firebaseio.com/', None)
    result = Firebase.get('/problems', 'id_' + str(problem_id))
    
    if connexion.request.is_json and result is not None:
        problem = Problem.from_dict(connexion.request.get_json())
        return jsonify(Firebase.put('/problems', 'id_' + str(problem_id), problem))
    else:
      return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
