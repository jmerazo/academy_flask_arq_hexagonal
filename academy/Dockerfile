FROM python:3.9.2-alpine

RUN apk add python3-dev \
    && pip3 install --upgrade pip

WORKDIR /src

COPY . /src
RUN pip3 install -r requirements.txt

ENV FLASK_APP=apps:app
ENV FLASK_RUN_HOST=0.0.0.0

CMD [ "flask", "run" ]
