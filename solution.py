import pandas as pd

bets_dataframe = pd.read_csv('bets.csv')
events_dataframe = pd.read_csv('events.csv')
interim_dataframe = bets_dataframe.merge(events_dataframe, on='event_id')
types = {'accept_time': 'datetime64[ns]',
         'create_time': 'datetime64[ns]',
         'settlement_time': 'datetime64[ns]'}
interim_dataframe = interim_dataframe.astype(types)
result_dataframe = interim_dataframe[(interim_dataframe['event_stage'] == 'Prematch') &
                                     (interim_dataframe['sport'] == 'E-Sports') &
                                     (interim_dataframe['bet_type'] != 'System') &
                                     (interim_dataframe['create_time'] >= '12:00 14.03.2022') &
                                     (interim_dataframe['settlement_time'] <= '12:00 15.03.2022') &
                                     (interim_dataframe['item_result'].isin(['Win', 'Lose'])) &
                                     (interim_dataframe['accepted_bet_odd'] >= 1.5) &
                                     (interim_dataframe['bet_size'] >= 10) &
                                     (interim_dataframe['is_free_bet'] == 0)]
print(result_dataframe)
