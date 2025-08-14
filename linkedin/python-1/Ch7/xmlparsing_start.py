# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing XML
#

import xml.dom.minidom
# use the parse() function to load and parse an XML file
doc = xml.dom.minidom.parse("samplexml.xml")

# print out the document node and the name of the first child tag
print(doc.nodeName)
print(doc.firstChild.tagName)

# create a new XML tag and add it into the document
new_skill = doc.createElement("skill")
new_skill.setAttribute("name", "JQuery")
doc.firstChild.appendChild(new_skill)

# get a list of XML tags from the document and print each one
skills = doc.getElementsByTagName("skill")
print("Skill count:", skills.length)
for skill in skills:
  print(f"skill:", skill.getAttribute("name"))
    