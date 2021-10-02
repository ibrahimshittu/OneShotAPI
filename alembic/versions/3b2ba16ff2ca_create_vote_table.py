"""create vote table

Revision ID: 3b2ba16ff2ca
Revises: bb2e3ecf97f7
Create Date: 2021-10-02 09:41:51.845973

"""
from sqlalchemy.sql.schema import ForeignKey
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b2ba16ff2ca'
down_revision = 'bb2e3ecf97f7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'votes',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('created_date', sa.DateTime),
        sa.Column('user_id', sa.Integer, ForeignKey("users.id")),
        sa.Column('contest_id', sa.Integer, ForeignKey("submission.id")),
    )


def downgrade():
    pass
