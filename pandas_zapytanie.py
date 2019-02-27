import pandas as pd
with open (r'/home/kinga/stosowanie_git/zapytania__sql_git.sql') as f:
   zapytanie=f.read()

import sqlite3
conn=sqlite3.connect("/home/kinga/sqlite/oreilly_getting_started_with_sql-master/rexon_metals.db")
df=pd.read_sql_query(zapytanie, conn)
df.to_excel('/home/kinga/stosowanie_git/wynik_excel.xlsx',sheet_name='raport',index=False)
df