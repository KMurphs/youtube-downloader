FROM ubuntu:16.04

# Get OS Distribution
# RUN source /etc/od-release
# RUN echo $NAME
# RUN echo $ID

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev


# Healthcheck
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ping || exit 1

# RUN adduser -D serveruser && chown -R serveruser /app
# RUN adduser --disabled-password serveruser && chown -R serveruser /app
# RUN useradd -d /app serveruser && chown -R serveruser /app



# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /youtube_downloader/requirements.txt
RUN pip3 install -r /youtube_downloader/requirements.txt

COPY ./app /youtube_downloader/app
WORKDIR /youtube_downloader/app

# COPY ./app /app/backend


# Create user and set ownership and permissions as required
RUN adduser --disabled-password --gecos '' serveruser && chown -R serveruser /youtube_downloader
# Finalize
USER serveruser
EXPOSE 8000
# ENTRYPOINT [ "python" ]
# CMD [ "app.py" ]
# ENTRYPOINT [ "flask" ]
# CMD [ "run" ]


# CMD [ "flask", "run" ]
# CMD ["gunicorn"  , "-w", "4", "-b", "0.0.0.0:8000", "__init__:app"]
# WORKDIR /app
CMD ["gunicorn", "__init__:app"]