FROM python:3.9

RUN mkdir /app

WORKDIR /app

# port documentation for docker container
EXPOSE 8000 

# copy requirements.txt into docker image
COPY requirements.txt .

# install depencies
RUN pip install --no-cache-dir -r requirements.txt

# copy current code base into docker image
COPY . .

RUN ["python", "my_app/manage.py", "migrate"]

# start the django development server on port 8000 in the docker container
CMD ["python", "my_app/manage.py", "runserver", "0.0.0.0:8000" ]
