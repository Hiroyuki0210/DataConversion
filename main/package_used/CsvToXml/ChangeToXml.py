import FileOperatorCX
import XmlMaker as xm

class ChangeToXml:
     def inputFilePath(self):
          print('読み込むCSVファイルのpathを指定してください。')
          filePath = input()
          return filePath

     def changeToXml(self, filePath):
          fo = FileOperatorCX.FileOperatorCX(filePath)

          readFile = fo.getReadFile()
          writeFile = fo.getWriteFile()
          self.writeFile = writeFile
          
          xm.makeCsv(readFile, writeFile)

     #テスト用に出力ファイルを取得
     def getWriteFile(self):
          return self.writeFile

if __name__ == '__main__':
     ctx = ChangeToXml()
     filePath = ctx.inputFilePath()
     ctx.changeToXml(filePath)