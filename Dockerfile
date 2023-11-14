FROM python:3.8

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["sh", "-c", "python users-xls.py && sleep 40"]
