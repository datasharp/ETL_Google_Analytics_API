import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from scrape import date_range
#from main import *


def bar_plot(df, x, y):
    plt.figure(figsize=(3, 3))
    sns.barplot(data=df, x=x,
        y=y).set_title(f'{date_range}: {x} by {y}')
    plt.xticks(rotation=70)
    plt.savefig(r"/Users/rose/Documents/nstem_dir/webscrape/graphs/{} '{}'".format(x,y), bbox_inches='tight');
      

#bar_plot(day_index,'Day_of_Week','Start_a_Chapter_Goal_5_Completions')


def line_plot(df, x, y):
    plt.figure(figsize=(3, 3))
    sns.lineplot(data=df, x=x,
        y=y).set_title(f'{date_range}: {x} by {y}')
    plt.xticks(rotation=70)
    plt.savefig(r"/Users/rose/Documents/nstem_dir/webscrape/graphs/{} '{}{}'".format(x,y,1), bbox_inches='tight');

#line_plot(day_index,'Day_of_Week','Start_a_Chapter_Goal_5_Completions')

def line_plot_rolling_avg(df,x,y):
    day_index[f'{rolling_window}day_rolling_avg'] = day_index[y].rolling(rolling_window).mean()

    plt.figure(figsize=(15,5))
    sns.lineplot(data=df, x=x, y=y).set_title(f'{date_range}: {y} by {x} with Rolling Average')
    sns.lineplot(data=df, x=x, y=f'{rolling_window}day_rolling_avg', label=f'{rolling_window} day rolling avg')
    plt.xticks(rotation=70)
    plt.savefig(r"/Users/rose/Documents/nstem_dir/webscrape/graphs/{} '{}'".format(x,y), bbox_inches='tight');

#line_plot_rolling_avg(day_index, 'Month', 'Start_a_Chapter_Goal_5_Completions')

def bar_plot_with_twinx_line(df, x, y, z):
    b = df.plot.bar(x=x,
                        y=y,
                        figsize=(15,5), 
                        color='#33DAFF',
                        fontsize=13, 
                        title= (f'{date_range}: {x} with {y} and {z}')
                        )
    b2=b.twinx()
    b2.plot(df[z].values, linestyle ='-', marker='o', linewidth=2.0,color="green")
    b2.figure.savefig(r"/Users/rose/Documents/nstem_dir/webscrape/graphs/{} '{}'{}".format(x,y,z), bbox_inches='tight');


