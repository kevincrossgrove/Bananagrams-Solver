from flask import Flask
from flask_restful import Api, Resource
from solver import createBoard

app = Flask(__name__)
api = Api(app)

class Bananagrams(Resource):
    def get(self, letters):
        print('Hello')
        data = createBoard(letters)
        return data

api.add_resource(Bananagrams, '/api/bananas/<string:letters>')

# Debug = True is for development environment only. Remove for production
if __name__ == "__main__":
    app.run(debug=True)

