import xml.etree.ElementTree as ET
import sys

def makeCsv(readFile, writeFile):
     root = []
     try:
          tree = ET.parse(readFile)
          root = tree.getroot()
     except ET.ParseError as e:
          print('変換に失敗しました')
          print('タグの記入に誤りがあります')
          print(e)
          sys.exit(1)

     csvDocuments = ''
     fieldName = ''
     if len(root) != 0:
          for userInf in root[0]:
               fieldName += userInf.tag + ','
          csvDocuments += fieldName.rstrip(',') + '\n'
     else:
          print('変換に失敗しました')
          print('子要素を記入してください')
          sys.exit(1)
     

     for user in root:
          value = ''
          for i in user:
               value += i.text + ','
          csvDocuments += value.rstrip(',') + '\n'
     csvDocuments = csvDocuments[:-1]
     
     with open(writeFile, mode = 'w') as wf:
          wf.write(csvDocuments)
