import xml.etree.ElementTree as ET

tree = ET.parse('aristoph.birds_gk.xml')
root = tree.getroot()

for l in root.iter('l'):
	print(l.text)