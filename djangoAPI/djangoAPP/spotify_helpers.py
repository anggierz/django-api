import os
from dotenv import load_dotenv
import requests
import base64
from rest_framework.response import Response
from rest_framework import status
from typing import Dict

load_dotenv()

#Function to generate a token to call spotify endpoints       
def get_spotify_token():
    CLIENT_ID = os.getenv("SPOTIFY_DEVELOPMENT_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_DEVELOPMENT_CLIENT_SECRET")
    URL_TOKEN = os.getenv("SPOTIFY_TOKEN_URL")
    
    client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode())

    token_headers = {
        "Authorization": "Basic " + client_credentials_base64.decode(),
    }

    token_data = {
        "grant_type": "client_credentials",
    }

    req = requests.post(URL_TOKEN, data=token_data, headers=token_headers)
    
    token = req.json()
    
    return token

#Get the ID of an artist from Spotify and return the first result
def get_artist_id_by_name(artist: str, token: str):
    SPOTIFY_SEARCH = os.getenv("SPOTIFY_ENDPOINT_SEARCH")
  
    url = f"{SPOTIFY_SEARCH}?q={artist}&type=artist"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    req = requests.get(url, headers=headers)

    artist_id = req.json()['artists']['items'][0]['id']
    
    return artist_id


#Function to search for an artist top tracks. It returns 10 results
def search_artist_top_tracks(artist: str):
    SPOTIFY_ARTISTS_URL = os.getenv("SPOTIFY_ENDPOINT_ARTISTS")
    
    spotify_token = get_spotify_token()
    artist_id = get_artist_id_by_name(artist, spotify_token['access_token'])
    url = f"{SPOTIFY_ARTISTS_URL}/{artist_id}/top-tracks"
    
    headers = {
        "Authorization": f"Bearer {spotify_token['access_token']}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != status.HTTP_200_OK:
        return Response({"Error fetching data from Spotify"}, status=response.status_code)
    
    # Limpiar la respuesta
    clean_response = clean_spotify_response(response.json(), "top-tracks")
    
    return clean_response


#Generic function to search for an item in spotify. Types avaulable are: album, artist, track
def spotify_search_for_item(item: str, type: str):
    SPOTIFY_SEARCH_URL = os.getenv("SPOTIFY_ENDPOINT_SEARCH")
    
    if type not in ["album", "artist", "track"]:
        return Response({"Error": f"Invalid type: {type}. Supported types are: album, artist, track"}, status=status.HTTP_400_BAD_REQUEST)
    
    spotify_token = get_spotify_token()
    
    url = f"{SPOTIFY_SEARCH_URL}?q={item}&type={type}&limit=1"
    
    headers = {
        "Authorization": f"Bearer {spotify_token['access_token']}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != status.HTTP_200_OK:
        return Response({"Error": "Error fetching data from Spotify"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Limpiar la respuesta
    clean_response = clean_spotify_response(response.json(), type)
    
    return clean_response


# Function to clean Spotify's response
def clean_spotify_response(data: Dict, type: str):
    clean_response = []
    
    if type == "artist":
        for artist in data.get("artists", {}).get("items", []):
            clean_response.append({
                "name": artist.get("name"),
                "id": artist.get("id"),
                "spotify_url": artist.get("external_urls", {}).get("spotify")
            })
            
    elif type == "top-tracks":
        for track in data.get("tracks", []):
            clean_response.append({
                "name": track.get("name"),
                "album": track.get("album", {}).get("name"),
                "track_number": track.get("track_number"),
                "release_date": track.get("album", {}).get("release_date"),
                "spotify_url": track.get("external_urls", {}).get("spotify")
            })
    
    elif type == "track":
        for track in data.get("tracks", {}).get("items", []):
            clean_response.append({
                "name": track.get("name"),
                "artist": track.get("artists", [{}])[0].get("name"), #Solo devolvemos primer artista
                "album": track.get("album", {}).get("name"),
                "track_number": track.get("track_number"),
                "release_date": track.get("album", {}).get("release_date"),
                "spotify_url": track.get("external_urls", {}).get("spotify")
            })
    
    elif type == "album":
        for album in data.get("albums", {}).get("items", []):
            clean_response.append({
                "name": album.get("name"),
                "artist": album.get("artists", [{}])[0].get("name"), #Solo devolvemos primer artista
                "release_date": album.get("release_date"),
                "spotify_url": album.get("external_urls", {}).get("spotify")
            })
    
    else:
        return Response({"Error": f"Invalid type: {type}. Supported types are: album, artist, track"}, status=status.HTTP_400_BAD_REQUEST)
    
    return clean_response