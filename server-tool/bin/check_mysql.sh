#!/bin/sh

echo $(service mysql status)
#if [ $(pgrep mysqld | wc -l) -le 2 ];
#then
#	echo "Mysql is down!!!!!"
#else
#	echo "Mysql is running."
#fi