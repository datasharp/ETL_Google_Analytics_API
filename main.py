from scrape import *
from cleaning import clean_cols, clean_vals, remove_percent_and_round, convert_numeric

start_date = '2022-12-01'
end_date = '2022-12-23'


df = google_analytics_reporting_api_data_extraction(viewID,dim,met,start_date,end_date,refresh_token,\
                                                    transaction_type,goal_number,condition)


def clean_and_visualize(df):
    clean_cols(df)
    clean_vals(df)
    remove_percent_and_round(df, 'bounceRate')
    remove_percent_and_round(df, 'goal5ConversionRate')
    convert_numeric(df)

    return df

clean_and_visualize(df)