import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xml.etree.ElementTree as ET
tree = ET.parse('iliad_1_1-32.xml')
root = tree.getroot()

file = open('iliad_1_1-32.txt','w')
for l in root.iter('l'):
	file.write(str(l.text) + "\n")
file.close()