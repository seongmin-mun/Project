#추가 정보 : 각 구조별 인풋의 양

# 공통 데이터

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


# itemsfreqdict = {'1': {'N&i/ka': 6, 'N&(l)ul': 3, 'N&eykey/hanthey': 4, 'N': 4},
#                  '2': {'actor&nom': 3, 'undergoer&acc': 3, 'undergoer&nom': 3, 'actor&dat': 3,
#                        'actor': 2, 'undergoer': 2, 'rec&dat': 1},
#                  '3': {'N&(l)ul': 2, 'N&i/ka': 4, 'N&eykey/hanthey': 2, 'N': 4, 'V': 3,
#                        'V&i/hi/li/ki': 2},
#                  '4': {'undergoer&acc': 2, 'actor&nom': 2, 'actor&dat': 2, 'undergoer&nom': 2,
#                        'undergoer': 2, 'actor': 2, 'action': 3, 'action&psv': 2},
#                  '5': {'V': 6, 'V&i/hi/li/ki': 6},
#                  '6': {'action': 6, 'action&psv': 6}}
# itemssquenfreq = [0, 17, 17, 17, 17, 12, 12]

# 일반 데이터
input_freq = [1757, 51, 2, 1, 268, 19, 6, 0, 0, 0, 0, 0, 935, 1938, 234, 407, 13, 53, 1155, 40, 0, 20, 0, 3, 0, 0, 0, 0, 0]
# origin_num = 5631

#각 구문들 초기 빈도 값 -> 판별 결과에 따라 업데이트 될 예정
# initial_construction_freq = {"Canonical_active_transitive":1757,
# "Scrambled_active_transitive":51,
# "Canonical_suffixal_passive":2,
# "Scrambled_suffixal_passive":1,
# "Canonical_active_transitive_NOM_only":268,
# "Canonical_active_transitive_ACC_only":19,
# "Scrambled_active_transitive_NOM_only":6,
# "Scrambled_active_transitive_ACC_only":0,
# "Canonical_suffixal_passive_NOM_only":0,
# "Canonical_suffixal_passive_DAT_only":0,
# "Scrambled_suffixal_passive_NOM_only":0,
# "Scrambled_suffixal_passive_DAT_only":0,
# "Active_transitive_actor_NOM_only":935,
# "Active_transitive_undergoer_ACC_only":1938,
# "Ditransitive_recipient_DAT_only":234,
# "Suffixal_passive_undergoer_NOM_only":407,
# "Suffixal_passive_actor_DAT_only":13}


