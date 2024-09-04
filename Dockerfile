FROM python:3.9

WORKDIR /BriefComm

ADD . /BriefComm

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]