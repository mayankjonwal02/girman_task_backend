from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from girman_app.serializer import UserDataSerializer
from girman_app.DB import insert_data , get_all_data


# Create your views here.
def home(request):
    return HttpResponse("Hello from Mayank Jonwal.")

class UserDataAPI(APIView):
    def get(self, request):
        # Handle GET request
        data = get_all_data()
        return Response({"message": "data retrieved", "data": data }, status=status.HTTP_200_OK)

    def post(self, request):
        # Handle POST request
        data = request.data
        serializer = UserDataSerializer(data=data)
        if serializer.is_valid():
            inserted_data = insert_data(data)
            if not inserted_data:
                return Response({"message": "Data not inserted"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({"message": "Data inserted", "data": inserted_data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

