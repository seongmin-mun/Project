# 추가 정보 : 각 구조별 인풋의 양
input_freq = [1757, 51, 2, 1, 268, 19, 6, 0, 0, 0, 0, 0, 0, 0, 935, 1938, 0, 234, 407, 13, 0]
input_freq_laplace = [1758, 52, 3, 2, 269, 20, 7, 1, 1, 1, 1, 1, 1, 1, 936, 1939, 1, 235, 408, 14, 1]
input_construction = ["Canonical_active_transitive​",
"Scrambled_active_transitive​",
"Canonical_suffixal_passive​",
"Scrambled_suffixal_passive​",
"Canonical_active_transitive_NOM_only​",
"Canonical_active_transitive_ACC_only​",
"Scrambled_active_transitive_NOM_only",
"Scrambled_active_transitive_ACC_only",
"Active_transitive_no_case_marking",
"Canonical_suffixal_passive_NOM_only​",
"Canonical_suffixal_passive_DAT_only​",
"Scrambled_suffixal_passive_NOM_only​",
"Scrambled_suffixal_passive_DAT_only​",
"Suffixal_passive_no_case_marking​​",
"Active_transitive_actor_NOM_only",
"Active_transitive_undergoer_ACC_only​",
"Active_no_case_marking​",
"Ditransitive_recipient_DAT_only",
"Suffixal_passive_undergoer_NOM_only​",
"Suffixal_passive_actor_DAT_only",
"Suffixal_passive_no_case_marking"]


input_sentence = ["N i/ka N (l)ul V",
"N (l)ul N i/ka V",
"N i/ka N eykey/hanthey V i/hi/li/ki",
"N eykey/hanthey N i/ka V i/hi/li/ki",
"N i/ka N V",
"N N (l)ul V",
"​N N i/ka V",
"​N (l)ul N V",
"​​N N V",
"N i/ka N V i/hi/li/ki",
"N N eykey/hanthey V i/hi/li/ki",
"N N i/ka V i/hi/li/ki",
"N eykey/hanthey N V i/hi/li/ki",
"N N V i/hi/li/ki",
"N i/ka V",
"N (l)ul V",
"N V",
"​N eykey/hanthey V",
"N i/ka V i/hi/li/ki",
"​N eykey/hanthey V i/hi/li/ki",
"N V i/hi/li/ki"]


sequence_construction_prob = {"Canonical_active_transitive":0.0038095238095238095,
"Scrambled_active_transitive":0.0038095238095238095,
"Canonical_suffixal_passive":0.0038095238095238095,
"Scrambled_suffixal_passive":0.005079365079365079,
"Canonical_active_transitive_NOM_only":0.06095238095238095,
"Canonical_active_transitive_ACC_only":0.007619047619047619,
"Scrambled_active_transitive_NOM_only":0.015238095238095238,
"Scrambled_active_transitive_ACC_only":0.030476190476190476,
"Active_transitive_no_case_marking":0.02857142857142857,
"Canonical_suffixal_passive_NOM_only":0.030476190476190476,
"Canonical_suffixal_passive_DAT_only":0.0038095238095238095,
"Scrambled_suffixal_passive_NOM_only":0.007619047619047619,
"Scrambled_suffixal_passive_DAT_only":0.020317460317460317,
"Suffixal_passive_no_case_marking":0.0019047619047619048,
"Active_transitive_actor_NOM_only":0.07142857142857142,
"Active_transitive_undergoer_ACC_only":0.03571428571428571,
"Active_no_case_marking":0.09523809523809523,
"Ditransitive_recipient_DAT_only":0.047619047619047616,
"Suffixal_passive_undergoer_NOM_only":0.009523809523809523,
"Suffixal_passive_actor_DAT_only":0.006349206349206348,
"Suffixal_passive_no_case_marking":0.004761904761904762}


