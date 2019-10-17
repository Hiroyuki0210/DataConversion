from converter import FileOperator
from converter import XmlMaker as xm
from converter import CsvMaker as cm

class Converter:
     #入力情報を返す
     def inputFilePath(self):
          print('変換したいXMLファイルもしくはCSVファイルの名前を指定してください。')
          filePath = input()
          return filePath

     #CSVファイルかXMLファイルかの判断
     def choiceXmlOrCsv(self, filePath):
          if 'csv' in filePath:
               return True
          else:
               return False
     
     #データ形式変換
     def conversion(self, readFile, writeFile):
          if self.choiceXmlOrCsv(readFile):
               xm.makeXml(readFile, writeFile)
          else:
               cm.makeCsv(readFile, writeFile)

def main():
     cv = Converter()
     fileName = cv.inputFilePath()
     fo = FileOperator.FileOperator(fileName)
     readFile = fo.getReadFile()
     writeFile = fo.getWriteFile()

     cv.conversion(readFile, writeFile)
