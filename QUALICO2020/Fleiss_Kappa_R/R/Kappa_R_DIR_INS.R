install.packages("irr")
library(irr)
data(diagnoses)
dat <- diagnoses[,1:3]
kappa2(dat[,c(1,2)], "unweighted")
kappam.fleiss(dat)




#1.예전 코퍼스 (형태-의미)
#memory & previous_works
gc()
rm(list=ls())

getwd()
setwd("/Users/seongminmun/Desktop/Corpus_annotation/Fleiss_Kappa_R/Data")
dir()
Kappa_lo <- read.csv("Fleiss_Kappa_lo.csv",head=T ) 
head(Kappa_lo)
summary(Kappa_lo)
kappam.fleiss(Kappa_lo)
