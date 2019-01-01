
# Authentication system project launching

In order to start running the project you need to:

- adjust **liquibase.properties** file in **migration** folder for your local db
- migrate changesets with liquibase from **migrations** folder
- install all needed libraries from **requirements.txt** file
- create **.env** file in your project root and put there variables listed below

**DB_URL** - string url that leads to your db

**SECRET_KEY** - key that is used for hashing passwords and generating authentication tokens

Endpoints are the following: 
* /auth/login
* /auth/register
* /home - accessable only when user has been properly authenticated
