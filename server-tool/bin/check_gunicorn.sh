#!/bin/sh

if [ $(pgrep gunicorn | wc -l) -le 2 ];
then
	echo "Gunicorn is down!!!!!"
else
	echo "Gunicorn is running."
fi