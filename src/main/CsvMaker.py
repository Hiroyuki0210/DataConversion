import xml.etree.ElementTree as ET

def makeCsv(readFile, writeFile):
     tree = ET.parse(readFile)
     root = tree.getroot()
     csvDocuments = ''

     fieldName = ''
     for userInf in root[0]:
          fieldName += userInf.tag + ','
     csvDocuments += fieldName.rstrip(',') + '\n'

     for user in root:
          value = ''
          for i in user:
               value += i.text + ','
          csvDocuments += value.rstrip(',') + '\n'
     csvDocuments = csvDocuments[:-1]
     
     with open(writeFile, mode = 'w') as wf:
          wf.write(csvDocuments)
