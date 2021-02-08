from influxdb_client import InfluxDBClient
import os

influx_client = InfluxDBClient(
    url=os.environ["HEAUME_INFLUXDB_URL"],
    token=os.environ["HEAUME_INFLUXDB_TOKEN"],
    org="Heaume"
)

def query(query):
    influx = influx_client.query_api()
    result = influx.query(query)
    return result