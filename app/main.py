from flask import Flask, jsonify, request
import services.descriptiveService
import services.tTestService
from routes import tTestRoutes

app = Flask(__name__)
app.register_blueprint(tTestRoutes.tTestRoutes)

descriptive = services.descriptiveService.Descriptive

@app.route('/summary', methods=['POST'])
def summary():
   return descriptive.summary(request.args.get('data'), (request.args.get('scale')))

@app.route('/')
def hello_world():
   return "test"

if __name__ == '__main__':
   app.run()