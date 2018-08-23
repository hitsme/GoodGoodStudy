#!/usr/bin/expect                   
set timeout 30                      
spawn ssh -N -f -R 2229:127.0.0.1:22 35.189.147.132
expect "*password*" 
sleep 5                
send "hitsme52035203\r"                
send "cd /data/logs\r"              
interact    
