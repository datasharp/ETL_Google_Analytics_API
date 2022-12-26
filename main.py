from scrape import *
from cleaning import clean_cols, clean_vals, remove_percent_and_round, convert_numeric, round_nearest_two
from visualize import bar_plot, bar_plot_with_twinx_line
from datetime import datetime, timedelta
from config import *
from upload_mysql_func import upload_mysql

# api call function

df = google_analytics_reporting_api_data_extraction(viewID,dim,met,start_date,end_date,refresh_token,\
                                                    transaction_type,goal_number,condition)


# cleaning dataset

def clean(df):
    clean_cols(df)
    clean_vals(df)
    remove_percent_and_round(df, 'bounceRate')
    remove_percent_and_round(df, 'goal5ConversionRate')
    round_nearest_two(df, 'avgSessionDuration')
    round_nearest_two(df, 'pageviewsPerSession')
    convert_numeric(df)

    return df

clean(df)


# visualizing and sending to graphs folder

bar_plot(df,'channelGrouping','users')

bar_plot_with_twinx_line(df, 'channelGrouping', 'goal5Completions', 'bounceRate')
bar_plot_with_twinx_line(df, 'channelGrouping', 'goal5Completions', 'goal5ConversionRate')


# uploading

upload_mysql(df)



