from scrape import *
from cleaning import clean_cols, clean_vals, remove_percent_and_round, convert_numeric
from visualize import bar_plot, bar_plot_with_twinx_line
from datetime import datetime, timedelta



start_date = datetime.strftime(datetime.now() - timedelta(days = 30),'%Y-%m-%d')
end_date = datetime.strftime(datetime.now(),'%Y-%m-%d')

rolling_window = 7


# api call function
df = google_analytics_reporting_api_data_extraction(viewID,dim,met,start_date,end_date,refresh_token,\
                                                    transaction_type,goal_number,condition)


def clean(df):
    clean_cols(df)
    clean_vals(df)
    remove_percent_and_round(df, 'bounceRate')
    remove_percent_and_round(df, 'goal5ConversionRate')
    convert_numeric(df)

    return df

clean(df)


bar_plot(df,'channelGrouping','users')
bar_plot_with_twinx_line(df, 'channelGrouping', 'goal5Completions', 'bounceRate')
bar_plot_with_twinx_line(df, 'channelGrouping', 'goal5Completions', 'goal5ConversionRate')

