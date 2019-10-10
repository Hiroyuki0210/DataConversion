import unittest
import sys
sys.path.append('../../main/original/XmlToCsv')
sys.path.append('../../main/original/CsvToXml')
import ChangeToCsv
import ChangeToXml

#CSV→XML→CSV変換テスト
class ChangeToCsvToXmlTest(unittest.TestCase):
     #初期化処理
     def setup(self):
          pass

     #終了処理
     def teardoen(self):
          pass

     def test_changeToCsvToXml(self):
          #XMLへの変換
          ctx = ChangeToXml.ChangeToXml()
          filePath = ctx.inputFilePath()
          ctx.changeToXml(filePath)
          firstWriteFile = ctx.getWriteFile()

          #CSVへの変換
          ctc = ChangeToCsv.ChangeToCsv()
          ctc.changeToCsv(firstWriteFile)
          secondWriteFile = ctc.getWriteFile()

          with open(secondWriteFile) as rf:
               resultValue = rf.read()

          expectedFilePath = '../../expected.csv'
          with open(expectedFilePath) as xf:
               expectedValue = xf.read()

          self.assertEqual(expectedValue.strip(), resultValue.strip())
     
if __name__ == '__main__':
     unittest.main()