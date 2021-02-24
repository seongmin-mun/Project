# 모화자와 학습자 데이터 모두 DF으로 합치기

topicNum = "2"
import pandas as pd
docDF = pd.DataFrame(columns=('index', 'documents'))

#한국어 모화자 주제 1에 대한 문서 데이터 로드해서 하나의 라인으로 구성된 문서로 생성


fileDir = "../../Data/essay/NSK/nsk_topic"+topicNum+".txt"
fr = open(fileDir, 'r')
contents = fr.readlines()
fr.close()

Corpus = pd.DataFrame(columns=('index', 'label', 'sentence'))
i = 0
index = ""
sentence = ""
for content in contents:
    index = i
    sentence = content.replace("\n", "").replace("  ", " ").replace(",", "").lstrip().rstrip()
    Corpus.loc[i] = [index, "0", sentence]
    i = i + 1


from Code.Function.DirectoryFiles import directoryFiles_class

DFs = directoryFiles_class("../../Data/essay/L2_t"+topicNum+"")
fileList = DFs.processing()

print(fileList)
#'KSL_1_topic1.txt', 'KSL_21_topic1.txt', 'KSL_16_topic1.txt', 'KSL_30_topic1.txt'

from Code.Function.LinsToLine import linesToLine_class

docNum = 1
for file in fileList:
    l2FileDir = "../../Data/essay/L2_t"+topicNum+"/"+file
    l2fr = open(l2FileDir, 'r')
    l2contents = l2fr.readlines()
    l2fr.close()
    #
    # l2LsTL = linesToLine_class(l2FileDir)
    # l2Line = l2LsTL.processing()
    # l2Line = l2Line.strip()
    #
    # from nltk import PunktSentenceTokenizer
    #
    # tokenizer = PunktSentenceTokenizer()
    # l2contents = tokenizer.tokenize(l2Line)

    for content in l2contents:
        index = i
        sentence = content.replace("\n", "").replace("  ", " ").replace(",", "").lstrip().rstrip()
        print(sentence)
        Corpus.loc[i] = [index, str(docNum), sentence]
        i = i + 1

    docNum = docNum + 1

print(Corpus)

Corpus.to_csv("../../Data/BERT/EssayTopic"+topicNum+".csv")