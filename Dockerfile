FROM bija/openalpr

RUN apt-get update && \
    apt-get install -y \
        python3-dev \
        python3-pip \
        python3-pandas && \
    pip3 install --upgrade pip && \
    apt-get purge -y python3-urllib3 python3-six

# Trying to prevent warning: libdc1394 error: Failed to initialize libdc1394
# https://github.com/openalpr/openalpr/issues/413
RUN ln -s /dev/null /dev/raw1394

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
