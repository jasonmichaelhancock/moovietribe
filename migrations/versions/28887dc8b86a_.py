"""empty message

Revision ID: 28887dc8b86a
Revises: 8b02f70f3bd9
Create Date: 2021-09-14 17:53:40.598697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28887dc8b86a'
down_revision = '8b02f70f3bd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('film11', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film12', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film13', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film14', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film15', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film16', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film17', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film18', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film19', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film20', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'film20')
    op.drop_column('user', 'film19')
    op.drop_column('user', 'film18')
    op.drop_column('user', 'film17')
    op.drop_column('user', 'film16')
    op.drop_column('user', 'film15')
    op.drop_column('user', 'film14')
    op.drop_column('user', 'film13')
    op.drop_column('user', 'film12')
    op.drop_column('user', 'film11')
    # ### end Alembic commands ###
