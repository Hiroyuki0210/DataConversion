import xml.etree.ElementTree as ET

def makeCSV(readFile):
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
     
     return csvDocuments