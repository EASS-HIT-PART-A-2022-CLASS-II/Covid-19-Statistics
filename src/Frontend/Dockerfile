FROM python:3.10

WORKDIR /app/src/Frontend

COPY . /app/src/Frontend

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install pymongo

EXPOSE 8501

CMD streamlit run Frontend.py
