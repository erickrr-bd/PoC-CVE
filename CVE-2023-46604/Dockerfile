FROM rockylinux:8.9

LABEL maintainer="Erick Rodriguez <erodriguez@tekium.mx>"

ADD jdk-8u441-linux-x64.rpm /tmp
RUN rpm -ivh /tmp/jdk-8u441-linux-x64.rpm
RUN rm -rf /tmp/jdk-8u441-linux-x64.rpm

RUN mkdir -p /opt/apache-activemq-5.16.4
COPY apache-activemq-5.16.4 /opt/apache-activemq-5.16.4

ENV JAVA_HOME=/usr/lib/jvm/jdk-1.8.0_441-oracle-x64
ENV ACTIVEMQ_HOME=/opt/apache-activemq-5.16.4
ENV PATH=$PATH:$ACTIVEMQ_HOME/bin

EXPOSE 8161/tcp
EXPOSE 61616/tcp

WORKDIR $ACTIVEMQ_HOME/bin
RUN chmod +x activemq

CMD ["./activemq", "console"]