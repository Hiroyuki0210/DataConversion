import FileOperatorXC
import CsvMaker as cm

#XML→CSV変換テスト
class ChangeToCsv:
     def inputFilePath(self):
          print('読み込むXMLファイルのpathを指定してください。')
          filePath = input()
          return filePath

     def changeToCsv(self, filePath):
          fo = FileOperatorXC.FileOperatorXC(filePath)

          readFile = fo.getReadFile()
          writeFile = fo.getWriteFile()
          self.writeFile = writeFile

          csvDocuments = cm.makeCSV(readFile)
          
          with open(writeFile, mode = 'w') as wf:
               wf.write(csvDocuments)

     def getWriteFile(self):
          return self.writeFile

if __name__ == '__main__':
     ctc = ChangeToCsv()
     filePath = ctc.inputFilePath()
     ctc.changeToCsv(filePath)