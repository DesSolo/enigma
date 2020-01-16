FROM python:3.7-slim

RUN mkdir /srv/enigma
WORKDIR /srv/enigma
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD ./app .

EXPOSE 8000

CMD python app.py

