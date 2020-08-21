# Pull base image for 1st stage build
FROM python:3.8.0-slim as build-python

# install dependencies
RUN apt-get update \
    && apt-get install -y binutils netcat \
    && rm -rf /var/lib/apt

# Upgrade pip and create wheels to be installed later
COPY ./dev-requirements.txt /
COPY ./requirements.txt /

RUN python3 -m pip install pip pip-tools
RUN python3 -m pip wheel --no-cache-dir --no-deps --retries 10 \
    --wheel-dir /wheels \
    -r requirements.txt -r dev-requirements.txt

# 2nd stage build
FROM python:3.8.0-slim

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy and install the previously created wheels
COPY --from=build-python /wheels /wheels
COPY --from=build-python requirements.txt .
RUN pip install --no-cache /wheels/*

# set work dir
WORKDIR /usr/app/enredarte

# copy project
COPY . .

# copy entrypoint
COPY ./entrypoint.sh .

# add and run as non-root user
RUN adduser --disabled-login myuser
USER myuser

# run entrypoint
ENTRYPOINT [ "/usr/app/enredarte/entrypoint.sh" ]