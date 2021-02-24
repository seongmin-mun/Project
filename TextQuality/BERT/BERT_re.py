class BERT_re_class:

    def __init__(self, tsneDir, outFile, topic, epoch):
        self.tsneDir = tsneDir
        self.outFile = outFile
        self.topic = topic
        self.epoch = epoch

    def processing(self):

        import pandas as pd

        cosineSimilarutyList = []

        for i in range(1,37):
            fileNum = str(i)
            tsneFile = self.tsneDir + "Topic" + str(self.topic) + "_tSNE_"+self.epoch+"_group_" + fileNum + ".csv"
            tsneDF = pd.read_csv(tsneFile,encoding="utf-8")


            nskDF = tsneDF[tsneDF["Label"] == 0]

            xSumnsk = nskDF["X"].sum()
            ySumnsk = nskDF["Y"].sum()

            Xnsk = xSumnsk / len(nskDF)
            Ynsk = ySumnsk / len(nskDF)

            import numpy as np
            from numpy import dot
            from numpy.linalg import norm

            def cos_sim(A, B):
                return dot(A, B) / (norm(A) * norm(B))

            nskArray = np.array([Xnsk, Ynsk])

            def nomalizationMinMax(Inlist):
                List = []
                minValue = min(Inlist)
                maxValue = max(Inlist)
                for i in range(0, len(Inlist)):
                    score = (Inlist[i] - minValue) / (maxValue - minValue)
                    List.append(score)
                return List

            eachDF = tsneDF[tsneDF["Label"] == 1]
            xSum = eachDF["X"].sum()
            ySum = eachDF["Y"].sum()

            centerX = xSum / len(eachDF)
            centerY = ySum / len(eachDF)

            eachArray = np.array([centerX, centerY])
            score = cos_sim(nskArray, eachArray)
            # score = (cos_sim(nskArray, eachArray)+1)/2
            cosineSimilarutyList.append(score)

        cosineSimilarutyList = nomalizationMinMax(cosineSimilarutyList)

        print(cosineSimilarutyList)

        similarDF = pd.DataFrame(columns=('name', 'similarity'))
        for j in range(0, len(cosineSimilarutyList)):
            similarDF.loc[j] = ["KSL_"+str(j+1), cosineSimilarutyList[j]]

        print(similarDF)
        similarDF.to_csv(self.outFile)

