import pandas as pd


#create function for column removal
###############################################################
def column_removal(input_path, output_path, columns_removal_choice, keyword_column, keyword):

    #read input csv into a dataframe
    df = pd.read_csv(input_path)

    #remove coloumns
    df = df.drop(columns_removal_choice, axis=1)

    #remove rows that match keyword in specific column
    df = df[~df[keyword_column].str.contains(keyword, na=False)]

    #save modified df to output csv
    df.to_csv(output_path, index=False)
###############################################################




input_path = "C:\\Temp\\usrdeets.csv" #your path where the csv is currently sitting
output_path = "C:\\Temp\\usrdeetsnoauth.csv" #path you want updated file to go to

#in order for the column removal choice var to work you must already know which columns you want removed. take a look at your CSV before running script
column_removal_choice = ['mfaCapable', 'passwordlessCapable', 'ssprCapable', 'ssprRegistered', 'ssprEnabled']

keyword_column = 'methodsRegistered' #the column containing the keyword
keyword = 'Microsoft Authenticator app' #the keyword itself

column_removal(input_path, output_path, column_removal_choice, keyword_column,keyword)
