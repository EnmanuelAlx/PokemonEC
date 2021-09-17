# Description
Django project with Django Rest Framework and Docker to know any Pokemon evolution chain 

# Entornos 
## Local
To run it in local mode  
_SETTINGS=local docker-compose -f local.yml up --build_

## Test
To run it in test mode  
_SETTINGS=test docker-compose -f local.yml up --build_
To run the test you need to get inside the app container and go the test path and run it  
 _pytest_

## Production
To run it in production mode  
_SETTINGS=production docker-compose -f production.yml up --build_


# Endpoint
To get the Pokemon evolution chain you need to execute the project and put it in the browser url:  
_http://localhost:8000/evolution-chain/{pokemon_name}_