#!/bin/bash

read -p 'Starting recordin by hitting 1 or other to exit' t

while [ "$t" -eq 1 ] 
do
	sudo echo "Starting talking by entering 1 or other to exit"
	sudo echo "Starting recording"
	sudo sudo arecord -t wav -c 1 -r 16000 -D "plughw:1,0" -d 5 -f S16_LE temp.wav
	sudo echo "Recording finished waiting for response"
	sudo python3 combine.py  
	read -p 'Starting recordin by 1' t
	if [ "$t" -ne 1 ];then break
	fi 
done