# origin_itemsfreqdict = {'N&i/ka': {'Canonical_active_transitive': 1757, 'Scrambled_active_transitive': 51, 'Canonical_suffixal_passive': 2, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 268, 'Canonical_active_transitive_ACC_only': 0, 'Scrambled_active_transitive_NOM_only': 6, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 935, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 407, 'Suffixal_passive_actor_DAT_only': 0}, 'N': {'Canonical_active_transitive': 0, 'Scrambled_active_transitive': 0, 'Canonical_suffixal_passive': 0, 'Scrambled_suffixal_passive': 0, 'Canonical_active_transitive_NOM_only': 268, 'Canonical_active_transitive_ACC_only': 19, 'Scrambled_active_transitive_NOM_only': 6, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 0}, 'N&(l)ul': {'Canonical_active_transitive': 1757, 'Scrambled_active_transitive': 51, 'Canonical_suffixal_passive': 0, 'Scrambled_suffixal_passive': 0, 'Canonical_active_transitive_NOM_only': 0, 'Canonical_active_transitive_ACC_only': 19, 'Scrambled_active_transitive_NOM_only': 0, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 1938, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 0}, 'V': {'Canonical_active_transitive': 1757, 'Scrambled_active_transitive': 51, 'Canonical_suffixal_passive': 0, 'Scrambled_suffixal_passive': 0, 'Canonical_active_transitive_NOM_only': 268, 'Canonical_active_transitive_ACC_only': 19, 'Scrambled_active_transitive_NOM_only': 6, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 935, 'Active_transitive_undergoer_ACC_only': 1938, 'Ditransitive_recipient_DAT_only': 234, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 0}, 'N&eykey/hanthey': {'Canonical_active_transitive': 0, 'Scrambled_active_transitive': 0, 'Canonical_suffixal_passive': 2, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 0, 'Canonical_active_transitive_ACC_only': 0, 'Scrambled_active_transitive_NOM_only': 0, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 234, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 13}, 'V&i/hi/li/ki': {'Canonical_active_transitive': 0, 'Scrambled_active_transitive': 0, 'Canonical_suffixal_passive': 2, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 0, 'Canonical_active_transitive_ACC_only': 0, 'Scrambled_active_transitive_NOM_only': 0, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 407, 'Suffixal_passive_actor_DAT_only': 13}, 'actor&nom': {'Canonical_active_transitive': 1757, 'Scrambled_active_transitive': 51, 'Canonical_suffixal_passive': 0, 'Scrambled_suffixal_passive': 0, 'Canonical_active_transitive_NOM_only': 268, 'Canonical_active_transitive_ACC_only': 0, 'Scrambled_active_transitive_NOM_only': 6, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 935, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 0}, 'undergoer&acc': {'Canonical_active_transitive': 1757, 'Scrambled_active_transitive': 51, 'Canonical_suffixal_passive': 0, 'Scrambled_suffixal_passive': 0, 'Canonical_active_transitive_NOM_only': 0, 'Canonical_active_transitive_ACC_only': 19, 'Scrambled_active_transitive_NOM_only': 0, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 1938, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 0}, 'action': {'Canonical_active_transitive': 1757, 'Scrambled_active_transitive': 51, 'Canonical_suffixal_passive': 0, 'Scrambled_suffixal_passive': 0, 'Canonical_active_transitive_NOM_only': 268, 'Canonical_active_transitive_ACC_only': 19, 'Scrambled_active_transitive_NOM_only': 6, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 935, 'Active_transitive_undergoer_ACC_only': 1938, 'Ditransitive_recipient_DAT_only': 234, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 0}, 'undergoer&nom': {'Canonical_active_transitive': 0, 'Scrambled_active_transitive': 0, 'Canonical_suffixal_passive': 2, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 0, 'Canonical_active_transitive_ACC_only': 0, 'Scrambled_active_transitive_NOM_only': 0, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 407, 'Suffixal_passive_actor_DAT_only': 0}, 'actor&dat': {'Canonical_active_transitive': 0, 'Scrambled_active_transitive': 0, 'Canonical_suffixal_passive': 2, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 0, 'Canonical_active_transitive_ACC_only': 0, 'Scrambled_active_transitive_NOM_only': 0, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 13}, 'action&psv': {'Canonical_active_transitive': 0, 'Scrambled_active_transitive': 0, 'Canonical_suffixal_passive': 2, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 0, 'Canonical_active_transitive_ACC_only': 0, 'Scrambled_active_transitive_NOM_only': 0, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 407, 'Suffixal_passive_actor_DAT_only': 13}, 'undergoer': {'Canonical_active_transitive': 0, 'Scrambled_active_transitive': 0, 'Canonical_suffixal_passive': 0, 'Scrambled_suffixal_passive': 0, 'Canonical_active_transitive_NOM_only': 268, 'Canonical_active_transitive_ACC_only': 0, 'Scrambled_active_transitive_NOM_only': 0, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 0}, 'actor': {'Canonical_active_transitive': 0, 'Scrambled_active_transitive': 0, 'Canonical_suffixal_passive': 0, 'Scrambled_suffixal_passive': 0, 'Canonical_active_transitive_NOM_only': 0, 'Canonical_active_transitive_ACC_only': 19, 'Scrambled_active_transitive_NOM_only': 0, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 0, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 0}, 'rec&dat': {'Canonical_active_transitive': 0, 'Scrambled_active_transitive': 0, 'Canonical_suffixal_passive': 0, 'Scrambled_suffixal_passive': 0, 'Canonical_active_transitive_NOM_only': 0, 'Canonical_active_transitive_ACC_only': 0, 'Scrambled_active_transitive_NOM_only': 0, 'Scrambled_active_transitive_ACC_only': 0, 'Canonical_suffixal_passive_NOM_only': 0, 'Canonical_suffixal_passive_DAT_only': 0, 'Scrambled_suffixal_passive_NOM_only': 0, 'Scrambled_suffixal_passive_DAT_only': 0, 'Active_transitive_actor_NOM_only': 0, 'Active_transitive_undergoer_ACC_only': 0, 'Ditransitive_recipient_DAT_only': 234, 'Suffixal_passive_undergoer_NOM_only': 0, 'Suffixal_passive_actor_DAT_only': 0}}


