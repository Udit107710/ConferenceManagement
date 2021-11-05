# Conference Mangament System

Deployed Version: https://aviyel-conf-mgmt.herokuapp.com

Postman Collection: https://www.getpostman.com/collections/6eb678d17dd4b6c9be66

## Steps to run locally

### Create .env file
Add:
```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=db
```

### Create admin user
Use below command to create an admin user
```
flask fab create-admin
```

### Create models
Enable (create)[app/views.py#98] for db models to be created in a new db

### Run app
```
flask run app
```

### Authenticate
Use your admin user to obtain token in response and use that token for making all the requests.

## Improvements:
- Projection based GET on nested data
    - Maybe use GraphQL is this a heavy read-based app
- OpenAPI documentation for all endpoints
- Modify the seralizers and desearlizers:
    - add `count` for each key where there are multiple keys
- Error handling:
    - Enouctered errors should propograte back to user
- pagination on nested data
- Enable auditing of models
    - keep track of when and who edited which model