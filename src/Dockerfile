FROM python:3.10.6

WORKDIR /app
WORKDIR /src
COPY . /app/src
COPY ./requirements.txt /app



RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "src.BackEnd:app", "--host=0.0.0.0", "--reload"]