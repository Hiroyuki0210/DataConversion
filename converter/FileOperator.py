import os
import sys

class FileOperator:
     def __init__(self, fileName):
          if ('csv' not in fileName) and ('xml' not in fileName):
               print('ファイル形式が誤っています')
               sys.exit(1)

          csvFile = 'BeforeConversion/CsvFiles/' + fileName
          xmlFile = 'BeforeConversion/XmlFiles/' + fileName
          if os.path.exists(csvFile) or os.path.exists(xmlFile):
               if os.path.exists(csvFile):
                    self.readFile = csvFile
               else:
                    self.readFile = xmlFile
          else:
               try:
                    raise AttributeError('そのようなファイルは存在しません')
               except AttributeError as e:
                    print(e)
                    print(type(e))

     def getReadFile(self):
          return self.readFile

     def getWriteFile(self):
          writeFile = ''

          if 'csv' in self.readFile:
               writeFile = self.readFile.replace('csv', 'xml').replace('BeforeConversion/CsvFiles', 'AfterConversion/XmlFiles')

          if 'xml' in self.readFile:
               writeFile = self.readFile.replace('xml', 'csv').replace('BeforeConversion/XmlFiles', 'AfterConversion/CsvFiles')

          return writeFile