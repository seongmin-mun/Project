class Word2Vec_class:

    def __init__(self, l2File, nskFile, preTrainedModel, outFile, topic):
        self.l2File = l2File
        self.nskFile = nskFile
        self.preTrainedModel = preTrainedModel
        self.outFile = outFile
        self.topic = topic

    def processing(self):

        #https://praveenbezawada.com/2019/03/22/document-similarity-using-gensim-word2vec/

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

        print(docDF.head(5))

        docLines = docDF['documents'].tolist()

        from gensim.corpora import Dictionary
        from gensim.models import LdaModel, Word2Vec, WordEmbeddingSimilarityIndex
        from gensim.similarities import SparseTermSimilarityMatrix


        dictionary = Dictionary(document.split() for document in docLines)

        nskTokens = []

        for word in docLines[0].split():
            nskTokens.append(word)
        print(nskTokens)

        nskBow = dictionary.doc2bow(nskTokens)
        print(nskBow)

        modelWord2VecKo = Word2Vec.load(self.preTrainedModel)  # pre-trained model (https://github.com/Kyubyong/wordvectors)

        similarity_index = WordEmbeddingSimilarityIndex(modelWord2VecKo.wv)
        similarity_matrix = SparseTermSimilarityMatrix(similarity_index, dictionary)

        print("similarity_index: ", similarity_index)
        print("similarity_matrix: ",similarity_matrix)

        cosineSimilarutyList = []

        for i in range(1, len(docLines)):
            l2Tokens = []
            for word in docLines[i].split():
                l2Tokens.append(word)
            print(l2Tokens)

            l2Bow = dictionary.doc2bow(l2Tokens)
            print(l2Bow)
            similarity = similarity_matrix.inner_product(nskBow, l2Bow, normalized=True)
            print(similarity)

            cosineSimilarutyList.append(similarity)

        print(cosineSimilarutyList)

        similarityDF = pd.DataFrame(columns=(fileList))
        similarityDF.loc[0] = cosineSimilarutyList
        print(similarityDF)

        l2TXTList = []
        for i in range(1, len(docLines)):
            l2TXTList.append("KSL_" + str(i) + "_topic" + str(self.topic))

        print(l2TXTList)
        print(similarityDF[l2TXTList[0]+".txt"][0])

        similarDF = pd.DataFrame(columns=('name', 'similarity'))
        for i in range(0, len(l2TXTList)):
            similarDF.loc[i] = [l2TXTList[i], similarityDF[l2TXTList[i] + ".txt"][0]]

        print(similarDF)
        # similarDF.to_csv(self.outFile)

