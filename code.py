#basic operation/automation (read write)

#advance automation & operations 

#all types of possible reporting (monitoring and audit)

#download python
#cd into that folder, typiclaly,
#c:\Users\Administrator\AppData\Local\Programs\Python\Python(latest version)
# then pip install pywin32
#adding one user, and how to check info you may care for of that user.
from pyad import * #import all form python ad
pyad.set_defaults(ldap_server="corp.globexpower.com",username="SWB",password="solarwinds123$") #path to where we are adding
#user=pyad.aduser.ADUser.from_cn("SWB") #adsi edit. then find the user to add
#print(user.get_attribute("userPrincipalName")) #shows users full name in the network/workgroup
#can also be "whencreated" "useraccountcontrol" alot of great options

#part two. bulk user add.
ou=pyad.adcontainer.ADContainer.from_dn("OU=test301project,DC=corp,DC=globexpower,DC=com")
with open("user_data.csv") as f1: #add a list of names and basic info
    import csv
    csvrow=csv.reader(f1,delimiter=",") #calls the file / list of workers Will be doing excel for this.

    i=0
    for row in csvrow:
        if(i>0):
            employeeID=row[0] # makes its easy to call that acount
            givenName=row[1] #first name
            sn=row[2] #last name
            department=row[3] #department they are in
            mail=row[4] #email
            sAMAaccountName=row[5] # user ID
            company=row[6] #company name
            new_user=pyad.aduser.ADUser.create(sAMAaccountName, ou, password=None, upn_suffix=None, enable=True, optional_attributes={"employeeID": employeeID,"givenName":givenName,"sn":sn,"mail":mail,"company":company,"department":department})
            print(employeeID)
        i=i+1

