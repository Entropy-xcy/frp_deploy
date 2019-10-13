FROM ubuntu:16.04
COPY . /app
RUN apt-get update && apt-get install -y python3 git wget tar
WORKDIR /app/
RUN ./client_deploy.sh

CMD tail -f /dev/null
