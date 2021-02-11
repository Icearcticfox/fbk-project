from app import app, conn
from flask_restful import Api
from resources.navalnyfreedom import NavalnyFreedom
from resources.upload import Upload

api = Api(app)

api.add_resource(NavalnyFreedom, "/")
api.add_resource(Upload, "/api/v1/upload")
