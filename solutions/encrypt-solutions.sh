#! /bin/bash

## Encrypt solutions with base64
task_nr="1"
task="01-*"
filename="solutions/${task}"
echo "Encrypting ${filename}"
base64 -i ${filename} -o ${task_nr}.base64
