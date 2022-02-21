FROM python:3
ADD src/main.py /
RUN pip install flask
RUN pip install flask-ngrok
CMD [ "python", "./main.py" ]