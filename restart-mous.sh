#!bin/bash
kill $(ps ax | grep -e "VBoxClient --draganddrop$" | awk '{print $1}'); VBoxClient --draganddrop
