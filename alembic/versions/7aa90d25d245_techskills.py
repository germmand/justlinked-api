"""techskills

Revision ID: 7aa90d25d245
Revises: 5b22512ba79b
Create Date: 2020-02-19 22:22:10.941431

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '7aa90d25d245'
down_revision = '5b22512ba79b'
branch_labels = None
depends_on = None


def upgrade():
    techskills = op.create_table(
        'techskills',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.PrimaryKeyConstraint('id')
    )

    skills_names = ['Python', 'React', 'Vue', 'Angular', 'Javascript', 'Svelte', 'C#', 'Go', 'PHP', 'Ruby', 'Java']

    op.bulk_insert(
        techskills,
        [
            {'id': i, 'created_at': datetime.now().isoformat(), 'updated_at': datetime.now().isoformat(), 'name': name}
            for i, name in enumerate(skills_names)
        ])

    op.create_table(
        'applicants_tech_skills',
        sa.Column('applicant_id', sa.Integer(), nullable=True),
        sa.Column('techskill_id', sa.Integer(), nullable=True),
        sa.Column('experience_years', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['applicant_id'], ['applicants.id'], ),
        sa.ForeignKeyConstraint(['techskill_id'], ['techskills.id'], )
    )
    op.create_table(
        'position_tech_skills',
        sa.Column('position_id', sa.Integer(), nullable=True),
        sa.Column('techskill_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['position_id'], ['positions.id'], ),
        sa.ForeignKeyConstraint(['techskill_id'], ['techskills.id'], )
    )


def downgrade():
    op.drop_table('applicants_tech_skills')
    op.drop_table('position_tech_skills')
    op.drop_table('techskills')
