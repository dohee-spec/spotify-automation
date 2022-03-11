import requests
import base64
from secrets import *

# Base64 Encode Client ID and Client Secret
def get_accessToken(client_id, client_secret, refresh_token):
    message = f"{client_id}:{client_secret}"
    message_bytes = message.encode()
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode()

    data = {
        "grant_type": "refresh_token", 
        "refresh_token": refresh_token
    }

    headers = {
        "Authorization": "Basic " + base64_message
    }

    r = requests.post("https://accounts.spotify.com/api/token", data = data, headers = headers)

    responseObject = r.json()
    #print(json.dumps(responseObject, indent=2))

    access_token = responseObject['access_token']

    return access_token

access_token_recent = get_accessToken(CLIENTID, CLIENTSECRET, REFRESHTOKEN)

#print(token)