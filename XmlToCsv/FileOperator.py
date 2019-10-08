import os

class FileOperator:
     def __init__(self, readFile):
          if os.path.exists(readFile):
               self.readFile = readFile
          else:
               print('そのようなファイルは存在しません')
     
     def getReadFile(self):
          return self.readFile

     def getWriteFile(self):
          writeFile = self.readFile.replace('xml', 'csv')
          return writeFile