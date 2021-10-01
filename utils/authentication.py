from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


ROLE_ADMIN = 0
ROLE_USER = 0

@auth.verify_password
def verify(username, password):
    return username == "admin" and password == "admin"
