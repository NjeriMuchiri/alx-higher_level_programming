#!/usr/bin/python3
"""Script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user"""
import requests
import sys

if __name__ == '__main__':
    the_letter = {'q': ""}
    the_letter['q'] = sys.argv[1]
    the_req = requests.post('http://0.0.0.0:5000/search_user', the_letter)

    try:
        obj_json = the_req.json()
        if not obj_json:
            print("No result")
        else:
            print("[{}] {}".format(obj_json.get('id'), obj_json.get('name')))
    except ValueError:
        print("Not a Valid JSON")
