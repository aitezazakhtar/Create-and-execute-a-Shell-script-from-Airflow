#!/bin/bash

#Task 1:
# Add a command in the shell script to extract the fields 
# timestamp and visitorid from the web-server-access-log.txt 
# and write to a file extracted.txt
cut -d"#" -f1,4 web-server-access-log.txt > extracted.txt

#Task 2:
#Update the shell script to add a command to capitalize the visitorid 
#and write to a new file capitalized.txt
tr [a-z] [A-Z] < extracted.txt > capitalized.txt

#Task 3:
#Update the shell script to add a command to compress 
#the transformed file capitalized.txt into a new file log.tar.gz
tar -czvf log.tar.gz capitalized.txt