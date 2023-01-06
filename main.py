#!/usr/bin/env python3

from src.scrape import *
from src.scraper_day_index import *
from src.cleaning import clean_cols, clean_vals, remove_percent_and_round, convert_numeric, round_nearest_two, day_index_add_month_and_day
from src.visualize import bar_plot, bar_plot_with_twinx_line,line_plot_rolling_avg, line_plot
from config import *
from src.upload_mysql_func import upload_mysql
                                                

day_index_add_month_and_day(day_index)

def main(df):

    # cleaning dataset
    clean_cols(df)
    clean_vals(df)
    remove_percent_and_round(df, 'bounceRate')
    remove_percent_and_round(df, 'goal5ConversionRate')
    round_nearest_two(df, 'avgSessionDuration')
    round_nearest_two(df, 'pageviewsPerSession')
    convert_numeric(df)
    
    # visualizing and sending to graphs folder
    bar_plot(df,'channelGrouping','users')
    bar_plot_with_twinx_line(df, 'channelGrouping', 'goal5Completions', 'bounceRate')
    bar_plot_with_twinx_line(df, 'channelGrouping', 'goal5Completions', 'goal5ConversionRate')

    ##### uploading
    #upload_mysql(df)

main(df)


'''export df to_csv'''
#df.to_csv('/Users/rose/Documents/nstem_dir/webscrape/data/df2',index=False)


def day_index_graphs(day_index):
    day_index_add_month_and_day(day_index)
    convert_numeric(day_index)

    line_plot(day_index,'day_of_week','goal5Completions')
    line_plot_rolling_avg(day_index, 'month', 'goal5Completions')
    bar_plot(day_index,'day_of_week','goal5Completions')

day_index_graphs(day_index)