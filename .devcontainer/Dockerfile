FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

RUN apt-get -qq update \
    && DEBIAN_FRONTEND=noninteractive apt-get -qq install --no-install-recommends -y\
    # utility
    peco\
    silversearcher-ag\
    vim\
    git\
    # networks
    curl \
    dnsutils \
    iproute2 \
    iputils-ping \
    telnet \
    traceroute \
    && apt-get clean\
    && rm -rf /var/lib/apt/lists/*

# hadolint for docker
ARG HADOLINT_URL
RUN curl -Lks -o /usr/local/bin/hadolint ${HADOLINT_URL}\
    && chmod o+x /usr/local/bin/hadolint

# git
WORKDIR /usr/share/doc/git/contrib/diff-highlight
RUN make\
    && chmod o+x diff-highlight\
    && ln -s /usr/share/doc/git/contrib/diff-highlight/diff-highlight /usr/local/bin

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
