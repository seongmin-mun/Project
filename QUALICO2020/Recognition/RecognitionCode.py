method = "euclidean" #"cosine"   #"euclidean"
for number_window in range(1,11):    #1,11
    # https://www.kaggle.com/gabrielaltay/word-vectors-from-pmi-matrix
    #positive pointwise mutual information
    # from collections import Counter

    total_accuracy = 0

    iter = 100
    for iteration_times in range(0, iter):

        import itertools
        import numpy as np
        import pandas as pd



        ##테스트 데이터 생성

        df_ins = pd.read_csv('./input/Annotated_INS_LO_test.csv')
        df_ins_10 = df_ins.sample(frac=.9)

        sentences_ins_10 = df_ins_10['Sentence'].tolist()

        df_dir = pd.read_csv('./input/Annotated_DIR_LO_test.csv')
        df_dir_10 = df_dir.sample(frac=.9)

        sentences_dir_10 = df_dir_10['Sentence'].tolist()

        test_sentences = []

        for sentence in sentences_ins_10:
            test_sentences.append("INS ### "+sentence)

        for sentence in sentences_dir_10:
            test_sentences.append("DIR ### "+sentence)

        ##테스트 문장 확인
        # for sentence in test_sentences:
        #     print(sentence)


        ##유사도 근거 생성
        similarity_dir = open("./Similarity/window"+str(number_window)+"_ppmi_svd_"+method+"_DIR.txt", "r")  # "w" 쓰기 "r" 읽기
        similarity_cosine_dir = similarity_dir.readlines()
        similarity_dir.close()

        dict_similarity_dir = {}

        for x in similarity_cosine_dir:
            line = x.split(",")
            if dict_similarity_dir.get(line[0].rstrip()) == None:
                dict_similarity_dir[line[0].rstrip()] = line[1].replace("\n", "")

        similarity_ins = open("./Similarity/window" + str(number_window) + "_ppmi_svd_"+method+"_INS.txt", "r")  # "w" 쓰기 "r" 읽기
        similarity_cosine_ins = similarity_ins.readlines()
        similarity_ins.close()

        dict_similarity_ins = {}

        for x in similarity_cosine_ins:
            line = x.split(",")
            if dict_similarity_ins.get(line[0].rstrip()) == None:
                dict_similarity_ins[line[0].rstrip()] = line[1].replace("\n", "")

        ##유사도 값 확인
        # for x, y in dict_similarity_ins.items():
        #     print(x, y)



        ####테스트 문장 유사도 값을 근거로 분류하기
        sen_num = 0
        correct_num = 0
        for sentence in test_sentences:
            input_test = sentence.split(" ### ")
            input_word = input_test[1].split(" ")

            original_class = input_test[0]
            categorized_class = ""

            score_dir = 0
            score_ins = 0

            for eachword in input_word:

                ##DIR 분류값 계산
                if dict_similarity_dir.get(eachword.rstrip()) == None:
                    score_dir = score_dir + 0
                else:
                    score_dir = score_dir + (float(dict_similarity_dir.get(eachword.rstrip())))

                ##INS 분류값 계산
                if dict_similarity_ins.get(eachword.rstrip()) == None:
                    score_ins = score_ins + 0
                else:
                    score_ins = score_ins + (float(dict_similarity_ins.get(eachword.rstrip())))

            if score_dir <= score_ins:
                categorized_class = "INS"
            else:
                categorized_class = "DIR"

            #print(original_class," ",categorized_class," ",score_dir," ",score_ins," ",input_test[1])

            if original_class == categorized_class:
                correct_num = correct_num + 1;

            sen_num = sen_num +1;


        accuracy_score = correct_num/sen_num

        total_accuracy = total_accuracy + accuracy_score


    print(number_window, " : ", total_accuracy / iter)