import click
from heaume_cli.utils.console import console
from heaume_cli.utils.influxdb import query
import pendulum

@click.command()
@click.option('--name', prompt='The name of the plant')
def status(name):
    """
    The status command gives the latest values from a plant
    """
    tables = query(
        f"""
        from(bucket: "Plant")
            |> range(start: -1d)
            |> filter(fn: (r) => r._measurement == "{name}")
            |> sort(columns: ["_time"], desc: true)
            |> limit(n: 1)
        """
    )

    metrics = dict()
    unit = {"moisture": "%", "luminosity": "%", "temperature": "°C"}

    if tables:
        for table in tables:
            try:
                record = table.records[0]
                date = record["_time"]
                field = record["_field"]
                value = record["_value"]
                metrics[field] = f"{value:.2f}"
            except IndexError:
                date = None
    else:
        date = None

    console.print(f"[bold green]:herb:[/bold green] Status of {name.capitalize()}")

    if date:
        max_key_size = max([len(m) for m in metrics.keys()])
        for key, value in metrics.items():
            str_key = key + " " * (max_key_size - len(key))
            console.print(f"   {str_key} > {value} {unit[key]}")
        ago = pendulum.instance(date).diff_for_humans()
    else:
        ago = "More than one day"

    console.print(f"[bold u]Last update:[/bold u] {ago}")
