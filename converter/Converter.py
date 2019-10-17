from converter import FileOperator
from converter import XmlMaker as xm
from converter import CsvMaker as cm
import sys

class Converter:
     #コマンドライン引数で指定したファイルリストを返す
     #(元からコマンドライン引数に含まれている__main__.pyは返さない)
     def getFiles(self):
          args = sys.argv
          files = []
          for arg in args:
               if '__main__.py' not in arg:
                    files.append(arg)
          return files

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
     files = cv.getFiles()

     for file in files:
          fo = FileOperator.FileOperator(file)
          readFile = fo.getReadFile()
          writeFile = fo.getWriteFile()
          cv.conversion(readFile, writeFile)
