# Pull official base image
FROM python:3.8.0-alpine

# set work dir
WORKDIR /usr/app/enredarte

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update \
    # GCC for alpine linux https://wiki.alpinelinux.org/wiki/GCC
    && apk add build-base \
    # Postgres
    postgresql-dev python3-dev musl-dev \
    # Pillow dependencies
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./*requirements.txt .
RUN pip install -r requirements.txt
RUN pip install -r prod-requirements.txt

# copy entrypoint
COPY ./entrypoint.sh .

# copy project
COPY . .

# add and run as non-root user
RUN adduser -D testuser
USER testuser

# run entrypoint
# ENTRYPOINT [ "/usr/app/enredarte/entrypoint.sh" ]

CMD gunicorn enredarte.wsgi:application --bind 0.0.0.0:$PORT