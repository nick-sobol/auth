
# Authentication system project launching

In order to start launch the project **locally** you need to:

- create **.env** file in root folder and put there all required environment variables listed below
- migrate changesets from **migration** folder using **./liquibase-migrate.sh** command
- run **make setup** in root folder
- run **make run-dev** in root folder

#
In order to launch tests you need to:

- create **.env_test** file in root folder and put there all required environment variables listed below
- migrate changesets from **migration** folder using **./liquibase-migrate.sh** command
- run **make setup** in root folder
- run **make run-test** in root folder

#

In order to start launch the project using **Docker** you need to:

- create **.env** file in a root folder and put there all required environment variables listed below
- run **docker-compose run build** in a root folder 


Environment variables
---

    SECRET_KEY=<string>                 # Key that is used for hashing passwords and generating authentication tokens, no default value
    POSTGRES_USER=<string>              # DB user name, no default value
    POSTGRES_PASSWORD=<string>          # DB password, no default value
    POSTGRES_PORT=<int>                 # DB listen port, default should be set to 5432 in program code
    POSTGRES_HOST=<string>              # DB host, no default value
    POSTGRES_DB=<string>                # DB name, no default value


Endpoints 
---

* /auth/login - accessable for any user
* /auth/register - accessable for any user
* /home - accessable only when user has been properly authenticated
