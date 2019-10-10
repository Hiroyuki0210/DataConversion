import unittest
import sys
sys.path.append('../../main/original/XmlToCsv')
import ChangeToCsv

#XML→CSV変換テスト
class ChangeToCsvTest(unittest.TestCase):
     #初期化処理
     def setup(self):
          pass

     #終了処理
     def teardown(self):
          pass

     def test_changeToCsv(self):
          ctc = ChangeToCsv.ChangeToCsv()

          filePath = ctc.inputFilePath()
          ctc.changeToCsv(filePath)
          writeFile = ctc.getWriteFile()
          with open(writeFile) as rf:
               resultValue = rf.read()

          expectedFilePath = '../../expected.csv'
          with open(expectedFilePath) as xf:
               expectedValue = xf.read()

          self.assertEqual(expectedValue.strip(), resultValue.strip())
     
if __name__ == '__main__':
     unittest.main()