# input_construction = ["Canonical_active_transitive​ ### N i/ka N (l)ul V",
# "Scrambled_active_transitive​ ### N (l)ul N i/ka V",
# "Canonical_suffixal_passive​ ### N i/ka N eykey/hanthey V i/hi/li/ki",
# "Scrambled_suffixal_passive​ ### N eykey/hanthey N i/ka V i/hi/li/ki",
# "Canonical_active_transitive_NOM_only​ ### N i/ka N V",
# "Canonical_active_transitive_ACC_only​ ### N N (l)ul V",
# "Scrambled_active_transitive_NOM_only ### ​N N i/ka V",
# "Scrambled_active_transitive_ACC_only ### ​N (l)ul N V",
# "Active_transitive_no_case_marking ### ​​N N V",
# "Canonical_suffixal_passive_NOM_only​ ### N i/ka N V i/hi/li/ki",
# "Canonical_suffixal_passive_DAT_only​ ### N N eykey/hanthey V i/hi/li/ki",
# "Scrambled_suffixal_passive_NOM_only​ ### N N i/ka V i/hi/li/ki",
# "Scrambled_suffixal_passive_DAT_only​ ### N eykey/hanthey N V i/hi/li/ki",
# "Suffixal_passive_no_case_marking​​ ### N N V i/hi/li/ki",
# "Active_transitive_actor_NOM_only​ ### N i/ka V",
# "Active_transitive_undergoer_ACC_only​ ### N (l)ul V",
# "Active_no_case_marking​ ### N V",
# "Ditransitive_recipient_DAT_only ### ​N eykey/hanthey V",
# "Suffixal_passive_undergoer_NOM_only​ ### N i/ka V i/hi/li/ki",
# "Suffixal_passive_actor_DAT_only ### ​N eykey/hanthey V i/hi/li/ki",
# "Suffixal_passive_no_case_marking ### ​N V i/hi/li/ki"]

#아이템 by 구문 형태 매트릭스 생성
item_list = ["N",
"i/ka",
"(l)ul",
"V",
"eykey/hanthey",
"i/hi/li/ki"]

diction = {}
for x in item_list:
    num = 0
    diction_inner = {}
    for y in input_construction:
        item = input_sentence[num].split(" ")
        checked = False
        for z in item:
            print(x," ",z)
            if x == z:
                print("true")
                checked = True
        if checked == True:
            print("d")
            diction_inner[y.replace("\u200b", "").rstrip()] = input_freq_laplace[num]
        else:
            diction_inner[y.replace("\u200b", "").rstrip()] = 1
        num += 1

    diction[x.replace("\u200b","").rstrip()] = diction_inner
    print(num)

print(diction)


