"""create submission table

Revision ID: 1cfbf24a6f92
Revises: c8063bff497c
Create Date: 2021-10-02 09:21:24.379179

"""
from sqlalchemy.sql.schema import ForeignKey
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cfbf24a6f92'
down_revision = 'c8063bff497c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'submission',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('created_date', sa.DateTime),
        sa.Column('file', sa.String(500)),
        sa.Column('text', sa.String(50000)),
        sa.Column('user_id', sa.Integer, ForeignKey("users.id")),
        sa.Column('contest_id', sa.Integer, ForeignKey("contests.id")),
    )


def downgrade():
    pass
