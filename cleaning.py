import pandas as pd
from main import df

# CLEANING

def clean_cols(df):
    df.columns = df.columns.str.replace(' ', '_').str.replace(r'/','').str.replace('__','_').str.replace(')','').str.replace('(','')
    return df


def clean_vals(df):
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.upper().str.replace('\t|\n|,', '', regex=True)


def remove_percent_and_round(df, col):
    df[col] = df[col].str.rstrip('%').astype('float') 
    df[col] = df[col].round(2)
    return df


def convert_numeric(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = pd.to_numeric(df[col], errors='ignore')
    return df
