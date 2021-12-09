"""empty message

Revision ID: 5a0015fd591e
Revises: e4ef635a131b
Create Date: 2021-09-24 13:38:57.872248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a0015fd591e'
down_revision = 'e4ef635a131b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('film81', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film82', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film83', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film84', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film85', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film86', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film87', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film88', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film89', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film90', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'film90')
    op.drop_column('user', 'film89')
    op.drop_column('user', 'film88')
    op.drop_column('user', 'film87')
    op.drop_column('user', 'film86')
    op.drop_column('user', 'film85')
    op.drop_column('user', 'film84')
    op.drop_column('user', 'film83')
    op.drop_column('user', 'film82')
    op.drop_column('user', 'film81')
    # ### end Alembic commands ###