# image based on fluentd v1.14-1
FROM fluentd:v1.14-1

# Use root account to use apk
USER root

# below RUN includes plugin as examples elasticsearch is not required# you may customize including plugins as you wish]

# copy fluentd configuration from host image
COPY ./conf/fluentd.conf /fluentd/etc/
# copy binary start file
COPY entrypoint.sh /bin/
RUN chmod +x /bin/entrypoint.sh

USER fluent
