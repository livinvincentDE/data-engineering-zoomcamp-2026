{{ config(materialized='table') }}

with trips_unioned as (

    select
        date_trunc('month', lpep_pickup_datetime) as revenue_month,
        PULocationID,
        total_amount,
        'green' as service_type
    from {{ ref('stg_green_tripdata') }}

    union all

    select
        date_trunc('month', tpep_pickup_datetime) as revenue_month,
        PULocationID,
        total_amount,
        'yellow' as service_type
    from {{ ref('stg_yellow_tripdata') }}

)

select
    revenue_month,
    PULocationID,
    service_type,
    count(*) as total_trips,
    sum(total_amount) as total_revenue,
    avg(total_amount) as avg_trip_revenue
from trips_unioned
group by
    revenue_month,
    PULocationID,
    service_type
order by
    revenue_month,
    PULocationID,
    service_type
