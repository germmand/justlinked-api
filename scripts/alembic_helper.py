from collections import Callable
from os import path, getcwd, environ

from alembic import command
from alembic.config import Config


def seek_alembic_ini():
    while True:
        current_path = getcwd()

        if path.isfile('alembic.ini'):
            return path.join(current_path, 'alembic.ini')
        elif not path.isfile('main.py'):
            current_path = path.join(current_path, '..')
        else:
            raise RuntimeError('alembic.ini not found')


cfg = Config(seek_alembic_ini())


def upgrade_latest(generate_data=False):
    fun = lambda: command.upgrade(cfg, 'head')
    if generate_data:
        return run_with_dummy_data(fun)
    return fun()


def downgrade_one():
    return command.downgrade(cfg, '-1')


def upgrade_to_revision(revision: str, generate_data=False):
    fun = lambda: command.upgrade(cfg, revision)

    if generate_data:
        return run_with_dummy_data(fun)
    return fun()


def downgrade_to_revision(revision: str):
    return command.downgrade(cfg, revision)


def generate_migration(revision=None, autogenerate=True):
    command.revision(revision, autogenerate)


def run_with_dummy_data(fun: Callable):
    environ.setdefault('GENERATE_DATA', True)
    fun()
    del environ['GENERATE_DATA']
