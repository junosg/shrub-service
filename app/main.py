from flask import Flask, jsonify, request
import services.descriptiveService
import services.tTestService
from routes import tTestRoutes
from routes import descriptiveRoutes

app = Flask(__name__)
app.register_blueprint(tTestRoutes.tTestRoutes)
app.register_blueprint(descriptiveRoutes.descriptiveRoutes)

@app.route('/')
def hello_world():
   return "test"

if __name__ == '__main__':
   app.run()