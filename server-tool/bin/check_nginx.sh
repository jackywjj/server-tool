#!/bin/sh

if [ $(pgrep nginx | wc -l) -le 2 ];
then
	echo "Nginx is down!!!!!"
else
	echo "Nginx is running."
fi