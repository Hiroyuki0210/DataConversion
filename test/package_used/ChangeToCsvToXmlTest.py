import unittest
import sys
sys.path.append('../../main/package_used/XmlToCsv')
sys.path.append('../../main/package_used/CsvToXml')
import ChangeToCsv
import ChangeToXml

#XML→CSV→XML変換テスト
class ChangeToCsvToXmlTest(unittest.TestCase):
     #初期化処理
     def setup(self):
          pass

     #終了処理
     def teardown(self):
          pass

     def test_changeToCsvToXml(self):
          #CSVへの変換
          ctc = ChangeToCsv.ChangeToCsv()
          filePath = ctc.inputFilePath()
          ctc.changeToCsv(filePath)
          firstWriteFile = ctc.getWriteFile()

          #XMLへの変換
          ctx = ChangeToXml.ChangeToXml()
          ctx.changeToXml(firstWriteFile)
          secondWriteFile = ctx.getWriteFile()

          with open(secondWriteFile) as rf:
               resultValue = rf.read()

          expectedFilePath = '../../expected.xml'
          with open(expectedFilePath) as xf:
               expectedValue = xf.read()

          self.assertEqual(expectedValue.strip(), resultValue.strip())
     
if __name__ == '__main__':
     unittest.main()