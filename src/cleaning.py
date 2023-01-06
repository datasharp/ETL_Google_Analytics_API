import pandas as pd

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

def round_nearest_two(df, col):
    df[col] = df[col].astype(float).round(2)
    return df


def convert_numeric(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = pd.to_numeric(df[col], errors='ignore')
    return df



def day_index_add_month_and_day(df):
    df.iloc[:,0] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month_name()
    df['day_of_week'] = df['date'].dt.day_name()
    return df






if __name__ == "__main__" :
    day_index_add_month_and_day()