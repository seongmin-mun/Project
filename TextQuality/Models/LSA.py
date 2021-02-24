class LSA_class:

    def __init__(self, l2File, nskFile, numTopic, outFile, topic):
        self.l2File = l2File
        self.nskFile = nskFile
        self.numTopic = numTopic
        self.outFile = outFile
        self.topic = topic

    def processing(self):

        #https://www.datacamp.com/community/tutorials/discovering-hidden-topics-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034352&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9056144&gclid=Cj0KCQjw7ZL6BRCmARIsAH6XFDJpUhYnTcg3pzf1Lefx9Hb83qPaQ0zp9GAcSnUSxUIspMKS4RfqfC0aAqxjEALw_wcB
        #https://towardsdatascience.com/latent-semantic-analysis-deduce-the-hidden-topic-from-the-document-f360e8c0614b

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


        # print(docDF)

        #하나의 DF로 합쳐진 데이터 정제하기
        docDF['documents'] = docDF['documents'].str.replace(r'[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》\\n\t]+', " ",regex=True)
        docDF['documents'] = docDF['documents'].str.replace(r'\t+', " ", regex=True)
        docDF['documents'] = docDF['documents'].str.replace(r'[\\n]+', " ", regex=True)
        docDF['documents'] = docDF['documents'].str.replace(r'  ', " ", regex=True)

        # print(docDF.head(5))

        docLines = docDF['documents'].tolist()

        from sklearn.feature_extraction.text import TfidfVectorizer

        vectorizer = TfidfVectorizer(encoding='utf-8', lowercase=False, stop_words=None, smooth_idf=True)

        X = vectorizer.fit_transform(docDF['documents'])

        print(X)

        #단어 리스트 (terms) 확인하기
        dictionary = vectorizer.get_feature_names()
        print(dictionary)

        #SVD
        from sklearn.decomposition import TruncatedSVD
        # SVD represent documents and terms in vectors
        svd_model = TruncatedSVD(n_components=self.numTopic, algorithm='randomized', n_iter=100, random_state=122)
        lsa = svd_model.fit_transform(X)

        #토픽수에 따라 토픽넘버 리스트 생성
        topicNumList = []
        for i in range(0,self.numTopic):
            topicNum = i+1
            topicString = "topic_" + str(topicNum)
            topicNumList.append(topicString)

        #print(topicNumList)

        #각 문서들의 토픽 가중치(weight) 확인하기

        pd.options.display.float_format = '{:,.16f}'.format
        topic_encoded_df = pd.DataFrame(lsa, columns=topicNumList)
        topic_encoded_df["documents"] = docDF['documents']
        # print(topic_encoded_df)

        #모화자 문서를 기준으로 다른 문서들간의 유사도 구하기
        from sklearn.metrics.pairwise import cosine_similarity
        import numpy as np
        topic_weight_df = topic_encoded_df[topicNumList]
        # print(len(topic_weight_df))
        # print(topic_weight_df.loc[0])

        nskArray = np.array([topic_weight_df.loc[0]])
        # print(nskArray)

        cosineSimilarutyList = []

        for i in range(1, len(topic_weight_df)):
            eachL2Array = np.array([topic_weight_df.loc[i]])
            score = cosine_similarity(nskArray, eachL2Array)
            #print(score[0][0])
            cosineSimilarutyList.append(score[0][0])

        # print(cosineSimilarutyList)

        similarityDF = pd.DataFrame(columns=(fileList))
        similarityDF.loc[0] = cosineSimilarutyList
        # print(similarityDF)

        l2TXTList = []
        for i in range(1,len(docLines)):
            l2TXTList.append("KSL_"+str(i)+"_topic"+str(self.topic))

        # print(l2TXTList)
        # print(similarityDF[l2TXTList[0]+".txt"][0])

        similarDF = pd.DataFrame(columns=('name', 'similarity'))
        for i in range(0,len(l2TXTList)):
            similarDF.loc[i] = [l2TXTList[i],similarityDF[l2TXTList[i]+".txt"][0]]

        # print(similarDF)
        similarDF.to_csv(self.outFile)

        # further analysis 토픽에 포함된 단어들이 각 토픽에 따라 가지는 가중치 값 계산하기
        # https://iq.opengenus.org/latent-semantic-analysis-for-text-summarization/

