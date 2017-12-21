import xml.etree.ElementTree as ET

tree = ET.parse('cic.fam_lat.xml')
root = tree.getroot()

while True:
	try:
		for name in root.iter('name'):
			print(root.tag, name.text)
	except xml.etree.ElementTree.ParseError:
		pass

for name in root.iter('name'):
	print(name.text)