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

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# COPY src/ /app/

# ENTRYPOINT ["python", "main.py", "--host", "0.0.0.0", "--port", "84", "--dest_host", "health_checker", "--dest_port", "84" ]
ENTRYPOINT [ "/bin/bash" ]
