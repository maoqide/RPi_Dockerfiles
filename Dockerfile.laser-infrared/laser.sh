#!/bin/sh
while true; do
    if [ -f "/var/log/rain.txt" ]; then
		if [ -z $(cat /var/log/avoid.txt | sed 's/,/ /g' | awk '{print $2}') ]; then 
			avoid=-1; 
		else 
			avoid=$(cat /var/log/avoid.txt | sed 's/,/ /g' | awk '{print $2}'); 
		fi;
	        if [ "$avoid" -eq "0" ] || [ "$avoid" -eq "1" ]; then
			ACTION=$((!avoid));
			python laser.py $GPIO_PIN $ACTION;
		fi
    fi
    sleep $INTERVAL;
done
