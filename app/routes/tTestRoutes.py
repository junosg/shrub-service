from flask import Blueprint, request
from services import tTestService

tTestRoutes = Blueprint('tTestRoutes', __name__)
tTest = tTestService.TTest

@tTestRoutes.route('/oneSampleTTest', methods=['POST'])
def oneSampleTTest():
   return tTest.oneSample(request.args.get('numericData'), request.args.get('popMean'), request.args.get('alternative'))

@tTestRoutes.route('/indSamplesTTest', methods=['POST'])
def indSamplesTTest():
   return tTest.independent(request.args.get('categoricalData'), request.args.get('numericData'), request.args.get('categories'), request.args.get('equalVariance'), request.args.get('alternative'))

@tTestRoutes.route('/pairedSamplesTTest', methods=['POST'])
def pairedSamplesTTest():
   return tTest.paired(request.args.get('preNumericData'), request.args.get('postNumericData'), request.args.get('alternative'))