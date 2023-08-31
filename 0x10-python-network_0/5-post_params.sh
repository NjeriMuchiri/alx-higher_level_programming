#!/bin/bash
#script that sends a POST request to the passed URL
curl -s -X POST -d "test@gmail.com&subject=I will always be here for PLD" "$1"
