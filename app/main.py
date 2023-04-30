from flask import Flask, jsonify, request
import services.descriptiveService
import services.tTestService

app = Flask(__name__)

descriptive = services.descriptiveService.Descriptive
tTest = services.tTestService.TTest

@app.route('/summary', methods=['POST'])
def summary():
   return descriptive.summary(request.args.get('data'), (request.args.get('scale')))

@app.route('/oneSampleTTest', methods=['POST'])
def oneSampleTTest():
   return tTest.oneSample(request.args.get('data'), request.args.get('popMean'), request.args.get('alternative'))

@app.route('/indSampleTTest', methods=['POST'])
def indSampleTTest():
   return tTest.independent(request.args.get('groupsValues'), request.args.get('dataValues'), request.args.get('groups'), request.args.get('equalVariance'), request.args.get('alternative'))

@app.route('/pairedSampleTTest', methods=['POST'])
def pairedSampleTTest():
   return tTest.paired(request.args.get('preDataValues'), request.args.get('postDataValues'), request.args.get('alternative'))

@app.route('/')
def hello_world():
   return "test"

if __name__ == '__main__':
   app.run()