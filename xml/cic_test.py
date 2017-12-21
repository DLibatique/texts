'''import xml.etree.ElementTree as ET

tree = ET.parse('cic.fam_lat.xml')
root = tree.getroot()

while True:
	try:
		for name in root.iter('name'):
			print(root.tag, name.text)
	except xml.etree.ElementTree.ParseError:
		pass'''

import lxml.etree as ET

parser = ET.XMLParser(recover=True)
tree = ET.parse('cic.fam_lat.xml', parser=parser)

for name in tree.iter('name'):
    print(name.getparent(), '--', name.text)