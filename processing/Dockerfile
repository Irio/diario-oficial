FROM python:3.7-stretch

ARG LOCAL_USER_ID

WORKDIR /mnt/code

COPY . /mnt/code

RUN adduser --system -u ${LOCAL_USER_ID:-1000} gazette \
	&& apt-get update \
	&& apt-get -y install postgresql-client wait-for-it sqlite3 \
	&& pip install --no-cache-dir -r requirements.txt

USER gazette
