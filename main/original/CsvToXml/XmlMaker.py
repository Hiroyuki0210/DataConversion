import sys

#各要素のタグをリストに格納
def makeTagList(elementName):
     elementName = elementName.strip()
     elementNameList = []
     tagList = []

     if ',' in elementName:
          elementNameList = elementName.split(',')
     elif elementName != '':
          elementNameList = [elementName]

     for element in elementNameList:
          first = '<' + element + '>'
          last = '</' + element + '>'
          tag = first + last
          tagList.append(tag)

     if len(tagList) == 0:
          print('項目を記入してください')
          sys.exit(1)

     return tagList

#各データ値をリストに格納
def makeValueList(values):
     values = values.strip()
     valueList = []
     if ',' in values:
          valueList = values.split(',')
     elif values != '':
          valueList = [values]

     if len(valueList) == 0:
          print('1組以上のデータを入力してください')
          sys.exit(1)

     return valueList

#タグ間にデータ値を挿入(要素の生成)
def insertValue(tag, value):
     insertionPlace = tag.index('>')
     element = tag[0:insertionPlace+1] + value + tag[insertionPlace+1:len(tag)]
     return element

#要素を作成
def makeElementList(readFile):
     elementList = []
     tags = readFile.readline()
     tagList = makeTagList(tags)
     
     for line in readFile:
          valueList = makeValueList(line)
          eachInf = []
          try:
               if len(valueList) != 0:
                    for i in range(len(tagList)):
                         eachInf.append(insertValue(tagList[i], valueList[i]))
          except IndexError as e:
               print('データ入力数が項目数と一致しません。')
               print(e)
          elementList.append(eachInf)
     
     return elementList

#XML文書の作成
def makeXML(writeFile, elementList):
     writeFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     writeFile.write('<users>\n')

     for eachInf in elementList:
          if len(eachInf) != 0:
               writeFile.write('     ' + '<user>\n')
               for i in range(len(eachInf)):
                    writeFile.write('          ' + eachInf[i] +'\n')
               writeFile.write('     ' + '</user>\n')

     writeFile.write('</users>')