#read an XML file from astrophys. journal
#[2] <item> 1st article on the list
#[2][0]  <title>
#[2][1]  <link>
#[2][2]  <description>
#[2][3]  <dc:author> all authors
#[2][4]  <dc:date> pub date
#
import random
import xml.etree.ElementTree as ET
tree = ET.parse('/Users/diego/Dropbox/enlaces/astrophys.xml')
root = tree.getroot()
total=len(root)
#random article
i=random.randint(2,total) 
#title
print(root[i][0].text)
#authors
print(root[i][3].text)
#description
#print(root[i][2].text)
#pub.date
print(root[i][4].text)
#link
print(root[i][1].text)

#to print all items in xml file
#for elem in root:
#    for subelm in elem:
#        print(subelm.text)
