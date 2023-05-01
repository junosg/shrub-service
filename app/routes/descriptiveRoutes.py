from flask import Blueprint, request
from services import descriptiveService

descriptiveRoutes = Blueprint('descriptiveRoutes', __name__)
descriptive = descriptiveService.Descriptive

@descriptiveRoutes.route('/summary', methods=['POST'])
def summary():
   return descriptive.summary(request.args.get('data'), (request.args.get('scale')))