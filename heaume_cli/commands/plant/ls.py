import click
from heaume_cli.utils.influxdb import query

@click.command()
def ls():
    """
    The status command gives the all plants of the system
    """
    tables = query(
        f"""
        from(bucket: "Plant")
            |> range(start: -1d)
            |> distinct(column: "_measurement")
            |> keep(columns: ["_measurement"])
        """
    )

    for table in tables:
        for record in table.records:
            print(record["_measurement"])
