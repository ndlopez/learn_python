#reading an XML file
#downloaded from astrophysical journal

from xml.dom import minidom

#parse an xml file by name
myXML = minidom.parse('/Users/diego/Dropbox/enlaces/astrophys.xml')
item = myXML.getElementsByTagName('title')
#one specific item attrib
print('Item #1 attrib:')
#if getEl... is set to item
#print(item[1].attributes['rdf:about'].value)
#print(item[2].firstChild.data)
link = myXML.getElementsByTagName('link')
desc = myXML.getElementsByTagName('description')
# print(item[3].firstChild.data)
# print(link[3].firstChild.data)
# print(desc[3].firstChild.data)
#to read all titles
print('All titles:')
for elem in item:
    print(elem.firstChild.data)
