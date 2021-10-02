"""create votes table

Revision ID: bb2e3ecf97f7
Revises: b595ecae3865
Create Date: 2021-10-02 09:37:37.228672

"""
from sqlalchemy.sql.schema import ForeignKey
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb2e3ecf97f7'
down_revision = 'b595ecae3865'
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
    op.drop_table('account')
