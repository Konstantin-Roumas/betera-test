SELECT *
FROM bets
INNER JOIN events
USING(event_id)
WHERE is_free_bet == 0
 AND event_stage == 'Prematch'
 AND sport == 'E-Sports'
 AND settlement_time <= '2022-03-15 12:00:00.000'
 AND create_time >= '2022-03-14 12:00:00.000'
 AND bet_type != 'System'
 AND item_result IN('Win','Lose')
 AND accepted_bet_odd >= 1.5
 AND  bet_size >= 10;