import FileOperator
import CssMaker

print('読み込むXMLファイルのpathを指定してください。')
filePath = input()
fo = FileOperator.FileOperator(filePath)


readFile = fo.getReadFile()
writeFile = fo.getWriteFile()

cm = CssMaker.CssMaker(readFile, writeFile)
cm.getFieldSet()
cm.getFieldNameSet()
cm.getFieldValueSet()
cm.makeCSV()

