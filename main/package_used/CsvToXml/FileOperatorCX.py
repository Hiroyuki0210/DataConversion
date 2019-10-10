import os
import sys

class FileOperatorCX:
     def __init__(self, readFile):
          if os.path.exists(readFile):
               self.readFile = readFile
          else:
               try:
                    raise AttributeError('そのようなファイルは存在しません')
               except AttributeError as e:
                    print(e)
                    print(type(e))

          if 'csv' not in readFile:
               print('ファイル形式が誤っています')
               sys.exit(1)
     
     def getReadFile(self):
          return self.readFile

     def getWriteFile(self):
          writeFile = self.readFile.replace('csv', 'xml')
          return writeFile