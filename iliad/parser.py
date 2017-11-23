import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xml.etree.ElementTree as ET
tree = ET.parse('iliad1.xml')
root = tree.getroot()

file = open('iliad1_clean.txt','w')
for l in root.iter('l'):
	file.write(''.join(l.itertext()) + "\n")
file.close()