#!/bin/bash

echo enter your monthly income
read income 

echo  enter your montly expenses 

read   expenses

if    [ $income !=  $expenses]

then 
 echo "client is not eliggable"
else 
 echo "client maybe eligible in two months"

fi 