# 라플라스 적용
input_freq_laplace = [1758, 52, 3, 2, 269, 20, 7, 1, 1, 1, 1, 1, 936, 1939, 235, 408, 14, 54, 1156, 41, 1, 21, 1, 4, 1, 1, 1, 1, 1]
# laplace_num = 5648

#각 구문들 초기 빈도 값 -> 판별 결과에 따라 업데이트 될 예정
# initial_construction_freq_laplace = {"Canonical_active_transitive":1758,
# "Scrambled_active_transitive":52,
# "Canonical_suffixal_passive":3,
# "Scrambled_suffixal_passive":2,
# "Canonical_active_transitive_NOM_only":269,
# "Canonical_active_transitive_ACC_only":20,
# "Scrambled_active_transitive_NOM_only":7,
# "Scrambled_active_transitive_ACC_only":1,
# "Canonical_suffixal_passive_NOM_only":1,
# "Canonical_suffixal_passive_DAT_only":1,
# "Scrambled_suffixal_passive_NOM_only":1,
# "Scrambled_suffixal_passive_DAT_only":1,
# "Active_transitive_actor_NOM_only":936,
# "Active_transitive_undergoer_ACC_only":1939,
# "Ditransitive_recipient_DAT_only":235,
# "Suffixal_passive_undergoer_NOM_only":408,
# "Suffixal_passive_actor_DAT_only":14}

