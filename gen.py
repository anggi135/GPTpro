import json

credentials = {
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "refresh_token": "your_refresh_token",
    "access_token": "",
    "token_expiry": "",
    "token_uri": "https://oauth2.googleapis.com/token",
    "user_agent": "your_app_name",
    "revoke_uri": "https://oauth2.googleapis.com/revoke",
    "id_token": None,
    "id_token_jwt": None,
    "token_response": None,
    "scopes": ["https://www.googleapis.com/auth/blogger"]
}

with open('credential.json', 'w') as f:
    json.dump(credentials, f)
