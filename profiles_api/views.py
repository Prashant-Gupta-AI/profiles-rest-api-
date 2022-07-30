from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, delete)',
            'is similar to a traiditionale Django Views',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