#
# input_construction = ["Canonical_active_transitive ### N_1&i/ka_1 actor_1&nom_1 N_2&(l)ul_2 undergoer_2&acc_2 V_3 action_3",
# "Scrambled_active_transitive ### N_1&(l)ul undergoer_1&acc_1 N_2&i/ka_2 actor_2&nom_2 V_3 action_3",
# "Canonical_suffixal_passive ### N_1&i/ka_1 undergoer_1&nom_1 N_2&eykey/hanthey_2 actor_2&dat_2 V&i/hi/li/ki_3 action&psv_3",
# "Scrambled_suffixal_passive ### N_1&eykey/hanthey_1 actor_1&dat_1 N_2&i/ka_2 undergoer_2&nom_2 V&i/hi/li/ki_3 action&psv_3",
# "Canonical_active_transitive_NOM_only ### N_1&i/ka_1 actor_1&nom_1 N_2 undergoer_2 V_3 action_3",
# "Canonical_active_transitive_ACC_only ### N_1 actor_1 N_2&(l)ul_2 undergoer_2&acc_2 V_3 action_3",
# "Scrambled_active_transitive_NOM_only ### N_1 undergoer_1 N_2&i/ka_2 actor_2&nom_2 V_3 action_3",
# "Scrambled_active_transitive_ACC_only ### N_1&(l)ul undergoer_1&acc_1 N_2 actor_2 V_3 action_3",
# "Canonical_suffixal_passive_NOM_only ### N_1&i/ka_1 undergoer_1&nom_1 N_2 actor_2 V&i/hi/li/ki_3 action&psv_3",
# "Canonical_suffixal_passive_DAT_only ### N_1 undergoer_1 N_2&eykey/hanthey_2 actor_2&dat_2 V&i/hi/li/ki_3 action&psv_3",
# "Scrambled_suffixal_passive_NOM_only ### N_1 actor_1 N_2&i/ka_2 undergoer_2&nom_2 V&i/hi/li/ki_3 action&psv_3",
# "Scrambled_suffixal_passive_DAT_only ### N_1&eykey/hanthey_1 actor_1&dat_1 N_2 undergoer_2 V&i/hi/li/ki_3 action&psv_3",
# "Active_transitive_actor_NOM_only ### N_1&i/ka_1 actor_1&nom_1 V_2 action_2",
# "Active_transitive_undergoer_ACC_only ### N_1&(l)ul undergoer_1&acc_1 V_2 action_2",
# "Ditransitive_recipient_DAT_only ### N_1&eykey/hanthey_1 rec_1&dat_1 V_2 action_2",
# "Suffixal_passive_undergoer_NOM_only ### N_1&i/ka_1 undergoer_1&nom_1 V&i/hi/li/ki_2 action&psv_2",
# "Suffixal_passive_actor_DAT_only ### N_1&eykey/hanthey_1 actor_1&dat_1 V&i/hi/li/ki_2 action&psv_2"]
#
#
# #각 결합 순서별 등장하는 아이템들의 빈도 확인
# diction = {}
# num = 0
# for x in input_construction:
#     sentence = x.split(" ### ")
#     item = sentence[1].split(" ")
#     target = 6  #값에 변화를 주어야하는 부분
#     if len(item) <= target:
#         pass
#     else:
#         num+=1
#         print(num," ",item[target])
#         if diction.get(item[target].rstrip()) == None:
#             diction[item[target].rstrip()] = 1
#         else:
#             diction[item[target].rstrip()] = diction.get(item[target].rstrip()) + 1
#
# print(diction)





#각 결합 구조별 구문들의 확률 계산
# itemsfreqdict = {'1': {'N_1': 21},
#                  '2': {'i/ka_1': 6, '(l)ul_1': 3, 'eykey/hanthey_1': 4, 'N_2': 6, 'V_2': 2},
#                  '3': {'N_2': 8, '(l)ul_2': 1, 'i/ka_2': 2, 'V_3': 2, 'eykey/hanthey_2': 1, 'V_2': 5,
#                        'i/hi/li/ki_2': 1},
#                  '4': {'(l)ul_2': 1, 'i/ka_2': 2, 'eykey/hanthey_2': 1, 'V_3': 8, 'i/hi/li/ki_3': 1, 'i/hi/li/ki_2': 2},
#                  '5': {'V_3': 4, 'i/hi/li/ki_3': 4},
#                  '6': {'i/hi/li/ki_3': 2}}
# squenfreq = [21, 21, 20, 15, 8, 2]
#
# for x in input_construction:
#     sentence = x.split(" ### ")
#     item = sentence[1].split(" ")
#     num = 0
#     proba = 1
#     for y in item:
#         total = squenfreq[num]
#         num += 1
#         #print(itemsfreqdict[str(num).rstrip()][y.replace("\u200b","").rstrip()])
#         child = itemsfreqdict[str(num).rstrip()][y.replace("\u200b","").rstrip()]
#         in_prob = child / total
#
#         proba = proba * in_prob
#
#     print("'",sentence[0].replace("\u200b",""), "':", proba,",")




#아이템들의 리스트 확인
# diction = {}
# num = 0
# for x in input_construction:
#     sentence = x.split(" ### ")
#     item = sentence[1].split(" ")
#     for y in item:
#         if diction.get(y.replace("\u200b","").rstrip()) == None:
#             diction[y.replace("\u200b","").rstrip()] = 1
#         else:
#             diction[y.replace("\u200b","").rstrip()] = diction.get(y.replace("\u200b","").rstrip()) + 1
#
# print(diction.items())
#
# for x,y in diction.items():
#     print(x)









#part2

