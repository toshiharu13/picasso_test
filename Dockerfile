FROM python:3.9.13
WORKDIR /code
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt  \
    && apt update -y && apt install redis -y
RUN chmod +x /code/worker.sh