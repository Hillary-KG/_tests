from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import PointsSerializer
from .functions import get_pair
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from rest_framework import status
from.models import Points


# Create your views here.
class ClosestPairView(APIView):
    """
    - POST a string of points, get closest points
    """
    def post(self, request, format=None):
        input_str = request.data['input_str']
        result = get_pair(eval(input_str))
        print(str(result[0]))
        points = ''.join(str(result[0])) + ''.join(str(result[1]))
        print(points)
        dist = ''.join(str(result[2]))

        data = {
            'input_str': input_str,
            'closest_pair': points,
            'distance': dist
        }
        serializer = PointsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ClosestPairDetail(APIView):
#     """
#     - GET the closest points given a string
#     """
#     def get(self, input_str, format=None):
#         try:
#             pair = Points.objects.get(input_str=input_str)
#             serializer = PointsSerializer(pair)
#             return JsonResponse(serializer.data, status=200)
#         except Points.DoesNotExist:
#             raise Http404
#
#     def delete(self, request, input_str, format=None):
#         try:
#             pair = Points.objects.get(input_str=input_str)
#             pair.delete()
#             return JsonResponse({'success': True}, status=200)
#         except Points.DoesNotExist:
#             raise HttpResponseBadRequest


