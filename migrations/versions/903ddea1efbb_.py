"""empty message

Revision ID: 903ddea1efbb
Revises: 1b45ad923d11
Create Date: 2021-09-23 18:27:33.516330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '903ddea1efbb'
down_revision = '1b45ad923d11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('film61', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film62', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film63', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film64', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film65', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film66', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film67', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film68', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film69', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film70', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'film70')
    op.drop_column('user', 'film69')
    op.drop_column('user', 'film68')
    op.drop_column('user', 'film67')
    op.drop_column('user', 'film66')
    op.drop_column('user', 'film65')
    op.drop_column('user', 'film64')
    op.drop_column('user', 'film63')
    op.drop_column('user', 'film62')
    op.drop_column('user', 'film61')
    # ### end Alembic commands ###
