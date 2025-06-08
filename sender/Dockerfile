FROM python:3.11.4-slim

RUN apt-get update -qq &&\
    apt-get install -qq --no-install-recommends -y \
    net-tools\
    curl \
    wget \
    ncat \
    dnsutils \
    iproute2 \
    iputils-ping \
    telnet \
    traceroute &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

RUN printf "PS1='[\@]\u@\h(\$(hostname -i)):\w \n\\$ '" >> /root/.bashrc

WORKDIR /workspace
COPY data.json .

ENTRYPOINT ["/bin/bash"]
