import unittest
import sys
sys.path.append('../main')
import Converter

#CSV→XML→CSV変換テスト
class ChangeToCsvToXmlTest(unittest.TestCase):
     #初期化処理
     def setup(self):
          pass

     #終了処理
     def teardoen(self):
          pass

     def test_changeToCsvToXml(self):
          cv = Converter.Converter()
          readFile = '../../TestFile/BeforeConversion/before.csv'
          firstWriteFile = '../../TestFile/AfterConversion/after.xml'
          secondWriteFile = '../../TestFile/AfterConversion/after.csv'

          #CSVへの変換
          cv.conversion(readFile, firstWriteFile)
          #XMLへの変換
          cv.conversion(firstWriteFile, secondWriteFile)

          with open(secondWriteFile) as rf:
               resultValue = rf.read()

          expectedFilePath = '../../TestFile/ExpectedFile/expected.csv'
          with open(expectedFilePath) as xf:
               expectedValue = xf.read()

          self.assertEqual(expectedValue.strip(), resultValue.strip())
     
if __name__ == '__main__':
     unittest.main()