#해당 데이터는 3단계 순서까지 사용
# input_construction = ["Canonical_active_transitive ### N_1&i/ka_1 actor_1&nom_1 N_2&(l)ul_2 undergoer_2&acc_2 V_3 action_3",
# "Scrambled_active_transitive ### N_1&(l)ul undergoer_1&acc_1 N_2&i/ka_2 actor_2&nom_2 V_3 action_3",
# "Canonical_suffixal_passive ### N_1&i/ka_1 undergoer_1&nom_1 N_2&eykey/hanthey_2 actor_2&dat_2 V&i/hi/li/ki_3 action&psv_3",
# "Scrambled_suffixal_passive ### N_1&eykey/hanthey_1 actor_1&dat_1 N_2&i/ka_2 undergoer_2&nom_2 V&i/hi/li/ki_3 action&psv_3",
# "Canonical_active_transitive_NOM_only ### N_1&i/ka_1 actor_1&nom_1 N_2 undergoer_2 V_3 action_3",
# "Canonical_active_transitive_ACC_only ### N_1 actor_1 N_2&(l)ul_2 undergoer_2&acc_2 V_3 action_3",
# "Scrambled_active_transitive_NOM_only ### N_1 undergoer_1 N_2&i/ka_2 actor_2&nom_2 V_3 action_3",
# "Scrambled_active_transitive_ACC_only ### N_1&(l)ul undergoer_1&acc_1 N_2 actor_2 V_3 action_3",
# "Canonical_suffixal_passive_NOM_only ### N_1&i/ka_1 undergoer_1&nom_1 N_2 actor_2 V&i/hi/li/ki_3 action&psv_3",
# "Canonical_suffixal_passive_DAT_only ### N_1 undergoer_1 N_2&eykey/hanthey_2 actor_2&dat_2 V&i/hi/li/ki_3 action&psv_3",
# "Scrambled_suffixal_passive_NOM_only ### N_1 actor_1 N_2&i/ka_2 undergoer_2&nom_2 V&i/hi/li/ki_3 action&psv_3",
# "Scrambled_suffixal_passive_DAT_only ### N_1&eykey/hanthey_1 actor_1&dat_1 N_2 undergoer_2 V&i/hi/li/ki_3 action&psv_3",
# "Active_transitive_actor_NOM_only ### N_1&i/ka_1 actor_1&nom_1 V_2 action_2",
# "Active_transitive_undergoer_ACC_only ### N_1&(l)ul undergoer_1&acc_1 V_2 action_2",
# "Ditransitive_recipient_DAT_only ### N_1&eykey/hanthey_1 rec_1&dat_1 V_2 action_2",
# "Suffixal_passive_undergoer_NOM_only ### N_1&i/ka_1 undergoer_1&nom_1 V&i/hi/li/ki_2 action&psv_2",
# "Suffixal_passive_actor_DAT_only ### N_1&eykey/hanthey_1 actor_1&dat_1 V&i/hi/li/ki_2 action&psv_2"]

#
#
# #1.각 결합 순서별 등장하는 아이템들의 빈도 확인
# diction = {}
# num = 0
# for x in input_construction:
#     sentence = x.split(" ### ")
#     item = sentence[1].split(" ")
#     target = 6  #값에 변화를 주어야하는 부분
#     if len(item) <= target:
#         pass
#     else:
#         num+=1
#         print(num," ",item[target])
#         if diction.get(item[target].rstrip()) == None:
#             diction[item[target].rstrip()] = 1
#         else:
#             diction[item[target].rstrip()] = diction.get(item[target].rstrip()) + 1
#
# print(diction)


