from __future__ import print_function
import os
import base64
from flask import Flask, jsonify, make_response
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# The scope for the OAuth2 request.
SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

# Defines a method to get an access token from the ServiceAccount object.
def get_access_token():
  return ServiceAccountCredentials.from_json_keyfile_name(
      "json-key.json", SCOPE).get_access_token().access_token

@app.route("/token")
def token():
    resp = make_response(jsonify(**{"token": get_access_token()}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    with open("json-key.json", "w") as f:
        f.write(base64.b64decode(os.environ.get("JSON_KEY")).decode('UTF-8'))
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