#laplace_itemsfreqdict = {'N&i/ka': {'Canonical_active_transitive': 1758, 'Scrambled_active_transitive': 52, 'Canonical_suffixal_passive': 3, 'Scrambled_suffixal_passive': 2, 'Canonical_active_transitive_NOM_only': 269, 'Canonical_active_transitive_ACC_only': 1, 'Scrambled_active_transitive_NOM_only': 7, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 936, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 408, 'Suffixal_passive_actor_DAT_only': 1}, 'N': {'Canonical_active_transitive': 1, 'Scrambled_active_transitive': 1, 'Canonical_suffixal_passive': 1, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 269, 'Canonical_active_transitive_ACC_only': 20, 'Scrambled_active_transitive_NOM_only': 7, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 1}, 'N&(l)ul': {'Canonical_active_transitive': 1758, 'Scrambled_active_transitive': 52, 'Canonical_suffixal_passive': 1, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 1, 'Canonical_active_transitive_ACC_only': 20, 'Scrambled_active_transitive_NOM_only': 1, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1939, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 1}, 'V': {'Canonical_active_transitive': 1758, 'Scrambled_active_transitive': 52, 'Canonical_suffixal_passive': 1, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 269, 'Canonical_active_transitive_ACC_only': 20, 'Scrambled_active_transitive_NOM_only': 7, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 936, 'Active_transitive_undergoer_ACC_only': 1939, 'Ditransitive_recipient_DAT_only': 235, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 1}, 'N&eykey/hanthey': {'Canonical_active_transitive': 1, 'Scrambled_active_transitive': 1, 'Canonical_suffixal_passive': 3, 'Scrambled_suffixal_passive': 2, 'Canonical_active_transitive_NOM_only': 1, 'Canonical_active_transitive_ACC_only': 1, 'Scrambled_active_transitive_NOM_only': 1, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 235, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 14}, 'V&i/hi/li/ki': {'Canonical_active_transitive': 1, 'Scrambled_active_transitive': 1, 'Canonical_suffixal_passive': 3, 'Scrambled_suffixal_passive': 2, 'Canonical_active_transitive_NOM_only': 1, 'Canonical_active_transitive_ACC_only': 1, 'Scrambled_active_transitive_NOM_only': 1, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 408, 'Suffixal_passive_actor_DAT_only': 14}, 'actor&nom': {'Canonical_active_transitive': 1758, 'Scrambled_active_transitive': 52, 'Canonical_suffixal_passive': 1, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 269, 'Canonical_active_transitive_ACC_only': 1, 'Scrambled_active_transitive_NOM_only': 7, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 936, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 1}, 'undergoer&acc': {'Canonical_active_transitive': 1758, 'Scrambled_active_transitive': 52, 'Canonical_suffixal_passive': 1, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 1, 'Canonical_active_transitive_ACC_only': 20, 'Scrambled_active_transitive_NOM_only': 1, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1939, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 1}, 'action': {'Canonical_active_transitive': 1758, 'Scrambled_active_transitive': 52, 'Canonical_suffixal_passive': 1, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 269, 'Canonical_active_transitive_ACC_only': 20, 'Scrambled_active_transitive_NOM_only': 7, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 936, 'Active_transitive_undergoer_ACC_only': 1939, 'Ditransitive_recipient_DAT_only': 235, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 1}, 'undergoer&nom': {'Canonical_active_transitive': 1, 'Scrambled_active_transitive': 1, 'Canonical_suffixal_passive': 3, 'Scrambled_suffixal_passive': 2, 'Canonical_active_transitive_NOM_only': 1, 'Canonical_active_transitive_ACC_only': 1, 'Scrambled_active_transitive_NOM_only': 1, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 408, 'Suffixal_passive_actor_DAT_only': 1}, 'actor&dat': {'Canonical_active_transitive': 1, 'Scrambled_active_transitive': 1, 'Canonical_suffixal_passive': 3, 'Scrambled_suffixal_passive': 2, 'Canonical_active_transitive_NOM_only': 1, 'Canonical_active_transitive_ACC_only': 1, 'Scrambled_active_transitive_NOM_only': 1, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 14}, 'action&psv': {'Canonical_active_transitive': 1, 'Scrambled_active_transitive': 1, 'Canonical_suffixal_passive': 3, 'Scrambled_suffixal_passive': 2, 'Canonical_active_transitive_NOM_only': 1, 'Canonical_active_transitive_ACC_only': 1, 'Scrambled_active_transitive_NOM_only': 1, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 408, 'Suffixal_passive_actor_DAT_only': 14}, 'undergoer': {'Canonical_active_transitive': 1, 'Scrambled_active_transitive': 1, 'Canonical_suffixal_passive': 1, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 269, 'Canonical_active_transitive_ACC_only': 1, 'Scrambled_active_transitive_NOM_only': 1, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 1}, 'actor': {'Canonical_active_transitive': 1, 'Scrambled_active_transitive': 1, 'Canonical_suffixal_passive': 1, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 1, 'Canonical_active_transitive_ACC_only': 20, 'Scrambled_active_transitive_NOM_only': 1, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 1, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 1}, 'rec&dat': {'Canonical_active_transitive': 1, 'Scrambled_active_transitive': 1, 'Canonical_suffixal_passive': 1, 'Scrambled_suffixal_passive': 1, 'Canonical_active_transitive_NOM_only': 1, 'Canonical_active_transitive_ACC_only': 1, 'Scrambled_active_transitive_NOM_only': 1, 'Scrambled_active_transitive_ACC_only': 1, 'Canonical_suffixal_passive_NOM_only': 1, 'Canonical_suffixal_passive_DAT_only': 1, 'Scrambled_suffixal_passive_NOM_only': 1, 'Scrambled_suffixal_passive_DAT_only': 1, 'Active_transitive_actor_NOM_only': 1, 'Active_transitive_undergoer_ACC_only': 1, 'Ditransitive_recipient_DAT_only': 235, 'Suffixal_passive_undergoer_NOM_only': 1, 'Suffixal_passive_actor_DAT_only': 1}}


#아이템 by 구문 형태 매트릭스 생성


#
#
# item_list = ["N&i/ka","N","N&(l)ul","V","N&eykey/hanthey","V&i/hi/li/ki","actor&nom","undergoer&acc","action","undergoer&nom","actor&dat","action&psv","undergoer","​actor","rec&dat", "nd"]
#
# diction = {}
# for x in item_list:
#     num = 0
#     diction_inner = {}
#     for y in input_construction:
#         item = input_sentence[num].split(" ")
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
#
# num = 0
# diction2 = {}
# for y in input_construction:
#     diction2[y.replace("\u200b", "").rstrip()] = input_sentence[num]
#     num += 1
#
# print(diction2)
#
#
# num = 0
# diction3 = {}
# for y in input_construction:
#     diction3[y.replace("\u200b", "").rstrip()] = input_freq_laplace[num]
#     num += 1
#
# print(diction3)


