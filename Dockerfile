FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

COPY requirements.txt /tmp/pip-tmp/

RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt

# RUN curl -s "https://get.sdkman.io" | bash

# RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install java 17.0.13-tem"

# RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install sbt"

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME
EXPOSE 4040
