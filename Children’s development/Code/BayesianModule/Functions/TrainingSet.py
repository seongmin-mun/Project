class training_dictionary:

    def training_dictionary_inner(self):
        # 초기 빈도수에 따라 인풋 데이터 생성하기
        import random

        # 빈 리스트 생성 -> 총 빈도의 합
        initialList = []

        # 초기 구조별 빈도수의 총합
        sizenum = 6902

        # 빈 초기 리스트에 1부터 10929까지 숫자를 입력
        for x in range(0, sizenum):
            initialList.append(x)

        # 추가 정보 : 각 구조별 인풋의 양
        input_freq = [1757, 51, 2, 1, 268, 19, 6, 0, 0, 0, 0, 0, 935, 1938, 234, 407, 13, 53, 1155, 40, 0, 20, 0, 3, 0, 0, 0, 0, 0]

        input_construction = ["Canonical_active_transitive",
                            "Scrambled_active_transitive",
                            "Canonical_suffixal_passive​",
                            "Scrambled_suffixal_passive",
                            "Canonical_active_transitive_no_ACC",
                            "Canonical_active_transitive_no_NOM​",
                            "Scrambled_active_transitive_no_ACC",
                            "Scrambled_active_transitive_no_NOM",
                            "Canonical_suffixal_passive_no_DAT",
                            "Canonical_suffixal_passive_no_NOM​",
                            "Scrambled_suffixal_passive_no_DAT",
                            "Scrambled_suffixal_passive_no_NOM",
                            "Active_transitive_actor_NOM_only",
                            "Active_transitive_undergoer_ACC_only​",
                            "Ditransitive_recipient_DAT_only",
                            "Suffixal_passive_undergoer_NOM_only​",
                            "Suffixal_passive_actor_DAT_only",
                            "Active_transitive_actor_no_case",
                            "Active_transitive_undergoer_no_case",
                            "Active_transitive_undetermined_no_case",
                            "Suffixal_passive_actor_no_case",
                            "Suffixal_passive_undergoer_no_case",
                            "Suffixal_passive_undetermined_no_case",
                            "Active_transitive_actor_undergoer_no_case",
                            "Active_transitive_undergoer_actor_no_case",
                            "Active_transitive_undetermined_undetermined_no_case",
                            "Suffixal_passive_actor_undergoer_no_case",
                            "Suffixal_passive_undergoer_actor_no_case",
                            "Suffixal_passive_undetermined_undetermined_no_case"]

        input_sentence = ["N&i/ka actor&nom N&(l)ul undergoer&acc V action",
                            "N&(l)ul undergoer&acc N&i/ka actor&nom V action",
                            "N&i/ka undergoer&nom N&eykey/hanthey actor&dat V&i/hi/li/ki action&psv",
                            "N&eykey/hanthey actor&dat N&i/ka undergoer&nom V&i/hi/li/ki action&psv",
                            "N&i/ka actor&nom N undergoer V action",
                            "N ​actor N&(l)ul undergoer&acc V action",
                            "N ​undergoer N&i/ka actor&nom V action",
                            "N&(l)ul undergoer&acc N actor V action",
                            "N&i/ka undergoer&nom N actor V&i/hi/li/ki action&psv",
                            "N ​undergoer N&eykey/hanthey actor&dat V&i/hi/li/ki action&psv",
                            "N ​actor N&i/ka undergoer&nom V&i/hi/li/ki action&psv",
                            "N&eykey/hanthey actor&dat N undergoer V&i/hi/li/ki action&psv",
                            "N&i/ka actor&nom V action",
                            "N&(l)ul undergoer&acc V action",
                            "N&eykey/hanthey rec&dat V action",
                            "N&i/ka undergoer&nom V&i/hi/li/ki action&psv",
                            "N&eykey/hanthey actor&dat V&i/hi/li/ki action&psv",
                            "N actor V action",
                            "N undergoer V action",
                            "N nd V action",
                            "N actor V&i/hi/li/ki action&psv",
                            "N undergoer V&i/hi/li/ki action&psv",
                            "N nd V&i/hi/li/ki action&psv",
                            "N actor N undergoer V action",
                            "N undergoer N actor V action",
                            "N nd N nd V action",
                            "N actor N undergoer V&i/hi/li/ki action&psv",
                            "N undergoer N actor V&i/hi/li/ki action&psv",
                            "N nd N nd V&i/hi/li/ki action&psv"
                          ]

        # 인풋 데이터를 만들기 위한 사전 -> 랜덤으로 부여된 숫자가 '키'값이 되고 각 숫자는 구조의 이름을 '값'으로 가진다.
        input_dic = {}

        # 각 구조를 초기 빈도만큼 넣어주는 부분
        for x in range(0, len(input_freq)):

            # 초기 리스트의 크기에서 랜덤하게 숫자를 뽑는다. 뽑힌 숫자의 위치에 있는 숫자를 인풋 사전에 '키'로 전달하고, 현재 구조 값을 '값'으로 전달한다.
            for y in range(0, input_freq[x]):
                # 랜덤하게 숫자를 뽑는다.
                num = random.randrange(0, len(initialList))
                # 인풋 사전에 '키'값과 '값'을 넘겨준다.
                input_dic[str(initialList[num])] = input_construction[x].replace("\u200b", "") + " ### " + \
                                                   input_sentence[x].replace("\u200b", "")

                # 리스트의 크기와 제거된 숫자를 확인하는 부분
                # print("len", len(initialList))
                # print(initialList[num])

                # 뽑힌 숫자를 초기 리스트에서 제거함 (리스트의 크기가 점점 줄어든다.)
                initialList.remove(initialList[num])

        # 데이터 확인: 0부터 10928까지가 '키'값으로 들어감
        # print(input_dic['10928'])

        return input_dic


    def training_dictionary_inner_laplace(self):
        # 초기 빈도수에 따라 인풋 데이터 생성하기
        import random

        # 빈 리스트 생성 -> 총 빈도의 합
        initialList = []

        # 초기 구조별 빈도수의 총합
        sizenum = 6931

        # 빈 초기 리스트에 1부터 10929까지 숫자를 입력
        for x in range(0, sizenum):
            initialList.append(x)

        # 추가 정보 : 각 구조별 인풋의 양
        input_freq_laplace = [1758, 52, 3, 2, 269, 20, 7, 1, 1, 1, 1, 1, 936, 1939, 235, 408, 14, 54, 1156, 41, 1, 21, 1, 4, 1, 1, 1, 1, 1]

        input_construction = ["Canonical_active_transitive",
                              "Scrambled_active_transitive",
                              "Canonical_suffixal_passive​",
                              "Scrambled_suffixal_passive",
                              "Canonical_active_transitive_no_ACC",
                              "Canonical_active_transitive_no_NOM​",
                              "Scrambled_active_transitive_no_ACC",
                              "Scrambled_active_transitive_no_NOM",
                              "Canonical_suffixal_passive_no_DAT",
                              "Canonical_suffixal_passive_no_NOM​",
                              "Scrambled_suffixal_passive_no_DAT",
                              "Scrambled_suffixal_passive_no_NOM",
                              "Active_transitive_actor_NOM_only",
                              "Active_transitive_undergoer_ACC_only​",
                              "Ditransitive_recipient_DAT_only",
                              "Suffixal_passive_undergoer_NOM_only​",
                              "Suffixal_passive_actor_DAT_only",
                              "Active_transitive_actor_no_case",
                              "Active_transitive_undergoer_no_case",
                              "Active_transitive_undetermined_no_case",
                              "Suffixal_passive_actor_no_case",
                              "Suffixal_passive_undergoer_no_case",
                              "Suffixal_passive_undetermined_no_case",
                              "Active_transitive_actor_undergoer_no_case",
                              "Active_transitive_undergoer_actor_no_case",
                              "Active_transitive_undetermined_undetermined_no_case",
                              "Suffixal_passive_actor_undergoer_no_case",
                              "Suffixal_passive_undergoer_actor_no_case",
                              "Suffixal_passive_undetermined_undetermined_no_case"]

        input_sentence = ["N&i/ka actor&nom N&(l)ul undergoer&acc V action",
                          "N&(l)ul undergoer&acc N&i/ka actor&nom V action",
                          "N&i/ka undergoer&nom N&eykey/hanthey actor&dat V&i/hi/li/ki action&psv",
                          "N&eykey/hanthey actor&dat N&i/ka undergoer&nom V&i/hi/li/ki action&psv",
                          "N&i/ka actor&nom N undergoer V action",
                          "N ​actor N&(l)ul undergoer&acc V action",
                          "N ​undergoer N&i/ka actor&nom V action",
                          "N&(l)ul undergoer&acc N actor V action",
                          "N&i/ka undergoer&nom N actor V&i/hi/li/ki action&psv",
                          "N ​undergoer N&eykey/hanthey actor&dat V&i/hi/li/ki action&psv",
                          "N ​actor N&i/ka undergoer&nom V&i/hi/li/ki action&psv",
                          "N&eykey/hanthey actor&dat N undergoer V&i/hi/li/ki action&psv",
                          "N&i/ka actor&nom V action",
                          "N&(l)ul undergoer&acc V action",
                          "N&eykey/hanthey rec&dat V action",
                          "N&i/ka undergoer&nom V&i/hi/li/ki action&psv",
                          "N&eykey/hanthey actor&dat V&i/hi/li/ki action&psv",
                          "N actor V action",
                          "N undergoer V action",
                          "N nd V action",
                          "N actor V&i/hi/li/ki action&psv",
                          "N undergoer V&i/hi/li/ki action&psv",
                          "N nd V&i/hi/li/ki action&psv",
                          "N actor N undergoer V action",
                          "N undergoer N actor V action",
                          "N nd N nd V action",
                          "N actor N undergoer V&i/hi/li/ki action&psv",
                          "N undergoer N actor V&i/hi/li/ki action&psv",
                          "N nd N nd V&i/hi/li/ki action&psv"
                          ]

        # 인풋 데이터를 만들기 위한 사전 -> 랜덤으로 부여된 숫자가 '키'값이 되고 각 숫자는 구조의 이름을 '값'으로 가진다.
        input_dic = {}

        # 각 구조를 초기 빈도만큼 넣어주는 부분
        for x in range(0, len(input_freq_laplace)):

            # 초기 리스트의 크기에서 랜덤하게 숫자를 뽑는다. 뽑힌 숫자의 위치에 있는 숫자를 인풋 사전에 '키'로 전달하고, 현재 구조 값을 '값'으로 전달한다.
            for y in range(0, input_freq_laplace[x]):
                # 랜덤하게 숫자를 뽑는다.
                num = random.randrange(0, len(initialList))
                # 인풋 사전에 '키'값과 '값'을 넘겨준다.
                input_dic[str(initialList[num])] = input_construction[x].replace("\u200b", "") + " ### " + \
                                                   input_sentence[x].replace("\u200b", "")

                # 리스트의 크기와 제거된 숫자를 확인하는 부분
                # print("len", len(initialList))
                # print(initialList[num])

                # 뽑힌 숫자를 초기 리스트에서 제거함 (리스트의 크기가 점점 줄어든다.)
                initialList.remove(initialList[num])

        # 데이터 확인: 0부터 10928까지가 '키'값으로 들어감
        # print(input_dic['10928'])

        return input_dic
