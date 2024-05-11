#!/bin/bash 

echo -n   "Enter the user name:"
read username   
echo   -n    "enter the password: "
read -s  password
sudo   adduser  "$username"
echo  "$password" | password "$username"  --stdin
echo "Granting sudo access to $username"
echo "$username ALL=(ALL) NOPASSWD:ALL" | sudo tee  /etc/sudoers.d/$
ls /home
cat  /etc/shadow
cat /etc/passwd