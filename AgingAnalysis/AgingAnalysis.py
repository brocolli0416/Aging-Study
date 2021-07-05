import csv
import pandas as pd
### Import mst_accuracy function to analyze Word MST
import sys
sys.path.append('c:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\ProjectBL\\CombinedMST\\Analysis\\')
from cMST_analysis import mst_accuracy
### Import all functions needed to analyze RT, false alarm rate, familiarity, and AFC accuracy rate
sys.path.append('c:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\ProjectBL\\SL alone_ver2\\Analysis\\')
import modifiedSLanalysis as sl

### Load data file ###
### Enter data files to import ###
df_list = [5]

### Get all data except for SL RT for each individual subject and output to csv
def preprocess(group, df_list):
    for i in df_list:
        ## Load MST file
        mstdf = pd.read_csv(f'{group}/MST/{str(i)}.csv')
        ## Get Z-scores, d'(recognition), d'(discrimination), and LDI
        acc_rate, alldata = mst_accuracy(mstdf, i)
        ## Look for order condition
        try:
            condition = [i for i in mstdf["Condition"] if pd.isnull(i) == False]
        except:
            condition = ['NA']

        sldf = pd.read_csv(f'{group}/SL/{str(i)}.csv')
        # Get familiarity rating
        old, part, word = sl.get_familiarity_rating(sldf)
        # Get AFC accuracy
        afc_accuracy = sl.get_afc_accuracy(sldf)
        # Check attentions
        attention = sl.check_pass(sldf)
        # Look for order condition
        try:
            condition = [i for i in sldf["Condition"] if pd.isnull(i) == False]
        except:
            condition = ['NA']
        # Combine all data into one list
        alldata.extend([old, part, word, afc_accuracy, condition[0]])
        alldata += attention

        ## Output all to csv
        with open (f'{group}raw.csv', 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(alldata)
    return

### SL preprocessing ###
def process_impsl(df_list): # Get data for RT and false alarm rate
    for i in df_list:
        df = pd.read_csv(f'YA/SL/{str(i)}.csv')
        sl.get_individual_RT(df, i)
        sl.get_fas(df, i)
    return

### Uncomment and run ###
preprocess('YA', df_list)
#process_impsl(df_list)