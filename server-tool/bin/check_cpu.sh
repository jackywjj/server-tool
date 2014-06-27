#!/bin/sh

cpu_number=$(nproc)
RESULT=$(uptime | sed "s/^.*age: \(.*\)$/\1/")

avg_1=$(echo $RESULT | awk -F "," '{print $1}')
avg_2=$(echo $RESULT | awk -F "," '{print $2}')
avg_3=$(echo $RESULT | awk -F "," '{print $3}')

echo $avg_1 / $cpu_number | bc -l
echo $avg_2 / $cpu_number | bc -l
echo $avg_3 / $cpu_number | bc -l