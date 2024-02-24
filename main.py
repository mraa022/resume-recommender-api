from flask import Flask,request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)

class RecommendResume(Resource):
    def get(self):
        request_data = request.get_json()
        resumes = request_data['resumes']
        resume_ids = [x['_id'] for x in resumes]
        
        return resume_ids

    
api.add_resource(RecommendResume, '/')

if __name__ == '__main__':
    app.run()