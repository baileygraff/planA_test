--create important views for BI/data vis

--top 3 by total revenue
DROP VIEW IF EXISTS top_3_revenue;
CREATE VIEW top_3_revenue AS
SELECT
    game,
    SUM(revenue) AS total_revenue
FROM   game_data_clean
GROUP  BY game
ORDER  BY total_revenue DESC, game ASC
LIMIT  3;

--general averages by game
DROP VIEW IF EXISTS game_data_average;
CREATE VIEW game_data_average AS
SELECT
    game,
    ROUND(AVG(revenue) , 2) AS average_revenue,
    ROUND(AVG(downloads) , 2) AS average_downloads,
    ROUND(AVG(average_session_duration) , 2) AS average_session_duration,
    ROUND(AVG(sessions_per_day) , 2) AS average_sessions_per_day
FROM game_data_clean
GROUP BY game
ORDER BY game ASC;

/*
--views to consider:

*/
