class bayes_process:

    def setdata(self, iteration, estimator, smoothing, sequencerange, estimator_test, sequencerange_test):
        self.iteration = iteration
        self.estimator = estimator
        self.smoothing = smoothing
        self.sequencerange = sequencerange
        self.estimator_test = estimator_test
        self.sequencerange_test = sequencerange_test

    def bayes_process_inner(self):

        print("반복 횟수 : ",self.iteration)
        print("추정량 : ",self.estimator)
        print("스무딩 : ",self.smoothing)
        print("연속 N값(워킹메모리) : ",self.sequencerange)
        print("테스트 추정량 : ", self.estimator_test)
        print("테스트 연속 N값(워킹메모리) : ", self.sequencerange_test)

        #트레이닝에 사용되는 문장을 생성하는 곳; 각 구문의 빈도에 따라 생성
        input_dic = {}

        # #스무딩 방법에 따라 학습데이터 달리 생성하기
        # if self.smoothing == 0:
        #     # print("Origin")
        #     from Functions.TrainingSet import training_dictionary
        #     training_generator = training_dictionary()
        #     for key, value in training_generator.training_dictionary_inner().items():
        #         input_dic[key] = value
        #
        # if self.smoothing == 1:
        #     # print("Laplace")
        #     from Functions.TrainingSet import training_dictionary
        #     training_generator = training_dictionary()
        #     for key, value in training_generator.training_dictionary_inner_laplace().items():
        #         input_dic[key] = value

        #스무딩 방법과 상관없이 학습데이터에 1을 기본값으로 주고 학습 데이터 생성
        from Functions.TrainingSet import training_dictionary
        training_generator = training_dictionary()
        for key, value in training_generator.training_dictionary_inner_laplace().items():
            input_dic[key] = value


        # print(input_dic)

        # 공통 초기의 데이터 목록
        from Data.AllData import alldatasets
        data = alldatasets()

        constructions = data.input_construction()
        constructions_sentence = data.input_constructions_sentence()
        itemsfreqdict = data.input_itemsfreqdict()
        itemssquenfreq = data.input_itemssquenfreq()
        bignames = data.bigNames()

        # print("constructions ",constructions)
        # print("constructions_sentence ",constructions_sentence)
        # print("itemsfreqdict ",itemsfreqdict)
        # print("itemssquenfreq ",itemssquenfreq)
        # print("bignames ", bignames)

        # 스무딩 방법에 따라 초기 값 달리 생성하기

        # 초기 빈도값 -> 판별 결과에 따라 업데이트 될 예정
        initial_num = 0
        initial_input_freq = []
        initial_construction_freq = {}
        initial_itemsfreqdict = {}
        input_sizenum = 0


        if self.smoothing == 0:
            input_sizenum = input_sizenum + data.origin_num()
            initial_num = initial_num + data.origin_num()
            for value in data.input_freq():  #배열(list)를 돌면서 값 추가하기
                initial_input_freq.append(value)
            for key, value in data.origin_construction_freq().items(): # 사전(dictionary)를 돌면서 값 추가하기
                initial_construction_freq[key] = value
            for key, value in data.origin_itemsfreqdict().items():  # 사전(dictionary)를 돌면서 값 추가하기
                initial_itemsfreqdict[key] = value


        if self.smoothing == 1:
            input_sizenum = input_sizenum + data.laplace_num()
            initial_num = initial_num + data.laplace_num()
            for value in data.input_freq_laplace():
                initial_input_freq.append(value)
            for key, value in data.laplace_construction_freq().items():
                initial_construction_freq[key] = value
            for key, value in data.laplace_itemsfreqdict().items():
                initial_itemsfreqdict[key] = value

        # print("initial_num ",initial_num)
        # print("initial_input_freq ", initial_input_freq)
        # print("initial_construction_freq", initial_construction_freq)
        # print("initial_itemsfreqdict ", initial_itemsfreqdict)

        # 학습을 하는 구간

        for i in range(0, self.iteration):
            print("\n반복 횟수: ", i + 1)

            # 정확히 판단한 경우 빈도
            accuracy_num = 0

            # 학습을 위해 인풋 사전의 데이터를 하나씩 순서대로 받아온다.
            for x in range(0, input_sizenum):

                #input_dic을 가져와 개별 아이템으로 생성
                items = input_dic[str(x)].split(" ### ")
                origin_class = items[0]
                itembefore = items[1].replace("\n", "").replace("\u200b", "")
                item = itembefore.split(" ")

                # 문장의 구조에 따라 계산된 사후 확률을 받는 부분 -> 판별의 기준으로 사용된다.
                classified_constructions = {}

                num_item = 1
                proba = 1

                squenitem = ""

                for each in item:  # 각각의 인풋 아이템들 선출  #인풋 아이템 각각을 받아서 아이템별 구조의 빈도를 업데이트 하는 위치

                    # .strip() [양옆 스페이스, 탭 문자, 줄 바꿈(\r 또는 \n)을 삭제] .lstrip() [왼쪽만] .rstrip() [오른쪽만]

                    # 개별 확률을 곱하는 부분 / 연속 확률을 곱하는 부분
                    total = itemssquenfreq[num_item]
                    child = itemsfreqdict[str(num_item).rstrip()][each.rstrip()]
                    in_prob = child / total
                    # proba = proba * in_prob # 연속될 확률을 누적해서 구하는 부분
                    proba = in_prob # 해당 아이템이 해당 순서에서 등장할 확률
                    squenitem = squenitem + " " + each

                    #print("before ", squenitem)


                    # 워킹 메모리의 값을 지정했는지 확인
                    if  self.sequencerange == 0:
                        # print("self.sequencerange = 0")
                        squenitem = squenitem.strip()
                        # 각각의 아이템들의 전체 빈도수 계산
                        item_total = 0
                        for construc in constructions:
                            construc = construc.replace("\u200b", "")
                            item_total = item_total + int(initial_itemsfreqdict[each][construc])

                        for construc in constructions:  # 인풋 아이템들이 각각의 구조에서 등장하는 빈도
                            construc = construc.replace("\u200b", "")
                            # 각 구조별 확률 P_BA
                            construc_prob = float(initial_construction_freq[construc] / initial_num)

                            # 워킹 메모리를 따로 지정하지 않은 경우 아이템이 등장하는 확률은 계산하지 않음
                            item_squen_prob = float((initial_itemsfreqdict[each][construc] / item_total))

                            P_B = (float(construc_prob) * item_squen_prob) + ((1 - construc_prob) * (1 - item_squen_prob))
                            P_AB = ((float(construc_prob) * item_squen_prob) / P_B)

                            # passive 가중치 주기 / weight (psv)
                            if "passive" in construc.strip():
                                P_AB = P_AB - 0.000000000000001703
                                if "undergoer&nom" in each.strip():
                                    P_AB = P_AB - 0.04754
                                if "actor&dat" in each.strip():
                                    P_AB = P_AB + 0.9975
                                if "V&i/hi/li/ki" in each.strip():
                                    P_AB = P_AB + 0.05
                                if "undergoer&nom N&eykey/hanthey" in itembefore.strip():
                                    if "N&eykey/hanthey" in each.strip():
                                        P_AB = P_AB + 0.4706
                                if "actor&dat V&i/hi/li/ki" in itembefore.strip():
                                    if "V&i/hi/li/ki" in each.strip():
                                        P_AB = P_AB - 0.9706

                            if classified_constructions.get(construc.strip()) == None:
                                classified_constructions[construc.strip()] = P_AB
                            else:
                                classified_constructions[construc.strip()] = classified_constructions.get(construc.strip()) + P_AB
                    else :
                        if self.sequencerange == 1:  # 워킹 메모리가 1인 경우
                            # print("self.sequencerange = 1")
                            squenitem = squenitem.strip()
                            if (squenitem.rstrip() != None) & (" " in squenitem.strip()):
                                squenitems = squenitem.rstrip().split(" ")
                                squenitem = squenitems[len(squenitems) - 1]
                                # print(squenitem)
                            else :
                                squenitem = squenitem.rstrip()
                                # print(squenitem)

                        else : # 워킹 메모리가 1 이상인 경우
                            # print("self.sequencerange = other ", squenitem.strip())
                            # if " " in squenitem.strip():
                            #     print("None")

                            if (squenitem.strip() != None) & (" " in squenitem.strip()):  # 값이 있고 공백을 포함하는 경우
                                squenitems = squenitem.split(" ")
                                workingSpace = " "
                                for j in range(0, self.sequencerange): # 0 1 2
                                    try:
                                        if squenitems[len(squenitems) - (1 + j)] == None:
                                            pass
                                        else:
                                            workingSpace = " " + squenitems[len(squenitems) - (1 + j)] + workingSpace
                                    except IndexError:
                                        pass


                                squenitem = workingSpace.strip()
                                # print(squenitem)
                            else :
                                squenitem = squenitem.strip()
                                # print(squenitem)



                        # 각각의 아이템들의 전체 빈도수 계산
                        item_total = 0
                        for construc in constructions:
                            construc = construc.replace("\u200b", "")
                            item_total = item_total + int(initial_itemsfreqdict[each][construc])

                        for construc in constructions:  # 인풋 아이템들이 각각의 구조에서 등장하는 빈도
                            construc = construc.replace("\u200b", "")
                            # 각 구조별 확률 P_BA
                            construc_prob = float(initial_construction_freq[construc] / initial_num)

                            # 아이템이 연속으로 등장 할 확률 * 개별 아이템이 등장할 확률
                            if constructions_sentence.get(construc.rstrip()).find(squenitem.rstrip())== -1: #연속된 부분이 없는 경우
                                item_squen_prob = float((initial_itemsfreqdict[each][construc] / item_total) * 0)
                            else:
                                item_squen_prob = float((initial_itemsfreqdict[each][construc] / item_total) * proba)

                            P_B = (float(construc_prob) * item_squen_prob) + ((1 - construc_prob) * (1 - item_squen_prob))
                            P_AB = ((float(construc_prob) * item_squen_prob) / P_B)

                            # passive 가중치 주기 / weight (psv)
                            if "passive" in construc.strip():
                                P_AB = P_AB - 0.000000000000001703
                                if "undergoer&nom" in each.strip():
                                    P_AB = P_AB - 0.04754
                                if "actor&dat" in each.strip():
                                    P_AB = P_AB + 0.9975
                                if "V&i/hi/li/ki" in each.strip():
                                    P_AB = P_AB + 0.05
                                if "undergoer&nom N&eykey/hanthey" in itembefore.strip():
                                    if "N&eykey/hanthey" in each.strip():
                                        P_AB = P_AB + 0.4706
                                if "actor&dat V&i/hi/li/ki" in itembefore.strip():
                                    if "V&i/hi/li/ki" in each.strip():
                                        P_AB = P_AB - 0.9706


                            if classified_constructions.get(construc.rstrip()) == None:
                                classified_constructions[construc.rstrip()] = P_AB
                            else:
                                classified_constructions[construc.rstrip()] = classified_constructions.get(
                                    construc.rstrip()) + P_AB

                    num_item += 1

                # 해당 문장이 포함될 확률이 가장 높은 문장 추출 (추정량 사용)
                def mid(lst):
                    return [i for i in sorted(lst)][len(lst) // 2]
                dic_min = min(classified_constructions.values())
                dic_mid = mid(classified_constructions.values())
                dic_max = max(classified_constructions.values())

                # print("dic_min ",dic_min)
                # print("dic_mid ", dic_mid)
                # print("dic_max ", dic_max)

                for x1, y1 in classified_constructions.items():
                    # 추정량을 계산하는 방법에 따라서 계산하
                    if self.estimator == 0:
                        if y1 == dic_min:

                            # 원래 문장의 구조와 판별된 문장의 구조를 나란히 보여준다.
                            # print(origin_class, " : ", x1)

                            # 정확도 계산을 위한 부분
                            if origin_class == x1:
                                accuracy_num = accuracy_num + 1

                            ############판별이 정확하지 않은 문장
                            # if origin_class != x1:
                            # print(origin_class, " : ", x1)

                            ############판별 결과에 관계없이 빈도를 업데이트한다.###########

                            # 판별한 곳으로 업데이트
                            # 전체 빈도 및 판별된 분류 값에 빈도수를 업데이트
                            initial_num = initial_num + 1
                            initial_construction_freq[x1.rstrip()] = initial_construction_freq.get(x1.rstrip()) + 1

                            # 아이템별 구조에 따른 확률 업데이트
                            for each in item:  # 각각의 인풋 아이템들 선출
                                initial_itemsfreqdict[each][x1] = initial_itemsfreqdict[each][x1] + 1

                            # # 판별이 정확할 경우에 업데이트
                            # # 전체 빈도 및 판별된 분류 값에 빈도수를 업데이트
                            # if origin_class == x1:
                            #     initial_num = initial_num + 1
                            #     initial_construction_freq[x1.rstrip()] = initial_construction_freq.get(x1.rstrip()) + 1
                            #
                            # # 아이템별 구조에 따른 확률 업데이트
                            # if origin_class == x1:
                            #     for each in item:  # 각각의 인풋 아이템들 선출
                            #         initial_itemsfreqdict[each][x1] = initial_itemsfreqdict[each][x1] + 1

                    if self.estimator == 1:
                        if y1 == dic_mid:

                            # 원래 문장의 구조와 판별된 문장의 구조를 나란히 보여준다.
                            # print(origin_class, " : ", x1)

                            # 정확도 계산을 위한 부분
                            if origin_class == x1:
                                accuracy_num = accuracy_num + 1

                            ############판별이 정확하지 않은 문장
                            # if origin_class != x1:
                            # print(origin_class, " : ", x1)

                            ############판별 결과에 관계없이 빈도를 업데이트한다.###########

                            # 판별한 곳으로 업데이트
                            # 전체 빈도 및 판별된 분류 값에 빈도수를 업데이트
                            initial_num = initial_num + 1
                            initial_construction_freq[x1.rstrip()] = initial_construction_freq.get(x1.rstrip()) + 1

                            # 아이템별 구조에 따른 확률 업데이트
                            for each in item:  # 각각의 인풋 아이템들 선출
                                initial_itemsfreqdict[each][x1] = initial_itemsfreqdict[each][x1] + 1

                            # # 판별이 정확할 경우에 업데이트
                            # # 전체 빈도 및 판별된 분류 값에 빈도수를 업데이트
                            # if origin_class == x1:
                            #     initial_num = initial_num + 1
                            #     initial_construction_freq[x1.rstrip()] = initial_construction_freq.get(x1.rstrip()) + 1
                            #
                            # # 아이템별 구조에 따른 확률 업데이트
                            # if origin_class == x1:
                            #     for each in item:  # 각각의 인풋 아이템들 선출
                            #         initial_itemsfreqdict[each][x1] = initial_itemsfreqdict[each][x1] + 1

                    if self.estimator == 2:
                        if y1 == dic_max:

                            # 원래 문장의 구조와 판별된 문장의 구조를 나란히 보여준다.
                            # print(origin_class, " : ", x1)

                            # 정확도 계산을 위한 부분
                            if origin_class == x1:
                                accuracy_num = accuracy_num + 1

                            ############판별이 정확하지 않은 문장
                            # if origin_class != x1:
                            # print(origin_class, " : ", x1)

                            ############판별 결과에 관계없이 빈도를 업데이트한다.###########

                            # 판별한 곳으로 업데이트
                            # 전체 빈도 및 판별된 분류 값에 빈도수를 업데이트
                            initial_num = initial_num + 1
                            initial_construction_freq[x1.rstrip()] = initial_construction_freq.get(x1.rstrip()) + 1

                            # 아이템별 구조에 따른 확률 업데이트
                            for each in item:  # 각각의 인풋 아이템들 선출
                                initial_itemsfreqdict[each][x1] = initial_itemsfreqdict[each][x1] + 1

                            # # 판별이 정확할 경우에 업데이트
                            # # 전체 빈도 및 판별된 분류 값에 빈도수를 업데이트
                            # if origin_class == x1:
                            #     initial_num = initial_num + 1
                            #     initial_construction_freq[x1.rstrip()] = initial_construction_freq.get(x1.rstrip()) + 1
                            #
                            # # 아이템별 구조에 따른 확률 업데이트
                            # if origin_class == x1:
                            #     for each in item:  # 각각의 인풋 아이템들 선출
                            #         initial_itemsfreqdict[each][x1] = initial_itemsfreqdict[each][x1] + 1

                # print(initial_itemsfreqdict)

            # 정확도 계산
            print("판별 정확도 : ", accuracy_num / input_sizenum)

            # 사후확률
            # print(initial_construction_freq)
            # print("전체 누적 빈도 수 : ", initial_num)
            print("\n각 구문별 업데이트 된 사후 확률:")
            for x, y in initial_construction_freq.items():
                print(x, " : ", float(y / initial_num))
            print("\n테스트 문장 판별 결과\n")

            test_construction = data.test_construction()
            test_constructions_sentence = data.test_constructions_sentence()

            # print(test_construction)
            # print(test_constructions_sentence)

            ################ 형태를 기반으로 의미를 추론하는 부분 ################

            accuracy_num_test = 0
            accuracy_bignames_num_test = 0

            for construc_test in test_construction:
                test_sen = test_constructions_sentence.get(construc_test.replace("\u200b", "").rstrip())
                test_item = test_sen.split(" ")

                origin_class_test = str(construc_test).replace("\u200b", "").rstrip()

                predict_num_item = 1
                predict_squenitem = ""


                for predict_each in test_item:

                    squenceforpredict = {}

                    test_squen_target = predict_each.replace("\u200b", "").rstrip()

                    # 인풋데이터의 문장 구조를 확인하여 의미를 추론하는 부분
                    for input_key, input_value in data.input_constructions_sentence().items():  # 사전(dictionary)를 돌면서 값 추가하기
                        # print("input_key ",input_key," input_value ",input_value)
                        input_value_item = input_value.split(" ")

                        if (predict_num_item <= len(input_value_item)):
                            if input_value_item[predict_num_item - 1].replace("\u200b", "").rstrip() == test_squen_target:
                                # print(input_key," next ",input_value_item[num_item].replace("\u200b", "").rstrip())
                                # 해당 순번 아이템의 구문 유형 빈도수
                                # print(" initial_construction_freq[input_key] ",initial_construction_freq[input_key])
                                # 해당 순번 아이템의 추론되는 의미의 구문 유형에 따른 빈도수
                                # print(" initial_itemsfreqdict[input_value_item[num_item]][input_key] ", initial_itemsfreqdict[input_value_item[num_item].replace("\u200b", "").rstrip()][input_key])

                                # 순번에 따른 아이템의 의미로 추론되는 의미들과 그 의미들이 해당 구문에서 가지는 빈도수의 총합
                                meaning = input_value_item[predict_num_item].replace("\u200b", "").rstrip()
                                if squenceforpredict.get(meaning) == None:
                                    squenceforpredict[meaning] = initial_itemsfreqdict[meaning][input_key]
                                else:
                                    squenceforpredict[meaning] = squenceforpredict.get(meaning) + \
                                                                 initial_itemsfreqdict[meaning][input_key]

                    squenceforpredict_max = max(squenceforpredict.values())

                    for squence_key, squence_value in squenceforpredict.items():
                        if squence_value == squenceforpredict_max:
                            predict_squenitem = predict_squenitem + predict_each + " " + squence_key + " "

                    predict_num_item += 2

                construc_binnames_test = ""

                for key, value in bignames.items():
                    for construcType in value:
                        if construc_test == construcType:
                            construc_binnames_test = construc_binnames_test+key

                print("테스트를 위해 인풋된 문장 유형과 문장 : ",construc_test," (",construc_binnames_test,") ",test_sen," 형태를 기반으로 의미가 예측된 형태 : ", predict_squenitem.rstrip())



                #추론된 의미를 사용하여 테스트 문장을 판별하는 곳

                # 문장의 구조에 따라 계산된 사후 확률을 받는 부분 -> 판별의 기준으로 사용된다.
                classified_constructions_test = {}

                test_item_formmeaning = predict_squenitem.rstrip().split(" ")

                num_item = 1
                squenitem = ""

                for each in test_item_formmeaning:

                    each = each.replace("\u200b", "").rstrip()

                    # 개별 확률을 곱하는 부분 / 연속 확률을 곱하는 부분
                    total = itemssquenfreq[num_item]
                    child = itemsfreqdict[str(num_item).rstrip()][each]
                    in_prob = child / total
                    # proba = proba * in_prob # 연속될 확률을 누적해서 구하는 부분
                    proba = in_prob # 해당 아이템이 해당 순서에서 등장할 확률
                    squenitem = squenitem + " " + each

                    #print("before ", squenitem)


                    # 워킹 메모리의 값을 지정했는지 확인
                    if  self.sequencerange_test == 0:
                        # print("self.sequencerange = 0")
                        squenitem = squenitem.strip()
                        # 각각의 아이템들의 전체 빈도수 계산
                        item_total = 0
                        for construc in constructions:
                            construc = construc.replace("\u200b", "")
                            item_total = item_total + int(initial_itemsfreqdict[each][construc])

                        for construc in constructions:  # 인풋 아이템들이 각각의 구조에서 등장하는 빈도
                            construc = construc.replace("\u200b", "")
                            # 각 구조별 확률 P_BA
                            construc_prob = float(initial_construction_freq[construc] / initial_num)

                            # 워킹 메모리를 따로 지정하지 않은 경우 아이템이 등장하는 확률은 계산하지 않음
                            item_squen_prob = float((initial_itemsfreqdict[each][construc] / item_total))

                            P_B = (float(construc_prob) * item_squen_prob) + ((1 - construc_prob) * (1 - item_squen_prob))
                            P_AB = ((float(construc_prob) * item_squen_prob) / P_B)

                            # passive 가중치 주기 / weight (psv)
                            if "passive" in construc.strip():
                                P_AB = P_AB - 0.000000000000001703
                                if "undergoer&nom" in each.strip():
                                    P_AB = P_AB - 0.04754
                                if "actor&dat" in each.strip():
                                    P_AB = P_AB + 0.9975
                                if "V&i/hi/li/ki" in each.strip():
                                    P_AB = P_AB + 0.05
                                if "undergoer&nom N&eykey/hanthey" in predict_squenitem.strip():
                                    if "N&eykey/hanthey" in each.strip():
                                        P_AB = P_AB + 0.4706
                                if "actor&dat V&i/hi/li/ki" in predict_squenitem.strip():
                                    if "V&i/hi/li/ki" in each.strip():
                                        P_AB = P_AB - 0.9706


                            if classified_constructions_test.get(construc.strip()) == None:
                                classified_constructions_test[construc.strip()] = P_AB
                            else:
                                classified_constructions_test[construc.strip()] = classified_constructions_test.get(construc.strip()) + P_AB
                    else :
                        if self.sequencerange_test == 1:  # 워킹 메모리가 1인 경우
                            # print("self.sequencerange = 1")
                            squenitem = squenitem.strip()
                            if (squenitem.rstrip() != None) & (" " in squenitem.strip()):
                                squenitems = squenitem.rstrip().split(" ")
                                squenitem = squenitems[len(squenitems) - 1]
                                # print(squenitem)
                            else :
                                squenitem = squenitem.rstrip()
                                # print(squenitem)

                        else : # 워킹 메모리가 1 이상인 경우
                            # print("self.sequencerange = other ", squenitem.strip())
                            # if " " in squenitem.strip():
                            #     print("None")

                            if (squenitem.strip() != None) & (" " in squenitem.strip()):  # 값이 있고 공백을 포함하는 경우
                                squenitems = squenitem.split(" ")
                                workingSpace = " "
                                for j in range(0, self.sequencerange_test): # 0 1 2
                                    try:
                                        if squenitems[len(squenitems) - (1 + j)] == None:
                                            pass
                                        else:
                                            workingSpace = " " + squenitems[len(squenitems) - (1 + j)] + workingSpace
                                    except IndexError:
                                        pass


                                squenitem = workingSpace.strip()
                                # print(squenitem)
                            else :
                                squenitem = squenitem.strip()
                                # print(squenitem)



                        # 각각의 아이템들의 전체 빈도수 계산
                        item_total = 0
                        for construc in constructions:
                            construc = construc.replace("\u200b", "")
                            item_total = item_total + int(initial_itemsfreqdict[each][construc])

                        for construc in constructions:  # 인풋 아이템들이 각각의 구조에서 등장하는 빈도
                            construc = construc.replace("\u200b", "")
                            # 각 구조별 확률 P_BA
                            construc_prob = float(initial_construction_freq[construc] / initial_num)

                            # 아이템이 연속으로 등장 할 확률 * 개별 아이템이 등장할 확률
                            if constructions_sentence.get(construc.rstrip()).find(squenitem.rstrip())== -1: #연속된 부분이 없는 경우
                                item_squen_prob = float((initial_itemsfreqdict[each][construc] / item_total) * 0)
                            else:
                                item_squen_prob = float((initial_itemsfreqdict[each][construc] / item_total) * proba)

                            P_B = (float(construc_prob) * item_squen_prob) + ((1 - construc_prob) * (1 - item_squen_prob))
                            P_AB = ((float(construc_prob) * item_squen_prob) / P_B)

                            # passive 가중치 주기 / weight (psv)
                            if "passive" in construc.strip():
                                P_AB = P_AB - 0.000000000000001703
                                if "undergoer&nom" in each.strip():
                                    P_AB = P_AB - 0.04754
                                if "actor&dat" in each.strip():
                                    P_AB = P_AB + 0.9975
                                if "V&i/hi/li/ki" in each.strip():
                                    P_AB = P_AB + 0.05
                                if "undergoer&nom N&eykey/hanthey" in predict_squenitem.strip():
                                    if "N&eykey/hanthey" in each.strip():
                                        P_AB = P_AB + 0.4706
                                if "actor&dat V&i/hi/li/ki" in predict_squenitem.strip():
                                    if "V&i/hi/li/ki" in each.strip():
                                        P_AB = P_AB - 0.9706

                            # # 이히리기를 포함하는 경우 가중치 주기 / weight (psv)
                            # if "V&i/hi/li/ki" in each.strip():
                            #     if "passive" in construc.strip():
                            #         P_AB = P_AB + ((initial_num * 0.001) / (i + 1))
                            #
                            # # weight (typicality)
                            # if "N&i/ka N&eykey/hanthey V&i/hi/li/ki" == predict_squenitem.strip() or "N&eykey/hanthey N&i/ka V&i/hi/li/ki" == predict_squenitem.strip() or "N&i/ka V&i/hi/li/ki" == predict_squenitem.strip() or "N&eykey/hanthey V&i/hi/li/ki" == predict_squenitem.strip():
                            #     if "V&i/hi/li/ki" in each.strip():
                            #         if "Canonical_suffixal_passive" == construc.strip() or "Scrambled_suffixal_passive" == construc.strip() or "Suffixal_passive_undergoer_NOM_only" == construc.strip() or "Suffixal_passive_actor_DAT_only" == construc.strip():
                            #             P_AB = P_AB + ((initial_num * 0.001) / (i + 1))
                            #
                            # # weight (surprisal)
                            # if "N&(l)ul N&i/ka V" == predict_squenitem.strip():
                            #     if "V" in each.strip():
                            #         if "Scrambled_active_transitive" == construc.strip():
                            #             P_AB = P_AB + ((initial_num * 0.001) / (i + 1))
                            #
                            # # weight (agt-1st)
                            # if "N N V" == predict_squenitem.strip() or "N V" == predict_squenitem.strip():
                            #     if "V" in each.strip():
                            #         if "Active_transitive_actor_undergoer_no_case" == construc.strip() or "Active_transitive_actor_no_case" == construc.strip():
                            #             P_AB = P_AB + ((initial_num * 0.001) / (i + 1))

                            if classified_constructions_test.get(construc.rstrip()) == None:
                                classified_constructions_test[construc.rstrip()] = P_AB
                            else:
                                classified_constructions_test[construc.rstrip()] = classified_constructions_test.get(
                                    construc.rstrip()) + P_AB

                    num_item += 1

                # 해당 문장이 포함될 확률이 가장 높은 문장 추출 (추정량 사용)

                dic_min = min(classified_constructions_test.values())
                dic_mid = mid(classified_constructions_test.values())
                dic_max = max(classified_constructions_test.values())

                # print("dic_min ",dic_min)
                # print("dic_mid ", dic_mid)
                # print("dic_max ", dic_max)

                for x1, y1 in classified_constructions_test.items():
                    # 추정량을 계산하는 방법에 따라서 계산하
                    if self.estimator_test == 0:
                        if y1 == dic_min:

                            if y1 == 0.0:
                                pass
                            else:
                                # 상위 개념 구조의 정확도 계산을 위한 부분
                                classified_construc_bignames = ""
                                for key, value in bignames.items():
                                    for construcType in value:
                                        if x1 == construcType:
                                            classified_construc_bignames = classified_construc_bignames + key

                                if construc_binnames_test == classified_construc_bignames:
                                    accuracy_bignames_num_test = accuracy_bignames_num_test + 1

                                # 개별구조 정확도 계산을 위한 부분
                                if origin_class_test == x1:
                                    accuracy_num_test = accuracy_num_test + 1

                                print("예측된 개별 구조 (하위 개념) : ",x1," 예측된 상위 구조 : ",classified_construc_bignames)

                    if self.estimator_test == 1:
                        if y1 == dic_mid:

                            if y1 == 0.0:
                                pass
                            else:
                                # 상위 개념 구조의 정확도 계산을 위한 부분
                                classified_construc_bignames = ""
                                for key, value in bignames.items():
                                    for construcType in value:
                                        if x1 == construcType:
                                            classified_construc_bignames = classified_construc_bignames + key

                                if construc_binnames_test == classified_construc_bignames:
                                    accuracy_bignames_num_test = accuracy_bignames_num_test + 1

                                # 정확도 계산을 위한 부분
                                if origin_class_test == x1:
                                    accuracy_num_test = accuracy_num_test + 1

                                print("예측된 개별 구조 (하위 개념) : ", x1, " 예측된 상위 구조 : ", classified_construc_bignames)

                    if self.estimator_test == 2:
                        if y1 == dic_max:

                            if y1 == 0.0:
                                pass
                            else:
                                # 상위 개념 구조의 정확도 계산을 위한 부분
                                classified_construc_bignames = ""
                                for key, value in bignames.items():
                                    for construcType in value:
                                        if x1 == construcType:
                                            classified_construc_bignames = classified_construc_bignames + key

                                if construc_binnames_test == classified_construc_bignames:
                                    accuracy_bignames_num_test = accuracy_bignames_num_test + 1

                                # 정확도 계산을 위한 부분
                                if origin_class_test == x1:
                                    accuracy_num_test = accuracy_num_test + 1

                                print("예측된 개별 구조 (하위 개념) : ", x1, " 예측된 상위 구조 : ", classified_construc_bignames)


            # 정확도 계산
            print("")
            print("상위 개념 구조 판별 정확도 : ", accuracy_bignames_num_test / 20)
            print("개별 구조 (하위 개념) 판별 정확도 : ", accuracy_num_test / 20)









