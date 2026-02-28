import duckdb

con = duckdb.connect("taxi_pipeline.duckdb")

print(con.execute("""
    SELECT ROUND(
        SUM(CASE WHEN payment_type = 'Credit' THEN 1 ELSE 0 END) 
        * 100.0 / COUNT(*),
    2)
    FROM taxi_data.taxi_trips
""").fetchall())