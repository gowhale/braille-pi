#!/bin/bash
# Usage: Automation of connecting to raspberry pi via SSH
# Author: gowhale
# -------------------------------------------------
# NOTE: to make process even better generate a passphraseless SSH key and push it to your Pi 
# NOTE: Also, create an ALIAS to run this script

finished=false
pi_address="INSERT PI ADDRESS HERE"
pi_username="INSERT PI USERNAME HERE"

while [ "${finished}" != "true" ]
do

    ping -q -c5 ${pi_address} > /dev/null
    
    if [ $? -eq 0 ]
    then
        echo -e "\x1B[1;32m ------------CONNECTION SUCCESFUL ----------------- \x1B[0m"

        echo -e "\x1B[1;35m   .~~.   .~~.
  '. \ ' ' / .'
   .~ .~~~..~.
  : .~.'~'.~. :
 ~ (   ) (   ) ~
( : '~'.~.'~' : )
 ~ .~ (   ) ~. ~
  (  : '~' :  ) 
   '~ .~~~. ~'
       '~'\x1B[0m"
        finished=true
    fi

done

ssh ${pi_username}@${pi_address}

echo "Finished"