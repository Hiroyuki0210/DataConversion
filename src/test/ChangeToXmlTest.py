import unittest
import sys
sys.path.append('../main')
import Converter

#CSV→XML変換テスト
class ChangeToXmlTest(unittest.TestCase):
     #初期化処理
     def setup(self):
          pass

     #終了処理
     def teardown(self):
          pass

     def test_changeToXml(self):
          cv = Converter.Converter()
          readFile = '../../TestFile/BeforeConversion/before.csv'
          writeFile = '../../TestFile/AfterConversion/after.xml'

          cv.conversion(readFile, writeFile)

          with open(writeFile) as rf:
               resultValue = rf.read()

          expectedFilePath = '../../TestFile/ExpectedFile/expected.xml'

          with open(expectedFilePath) as xf:
               expectedValue = xf.read()

          self.assertEqual(expectedValue.strip(), resultValue.strip())
     
if __name__ == '__main__':
     unittest.main()