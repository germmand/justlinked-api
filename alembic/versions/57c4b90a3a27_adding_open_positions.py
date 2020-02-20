"""adding open positions

Revision ID: 57c4b90a3a27
Revises: 2bace6eec6bd
Create Date: 2020-02-20 07:51:37.372092

"""
from datetime import datetime
from os import environ
from random import choice, randrange

import sqlalchemy as sa
from alembic import op
from faker import Faker
from faker.providers import company
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '57c4b90a3a27'
down_revision = '2bace6eec6bd'
branch_labels = None
depends_on = None

max_positions = 100


def upgrade():
    if not environ['GENERATE_DATA']:
        print('Migration skipped since it adds dummy data, for this migration to run set the GENERATE_DATA env')

    positions = []
    fake = Faker()
    fake.add_provider(company)

    positions_table = table(
        'positions',
        column('id', sa.Integer()),
        column('created_at', sa.DateTime()),
        column('updated_at', sa.DateTime()),
        column('name', sa.String()),
        column('required_experience_years', sa.Integer()),
        column('needs_travel', sa.Boolean()),
        column('needs_relocation', sa.Boolean()),
        column('modality_id', sa.Integer())
    )

    for i in range(max_positions):
        positions.append({
            'id': i,
            'name': fake.catch_phrase(),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'required_experience_years': randrange(50),
            'needs_travel': choice([True, False]),
            'needs_relocation': choice([True, False]),
            'modality_id': choice([0, 1, 2])
        })
    op.bulk_insert(positions_table, positions)


def downgrade():
    positions = table('positions', sa.column('id', sa.Integer()))

    for i in range(max_positions):
        op.execute(
            positions.delete().where(positions.c.id == op.inline_literal(i))
        )
