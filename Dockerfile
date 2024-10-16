FROM python:3.11-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update --no-cache \
    && apk add build-base postgresql-dev libpq --no-cache --virtual .build-deps \
    && pip install --no-cache-dir --upgrade pip
WORKDIR /app
COPY ./scripts/entrypoint.sh /scripts/entrypoint.sh
COPY requirements.txt requirements.txt
RUN pip install -r --no-cache-dir requirements.txt
RUN apk del .build-deps
COPY . .
EXPOSE 8000
RUN chmod +x /scripts/entrypoint.sh
CMD ["sh", "/scripts/entrypoint.sh"]
