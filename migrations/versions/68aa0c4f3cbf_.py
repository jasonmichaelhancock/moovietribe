"""empty message

Revision ID: 68aa0c4f3cbf
Revises: f7ac3d27bb1d
Create Date: 2021-09-09 11:49:05.968582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68aa0c4f3cbf'
down_revision = 'f7ac3d27bb1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_username', table_name='user')
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    # ### end Alembic commands ###
