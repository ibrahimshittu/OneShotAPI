"""create wishlist table

Revision ID: b2149cf82f4d
Revises: 3b2ba16ff2ca
Create Date: 2021-10-04 10:17:32.107198

"""

from sqlalchemy.sql.schema import ForeignKey
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2149cf82f4d'
down_revision = '3b2ba16ff2ca'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'wishlist',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('date_added', sa.DateTime),
        sa.Column('user_id', sa.Integer, ForeignKey("users.id")),
        sa.Column('contest_id', sa.Integer, ForeignKey("submission.id")),
    )





def downgrade():
    op.drop_table('wishlist')
