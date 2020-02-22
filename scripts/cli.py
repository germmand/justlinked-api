import click

from .alembic_helper import *


@click.group()
def cli():
    """Just linked API CLI"""
    pass


@cli.command()
@click.option('--port', default=8000, help='Puerto para correr la app', type=click.IntRange(0, 52000),
              show_default=True)
@click.option('--host', default='localhost', help='Host para correr la app', type=click.STRING)
@click.option('--with-migrations', default=False, show_default=True, is_flag=True,
              help='Ejecuta la última migración de la db')
@click.option('--with-fake-data', default=False, show_default=True, is_flag=True, help='Generar data de prueba')
def run(port, host, with_migrations, with_fake_data):
    """Ejecuta el servicor de desarrollo"""
    if with_migrations:
        upgrade_latest(with_fake_data)
    from .server_runner import run_app
    from src import app
    return run_app(app, port, host)


@cli.command()
@click.option('--generate-data', default=False, help='Generar data de prueba', show_default=True)
@click.option('--latest', default=True, help='Migración más reciente', show_default=True, type=click.BOOL)
@click.option('--revision', help='Id de la migración', type=click.STRING)
def upgrade(generate_data, latest, revision):
    """Ejecuta migraciones de la base de datos"""
    if latest:
        return upgrade_latest(generate_data)
    elif revision is not None and not latest:
        return upgrade_to_revision(revision, generate_data)
    click.secho('Error, no se ha especificado el parámetro --latest y no se ha especificado una revisión.', fg='red')


@cli.command()
@click.option('--one', default=True, help='Regresar una versión', show_default=True, type=click.BOOL)
@click.option('--revision', help='Id de la migración', type=click.STRING)
def downgrade(one, revision):
    """Deshace migraciones de la base de datos"""
    if one:
        return downgrade_one()
    elif revision is not None and not one:
        return downgrade_to_revision(revision)
    click.secho('Error, no se ha especificado el parámetro --one y no se ha especificado una revisión.', fg='red')
