FROM python:3.11

WORKDIR /code

COPY ./container/requirements.txt /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN mkdir /code/production_settings
COPY ./container/production/requirements.txt /code/production_settings
RUN pip install --no-cache-dir --upgrade -r /code/production_settings/requirements.txt

COPY . /code/backend