#2.각 결합 구조별 구문들의 확률 계산
itemsfreqdict = {'1': {'N_1&i/ka_1': 6, 'N_1&(l)ul': 3, 'N_1&eykey/hanthey_1': 4, 'N_1': 4},
                 '2': {'actor_1&nom_1': 3, 'undergoer_1&acc_1': 3, 'undergoer_1&nom_1': 3, 'actor_1&dat_1': 3, 'actor_1': 2, 'undergoer_1': 2, 'rec_1&dat_1': 1},
                 '3': {'N_2&(l)ul_2': 2, 'N_2&i/ka_2': 4, 'N_2&eykey/hanthey_2': 2, 'N_2': 4, 'V_2': 3, 'V&i/hi/li/ki_2': 2},
                 '4': {'undergoer_2&acc_2': 2, 'actor_2&nom_2': 2, 'actor_2&dat_2': 2, 'undergoer_2&nom_2': 2, 'undergoer_2': 2, 'actor_2': 2, 'action_2': 3, 'action&psv_2': 2},
                 '5': {'V_3': 6, 'V&i/hi/li/ki_3': 6},
                 '6': {'action_3': 6, 'action&psv_3': 6}}
squenfreq = [17, 17, 17, 17, 12, 12]
#
# for x in input_construction:
#     sentence = x.split(" ### ")
#     item = sentence[1].split(" ")
#     num = 0
#     proba = 1
#     for y in item:
#         total = squenfreq[num]
#         num += 1
#         #print(itemsfreqdict[str(num).rstrip()][y.replace("\u200b","").rstrip()])
#         child = itemsfreqdict[str(num).rstrip()][y.replace("\u200b","").rstrip()]
#         in_prob = child / total
#
#         proba = proba * in_prob
#
#     print("'",sentence[0].replace("\u200b",""), "':", proba,",")

#result form 2
# sequence_construction_prob = {"Canonical_active_transitive": 0.00021551466098346526,
# "Scrambled_active_transitive": 0.00021551466098346526,
# "Canonical_suffixal_passive": 0.00021551466098346526,
# "Scrambled_suffixal_passive": 0.000287352881311287,
# "Canonical_active_transitive_NOM_only": 0.00043102932196693053,
# "Canonical_active_transitive_ACC_only": 9.578429377042899e-05,
# "Scrambled_active_transitive_NOM_only": 0.00019156858754085799,
# "Scrambled_active_transitive_ACC_only": 0.00021551466098346526,
# "Canonical_suffixal_passive_NOM_only": 0.00043102932196693053,
# "Canonical_suffixal_passive_DAT_only": 9.578429377042899e-05,
# "Scrambled_suffixal_passive_NOM_only": 0.00019156858754085799,
# "Scrambled_suffixal_passive_DAT_only": 0.000287352881311287,
# "Active_transitive_actor_NOM_only": 0.0019396319488511878,
# "Active_transitive_undergoer_ACC_only": 0.0009698159744255939,
# "Ditransitive_recipient_DAT_only": 0.0004310293219669306,
# "Suffixal_passive_undergoer_NOM_only": 0.0008620586439338611,
# "Suffixal_passive_actor_DAT_only": 0.000574705762622574}



#3.아이템들의 리스트 확인
# diction = {}
# num = 0
# for x in input_construction:
#     sentence = x.split(" ### ")
#     item = sentence[1].split(" ")
#     for y in item:
#         if diction.get(y.replace("\u200b","").rstrip()) == None:
#             diction[y.replace("\u200b","").rstrip()] = 1
#         else:
#             diction[y.replace("\u200b","").rstrip()] = diction.get(y.replace("\u200b","").rstrip()) + 1
#
# print(diction.items())
#
# for x,y in diction.items():
#     print("#",x,",")



