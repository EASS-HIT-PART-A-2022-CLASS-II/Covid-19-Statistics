FROM python:3.10.6

WORKDIR /app/src/BackEnd
WORKDIR /app

COPY . /app/src/BackEnd
COPY ./requirements.txt /app


RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.BackEnd:app", "--host=0.0.0.0", "--reload"]