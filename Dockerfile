FROM openalpr/openalpr

RUN apt-get install -y python3-pip python3-dev && \
    pip3 install --upgrade pip && \
    apt-get purge -y python3-urllib3

# Prevent reinstalling
COPY slackbot/requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3 install -r requirements.txt

# This content changes all the time...
COPY slackbot /app

# Print Python stdout directly
ENV PYTHONUNBUFFERED=0

EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "application.py" ]


