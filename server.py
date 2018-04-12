from flask import Flask, request
from flask_restful import Resource, Api
from optimize import optimize_blocks

app = Flask(__name__)
api = Api(app)

class GetPose(Resource):
    def post(self):
        env_configs = request.get_json()
        return optimize_blocks(env_configs)

api.add_resource(GetPose, '/getpose')

if __name__ == '__main__':
    app.run(debug=True)