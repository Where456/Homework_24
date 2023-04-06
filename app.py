import os
from utils import filters
from typing import Dict
from flask_restx import Resource, Namespace, Api
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

data_ns = Namespace('perform_query')
api = Api(app)
api.add_namespace(data_ns)


@data_ns.route("/")
class PerformQuery(Resource):
    def post(self) -> Response:
        response: Dict[str, str] = request.json
        filename: str = response["file_name"]
        cmd1: str = response["cmd1"]
        value1: str = response["value1"]
        cmd2: str = response["cmd2"]
        value2: str = response["value2"]
        with open(f'data/{filename}', 'r', encoding='utf-8') as file:
            data = file.readlines()

        res = filters(file=data, cmd=cmd1, value=value1)
        res = filters(file=res, cmd=cmd2, value=value2)

        return jsonify(res)


if __name__ == "__main__":
    app.run()