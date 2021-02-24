#LSA
# from Code.Models.LSA import LSA_class
# topicNum = 2
# lsa = LSA_class("../../Data/essay/L2_t"+str(topicNum),"../../Data/essay/NSK/nsk_topic"+str(topicNum)+".txt",10,"../../Data/OutPut/LSA_Cosine_Similarity_t"+str(topicNum)+".csv",topicNum)
# lsa.processing()

# LDA
# from Code.Models.LDA import LDA_class
# topicNum = 2
# lda = LDA_class("../../Data/essay/L2_t"+str(topicNum),"../../Data/essay/NSK/nsk_topic"+str(topicNum)+".txt",10,"../../Data/OutPut/LDA_Cosine_Similarity_t"+str(topicNum)+".csv", topicNum)
# lda.processing()

# # Word2Vec
# from Code.Models.Word2Vec import Word2Vec_class
# topicNum = 2
# word2Vec = Word2Vec_class("../../Data/essay/L2_t"+str(topicNum),"../../Data/essay/NSK/nsk_topic"+str(topicNum)+".txt", "../../Data/ko/ko.bin", "../../Data/OutPut/Word2Vec_Cosine_Similarity_t"+str(topicNum)+".csv", topicNum)
# word2Vec.processing()


# All-BERT
from Code.BERT.BERT import BERT_class

for topicNum in range(1,3):
    topicNum = str(topicNum)
    for i in range(0,10):
        runBERT = BERT_class("../../Data/t-SNE/All_37dim/Topic"+str(topicNum)+"_tSNE_epoch_"+str(i)+".csv", "../../Data/BERTOutput/All_37dim/BERT_Cosine_Similarity_topic"+str(topicNum)+"_epoch_"+str(i)+".csv", topicNum, 0.2)
        runBERT.processing()


# # eachOther-BERT
# from Code.BERT.BERT_re import BERT_re_class
#
# for i in range(1,3):
#     topicNum = i
#     for j in range(0, 10):
#         epoch = "epoch_"+str(j)
#         runBERT = BERT_re_class("../../Data/t-SNE/eachOther/", "../../Data/BERTOutput/eachOther/BERT_Cosine_Similarity_t"+str(topicNum)+"_independence_"+epoch+".csv", topicNum, epoch)
#         runBERT.processing()