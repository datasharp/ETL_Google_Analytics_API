import pandas as pd
from sqlalchemy import create_engine
import os
import pymysql


password = os.getenv('sql_password')

def upload_mysql(df):
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/nstem_start_a_chapter")



    df.to_sql(name='default_chapters',con=engine, if_exists='replace', index=False)  



if __name__ == "__main__" :
    upload_mysql()