#bigNames

# bigNames = {
#             "Canonical_active_transitive_pt": ["Canonical_active_transitive", "Canonical_active_transitive_no_ACC",
#                                                "Canonical_active_transitive_no_NOM"],
#             "Scrambled_active_transitive_pt": ["Scrambled_active_transitive", "Scrambled_active_transitive_no_ACC",
#                                                "Scrambled_active_transitive_no_NOM"],
#             "Canonical_suffixal_passive_pt": ["Canonical_suffixal_passive", "Canonical_suffixal_passive_NOM_only",
#                                               "Canonical_suffixal_passive_no_NOM"],
#             "Scrambled_suffixal_passive_pt": ["Scrambled_suffixal_passive", "Scrambled_suffixal_passive_no_DAT",
#                                               "Scrambled_suffixal_passive_no_NOM"],
#             "Active_transitive_pt": ["Active_transitive_actor_NOM_only", "Active_transitive_undergoer_ACC_only",
#                                      "Active_transitive_actor_no_case", "Active_transitive_undergoer_no_case",
#                                      "Active_transitive_undetermined_no_case",
#                                      "Active_transitive_actor_undergoer_no_case",
#                                      "Active_transitive_undergoer_actor_no_case",
#                                      "Active_transitive_undetermined_undetermined_no_case"],
#             "Suffixal_passive_pt": ["Suffixal_passive_undergoer_NOM_only", "Suffixal_passive_actor_DAT_only",
#                                     "Suffixal_passive_actor_no_case", "Suffixal_passive_undergoer_no_case",
#                                     "Suffixal_passive_undetermined_no_case", "Suffixal_passive_actor_undergoer_no_case",
#                                     "Suffixal_passive_undergoer_actor_no_case",
#                                     "Suffixal_passive_undetermined_undetermined_no_case"],
#             "Ditransitive_pt": ["Ditransitive_recipient_DAT_only"]
#             }
# a = "Canonical_active_transitive_no_NOM"
# b = "Canonical_active_transitive"
# for key, value in bigNames.items():
#     for construcType in value:
#         if a == construcType:
#             print(key)


##regression
# input_construction
# input_sentence
# input_freq

# itemFreq = {}
#
# num = 0
# for x in input_freq:
#     if "passive" in input_construction[num]:
#         if input_freq[num] != 0:
#             print(input_construction[num], " ", input_sentence[num], " ", input_freq[num])
#             item = input_sentence[num].split(" ")
#             for y in item:
#                 if itemFreq.get(y) == None:
#                     itemFreq[y] = input_freq[num]
#                 else:
#                     itemFreq[y] = itemFreq.get(y) + input_freq[num]
#     num = num + 1
#
# print(itemFreq)


def getNGrams(wordlist, n):
    ngrams = []
    for i in range(len(wordlist)-(n-1)):
        ngrams.append(wordlist[i:i+n])
    return ngrams


itemList = {}

##Ngram사용해서 리스트 생성하기

num = 0
for x in input_freq:
    if "passive" in input_construction[num]:
        if input_freq[num] != 0:
            #print(input_construction[num], " ", input_sentence[num], " ", input_freq[num])
            item = input_sentence[num].split(" ")
            wordlist = []
            for y in item:
                wordlist.append(y)
            #print(wordlist)
            for num in range(1, len(wordlist) + 1):
                for x in getNGrams(wordlist, num):
                    out = ""
                    for y in x:
                        out = out + y + " "
                    store = out.lstrip()
                    if itemList.get(store) == None:
                        itemList[store] = 1
                    else:
                        pass
    num = num + 1

#print(itemList)
print("Construction",",", end=' ')
for x, y in itemList.items():
    print(x.strip().replace(" ","_"),",", end=' ')

print("Passive",",", end=' ')
##리스트 단어에 빈도수 입히기

itemFreq = {}


num = 0
for x in input_freq:
    print("")
    print(input_construction[num], ",", end=' ')
    for x, y in itemList.items():
        if x in input_sentence[num]:
            print(input_freq[num], ",", end=' ')
        else:
            print(0, ",", end=' ')
    if "passive" in input_construction[num] and input_freq[num] != 0:
        print(1, "", end='')
    else:
        print(0, "", end='')

    num = num + 1