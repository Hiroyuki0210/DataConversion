import FileOperator
import XmlMaker as xm

print('読み込むCSVファイルのpathを指定してください。')
filePath = input()
fo = FileOperator.FileOperator(filePath)

readFile = fo.getReadFile()
writeFile = fo.getWriteFile()
elementList = []

with open(readFile) as rf:
     elementList = xm.makeElementList(rf)

with open(writeFile, mode='w') as wf:
     xm.makeXML(wf, elementList)