from flask import Flask, jsonify
from flask_restful import Api, Resource
from solver import createBoard

app = Flask(__name__)
api = Api(app)

class Bananagrams(Resource):
    def get(self, letters, extensive):
        ext = True if extensive == 'true' else False
        data = createBoard(letters, extensive=ext)
        return data

api.add_resource(Bananagrams, '/api/bananas/<string:letters>/<string:extensive>')

# Debug = True is for development environment only. Remove for production
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)

