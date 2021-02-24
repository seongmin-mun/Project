class removeOutlier_class:

    def __init__(self, tsneFile, ratio):
        self.tsneFile = tsneFile
        self.ratio = ratio

    def processing(self):

        ##https://godongyoung.github.io/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D/2019/03/11/Local-Outlier-Factor(LOF).html

        import numpy as np
        import pandas as pd
        from sklearn.neighbors import LocalOutlierFactor

        fileDir = self.tsneFile
        fr = open(fileDir, 'r')
        contents = fr.readlines()
        fr.close()

        tsnein = pd.DataFrame(columns=('dim0','dim1','dim2','dim3','dim4','dim5','dim6','dim7','dim8','dim9','dim10','dim11','dim12','dim13','dim14','dim15','dim16','dim17','dim18','dim19','dim20','dim21','dim22','dim23','dim24','dim25','dim26','dim27','dim28','dim29','dim30','dim31','dim32','dim33','dim34','dim35','dim36','label'))
        i = 0
        for content in contents:
            if i == 0:
                pass
            else:
                infos = content.split(",")
                label = infos[1]
                dim0 = float(infos[2])
                dim1 = float(infos[3])
                dim2 = float(infos[4])
                dim3 = float(infos[5])
                dim4 = float(infos[6])
                dim5 = float(infos[7])
                dim6 = float(infos[8])
                dim7 = float(infos[9])
                dim8 = float(infos[10])
                dim9 = float(infos[11])
                dim10 = float(infos[12])
                dim11 = float(infos[13])
                dim12 = float(infos[14])
                dim13 = float(infos[15])
                dim14 = float(infos[16])
                dim15 = float(infos[17])
                dim16 = float(infos[18])
                dim17 = float(infos[19])
                dim18 = float(infos[20])
                dim19 = float(infos[21])
                dim20 = float(infos[22])
                dim21 = float(infos[23])
                dim22 = float(infos[24])
                dim23 = float(infos[25])
                dim24 = float(infos[26])
                dim25 = float(infos[27])
                dim26 = float(infos[28])
                dim27 = float(infos[29])
                dim28 = float(infos[30])
                dim29 = float(infos[31])
                dim30 = float(infos[32])
                dim31 = float(infos[33])
                dim32 = float(infos[34])
                dim33 = float(infos[35])
                dim34 = float(infos[36])
                dim35 = float(infos[37])
                dim36 = float(infos[38].replace("\n", ""))
                tsnein.loc[i] = [dim0,dim1,dim2,dim3,dim4,dim5,dim6,dim7,dim8,dim9,dim10,dim11,dim12,dim13,dim14,dim15,dim16,dim17,dim18,dim19,dim20,dim21,dim22,dim23,dim24,dim25,dim26,dim27,dim28,dim29,dim30,dim31,dim32,dim33,dim34,dim35,dim36,label]
            i = i + 1

        # print(tsnein)

        tsneDF = tsnein

        # print(tsneDF)

        final0 = []
        final1 = []
        final2 = []
        final3 = []
        final4 = []
        final5 = []
        final6 = []
        final7 = []
        final8 = []
        final9 = []
        final10 = []
        final11 = []
        final12 = []
        final13 = []
        final14 = []
        final15 = []
        final16 = []
        final17 = []
        final18 = []
        final19 = []
        final20 = []
        final21 = []
        final22 = []
        final23 = []
        final24 = []
        final25 = []
        final26 = []
        final27 = []
        final28 = []
        final29 = []
        final30 = []
        final31 = []
        final32 = []
        final33 = []
        final34 = []
        final35 = []
        final36 = []
        finalLabel = []

        indexNum = 0

        for document in range(0, 37):
            eachDF = tsneDF[tsneDF["label"] == str(document)+".0"]

            array = []

            # print(eachDF)
            #
            #print(len(eachDF),(indexNum+1),((indexNum+1)+(len(eachDF))))

            for i in range((indexNum+1),((indexNum+1)+(len(eachDF)))):

                # print(eachDF.loc[i]["dim0"])
                arrayinner = []
                arrayinner.append(eachDF.loc[i]["dim0"])
                arrayinner.append(eachDF.loc[i]["dim1"])
                arrayinner.append(eachDF.loc[i]["dim2"])
                arrayinner.append(eachDF.loc[i]["dim3"])
                arrayinner.append(eachDF.loc[i]["dim4"])
                arrayinner.append(eachDF.loc[i]["dim5"])
                arrayinner.append(eachDF.loc[i]["dim6"])
                arrayinner.append(eachDF.loc[i]["dim7"])
                arrayinner.append(eachDF.loc[i]["dim8"])
                arrayinner.append(eachDF.loc[i]["dim9"])
                arrayinner.append(eachDF.loc[i]["dim10"])
                arrayinner.append(eachDF.loc[i]["dim11"])
                arrayinner.append(eachDF.loc[i]["dim12"])
                arrayinner.append(eachDF.loc[i]["dim13"])
                arrayinner.append(eachDF.loc[i]["dim14"])
                arrayinner.append(eachDF.loc[i]["dim15"])
                arrayinner.append(eachDF.loc[i]["dim16"])
                arrayinner.append(eachDF.loc[i]["dim17"])
                arrayinner.append(eachDF.loc[i]["dim18"])
                arrayinner.append(eachDF.loc[i]["dim19"])
                arrayinner.append(eachDF.loc[i]["dim20"])
                arrayinner.append(eachDF.loc[i]["dim21"])
                arrayinner.append(eachDF.loc[i]["dim22"])
                arrayinner.append(eachDF.loc[i]["dim23"])
                arrayinner.append(eachDF.loc[i]["dim24"])
                arrayinner.append(eachDF.loc[i]["dim25"])
                arrayinner.append(eachDF.loc[i]["dim26"])
                arrayinner.append(eachDF.loc[i]["dim27"])
                arrayinner.append(eachDF.loc[i]["dim28"])
                arrayinner.append(eachDF.loc[i]["dim29"])
                arrayinner.append(eachDF.loc[i]["dim30"])
                arrayinner.append(eachDF.loc[i]["dim31"])
                arrayinner.append(eachDF.loc[i]["dim32"])
                arrayinner.append(eachDF.loc[i]["dim33"])
                arrayinner.append(eachDF.loc[i]["dim34"])
                arrayinner.append(eachDF.loc[i]["dim35"])
                arrayinner.append(eachDF.loc[i]["dim36"])
                # print(arrayinner)
                array.append(arrayinner)
            # print(array)

            # print(len(array))

            ground_truth = np.ones(len(array), dtype=int)
            clf = LocalOutlierFactor(n_neighbors=round(len(array)*0.5), contamination=self.ratio)
            y_pred = clf.fit_predict(array)
            n_errors = (y_pred != ground_truth).sum()
            X_scores = clf.negative_outlier_factor_
            # print(y_pred)
            # print(len(y_pred))

            varNum = 0
            for i in range(0,len(y_pred)):
                if y_pred[i] == 1:
                    # print(y_pred[i])
                    final0.append(eachDF.loc[(indexNum+1)+i]["dim0"])
                    final1.append(eachDF.loc[(indexNum + 1) + i]["dim1"])
                    final2.append(eachDF.loc[(indexNum + 1) + i]["dim2"])
                    final3.append(eachDF.loc[(indexNum + 1) + i]["dim3"])
                    final4.append(eachDF.loc[(indexNum + 1) + i]["dim4"])
                    final5.append(eachDF.loc[(indexNum + 1) + i]["dim5"])
                    final6.append(eachDF.loc[(indexNum + 1) + i]["dim6"])
                    final7.append(eachDF.loc[(indexNum + 1) + i]["dim7"])
                    final8.append(eachDF.loc[(indexNum + 1) + i]["dim8"])
                    final9.append(eachDF.loc[(indexNum + 1) + i]["dim9"])
                    final10.append(eachDF.loc[(indexNum + 1) + i]["dim10"])
                    final11.append(eachDF.loc[(indexNum + 1) + i]["dim11"])
                    final12.append(eachDF.loc[(indexNum + 1) + i]["dim12"])
                    final13.append(eachDF.loc[(indexNum + 1) + i]["dim13"])
                    final14.append(eachDF.loc[(indexNum + 1) + i]["dim14"])
                    final15.append(eachDF.loc[(indexNum + 1) + i]["dim15"])
                    final16.append(eachDF.loc[(indexNum + 1) + i]["dim16"])
                    final17.append(eachDF.loc[(indexNum + 1) + i]["dim17"])
                    final18.append(eachDF.loc[(indexNum + 1) + i]["dim18"])
                    final19.append(eachDF.loc[(indexNum + 1) + i]["dim19"])
                    final20.append(eachDF.loc[(indexNum + 1) + i]["dim20"])
                    final21.append(eachDF.loc[(indexNum + 1) + i]["dim21"])
                    final22.append(eachDF.loc[(indexNum + 1) + i]["dim22"])
                    final23.append(eachDF.loc[(indexNum + 1) + i]["dim23"])
                    final24.append(eachDF.loc[(indexNum + 1) + i]["dim24"])
                    final25.append(eachDF.loc[(indexNum + 1) + i]["dim25"])
                    final26.append(eachDF.loc[(indexNum + 1) + i]["dim26"])
                    final27.append(eachDF.loc[(indexNum + 1) + i]["dim27"])
                    final28.append(eachDF.loc[(indexNum + 1) + i]["dim28"])
                    final29.append(eachDF.loc[(indexNum + 1) + i]["dim29"])
                    final30.append(eachDF.loc[(indexNum + 1) + i]["dim30"])
                    final31.append(eachDF.loc[(indexNum + 1) + i]["dim31"])
                    final32.append(eachDF.loc[(indexNum + 1) + i]["dim32"])
                    final33.append(eachDF.loc[(indexNum + 1) + i]["dim33"])
                    final34.append(eachDF.loc[(indexNum + 1) + i]["dim34"])
                    final35.append(eachDF.loc[(indexNum + 1) + i]["dim35"])
                    final36.append(eachDF.loc[(indexNum + 1) + i]["dim36"])
                    finalLabel.append(eachDF.loc[(indexNum+1) + i]["label"])

                varNum = varNum + 1


            indexNum = indexNum + varNum

        # print(finalX)
        # print(finalY)
        # print(finalLabel)

        tsneFinalDF = pd.DataFrame(columns=('dim0','dim1','dim2','dim3','dim4','dim5','dim6','dim7','dim8','dim9','dim10','dim11','dim12','dim13','dim14','dim15','dim16','dim17','dim18','dim19','dim20','dim21','dim22','dim23','dim24','dim25','dim26','dim27','dim28','dim29','dim30','dim31','dim32','dim33','dim34','dim35','dim36','label'))

        for numID in range(0,len(final0)):
            tsneFinalDF.loc[numID] = [final0[numID], final1[numID], final2[numID], final3[numID], final4[numID], final5[numID], final6[numID], final7[numID], final8[numID], final9[numID], final10[numID], final11[numID], final12[numID], final13[numID], final14[numID], final15[numID], final16[numID], final17[numID], final18[numID], final19[numID], final20[numID], final21[numID], final22[numID], final23[numID], final24[numID], final25[numID], final26[numID], final27[numID], final28[numID], final29[numID], final30[numID], final31[numID], final32[numID], final33[numID], final34[numID], final35[numID], final36[numID], finalLabel[numID]]

        #print(tsneFinalDF)

        return tsneFinalDF
