#LIST ARE USED TO STORE MULTIPLE ITEMS IN A SISNGLE VARIABLE
# WHAT IS THE DIFFERENCE BETWEEN LIST AND DICTIONARY IN PYTHON

devop_tools  =  ["linux",  "git",    "docker"]

print(devop_tools)

availabilty_zones = ["us-east-1a",    "us-east-1b", "us-east-1c"]

print(availabilty_zones)


instance_size     = ["t2.micro",  "t2.medium", "t3.micro"]  

print(instance_size)


#PYTHON  ACCESS LIST ITEMS
# List Items  are indexed and cab access by referring to te index nmber
print(instance_size[0])

# changing List names
price  =      ["500",   "333",   "600"  "4400"]   
   #indexpo       0       1         2     3
   
Students_Names  = [ "elvis",  "john", "mercy"]

# Acces the second name on the list Students_names
print(Students_Names[2])

# change the second nam,e on the list Jame
#Item Value 
Students_Names[1] = "James"
print(Students_Names)

#DEVOPS EXAMPLE

aws_regions  = ["us-east-1", "us-east-2",  "ca-central-1"]
# change us-east-1 to us-west-1 
aws_regions[0] = "us-west-1"
print(aws_regions)

#change a Range of Item Values

app_regions  = ["us-east-1", "us-east-2",  "ca-central-1"]
app_regions[0:2]  =  ["us-west-1", "us-west-2"]
print(app_regions)

cars_inventory  = ["honda",  "toyota"]
# append is used to add more values to a list

cars_inventory.append("bmw")
cars_inventory.append("lexus")
print(cars_inventory)

# Insert Items 
cars_inventory.insert(0, "ford")
print(cars_inventory)

#Extend List

cars_inventory.extend(aws_regions)

print(cars_inventory)