import click


@click.group()
def cli():
    click.echo('Ayudante de linea de comandos')


@cli.command()
@click.option('--port', default=8000, help='Puerto para correr la app', type=click.IntRange(0, 52000), show_default=True)
@click.option('--host', default='localhost', help='Host para correr la app', type=click.STRING)
def run(port, host):
    from .server_runner import run_app
    from src import app
    return run_app(app, port, host)
