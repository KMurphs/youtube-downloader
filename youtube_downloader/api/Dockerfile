FROM ubuntu:20.10

# Get OS Distribution
# RUN source /etc/od-release
# RUN echo $NAME
# RUN echo $ID

RUN apt-get update -y && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.9 && \
    apt install -y curl && \
    apt install -y python3.9-distutils && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.9 get-pip.py
# RUN apt-get update -y && \
    # apt-get install -y software-properties-common && \
    # add-apt-repository ppa:deadsnakes/ppa && \
    # apt install -y python3.9
# RUN apt-get install -y python3-pip
    # apt-get install -y python3-pip python3-dev


# Healthcheck
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ping || exit 1


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /youtube_downloader/requirements.txt
RUN pip3 install -r /youtube_downloader/requirements.txt



COPY ./app /youtube_downloader/app
WORKDIR /youtube_downloader/app



# Create user and set ownership and permissions as required
RUN adduser --disabled-password --gecos '' serveruser && chown -R serveruser /youtube_downloader
# Finalize
USER serveruser
EXPOSE 8000

CMD ["gunicorn", "api:app"]