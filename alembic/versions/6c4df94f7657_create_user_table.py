"""create User table

Revision ID: 6c4df94f7657
Revises: 273df8929cc0
Create Date: 2021-10-02 08:55:04.321876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c4df94f7657'
down_revision = '273df8929cc0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('name', sa.String(500), nullable=False),
        sa.Column('email', sa.String(5000), nullable=False),
        sa.Column('password', sa.String(5000), nullable=False),
        sa.Column('created_date', sa.DateTime),
        sa.Column('is_active', sa.Boolean),
        sa.Column('is_superuser', sa.Boolean),

    )


def downgrade():
    pass
