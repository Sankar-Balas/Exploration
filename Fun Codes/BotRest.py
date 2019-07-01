# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = "Wipro"
api = Api(app)

tests = []
initials = []


class AnalyzeFailure(Resource):
    def post(self):
        data = request.get_json()
        test = {"id": data["TestCase_ID"], "build": data["Build_No"],
                "description": data["Failure_Description"],
                "module": data["IN_Module"]}
        tests.append(test)
        # print(data, tests)
        if data["TestCase_ID"] and data["Build_No"] and data["Failure_Description"] and data["IN_Module"]:
            return {"message": data["TestCase_ID"]}, 200
        else:
            return {"message": "Some of the fileds are missing"}, 400


class Initialize_Bot(Resource):
    def post(self):
        data = request.get_json()
        initial = {"build": data["Build_No"], "variant": data["Variant"],
                   "regional_code": data["Regional_Code"]}
        initials.append(initial)
        # print(data, initials)
        if data["Build_No"] and data["Variant"] and data["Regional_Code"]:
            return {"Message": "S_OK"}, 200
        else:
            return {"Message": "Error has occured"}, 400


api.add_resource(AnalyzeFailure, "/analyze/")
api.add_resource(Initialize_Bot, "/inbot/")
app.run(port=8080, debug=True)
