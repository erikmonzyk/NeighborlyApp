#--------- Flask settings
SERVER_HOST = 'https://neighborlywebapp.azurewebsites.net' # Update this for the appropriate front-end website when up
#SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000
FLASK_DEBUG = True # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants

#API_URL = " https://neighborlyfunctapp.azurewebsites.net/api"

# for local host if Azure functions served locally
#API_URL = "http://localhost:7071/api/"
API_URL = "https://neighborfa.azurewebsites.net/api"
