#!/bin/sh

disk=$(df -h|grep /$|awk '{print $2,$5}')
disk_used=$(echo $disk|awk '{print $1}'|tr -d '%')
disk_percent=$(echo $disk|awk '{print $2}'|tr -d '%')
echo $disk_used
echo $disk_percent