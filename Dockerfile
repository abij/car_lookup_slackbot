FROM openalpr/openalpr
#FROM bija/openalpr
# TODO: Update bija/openalpr with new Ubuntu AND correct OpenCV to suppoer Python 3.9+.

# Install Tesseract 4.1, resolving OpenALPR Segmentation Fault
# See: https://github.com/openalpr/openalpr/issues/761
RUN apt-get update -y && \
    apt-get install software-properties-common -y && \
    add-apt-repository ppa:alex-p/tesseract-ocr -y && \
    apt-get update -y && \
    apt-get purge libtesseract-dev -y && \
    apt-get install libtesseract-dev -y && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime && \
    PS1="\\u@carlookup:\\w$ " >> /root/.bashrc && \
    apt install -y python3 python3-pip

# Prevent reinstalling
COPY requirements.txt /app/requirements.txt
COPY setup.py /app/
WORKDIR /app

RUN python3 -m pip install -r requirements.txt

# Print Python stdout directly
ENV PYTHONUNBUFFERED=0

# This content changes all the time...
COPY slackbot /app/slackbot

EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD ["-m", "slackbot.application" ]
