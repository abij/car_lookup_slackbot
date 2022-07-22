FROM openalpr/openalpr
#FROM bija/openalpr
# TODO: Update bija/openalpr with new Ubuntu AND correct OpenCV to suppoer Python 3.9+.

RUN apt-get update && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime && \
    PS1="\\u@carlookup:\\w$ " >> /root/.bashrc && \
    apt install -y python3 python3-pip

# Prevent reinstalling
COPY requirements.txt /app/requirements.txt
COPY setup.py /app/
WORKDIR /app

# This content changes all the time...
COPY slackbot /app/slackbot
RUN python3 -m pip install .

# Print Python stdout directly
ENV PYTHONUNBUFFERED=0

EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD ["-m", "slackbot.application" ]
