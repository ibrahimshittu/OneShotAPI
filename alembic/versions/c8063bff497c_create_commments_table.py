"""create commments table

Revision ID: c8063bff497c
Revises: a6079bb866a6
Create Date: 2021-10-02 09:18:24.023553

"""

from sqlalchemy.sql.schema import ForeignKey
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8063bff497c'
down_revision = 'a6079bb866a6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('body', sa.String(5000), nullable=False),
        sa.Column('is_parent', sa.Integer, default=None),
        sa.Column('user_id', sa.Integer, ForeignKey("users.id")),
        sa.Column('contest_id', sa.Integer, ForeignKey("contests.id")),
        sa.Column('created_date', sa.DateTime),
        sa.Column('is_active', sa.Boolean, default=True),

    )


def downgrade():
    op.drop_table('Comments')