#4.아이템 by 구문 형태 매트릭스 생성
# input_freq_laplace = [1758, 52, 3, 2, 269, 20, 7, 1, 1, 1, 1, 1, 936, 1939, 235, 408, 14]
# input_construction = ["Canonical_active_transitive​",
# "Scrambled_active_transitive​",
# "Canonical_suffixal_passive​",
# "Scrambled_suffixal_passive​",
# "Canonical_active_transitive_NOM_only​",
# "Canonical_active_transitive_ACC_only​",
# "Scrambled_active_transitive_NOM_only",
# "Scrambled_active_transitive_ACC_only",
# "Canonical_suffixal_passive_NOM_only​",
# "Canonical_suffixal_passive_DAT_only​",
# "Scrambled_suffixal_passive_NOM_only​",
# "Scrambled_suffixal_passive_DAT_only​",
# "Active_transitive_actor_NOM_only",
# "Active_transitive_undergoer_ACC_only​",
# "Ditransitive_recipient_DAT_only",
# "Suffixal_passive_undergoer_NOM_only​",
# "Suffixal_passive_actor_DAT_only"]
# #
# input_sentence = ["N_1&i/ka_1 actor_1&nom_1 N_2&(l)ul_2 undergoer_2&acc_2 V_3 action_3",
#                           "N_1&(l)ul undergoer_1&acc_1 N_2&i/ka_2 actor_2&nom_2 V_3 action_3",
#                           "N_1&i/ka_1 undergoer_1&nom_1 N_2&eykey/hanthey_2 actor_2&dat_2 V&i/hi/li/ki_3 action&psv_3",
#                           "N_1&eykey/hanthey_1 actor_1&dat_1 N_2&i/ka_2 undergoer_2&nom_2 V&i/hi/li/ki_3 action&psv_3",
#                           "N_1&i/ka_1 actor_1&nom_1 N_2 undergoer_2 V_3 action_3",
#                           "N_1 ​actor_1 N_2&(l)ul_2 undergoer_2&acc_2 V_3 action_3",
#                           "N_1 ​undergoer_1 N_2&i/ka_2 actor_2&nom_2 V_3 action_3",
#                           "N_1&(l)ul undergoer_1&acc_1 N_2 actor_2 V_3 action_3",
#                           "N_1&i/ka_1 undergoer_1&nom_1 N_2 actor_2 V&i/hi/li/ki_3 action&psv_3",
#                           "N_1 ​undergoer_1 N_2&eykey/hanthey_2 actor_2&dat_2 V&i/hi/li/ki_3 action&psv_3",
#                           "N_1 ​actor_1 N_2&i/ka_2 undergoer_2&nom_2 V&i/hi/li/ki_3 action&psv_3",
#                           "N_1&eykey/hanthey_1 actor_1&dat_1 N_2 undergoer_2 V&i/hi/li/ki_3 action&psv_3",
#                           "N_1&i/ka_1 actor_1&nom_1 V_2 action_2",
#                           "N_1&(l)ul undergoer_1&acc_1 V_2 action_2",
#                           "N_1&eykey/hanthey_1 rec_1&dat_1 V_2 action_2",
#                           "N_1&i/ka_1 undergoer_1&nom_1 V&i/hi/li/ki_2 action&psv_2",
#                           "N_1&eykey/hanthey_1 actor_1&dat_1 V&i/hi/li/ki_2 action&psv_2"
#                           ]
#
# item_list = ["N_1&i/ka_1",
# "actor_1&nom_1",
# "N_2&(l)ul_2",
# "undergoer_2&acc_2",
# "V_3",
# "action_3",
# "N_1&(l)ul",
# "undergoer_1&acc_1",
# "N_2&i/ka_2",
# "actor_2&nom_2",
# "undergoer_1&nom_1",
# "N_2&eykey/hanthey_2",
# "actor_2&dat_2",
# "V&i/hi/li/ki_3",
# "action&psv_3",
# "N_1&eykey/hanthey_1",
# "actor_1&dat_1",
# "undergoer_2&nom_2",
# "N_2",
# "undergoer_2",
# "N_1",
# "actor_1",
# "undergoer_1",
# "actor_2",
# "V_2",
# "action_2",
# "rec_1&dat_1",
# "V&i/hi/li/ki_2",
# "action&psv_2"]
#
# diction = {}
# for x in item_list:
#     num = 0
#     diction_inner = {}
#     for y in input_construction:
#         item = input_sentence[num].replace("\u200b", "").split(" ")
#         checked = False
#         for z in item:
#             print(x," ",z)
#             if x == z:
#                 print("true")
#                 checked = True
#         if checked == True:
#             print("d")
#             diction_inner[y.replace("\u200b", "").rstrip()] = input_freq_laplace[num]
#         else:
#             diction_inner[y.replace("\u200b", "").rstrip()] = 1
#         num += 1
#
#     diction[x.replace("\u200b","").rstrip()] = diction_inner
#     print(num)
#
# print(diction)