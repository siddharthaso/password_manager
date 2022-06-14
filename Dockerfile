FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

ADD . /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app


#  RUN npm install

#  ENV PORT=8080

#  EXPOSE 8080

#  CMD ["npm","start"]

# FROM creates a layer from the ubuntu:18.04 Docker image.
# COPY adds files from your Docker client’s current directory.
# RUN builds your application with make.
# CMD specifies what command to run within the container.