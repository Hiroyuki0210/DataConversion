class CssMaker:
     #コンストラクタ
     def __init__(self, readFile, writeFile):
          self.readFile = readFile
          self.writeFile = writeFile
     
     #フィールド名+フィールド値のセットを取得
     def getFieldSet(self):
          readFile = self.readFile
          fieldSet = []
          flag = False

          with open(readFile) as rf:
               for s in rf:
                    if '<user>' in s:
                         flag = True
                         continue
                    if '</user>' in s:
                         flag = False

                    if flag and ('</' in s):
                         fieldSet.append(s.strip())
          self.fieldSet = fieldSet

     #フィールド名一覧を取得
     def getFieldNameSet(self):
          fieldSet = self.fieldSet
          fieldNameSet = []

          for field in fieldSet:
               fieldName = field[field.index("<") + 1 : field.index(">")]
               fieldNameSet.append(fieldName)
               
          fieldNameSet = list(set(fieldNameSet))

          self.fieldNameSet = fieldNameSet

     #フィールド値一覧を取得
     def getFieldValueSet(self):
          fieldSet = self.fieldSet
          fieldNameSet = self.fieldNameSet
          fieldValue = []
          fieldValueSet = []

          for field in fieldSet:
               fieldValue.append(field[field.index(">") + 1 : field.index("</")])
               if len(fieldValue) == len(fieldNameSet):
                    fieldValueSet.append(fieldValue)
                    fieldValue = []
          
          self.fieldValueSet = fieldValueSet

     #CSV文書の作成
     def makeCSV(self):
          writeFile = self.writeFile
          fieldNameSet = self.fieldNameSet
          fieldValueSet = self.fieldValueSet

          with open(writeFile, mode = 'w') as wf:
               fieldNames = self.joinFieldValues(fieldNameSet)

               wf.write(fieldNames + '\n')

               for fieldValues in fieldValueSet:
                    eachValue = self.joinFieldValues(fieldValues)
                    wf.write(eachValue + '\n')
                    eachValue = ''

     #フィールド名またはフィールド値の","による結合
     def joinFieldValues(self, fieldList):
          value = ''
          for fieldValue in fieldList:
                    if fieldValue != fieldList[len(fieldList)-1]:
                         value += fieldValue + ','
                    else:
                         value += fieldValue
          return value
