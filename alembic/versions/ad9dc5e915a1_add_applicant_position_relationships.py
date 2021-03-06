"""Add applicant position.py relationships

Revision ID: ad9dc5e915a1
Revises: 
Create Date: 2020-02-19 16:48:01.979445

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ad9dc5e915a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applicants',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('fullname', sa.String(), nullable=True),
                    sa.Column('age', sa.Integer(), nullable=True),
                    sa.Column('address', sa.String(), nullable=True),
                    sa.Column('country_of_residence', sa.String(), nullable=True),
                    sa.Column('nacionality', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('positions',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('required_experience_years', sa.Integer(), nullable=True),
                    sa.Column('needs_travel', sa.Boolean(), nullable=True),
                    sa.Column('needs_relocation', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('positions')
    op.drop_table('applicants')
    # ### end Alembic commands ###
