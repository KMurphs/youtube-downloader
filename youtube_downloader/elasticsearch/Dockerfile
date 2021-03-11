FROM docker.elastic.co/elasticsearch/elasticsearch:6.4.1

# Get OS Distribution
# RUN source /etc/od-release
# RUN echo $NAME
# RUN echo $ID

# Install elasticdump on system
RUN yum update -y
# Add node repo to yum registry
RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash -
RUN yum install nodejs -y
RUN npm install elasticdump
