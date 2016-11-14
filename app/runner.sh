#!/bin/sh

cat /app/config/filebeat.yml | envsubst > /etc/filebeat/filebeat.yml

python /app/get_halo_events.py | grep -v "Last event timestamp" | /usr/bin/filebeat -c "/etc/filebeat/filebeat.yml"

echo "As death takes us all, it has taken this container... RIP `cat /tmp/halo_events_tstamp`"
