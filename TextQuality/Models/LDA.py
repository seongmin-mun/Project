class LDA_class:

    def __init__(self, l2File, nskFile, numTopic, outFile, topic):
        self.l2File = l2File
        self.nskFile = nskFile
        self.numTopic = numTopic
        self.outFile = outFile
        self.topic = topic

    def processing(self):

        #https://stackoverflow.com/questions/22433884/python-gensim-how-to-calculate-document-similarity-using-the-lda-model

        # 모화자와 학습자 데이터 모두 DF으로 합치기
        import pandas as pd
        docDF = pd.DataFrame(columns=('index', 'documents'))

        #한국어 모화자 주제 1에 대한 문서 데이터 로드해서 하나의 라인으로 구성된 문서로 생성

        from Code.Function.LinsToLine import linesToLine_class

        nskLsTL = linesToLine_class(self.nskFile)
        nskLine = nskLsTL.processing()

        #print(nskLine)

        docDF.loc[0] = [0, nskLine.strip()]

        # 학습자 데이터 정제하기
        # 디렉션에 있는 문서들 리스트로 받아와서 각각의 라인으로 구성된 문서로 생성하기

        from Code.Function.DirectoryFiles import directoryFiles_class

        DFs = directoryFiles_class(self.l2File)
        fileList = DFs.processing()

        #print(fileList)
        #'KSL_1_topic1.txt', 'KSL_21_topic1.txt', 'KSL_16_topic1.txt', 'KSL_30_topic1.txt'

        docNum = 1
        for file in fileList:
            l2FileDir = self.l2File+"/"+file

            l2LsTL = linesToLine_class(l2FileDir)
            l2Line = l2LsTL.processing()

            #print(l2Line)

            docDF.loc[docNum] = [docNum, l2Line.strip()]

            docNum = docNum + 1


        # print(docDF["documents"][0])

        # 하나의 DF로 합쳐진 데이터 정제하기
        docDF['documents'] = docDF['documents'].str.replace(r'[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》\\n\t]+', " ", regex=True)
        docDF['documents'] = docDF['documents'].str.replace(r'\t+', " ", regex=True)
        docDF['documents'] = docDF['documents'].str.replace(r'[\\n]+', " ", regex=True)
        docDF['documents'] = docDF['documents'].str.replace(r'  ', " ", regex=True)

        # print(docDF.head(5))

        docLines = docDF['documents'].tolist()


        #배열 형태로 데이터 정제하기

        documentArray = []

        for i in range(0,len(docDF["documents"])):
            documentArray.append(docDF["documents"][i])

        # print("documentArray: ",documentArray)

        # Convert document to tokens
        docs = [doc.split() for doc in documentArray]

        # print("docs: ", docs)

        # A mapping from token to id in each document
        from gensim.corpora.dictionary import Dictionary
        from gensim.models.ldamodel import LdaModel

        dictionary = Dictionary(docs)

        # print("dictionary: ", dictionary)

        # Representing the corpus as a bag of words
        corpus = [dictionary.doc2bow(doc) for doc in docs]

        # print("corpus: ", corpus)

        # Training the model
        model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=self.numTopic)

        # print("model: ", model)

        nskValue = model.get_document_topics(corpus[0], minimum_probability=0)

        # print("nskValue: ", nskValue[2][0])

        nskValueList = []

        for i in range(0, self.numTopic):
            nskValueList.append(nskValue[i][1])

        import numpy as np
        from numpy import dot
        from numpy.linalg import norm

        def cos_sim(A, B):
            return dot(A, B) / (norm(A) * norm(B))

        cosineSimilarutyList = []

        for i in range(1, len(documentArray)):
            eachL2Value = model.get_document_topics(corpus[i], minimum_probability=0)

            # print("eachL2Value: ", eachL2Value)

            eachL2ValueList = []

            for j in range(0, self.numTopic):
                eachL2ValueList.append(eachL2Value[j][1])

            score = cos_sim(nskValueList, eachL2ValueList)

            # print("score: ", score)
            cosineSimilarutyList.append(score)

        # print(cosineSimilarutyList)

        similarityDF = pd.DataFrame(columns=(fileList))
        similarityDF.loc[0] = cosineSimilarutyList
        # print(similarityDF)

        l2TXTList = []
        for i in range(1, len(docLines)):
            l2TXTList.append("KSL_" + str(i) + "_topic" + str(self.topic))

        # print(l2TXTList)
        # print(similarityDF[l2TXTList[0]+".txt"][0])

        similarDF = pd.DataFrame(columns=('name', 'similarity'))
        for i in range(0, len(l2TXTList)):
            similarDF.loc[i] = [l2TXTList[i], similarityDF[l2TXTList[i] + ".txt"][0]]

        # print(similarDF)
        similarDF.to_csv(self.outFile)




