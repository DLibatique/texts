import xml.etree.ElementTree as ET

tree = ET.parse('cic.fam_lat.xml')
root = tree.getroot()

for name in root.iter('name'):
	print(root.tag, name.text)