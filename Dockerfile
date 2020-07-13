FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /apprest
WORKDIR /apprest
COPY . .
ADD . /apprest/
RUN pip install --upgrade pip
RUN pip install -r /apprest/requirements-docker.txt
RUN python manage.py migrate
RUN python manage.py seed_fake_data