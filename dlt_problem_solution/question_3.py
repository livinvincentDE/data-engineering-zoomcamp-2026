import duckdb

con = duckdb.connect("taxi_pipeline.duckdb")

print(con.execute("""
    SELECT ROUND(SUM(tip_amt), 2)
    FROM taxi_data.taxi_trips
""").fetchall())