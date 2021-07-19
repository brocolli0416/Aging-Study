library(ggplot2)
library(tidyr)
library(lme4)
library(dplyr)

## Load Data file ##
sldf = read.csv("./Ver3_YA_SL_RTs.csv")
  filter(Oc == 1) 
fadf = read.csv("./Ver3_FA_Summary.csv")


##### Overall Summary #####
str(sldf)
sum_df = sldf %>%
  #filter(Occurrence == "3") %>%
  dplyr::group_by(Subject, Position) %>%
  dplyr::summarise(mean = mean(RT))
  pivot_wider(names_from = 'Position', values_from = 'mean')

sum_fa = fadf %>%
  filter(Subject == "14"| Subject == '15') %>%
  group_by(Subject, Position) %>%
  summarise(mean = mean(False.Alarm)) %>%
  pivot_wider(names_from = 'Position', values_from = 'mean')
  

write.table(sum_df, "./Ver3_Summary.csv", append=TRUE, sep = ',')


##### Position wise Summary #####
positionwise.rt = sldf %>%
  group_by(Subject, Occurrence, Position) %>%
  summarise(rt_mean=mean(RT), hit_n=n()/16)
  pivot_wider(names_from = 'Position', values_from = 'rt_mean')
  rename('Pos1' = 3, 'Pos2' = 4, 'Pos3'= 5)

write.table(positionwise.rt, "./Apr28.Recognition.csv", append=TRUE, sep = ',')
  
  
##### Syllable wise Summary #####
syllablewise.rt = sldf %>%
    group_by(Position, Syllable) %>%
    summarise(rt_mean=mean(RT), hit_n=n()/4)
    pivot_wider(names_from = 'Syllable', values_from = 'rt_mean')
    rename('Pos1' = 3, 'Pos2' = 4, 'Pos3'= 5)

write.table(syllablewise.rt, "./Apr28.Recognition.csv", append=TRUE, sep = ',')
    

############################## Visualize ##########################

ggplot(sum_df, aes(x=Position, y=mean)) +
  geom_bar(stat="identity", fill='blue', alpha = 0.3) +
  ylab('Mean RT') +
  xlab('Syllable position') 

############################### GLM ###############################

df_mutated = mutate(sldf, pos2 = case_when(Position == 1 ~ -1,
                                         Position == 2 ~ 1,
                                         Position == 3 ~ 0),
                    pos3 = case_when(Position == 1 ~ -1,
                                     Position == 2 ~ 0,
                                     Position == 3 ~ 1))
df_mutated = mutate(df_mutated, oc2 = case_when(Occurrence == 1 ~ -1,
                                           Occurrence == 2 ~ 1,
                                           Occurrence == 3 ~ 0),
                    oc3 = case_when(Occurrence == 1 ~ -1,
                                     Occurrence == 2 ~ 0,
                                     Occurrence == 3 ~ 1))
#df_centered = mutate(df_mutated, centered_rt = RT - mean(RT))

test_model = lmer(RT ~ pos2 + pos3 + (1|Subject), data=df_centered)
summary(test_model)
model2 = lm(RT ~ pos2 + pos3, data = df_centered)
summary(model2)
anova(test_model, model2)
