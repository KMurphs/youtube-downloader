FROM ubuntu:16.04

# Get OS Distribution
# RUN source /etc/od-release
# RUN echo $NAME
# RUN echo $ID

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev


# Healthcheck
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ping || exit 1

# RUN adduser -D serveruser && chown -R serveruser /app
# RUN adduser --disabled-password serveruser && chown -R serveruser /app
# RUN useradd -d /app serveruser && chown -R serveruser /app



# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./app /app


# Create user and set ownership and permissions as required
RUN adduser --disabled-password --gecos '' serveruser && chown -R serveruser /app
# Finalize
USER serveruser
# ENTRYPOINT [ "python" ]
# CMD [ "app.py" ]
ENTRYPOINT [ "flask" ]
CMD [ "run" ]