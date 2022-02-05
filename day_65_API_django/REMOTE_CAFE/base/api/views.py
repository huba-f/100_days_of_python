from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Cafe
from .serializers import CafeSerializer

@api_view(['GET'])
def getRoutes(request):
	routes = [
	'GET /api',
	'GET /api/cafes',
	'get /api/cafes/:id'
	]
	return Response(routes)

@api_view(['GET'])
def get_cafes(request):
	cafes = Cafe.objects.all()
	serializer = CafeSerializer(cafes, many=True)
	return Response(serializer.data)
