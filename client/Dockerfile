FROM python:3.6

EXPOSE 5001

WORKDIR /client

COPY requirements.txt /client
RUN pip install -r requirements.txt

COPY app.py /client
CMD python app.py "http://service:5002/"
