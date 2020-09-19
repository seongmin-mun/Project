from Functions.Bayesian import bayes_process

bayes_processing = bayes_process()
bayes_processing.setdata(5,2,1,4,2,10)  #반복 횟수, 추정량, 스무딩, 연속 N값(워킹메모리), 테스트 추정량, 테스트 연속 N값(워킹메모리)
bayes_processing.bayes_process_inner()