#!/bin/sh

echo $(service php5-fpm status)
#if [ $(pgrep php-fpm | wc -l) -le 2 ];
#then
#	echo "PHP fpm is down!!!!!"
#else
#	echo "PHP fpm is running."
#fi