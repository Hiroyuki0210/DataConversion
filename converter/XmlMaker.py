import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as md
import sys

def makeXml(readFile, writeFile):
     with open(readFile) as f:
          reader = csv.reader(f)
          #データを格納するリスト
          #各行を1組のリストとして、それを複数格納する2次元配列型
          elements = []

          for i in reader:
               elements.append(i)

     if len(elements) == 0:
          print('項目名とデータを入力してください')
          sys.exit(1)

     if len(elements) == 1:
          print('データを入力してください')
          sys.exit(1)

     for i in range(1, len(elements)):
          if len(elements[i]) > len(elements[0]):
               print('変換に失敗しました')
               print('項目数より多くのデータを入力しています')
               sys.exit(1)

     for name in elements[0]:
          if name.strip() == '':
               print('無名の項目は定義しないでください')
               sys.exit(1)

     root = ET.Element('users')
     
     for j in range(1, len(elements)):
          user = ET.SubElement(root, 'user')
          for i in range(len(elements[j])):
               userInf = ET.SubElement(user, elements[0][i])
               userInf.text = elements[j][i]
     
     document = md.parseString(ET.tostring(root, 'UTF-8'))

     with open(writeFile, 'w') as wf:
          document.writexml(wf, encoding='UTF-8', newl='\n', indent='', addindent='     ')