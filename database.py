import pandas as pd
import sqlalchemy as sql

bets_dataframe = pd.read_csv('bets.csv')
events_dataframe = pd.read_csv('events.csv')
engine = sql.create_engine('sqlite:///betera.db', echo=False)
events_dataframe.to_sql('events', engine)
bets_dataframe.to_sql('bets', engine)
