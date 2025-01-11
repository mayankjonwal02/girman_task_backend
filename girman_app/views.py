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
    
class UserDataAPI_byname(APIView):
    def get(self, request,name):
        # Retrieve all data
        data = get_all_data()   

        # Extract 'name' query parameter
        # name = request.query_params.get('name', '').strip()
        if not name:
            return Response({"message": "Name query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Convert name to lowercase for case-insensitive comparison
        name = name.lower()

        # Filter data for matches in first_name or last_name (case-insensitive)
        matching_data = [
            record for record in data 
            if name in record.get('first_name', '').lower() or name in record.get('last_name', '').lower()
        ]

        # Check if matches are found
        if matching_data:
            return Response(
                {"message": "Data retrieved", "data": matching_data},
                status=status.HTTP_200_OK
            )

        # If no matches are found
        return Response(
            {"message": "Data not found"},
            status=status.HTTP_404_NOT_FOUND
        )


