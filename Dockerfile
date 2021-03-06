FROM bija/openalpr

RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime && \
    PS1="\\u@carlookup:\\w$ " >> /root/.bashrc && \
    apt-get install -y python3.6 && \
    curl https://bootstrap.pypa.io/get-pip.py | python3.6

# Prevent reinstalling
COPY requirements.txt /app/requirements.txt
COPY setup.py /app/
WORKDIR /app

RUN python3.6 -m pip install --no-cache-dir -r requirements.txt

# This content changes all the time...
COPY slackbot /app/slackbot
RUN python3.6 -m pip install .

# Print Python stdout directly
ENV PYTHONUNBUFFERED=0

EXPOSE 5000
ENTRYPOINT [ "python3.6" ]
CMD ["-m", "slackbot.application" ]
