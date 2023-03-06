#! /bin/bash

## Encrypt solutions with base64
task_nr="4"
task="04-explain-and-port-code.py"
filename="solutions/${task}"
echo "Encrypting ${filename}"
base64 -i ${filename} -o ./solutions/${task_nr}.base64
