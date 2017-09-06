from flask_restful import Resource, Api, reqparse

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
