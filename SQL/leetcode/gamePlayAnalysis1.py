# https://leetcode.com/problems/game-play-analysis-i/submissions/

# Write your MySQL query statement below
SELECT
    player_id
    , min(event_date) as first_login
FROM Activity
GROUP BY 1;