# Backend Engineer test
For this exercise, we want to create two basic web services. Both of them will expose a minimalistic REST API that exposes the needed operations on the models. One service will be in charge of managing users and to authenticate users. It will expose the needed endpoints for registering a new user and to login with a valid user. The second service will expose an endpoint that just will say hello by using its names for the users if it is already registered and logged within the first service.


* We are asking for a simple but a complete solution.
* We expect that both services expose a minimal HTTP interface but we recommend to avoid direct communication between the services.
* You can use the frameworks and libraries you think you need and you feel more comfortable with but remember, keep it simple.
* If you need persistence, you can use SQLite or even to write in disc. We don’t expect to have the data distributed or services replicated.
* We recommend using docker-compose or/and Helm Charts.
* Even if there are a few lines of code, please, test it.

---

## API Auth

Auth API based on Django and Django Rest Framework (DRF)

## Introduction

I have chosen to use these technologies to emulate as much as possible a functional project to be deployed in production.

This API is the first I've done at user authentication level, previously I worked on a Java Rest API where JWT bearer token was already used, so I decided to use the same concept / solution.

I'm sure you will find bugs or things to improve, I'm open to learn and improve as much as possible.

## Requeriments

Development:
* Django
* DRF
    * DRF Auth
    * DRF JWT
    
DevOps:
* BBDD:
    * SQLite3
* Deployment:
    * Docker
    * Docker Compose
* Testing:
    * Curl
    * Postman (Collection and Environment included)
    * Django Test
    * DRF


## Docker services for deployment
```bash
docker-compose run web
docker-compose run web_migrate
docker-compose run web_run
```

## Demostration 

First service, manage users and auth them

Need endpoinds to ...

* Register new user:

Example:

```bash
curl --location --request POST 'http://localhost:8000/api/users/' \
--header 'Authorization: Bearer {{token_admin}}' \
--header 'Cookie: csrftoken=sptVHJ1EEEE7GF5q3frGrLRGpz1Wl0B4ktlHxUA3URyNtCU96jSSZbygPTsEfZXm; sessionid=po7046e0dn15mz9uqzx8eacpxjr9ry42' \
--form 'email="test3@test3.com"' \
--form 'firstname="test3"' \
--form 'lastname="test3"' \
--form 'password="test3"' \
--form 'username="test3"' \
--form 'profile="test3"'
```

![Register new user](media/user_create.png "Register new user")

* Login of a valid user:

Example: 
```bash
curl --location --request POST 'http://localhost:8000/api/auth/login/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImNwcmFkYTg3QGdtYWlsLmNvbSIsImV4cCI6MTYxNjg0MDYzOSwiZW1haWwiOiJjcHJhZGE4N0BnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTYxNjgzNzAzOX0.j0KewXUAopmdapCqXgunNjGA2DeV0qceDuI6fweUvyk' \
--header 'Cookie: csrftoken=sptVHJ1EEEE7GF5q3frGrLRGpz1Wl0B4ktlHxUA3URyNtCU96jSSZbygPTsEfZXm; sessionid=po7046e0dn15mz9uqzx8eacpxjr9ry42' \
--form 'username="morphheus"' \
--form 'password="admin"' \
--form 'email="cprada87@gmail.com"'
```

![Login user](media/user_login.png "Login user")

If we visit Django Administration ...

```bash
http://localhost:8080/admin/
```

![django_administration_users](media/django_admin_users.png "Django administration users")

### Additional wee can ...

* We can list all users:

Example:
```bash
curl --location --request GET 'http://localhost:8000/api/users/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImNwcmFkYTg3QGdtYWlsLmNvbSIsImV4cCI6MTYxNjg0MDYzOSwiZW1haWwiOiJjcHJhZGE4N0BnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTYxNjgzNzAzOX0.j0KewXUAopmdapCqXgunNjGA2DeV0qceDuI6fweUvyk' \
--header 'Cookie: csrftoken=sptVHJ1EEEE7GF5q3frGrLRGpz1Wl0B4ktlHxUA3URyNtCU96jSSZbygPTsEfZXm; sessionid=po7046e0dn15mz9uqzx8eacpxjr9ry42'
```


![List all users](media/user_list.png "List all users")

* We can also see the instance of each:

Example:
```bash
curl --location --request GET 'http://localhost:8000/api/users/3/' \
--header 'Cookie: csrftoken=sptVHJ1EEEE7GF5q3frGrLRGpz1Wl0B4ktlHxUA3URyNtCU96jSSZbygPTsEfZXm; sessionid=po7046e0dn15mz9uqzx8eacpxjr9ry42'
```

![User instance](media/user_instance.png "User instance")


Second service, say hello, using names for users if is already register and logged 

Need endpoinds to ...

* Say hello:

Example:
```bash
curl --location --request GET 'http://localhost:8000/api/auth/index' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImNwcmFkYTg3QGdtYWlsLmNvbSIsImV4cCI6MTYxNjg0MDYzOSwiZW1haWwiOiJjcHJhZGE4N0BnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTYxNjgzNzAzOX0.j0KewXUAopmdapCqXgunNjGA2DeV0qceDuI6fweUvyk' \
--header 'Cookie: csrftoken=sptVHJ1EEEE7GF5q3frGrLRGpz1Wl0B4ktlHxUA3URyNtCU96jSSZbygPTsEfZXm; sessionid=po7046e0dn15mz9uqzx8eacpxjr9ry42'
```

![Say hello](media/say_hello.png "Say hello")

* If the user isn't logging first or not exists:

![Say hello 404](media/say_hello_404.png "Say hello 404")


## Troubleshooting
TODO

## FAQ 
TODO

## Maintainers
- Christian Prada Osuna
- 2021

## Contributing
TODO

## License
[MIT](https://choosealicense.com/licenses/mit/)