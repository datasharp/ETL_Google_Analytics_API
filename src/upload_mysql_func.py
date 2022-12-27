import pandas as pd
from sqlalchemy import create_engine
import os
import pymysql

password = os.getenv('sql_password')


def upload_mysql(df):
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/nstem_start_a_chapter")

    print(engine)

    df_database_before_append = pd.read_sql_table(table_name='default_chapters', con=engine, index_col=None)


    df.to_sql(name='default_chapters',con=engine, if_exists='append', index=False)  


    conn = engine.connect()
    print(conn)
        
    df_database = pd.read_sql_table(table_name='default_chapters', con=engine, index_col=None)

    if df.equals(df_database):
        print('The data is the same')

    else:
        print('Data is different')

        # Append data
        df.to_sql(name='default_chapters', con=engine, if_exists='append', index=False)

        
        df_database_appended = pd.read_sql_table(table_name='default_chapters', con=engine, index_col=None)


        df_combined = pd.concat([df, df_database_before_append])

        df_combined = df_combined.drop_duplicates()
        
        df_combined.to_sql('default_chapters', con=engine, if_exists='replace',index=False)

        print('Duplicate data dealt with')
        pd.read_sql_table(table_name='default_chapters', con=engine, index_col=False)   

        










if __name__ == "__main__" :
    upload_mysql()