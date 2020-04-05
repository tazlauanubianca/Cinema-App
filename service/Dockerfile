FROM python:3.6

EXPOSE 5002

WORKDIR /service

COPY requirements.txt /service
RUN pip install -r requirements.txt

COPY app.py /service
CMD python app.py
