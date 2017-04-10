#!/bin/sh

./rtc-pi $SETTIME
echo "$SETTIME, TIME SET."

if [ $DISPLAY -eq 0 ]; then
  exit 0
else

  while true;
  do
  
  #init
  output=$(date +%s) && \

  #seprator
  output="$output," && \

  #main
  echo "$output$(date "+%Y%m%d%H%M%S")" > /var/log/ds1302.txt && \
  
  #interval
  sleep $INTERVAL;

  done

fi

