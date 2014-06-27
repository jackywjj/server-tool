#!/bin/sh

echo $(free -m| grep ^Mem |awk '{print $2,$3,$4}')