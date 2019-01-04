FROM rappdw/docker-java-python

WORKDIR /code

COPY . /code

RUN pip install --trusted-host pypi.python.org -r requirements.txt