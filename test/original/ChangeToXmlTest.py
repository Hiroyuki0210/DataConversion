import unittest
import sys
sys.path.append('../../main/original/CsvToXml')
import ChangeToXml

#CSV→XML変換テスト
class ChangeToXmlTest(unittest.TestCase):
     #初期化処理
     def setup(self):
          pass

     #終了処理
     def teardown(self):
          pass

     def test_changeToXml(self):
          ctx = ChangeToXml.ChangeToXml()

          filePath = ctx.inputFilePath()
          ctx.changeToXml(filePath)
          writeFile = ctx.getWriteFile()
          with open(writeFile) as rf:
               resultValue = rf.read()

          expectedFilePath = '../../expected.xml'
          with open(expectedFilePath) as xf:
               expectedValue = xf.read()

          self.assertEqual(expectedValue, resultValue)
     
if __name__ == '__main__':
     unittest.main()