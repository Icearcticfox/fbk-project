from flask import Flask, request
from flask_restful import Resource, Api
from action import Action

app = Flask(__name__)
api = Api(app)


class NavalnyFreedom(Resource):
    def get(self):
        return {'СВОБОДУ': 'НАВАЛЬНОМУ!'}


class Upload(Resource):
    def post(self):
        data = request.get_json()
        if data is None:
            return {'error': 'Missing input'}, 400
        else:
            transaction = Action().transaction_insert(data)
            response_data = {
                "result": transaction["result"],
                "sucess": transaction["success"],
                "status_code": 200,
            }
            return response_data


api.add_resource(NavalnyFreedom, '/')
api.add_resource(Upload, '/api/v1/upload')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5090)
    #app.run(host="0.0.0.0", port=7090)
