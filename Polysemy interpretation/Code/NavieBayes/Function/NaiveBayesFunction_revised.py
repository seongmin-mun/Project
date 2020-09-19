class NaiveBayesAlgorithm:

    def setdata(self, directional_num, instrumental_num, noise_num, iteration_num, training_route, test_route):
        self.directional_num = directional_num
        self.instrumental_num = instrumental_num
        self.noise_num = noise_num
        self.iteration_num = iteration_num
        self.training_route = training_route
        self.test_route = test_route

    def NaiveBayes_Calculation(self):
        import random
        ##############################################################
        ##############################################################
        #####################트레이닝단계(Traning)########################
        ##############################################################
        ##############################################################

        Training = open(self.training_route, "r")  # "w" 쓰기 "r" 읽기
        Training_Noun = Training.readlines()
        Training.close()

        ######################요인들 정리###########################
        iteration_times = self.iteration_num

        ######################요소들 정리###########################

        # 분류 카테고리 정리(집합 자료형)
        categories = set([])

        # 분류 키워드 정리(집합 자료형)
        keywords = set([])

        #######################빈도계산##############################

        # 분류 카테고리 총합, 카테고리별 빈도(딕셔너리)
        dict_categories_first = {}

        text_list = []

        # 카테고리의 종류와 카테고리별 문장의 수를 카운팅
        for x in Training_Noun:
            text_list.append(x)
            line = x.split("\t")
            if dict_categories_first.get(line[0].rstrip()) == None:
                dict_categories_first[line[0].rstrip()] = 1
            else:
                dict_categories_first[line[0].rstrip()] = dict_categories_first.get(line[0].rstrip()) + 1
            categories.add(line[0].rstrip())

        # 카테고리의 종류에 따라 문장을 딕셔너리에 저장
        categories_sentences = {}

        for x in categories:
            category_sentences = []
            for y in Training_Noun:
                line = y.split("\t")
                if line[0] == x:
                    category_sentences.append(y)
            categories_sentences[x] = category_sentences

        # print(categories_sentences)

        # 카테고리에 따라 문장의 절반 * 반복 횟수 만큰 문장 추출하여 학습 말뭉치 재구성

        ramdon_selected_sentences = []

        # print(dict_categories_first)
        # print(categories)

        for x in range(0, iteration_times):  # if 3 -> 0,1,2
            for y in categories:
                if y == "directional":
                    for z in range(0, self.directional_num):
                        num = random.randrange(0, dict_categories_first[y])
                        ramdon_selected_sentences.append(categories_sentences[y][num].replace("\n", ""))
                if y == "instrumental":
                    for z in range(0, self.instrumental_num):
                        num = random.randrange(0, dict_categories_first[y])
                        ramdon_selected_sentences.append(categories_sentences[y][num].replace("\n", ""))
                if y == "undetermined":
                    for z in range(0, self.noise_num):
                        num = random.randrange(0, dict_categories_first[y])
                        ramdon_selected_sentences.append(categories_sentences[y][num].replace("\n", ""))

        dict_categories = {}

        for x in ramdon_selected_sentences:
            # print(x)
            line = x.split("\t")
            if dict_categories.get(line[0].rstrip()) == None:
                dict_categories[line[0].rstrip()] = 1
            else:
                dict_categories[line[0].rstrip()] = dict_categories.get(line[0].rstrip()) + 1
            categories.add(line[0].rstrip())
            keyword = line[1].split(" ")
            for y in keyword:
                if y is not None:
                    keywords.add(y.rstrip())

        categories_total_frequncy = len(ramdon_selected_sentences)


        # print(categories)
        # print(keywords)
        # print(dict_categories)

        # 카테고리별 키워드 출현빈도 빈도(딕셔너리)

        dict_keywords = {}

        for x in categories:
            dict_category = {}
            for y in ramdon_selected_sentences:
                line = y.split("\t")
                keyword = line[1].split(" ")
                # 한 문장에 등장한 단어들 집합(한문장에 같은 단어가 여러번 등장해서 확률에 영향을 주는것을 방지한다.)
                keyword_set = set([])
                for z in keyword:
                    if z is not None:
                        z = z.replace("\n", "")
                        keyword_set.add(z)
                if x == line[0]:
                    for z in keyword_set:
                        if dict_category.get(z) == None:
                            dict_category[z] = 1
                        else:
                            dict_category[z] = dict_category.get(z) + 1
            for y in keywords:
                if dict_category.get(y) == None:
                    dict_category[y] = 0
            dict_keywords[x] = dict_category

        # print(dict_keywords)

        #########################확률로 변환############################

        # 분류 카테고리 총합, 카테고리별 빈도 값을 확률로 변환(딕셔너리)(카테고리 출현 횟수 / 전체문장의 수), 소수점 4째 자리
        dict_categories_probability = {}

        for x in categories:
            dict_categories_probability[x] = round((dict_categories.get(x) / categories_total_frequncy) * 100, 4)

        # print(dict_categories_probability)

        # 각 분류별 by 키워드별, 전체 문장에서 출현 확률을 계산한다(딕셔너리)(키워드 출현 횟수 / 전체문장의 수), 소수점 4째 자리
        dict_keywords_probability = {}

        for x in categories:
            dict_category = {}
            for y in keywords:
                if y is not None:
                    dict_category[y] = round((dict_keywords[x][y] / categories_total_frequncy) * 100, 4)
            dict_keywords_probability[x] = dict_category

        # print(dict_keywords_probability)

        # 각 분류별 by 키워드별, 전체 문장에서 출현 안 할 확률을 계산한다(딕셔너리)(100-키워드 출현 확률)
        dict_keywords_probability_none = {}

        for x in categories:
            dict_category = {}
            for y in keywords:
                if y is not None:
                    dict_category[y] = round((dict_categories_probability.get(x) - dict_keywords_probability[x][y]), 2)
            dict_keywords_probability_none[x] = dict_category

        # print(dict_keywords_probability_none)

        #########################라플라스############################
        # 라플라스 추정기법도 사용(Laplace estimator) (각 빈도수에 1을 더하고 각 분류 확률에 키워드의 수만큼 더한다.)

        # 라플라스를 적용한 분류 카테고리 확률(딕셔너리)(카테고리 확률 + 전체키워드의 수), 소수점 4째 자리
        dict_categories_laplace = {}

        for x in categories:
            dict_categories_laplace[x] = dict_categories_probability.get(x) + len(
                keywords)  # len(keywords)  #(len(keywords)/10)

        # print(dict_categories_laplace)

        # 라플라스를 적용한 각 분류별 by 키워드별 확률(딕셔너리)(키워드 출현 확률 + 1), 소수점 4째 자리
        dict_keywords_laplace = {}

        for x in categories:
            dict_category = {}
            for y in keywords:
                if y is not None:
                    dict_category[y] = dict_keywords_probability[x][y] + 1  # 1   #0.1
            dict_keywords_laplace[x] = dict_category

        # print(dict_keywords_laplace)

        # 라플라스를 적용한 각 분류별 by 키워드별 출현 안 할 확률(딕셔너리)(키워드 출현 안 할 확률 + 1), 소수점 4째 자리
        dict_keywords_none_laplace = {}

        for x in categories:
            dict_category = {}
            for y in keywords:
                if y is not None:
                    dict_category[y] = dict_keywords_probability_none[x][y] + 1  # 1  #0.1
            dict_keywords_none_laplace[x] = dict_category

        # print(dict_keywords_none_laplace)

        ##############################################################
        ########################데이터변수정리############################
        ##############################################################
        # print(categories) ##분류 목록
        # print(keywords) ##트레이닝에 사용된 키워드 목록
        # print(dict_categories_probability) ##각 카테고리별 원래의 확률
        # print(dict_categories_laplace) ##각 카테고리별 라플라시 추정법을 적용한 확률
        # print(dict_keywords_laplace) ##각 카테고리별 라플라시 추정법을 적용한 키워드가 포함될 확률
        # print(dict_keywords_none_laplace) ##각 카테고리별 라플라시 추정법을 적용한 키워드가 포함되지 않을 확률

        ##############################################################
        ##############################################################
        #####################테스트,검증단계(Test)########################
        ##############################################################
        ##############################################################

        Testdata = open(self.test_route, "r")  # "w" 쓰기 "r" 읽기
        Testdata_lines = Testdata.readlines()
        Testdata.close()

        #########################요소들 정리#############################

        # 분류기의 정확도를 측정 할 원래 포함 집단(리스트-요소의 값을 변경 할 수 있음)
        test_categories = []

        for x in Testdata_lines:
            line = x.split("\t")
            test_categories.append(line[0].rstrip())

        # print(test_categories) #테스트 데이터에 포함된 문장들의 원 집단(카테고리)

        #########################요소들 정리#############################

        likelihood_for_each_sentences = {}
        likelihood_for_each_sentences_probability = {}

        number = 0
        for x in Testdata_lines:
            line = x.split("\t")
            keyword = line[1].split(" ")
            # 한 문장에 등장한 단어들 집합(한문장에 같은 단어가 여러번 등장해서 확률에 영향을 주는것을 방지한다.)
            test_keyword_dic = {}
            for y in keyword:
                if y is not None:
                    y = y.replace("\n", "")
                    test_keyword_dic[y] = 1
            likelihood = {}
            totla_likelihood = 0
            for y in categories:
                # 각 분류별 우도 계산
                value = 1
                for z in keywords:
                    # 테스트 문장에 등장한 단어를 기준으로 우도를 계산한다.
                    if test_keyword_dic.get(z) == None:
                        # value = value * (dict_keywords_none_laplace[y].get(z) / dict_categories_laplace.get(y))
                        pass
                    else:
                        value = value * (dict_keywords_laplace[y].get(z) / dict_categories_laplace.get(y))
                value = value * (dict_categories_probability.get(y) / 100)

                likelihood[y] = value
                totla_likelihood = totla_likelihood + value
            likelihood_for_each_sentences[number] = likelihood
            # 우도를 기반으로 확률 계산(소수점 2자리)
            likelihood_probability = {}
            for y in categories:
                likelihood_probability[y] = round(likelihood.get(y) / totla_likelihood, 2)
            likelihood_for_each_sentences_probability[number] = likelihood_probability
            number = number + 1

        # print(likelihood_for_each_sentences)
        # print(likelihood_for_each_sentences_probability)
        # print(len(likelihood_for_each_sentences_probability))
        accuracy_total = 0
        accuracy_directional = 0
        accuracy_instrumental = 0
        for x in likelihood_for_each_sentences:
            inverse = [(value, key) for key, value in likelihood_for_each_sentences[x].items()]
            # print(inverse)
            # print("compare = ",test_categories[x],"  :  ",max(inverse)[1])

            if test_categories[x] == max(inverse)[1]:
                accuracy_total = accuracy_total + 1

            if test_categories[x] == "directional":
                if test_categories[x] == max(inverse)[1]:
                    accuracy_directional = accuracy_directional + 1

            if test_categories[x] == "instrumental":
                if test_categories[x] == max(inverse)[1]:
                    accuracy_instrumental = accuracy_instrumental + 1

        # print("accuracy = ", accuracy_frequncy / len(test_categories) * 100, "%")

        accuracy_results = []

        # accuracy_total
        accuracy_results.append((accuracy_total / len(test_categories)) * 100)

        # accuracy_directional
        accuracy_results.append((accuracy_directional / (len(test_categories)/2)) * 100)

        # accuracy_instrumental
        accuracy_results.append((accuracy_instrumental / (len(test_categories)/2)) * 100)

        return accuracy_results