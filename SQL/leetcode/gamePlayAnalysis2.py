# https://leetcode.com/problems/game-play-analysis-ii/

# Write your MySQL query statement below
SELECT
    player_id
    , device_id
FROM Activity
WHERE 
    (player_id, event_date) IN ( 
        SELECT player_id, min(event_date) 
        FROM ACTIVITY
        GROUP BY player_id
    )

