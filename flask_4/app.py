import json

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

STAFF = [
    {
        'Name': 'name_1',
        'PassportID': 'PassportID_1',
        'Position': 'Position_1',
        'Salary': 'Salary_1'
    },
    {
        'Name': 'name_2',
        'PassportID': 'PassportID_2',
        'Position': 'Position_2',
        'Salary': 'Salary_2'
    },
    {
        'Name': 'name_3',
        'PassportID': 'PassportID_3',
        'Position': 'Position_3',
        'Salary': 'Salary_3'
    }
]


class Staff(Resource):
    def get(self):
        result = dict()
        for i, elem in enumerate(STAFF):
            result[i] = elem
        return result, 200

    def patch(self):
        data = json.loads(request.data)
        print(data)

    def delete(self):
        pass


api.add_resource(Staff, '/staff')

if __name__ == "__main__":
    app.run(debug=True)
