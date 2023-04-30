from flask import Blueprint, request
from services import tTestService

tTestRoutes = Blueprint('tTestRoutes', __name__)
tTest = tTestService.TTest

@tTestRoutes.route('/oneSampleTTest', methods=['POST'])
def oneSampleTTest():
   return tTest.oneSample(request.args.get('data'), request.args.get('popMean'), request.args.get('alternative'))

@tTestRoutes.route('/indSampleTTest', methods=['POST'])
def indSampleTTest():
   return tTest.independent(request.args.get('groupsValues'), request.args.get('dataValues'), request.args.get('groups'), request.args.get('equalVariance'), request.args.get('alternative'))

@tTestRoutes.route('/pairedSampleTTest', methods=['POST'])
def pairedSampleTTest():
   return tTest.paired(request.args.get('preDataValues'), request.args.get('postDataValues'), request.args.get('alternative'))