class BERT_class:

    def __init__(self, tsneFile, outFile, topic, ratio):
        self.tsneFile = tsneFile
        self.outFile = outFile
        self.topic = topic
        self.ratio = ratio

    def processing(self):

        import pandas as pd

        from Code.Function.RemoveOutlier import removeOutlier_class

        reviseDF = removeOutlier_class(self.tsneFile, self.ratio)
        tsneDF = reviseDF.processing()

        print(tsneDF)


        nskDF = tsneDF[tsneDF["label"] == str(0)+".0"]
        nskDim0 = (nskDF["dim0"].sum())/len(nskDF)
        nskDim1 = (nskDF["dim1"].sum()) / len(nskDF)
        nskDim2 = (nskDF["dim2"].sum()) / len(nskDF)
        nskDim3 = (nskDF["dim3"].sum()) / len(nskDF)
        nskDim4 = (nskDF["dim4"].sum()) / len(nskDF)
        nskDim5 = (nskDF["dim5"].sum()) / len(nskDF)
        nskDim6 = (nskDF["dim6"].sum()) / len(nskDF)
        nskDim7 = (nskDF["dim7"].sum()) / len(nskDF)
        nskDim8 = (nskDF["dim8"].sum()) / len(nskDF)
        nskDim9 = (nskDF["dim9"].sum()) / len(nskDF)
        nskDim10 = (nskDF["dim10"].sum()) / len(nskDF)
        nskDim11 = (nskDF["dim11"].sum()) / len(nskDF)
        nskDim12 = (nskDF["dim12"].sum()) / len(nskDF)
        nskDim13 = (nskDF["dim13"].sum()) / len(nskDF)
        nskDim14 = (nskDF["dim14"].sum()) / len(nskDF)
        nskDim15 = (nskDF["dim15"].sum()) / len(nskDF)
        nskDim16 = (nskDF["dim16"].sum()) / len(nskDF)
        nskDim17 = (nskDF["dim17"].sum()) / len(nskDF)
        nskDim18 = (nskDF["dim18"].sum()) / len(nskDF)
        nskDim19 = (nskDF["dim19"].sum()) / len(nskDF)
        nskDim20 = (nskDF["dim20"].sum()) / len(nskDF)
        nskDim21 = (nskDF["dim21"].sum()) / len(nskDF)
        nskDim22 = (nskDF["dim22"].sum()) / len(nskDF)
        nskDim23 = (nskDF["dim23"].sum()) / len(nskDF)
        nskDim24 = (nskDF["dim24"].sum()) / len(nskDF)
        nskDim25 = (nskDF["dim25"].sum()) / len(nskDF)
        nskDim26 = (nskDF["dim26"].sum()) / len(nskDF)
        nskDim27 = (nskDF["dim27"].sum()) / len(nskDF)
        nskDim28 = (nskDF["dim28"].sum()) / len(nskDF)
        nskDim29 = (nskDF["dim29"].sum()) / len(nskDF)
        nskDim30 = (nskDF["dim30"].sum()) / len(nskDF)
        nskDim31 = (nskDF["dim31"].sum()) / len(nskDF)
        nskDim32 = (nskDF["dim32"].sum()) / len(nskDF)
        nskDim33 = (nskDF["dim33"].sum()) / len(nskDF)
        nskDim34 = (nskDF["dim34"].sum()) / len(nskDF)
        nskDim35 = (nskDF["dim35"].sum()) / len(nskDF)
        nskDim36 = (nskDF["dim36"].sum()) / len(nskDF)


        import numpy as np
        from numpy import dot
        from numpy.linalg import norm

        def cos_sim(A, B):
            return dot(A, B) / (norm(A) * norm(B))

        nskArray = np.array([nskDim0, nskDim1, nskDim2, nskDim3, nskDim4, nskDim5, nskDim6, nskDim7, nskDim8, nskDim9, nskDim10, nskDim11, nskDim12, nskDim13, nskDim14, nskDim15, nskDim16, nskDim17, nskDim18, nskDim19, nskDim20, nskDim21, nskDim22, nskDim23, nskDim24, nskDim25, nskDim26, nskDim27, nskDim28, nskDim29, nskDim30, nskDim31, nskDim32, nskDim33, nskDim34, nskDim35, nskDim36])

        print(nskArray)

        cosineSimilarutyList = []

        def nomalizationMinMax(Inlist):
            List = []
            minValue = min(Inlist)
            maxValue = max(Inlist)
            for i in range(0,len(Inlist)):
                score = (Inlist[i] - minValue) / (maxValue - minValue)
                List.append(score)
            return List


        for document in range(1,37):

            eachDF = tsneDF[tsneDF["label"]==str(document)+".0"]
            eachDim0 = (eachDF["dim0"].sum()) / len(eachDF)
            eachDim1 = (eachDF["dim1"].sum()) / len(eachDF)
            eachDim2 = (eachDF["dim2"].sum()) / len(eachDF)
            eachDim3 = (eachDF["dim3"].sum()) / len(eachDF)
            eachDim4 = (eachDF["dim4"].sum()) / len(eachDF)
            eachDim5 = (eachDF["dim5"].sum()) / len(eachDF)
            eachDim6 = (eachDF["dim6"].sum()) / len(eachDF)
            eachDim7 = (eachDF["dim7"].sum()) / len(eachDF)
            eachDim8 = (eachDF["dim8"].sum()) / len(eachDF)
            eachDim9 = (eachDF["dim9"].sum()) / len(eachDF)
            eachDim10 = (eachDF["dim10"].sum()) / len(eachDF)
            eachDim11 = (eachDF["dim11"].sum()) / len(eachDF)
            eachDim12 = (eachDF["dim12"].sum()) / len(eachDF)
            eachDim13 = (eachDF["dim13"].sum()) / len(eachDF)
            eachDim14 = (eachDF["dim14"].sum()) / len(eachDF)
            eachDim15 = (eachDF["dim15"].sum()) / len(eachDF)
            eachDim16 = (eachDF["dim16"].sum()) / len(eachDF)
            eachDim17 = (eachDF["dim17"].sum()) / len(eachDF)
            eachDim18 = (eachDF["dim18"].sum()) / len(eachDF)
            eachDim19 = (eachDF["dim19"].sum()) / len(eachDF)
            eachDim20 = (eachDF["dim20"].sum()) / len(eachDF)
            eachDim21 = (eachDF["dim21"].sum()) / len(eachDF)
            eachDim22 = (eachDF["dim22"].sum()) / len(eachDF)
            eachDim23 = (eachDF["dim23"].sum()) / len(eachDF)
            eachDim24 = (eachDF["dim24"].sum()) / len(eachDF)
            eachDim25 = (eachDF["dim25"].sum()) / len(eachDF)
            eachDim26 = (eachDF["dim26"].sum()) / len(eachDF)
            eachDim27 = (eachDF["dim27"].sum()) / len(eachDF)
            eachDim28 = (eachDF["dim28"].sum()) / len(eachDF)
            eachDim29 = (eachDF["dim29"].sum()) / len(eachDF)
            eachDim30 = (eachDF["dim30"].sum()) / len(eachDF)
            eachDim31 = (eachDF["dim31"].sum()) / len(eachDF)
            eachDim32 = (eachDF["dim32"].sum()) / len(eachDF)
            eachDim33 = (eachDF["dim33"].sum()) / len(eachDF)
            eachDim34 = (eachDF["dim34"].sum()) / len(eachDF)
            eachDim35 = (eachDF["dim35"].sum()) / len(eachDF)
            eachDim36 = (eachDF["dim36"].sum()) / len(eachDF)

            eachArray = np.array([eachDim0, eachDim1, eachDim2, eachDim3, eachDim4, eachDim5, eachDim6, eachDim7, eachDim8, eachDim9, eachDim10, eachDim11, eachDim12, eachDim13, eachDim14, eachDim15, eachDim16, eachDim17, eachDim18, eachDim19, eachDim20, eachDim21, eachDim22, eachDim23, eachDim24, eachDim25, eachDim26, eachDim27, eachDim28, eachDim29, eachDim30, eachDim31, eachDim32, eachDim33, eachDim34, eachDim35, eachDim36])
            score = cos_sim(nskArray, eachArray)
            #score = (cos_sim(nskArray, eachArray)+1)/2
            cosineSimilarutyList.append(score)
            # print(score," ",document)

        cosineSimilarutyList = nomalizationMinMax(cosineSimilarutyList)

        print(cosineSimilarutyList)


        similarDF = pd.DataFrame(columns=('name', 'similarity'))
        for i in range(1, 37):
            similarDF.loc[i] = ["KSL_"+str(i), cosineSimilarutyList[i-1]]

        print(similarDF)
        similarDF.to_csv(self.outFile)

