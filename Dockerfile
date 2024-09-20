FROM python:3.10

WORKDIR /backend

RUN pip3 install flask
RUN pip3 install pymysql
RUN pip3 install flask-cors
RUN pip3 install pytest

COPY . .

CMD [ "python", "app.py" , "--host", "0.0.0.0", "--port", "5000"]
EXPOSE 5000
