#!/bin/sh
while true; do
        if [ -f "/var/log/voice.txt" ] && [ -f "/var/log/light.txt" ]; then
		if [ -z $(cat /var/log/voice.txt | sed 's/,/ /g' | awk '{print $2}') ]; then voice=-1; else voice=$(cat /var/log/voice.txt | sed 's/,/ /g' | awk '{print $2}'); fi;
		if [ -z $(cat /var/log/light.txt | sed 's/,/ /g' | awk '{print $2}') ]; then light=-1; else light=$(cat /var/log/light.txt | sed 's/,/ /g' | awk '{print $2}'); fi;
        	if [ "$voice" -eq "0" ] || [ "$voice" -eq "1" ] || [ "$light" -eq "0" ] || [ "$light" -eq "1" ]; then
			ACTION=$(( !voice & light ));
			python laser.py $GPIO_PIN $ACTION;
		fi
        fi
        sleep $INTERVAL
done

