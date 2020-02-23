FROM python:3.8.1-slim

WORKDIR /opt

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

COPY . /opt/

CMD ["python", "/opt/main.py"]