FROM python:3.10

ARG NAME
ARG PORT

RUN mkdir -p "/usr/src/${NAME}_backend"

WORKDIR "/usr/src/${NAME}_backend"

COPY ./requirements.txt "/usr/src/${NAME}_backend"
RUN pip install --no-cache-dir -r requirements.txt
COPY . "/usr/src/${NAME}_backend"
EXPOSE ${PORT}

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}