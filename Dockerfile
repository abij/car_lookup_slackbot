FROM bija/openalpr

RUN apt-get update && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime && \
    apt-get install -y \
        python3-dev \
        python3-pip \
        python3-pandas && \
    pip3 install --upgrade pip && \
    apt-get purge -y python3-urllib3 python3-six

# Prevent reinstalling
COPY requirements.txt /app/requirements.txt
COPY setup.py /app/
WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

# This content changes all the time...
COPY slackbot /app/slackbot
RUN pip3 install .

# Print Python stdout directly
ENV PYTHONUNBUFFERED=0

EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD ["-m", "slackbot.application" ]
