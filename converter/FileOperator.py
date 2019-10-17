import os
import sys

class FileOperator:
     def __init__(self, readFile):
          if ('csv' not in readFile) and ('xml' not in readFile):
               print('誤ったファイル形式を入力しています')
               sys.exit(1)

          if os.path.exists(readFile):
               self.readFile = readFile
          else:
               try:
                    raise AttributeError('存在しないファイルを入力しています')
               except AttributeError as e:
                    print(e)
                    print(type(e))

     def getReadFile(self):
          return self.readFile

     def getWriteFile(self):
          readFile = self.readFile
          writeFile = ''

          if ('csv' in readFile):
               if '/' in readFile:
                    fileName = readFile[readFile.rfind('/') + 1 : readFile.index('.csv')]
               else:
                    fileName = readFile[0 : readFile.index('.csv')]
               writeFile = 'AfterConversion/XmlFiles/' + fileName + '.xml'

          if ('xml' in readFile):
               if '/' in readFile:
                    fileName = readFile[readFile.rfind('/') + 1 : readFile.index('.xml')]
               else:
                    fileName = readFile[0 : readFile.index('.xml')]
               writeFile = 'AfterConversion/CsvFiles/' + fileName + '.csv'

          return writeFile