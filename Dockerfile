FROM python:3.8-buster

# made a directory for the application
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the source code
COPY /app/ .

# run the application
CMD [ "python", "app.py" ]
