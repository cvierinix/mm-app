FROM python

RUN mkdir /app
WORKDIR /app

RUN pip install --no-cache-dir flask pymongo
COPY . /app
EXPOSE 5000

CMD [ "python", "./app.py" ]
