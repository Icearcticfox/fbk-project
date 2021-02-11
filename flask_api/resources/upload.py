from actions.dbaction import Action
from app import conn
from flask import request
from flask_restful import Resource


class Upload(Resource):
    def post(self):
        data = request.get_json()
        if data is None:
            response_data = {
                "error": "Missing input",
                "status_code": 400,
            }
            return response_data
        else:
            transaction = Action().transaction_insert(conn, data)
            response_data = {
                "result": transaction["result"],
                "success": transaction["success"],
                "status_code": 200,
            }
            return response_data
