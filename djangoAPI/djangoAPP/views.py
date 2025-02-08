from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from .spotify_helpers import search_artist_top_tracks, spotify_search_for_item

# --------------------------- USER CRUD OPERATIONS --------------------------

#Get all users
@api_view(['GET'])
def get_users(request):
    return Response(User.objects.all(), status=status.HTTP_200_OK)

#Get User By Id
@api_view(['GET'])
def get_user_by_id(request, id):
    user = User.objects.filter(id=id)
    if not user.exists():
        return Response({'Error': f"User with id {id} not found in database"}, status=status.HTTP_404_NOT_FOUND)
    
    return Response(user, status=status.HTTP_200_OK)


#Create User
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Update User https://medium.com/@altafkhan_24475/patch-method-of-apiview-in-django-rest-framework-e7c0d574a47f
@api_view(['PATCH'])
def update_user(request, id):
    try:
        #Retrieve the item by Id 
        user_retrieved = User.objects.get(id=id) 
    except User.DoesNotExist:
        return Response({"Error": f"User with {id} not found"}, status=status.HTTP_404_NOT_FOUND)
            
     #Partially update with incoming data serializer UserSerializer(item, data-request.data, partial-True)
    serializer = UserSerializer(user_retrieved, data=request.data, partial=True)
    if serializer.is_valid():
        #Save only the fields provided 
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#Delete User
@api_view(['DELETE'])
def delete_user(request, id):
    try:
        #Retrieve the item by Id 
        user_retrieved = User.objects.get(id=id) 
    except User.DoesNotExist:
        return Response({"Error": f"User with {id} not found"}, status=status.HTTP_404_NOT_FOUND)
    
    user_retrieved.delete()
    
    return Response({"Response": f"User deletion completed successfully"}, status=status.HTTP_200_OK)


# --------------------------- SPOTIFY API ----------------------------

@api_view(['GET'])
def get_artist_top_tracks(request, artist): 
    return search_artist_top_tracks(artist)


@api_view(['GET'])
def search_item(request, item, type):
    return spotify_search_for_item(item,type)