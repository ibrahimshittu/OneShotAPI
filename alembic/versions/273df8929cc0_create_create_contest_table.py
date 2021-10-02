"""create create_contest table"

Revision ID: 273df8929cc0
Revises: 
Create Date: 2021-10-02 08:39:07.534355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '273df8929cc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'contests',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('contest_name', sa.String(500), nullable=False),
        sa.Column('contest_description', sa.String(5000), nullable=False),
        sa.Column('contest_prize', sa.String(5000), nullable=False),
        sa.Column('contest_category', sa.String(5000), nullable=False),
        sa.Column('start_date', sa.DateTime),
        sa.Column('end_date', sa.DateTime),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('created_date', sa.DateTime),
        sa.Column('published', sa.Boolean),

    )


def downgrade():
    pass
