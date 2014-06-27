#!/bin/sh

if [ $(pgrep uwsgi | wc -l) -le 2 ];
then
	echo "Uwsgi is down!!!!!"
else
	echo "Uwsgi is running."
fi