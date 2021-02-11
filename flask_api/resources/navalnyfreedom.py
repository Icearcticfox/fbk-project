from flask_restful import Resource


class NavalnyFreedom(Resource):
    def get(self):
        return {"СВОБОДУ": "НАВАЛЬНОМУ!"}
