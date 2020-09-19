from Function.NaiveBayesFunction_revised import NaiveBayesAlgorithm


direc_num = 25
inst_num = 73
noise_num = 2

# 코퍼스의 누적 생성 횟수 (설명: 100개의 문장이 코퍼스로 존재 할때 위에 정해준 각 요소들의 값 만큰 코퍼스를 추출한다. 그 추출을 몇번 수행 할지 정하는 부분; 코퍼스의 양과 연관 있다.)
iteration_times = [1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81,86,91,96,101]#[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]#[1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81,86,91,96,101]#[5,10,15,20,25,30,35,40,45,50]

# 분석 타겟 정하기 (베이스(0) / 명사(1) / 동사(2))
test_target = ["base", "nountarget", "verbtarget"]
# 위의 부분은 조정 할 필요가 없고 아래의 부분을 관심 타겟이 따라 변경하면 된다.
test_target_type = 2

#정확한 정확도 값을 위한 반복측정 값 (이유: 한번 분석 후 생선된 정확도는 매 측정 마다 달라진 수 있다. 그래서 여러번 같은 분석을 수행후 생성된 정확도들의 평균값을 정확도로 사용한다; 수렴된 정확도 값과 연관 있다.)
repeat_num = 100


# 여기서부터는 개발된 나이브 베이즈를 활용하여 분석을 수행하는 부분이다.
# 정확도는 매 반복 측정 마다 리스트로 출력되며, 리스트의 값은 왼쪽부터, 전체 정확도, 방향에 대한 정확도, 도구에 대한 정확도 순이다.
naivebayesclass = NaiveBayesAlgorithm()

for num in iteration_times:
    average_repeat_total = 0
    average_repeat_directional = 0
    average_repeat_instrumental = 0
    outresult = ""
    for repeat in range(0,repeat_num): #base  nountarget   verbtarget  #"./DataFolder/form-feature-revised/20190516/"
        naivebayesclass.setdata(direc_num,inst_num,noise_num,num, "./DataFolder/form-feature-revised/"+test_target[test_target_type]+".txt", "./DataFolder/form-feature-revised/test.txt")
        average_repeat_total = average_repeat_total + naivebayesclass.NaiveBayes_Calculation()[0]
        average_repeat_directional = average_repeat_directional + naivebayesclass.NaiveBayes_Calculation()[1]
        average_repeat_instrumental = average_repeat_instrumental + naivebayesclass.NaiveBayes_Calculation()[2]
        # print(naivebayesclass.NaiveBayes_Calculation()[0],naivebayesclass.NaiveBayes_Calculation()[1],naivebayesclass.NaiveBayes_Calculation()[2])
    outresult = "["+str(round(average_repeat_total/repeat_num,2))+","+str(round(average_repeat_directional/repeat_num,2))+","+str(round(average_repeat_instrumental/repeat_num,2))+"]"
    print(outresult,",", end=' ')