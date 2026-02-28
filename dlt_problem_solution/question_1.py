import duckdb

con = duckdb.connect("taxi_pipeline.duckdb")

print("\nStart & End Date:")
print(con.execute("""
    SELECT MIN(trip_pickup_date_time),
           MAX(trip_pickup_date_time)
    FROM taxi_data.taxi_trips
""").fetchall())

print("\nCredit Card Percentage:")
print(con.execute("""
    SELECT ROUND(
        SUM(CASE WHEN payment_type = 'Credit card' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
    2)
    FROM taxi_data.taxi_trips
""").fetchall())

print("\nTotal Tips:")
print(con.execute("""
    SELECT ROUND(SUM(tip_amt), 2)
    FROM taxi_data.taxi_trips
""").fetchall())