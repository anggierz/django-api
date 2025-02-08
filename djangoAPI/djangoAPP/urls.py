from django.urls import path
from .views import get_users, get_user_by_id, create_user, update_user, delete_user, get_artist_top_tracks, search_item


urlpatterns = [
     path('users/', get_users, name='get-users'),
     path('users/<int:id>', get_user_by_id, name='get-user-by-id'),
     path('users/create/', create_user, name='create-user'),
     path('users/update/<int:id>', update_user, name='update-user'),
     path('users/delete/<int:id>', delete_user, name='delete-user'),
     path('spotify/artist-top-tracks/<str:artist>', get_artist_top_tracks, name='get-artist-top-tracks'),
     path('spotify/search/<str:item>/<str:type>', search_item, name='search-item')  
]