import unittest
import sys
from converter import Converter

#XML→CSV変換テスト
class ChangeToCsvTest(unittest.TestCase):
     #初期化処理
     def setup(self):
          pass

     #終了処理
     def teardown(self):
          pass

     def test_changeToCsv(self):
          cv = Converter.Converter()
          readFile = 'sample/BeforeConversion/before.xml'
          writeFile = 'sample/AfterConversion/after.csv'

          cv.conversion(readFile, writeFile)

          with open(writeFile) as rf:
               resultValue = rf.read()

          expectedFilePath = 'sample/ExpectedFile/expected.csv'
          with open(expectedFilePath) as xf:
               expectedValue = xf.read()

          self.assertEqual(expectedValue.strip(), resultValue.strip())
     
if __name__ == '__main__':
     unittest.main()