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

### Create models
Enable (create)[https://github.com/Udit107710/ConferenceManagement/blob/0d73a0970e3a7da5f0ff7ce849e8a4c431c3098e/app/views.py#L98] for db models to be created in a new db


### Docker Compose
```
docker-compose up
```

### Create admin user
After the constainer is up. Run below command inside the container
```
flask fab create-admin
```


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