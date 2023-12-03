FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Assuming 'static' directory is in the same directory as Dockerfile
COPY ./app/static /app/static

COPY ./app /app/app

EXPOSE 80