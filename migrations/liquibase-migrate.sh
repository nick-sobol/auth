#!/bin/bash

if [ -n "${POSTGRES_USER}" -a -n "${POSTGRES_PASSWORD}" \
     -a -n "${POSTGRES_HOST}" -a -n "${POSTGRES_DB}" ]; then

    POSTGRES_PORT=${POSTGRES_PORT:-5432};

    java -jar liquibase.jar \
        --url=jdbc:postgresql://${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB} \
        --driver=org.postgresql.Driver \
        --classpath=jdbcdrivers/postgresql-42.2.5.jar \
        --username="${POSTGRES_USER}" \
        --password="${POSTGRES_PASSWORD}" \
        --changeLogFile=changelog.xml update
else
	echo "You should specify all variables: POSTGRES_USER," \
	"POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB"

	exit 1
fi
