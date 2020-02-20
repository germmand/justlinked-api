"""work_modalities

Revision ID: 5b22512ba79b
Revises: ad9dc5e915a1
Create Date: 2020-02-19 22:06:36.720658

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5b22512ba79b'
down_revision = 'ad9dc5e915a1'
branch_labels = None
depends_on = None


def upgrade():
    modality_table = op.create_table(
        'modality',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.PrimaryKeyConstraint('id')
    )

    modalities_name = ['Remoto', 'Presencial', 'Presencial con posibilidad de remoto']

    op.bulk_insert(
        modality_table,
        [
            {'id': i, 'created_at': datetime.now().isoformat(), 'updated_at': datetime.now().isoformat(), 'name': name}
            for i, name in enumerate(modalities_name)
        ]
    )

    with op.batch_alter_table('positions') as positions_table:
        positions_table.add_column(
            sa.Column('modality_id', sa.Integer(), nullable=True)
        )
    with op.batch_alter_table('applicants') as applicants_table:
        applicants_table.add_column(
            sa.Column('modality_id', sa.Integer(), nullable=True)
        )
    op.create_foreign_key(
        'modality_id', 'applicants', 'modality', ['modality_id'], ['id']
    )
    op.create_foreign_key(
        'modality_id', 'positions', 'modality', ['modality_id'], ['id']
    )


def downgrade():
    op.drop_column('positions', 'modality_id')
    op.drop_column('applicants', 'modality_id')
    op.drop_table('modality')
