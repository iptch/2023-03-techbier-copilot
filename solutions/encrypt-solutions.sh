#! /bin/bash

## Encrypt solutions with base64
task_nr="2"
task="02-hello-world.py"
filename="solutions/${task}"
echo "Encrypting ${filename}"
base64 -i ${filename} -o ./solutions/${task_nr}.base64
