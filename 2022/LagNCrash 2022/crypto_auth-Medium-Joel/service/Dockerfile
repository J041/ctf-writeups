FROM python:3.8-slim-buster
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN ls
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
