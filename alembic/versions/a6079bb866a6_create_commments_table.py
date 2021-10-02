"""create Commments table

Revision ID: a6079bb866a6
Revises: 6c4df94f7657
Create Date: 2021-10-02 09:05:31.063209

"""
from sqlalchemy.sql.schema import ForeignKey
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6079bb866a6'
down_revision = '6c4df94f7657'
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
