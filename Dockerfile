FROM python:3.9-slim

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

WORKDIR /

EXPOSE 90

CMD ["uvicorn", "app.test:app","--host","0.0.0.0","--port","90"]


