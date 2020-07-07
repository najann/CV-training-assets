FROM python:3.7-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080

COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]