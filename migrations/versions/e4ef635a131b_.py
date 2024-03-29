"""empty message

Revision ID: e4ef635a131b
Revises: 903ddea1efbb
Create Date: 2021-09-24 12:44:05.204018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4ef635a131b'
down_revision = '903ddea1efbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('film71', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film72', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film73', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film74', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film75', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film76', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film77', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film78', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film79', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film80', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'film80')
    op.drop_column('user', 'film79')
    op.drop_column('user', 'film78')
    op.drop_column('user', 'film77')
    op.drop_column('user', 'film76')
    op.drop_column('user', 'film75')
    op.drop_column('user', 'film74')
    op.drop_column('user', 'film73')
    op.drop_column('user', 'film72')
    op.drop_column('user', 'film71')
    # ### end Alembic commands ###
