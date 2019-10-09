import os
import sys

class FileOperatorXC:
     def __init__(self, readFile):
          if os.path.exists(readFile):
               self.readFile = readFile
          else:
               try:
                    raise AttributeError('そのようなファイルは存在しません')
               except AttributeError as e:
                    print(e)
                    print(type(e))

          if 'xml' not in readFile:
               print('ファイル形式が誤っています')
               sys.exit(1)
     
     def getReadFile(self):
          return self.readFile

     def getWriteFile(self):
          writeFile = self.readFile.replace('xml', 'csv')
          return writeFile