import csv
import glob
import os
import pandas as pd
from pandas.io.parsers import read_csv
from sklearn import linear_model
### Import mst_accuracy function to analyze Word MST
import sys
sys.path.append('c:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\ProjectBL\\CombinedMST\\Analysis\\')
from cMST_analysis import mst_accuracy
from cMST_analysis import check_pass
### Import all functions needed to analyze RT, false alarm rate, familiarity, and AFC accuracy rate
sys.path.append('c:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\ProjectBL\\SL alone_ver2\\Analysis\\')
import modifiedSLanalysis as sl

#####################################
### Prepare classes and functions ###
#####################################

class File:
    def __init__(self, subject, group, session, condition):
        self.subject = subject
        self.group = group
        self.session = session
        self.condition = condition
    
    def mst_process(self):
        mstdf = pd.read_csv(f'{self.group}/Renamed/{self.subject}_1.csv')
        acc_rate, alldata = mst_accuracy(mstdf, self.subject)
        headphone_resp = check_pass(mstdf)
        alldata.append(headphone_resp)
        return alldata # Return a list of z-scores, d-primes, LDI, and subject ID

    def sl_process(self):
        allSLdata = []
        sldf = pd.read_csv(f'{self.group}/Renamed/{self.subject}_2.csv')
         # Get familiarity rating
        old, part, word = sl.get_familiarity_rating(sldf)
        # Get AFC accuracy
        afc_accuracy = sl.get_afc_accuracy(sldf)
        # Check attentions
        attention = sl.check_pass(sldf) 
        allSLdata.extend([self.subject, old, part, word, afc_accuracy])
        allSLdata += attention
        return allSLdata # Return a list

    def sl_RT(self):
        sldf = pd.read_csv(f'{self.group}/Renamed/{self.subject}_2.csv')
        rt_df = sl.get_individual_RT(sldf, self.subject)
        return rt_df # Return a dataframe

### Rename data files and get file variables
def tidyFiles(group, session):
    path = os.getcwd()
    df_list = glob.glob(os.path.join(path, f"{group}/", "*.csv"))
    mst_subjects = []
    sl_subjects = []
    all_files = []
    for i in df_list:
        df = pd.read_csv(i)
        subject = df["participant"][0]
        condition = [i for i in df["Condition"] if pd.isnull(i) == False]
        condition = condition[0]
        newdf = os.path.join(path, f"{group}/Renamed/{subject}_{condition}.csv")
        os.rename(i, newdf)
        if condition[0] == '1':
            mst_subjects.append(subject)
        elif condition[0] == '2':
            sl_subjects.append(subject)
        file = File(subject, group, session, condition)
        all_files.append(file)
    return mst_subjects, sl_subjects, all_files

### SL Reaction Time preprocessing and return a cleaner dataframe, output dataframe to csv
def get_positionwise(df):
    grouped_df = df.groupby(['Subject','Position']).mean()
    wider_df = grouped_df.pivot_table(index=['Subject'], columns='Position', values='RT')
    wider_df.to_csv('YA_RT_byposition.csv', mode = 'a')
    return wider_df

########################
### Perform analyses ###
########################

### Get all data for each individual subject and output to csv
### Can perform after only one session

# mstlist, sllist, alllist = tidyFiles("OA", 1)
# print(mstlist) # participant list for MST follow-up
# print(sllist) # participant list for SL follow-up

# for file in alllist:
#     if file.condition == '1':
#         data = file.mst_process()
#         pass
#     elif file.condition == '2':
#         data = file.sl_process()
#         RTdata = file.sl_RT()
#         RTdata.to_csv(f'{file.group}_rawRT.csv', mode='a', header=False, index=False)
#         pass
#     with open (f'{file.group}raw.csv', 'a', newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow(data)

### Uncomment below to get average RT per position per individual
RTdata = pd.read_csv('OA_rawRT.csv')
get_positionwise(RTdata)


