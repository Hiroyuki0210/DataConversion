import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as md

def makeCsv(readFile, writeFile):
     with open(readFile) as f:
          reader = csv.reader(f)
          elements = []

          for i in reader:
               elements.append(i)

     root = ET.Element('users')
     for j in range(1, len(elements)):
          user = ET.SubElement(root, 'user')
          for i in range(len(elements[0])):
               userInf = ET.SubElement(user, elements[0][i])
               userInf.text = elements[j][i]
     
     document = md.parseString(ET.tostring(root, 'UTF-8'))
     with open(writeFile, 'w') as wf:
          document.writexml(wf, encoding='UTF-8', newl='\n', indent='', addindent='     ')