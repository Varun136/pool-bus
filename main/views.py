from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.db.models import Q
from .serailizers import SearchRoutesSerializer, StopListSerialziers
from rest_framework.response import Response
from .models import Route, Stop

class SearchRoutesView(APIView):
    """List the most optimal routes for the user from origin to destination. """

    def get(self, request):
        serializer = SearchRoutesSerializer(data=request.data)
        serializer.is_valid()
        origin = serializer.data.get("origin_stop")
        destination = serializer.data.get("destination_stop")

        origin_routes = Route.objects.filter(stop__name=origin)
        destination_routes = Route.objects.filter(stop__name=destination)
        
        return Response({}, 200)


class ListStopView(ListAPIView):
    """ Lists all the stops available in the system. """

    queryset = Stop.objects.all()
    serializer_class = StopListSerialziers

