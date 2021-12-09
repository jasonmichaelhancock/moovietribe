"""empty message

Revision ID: e1ad6341523d
Revises: 68aa0c4f3cbf
Create Date: 2021-09-10 18:21:55.661039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1ad6341523d'
down_revision = '68aa0c4f3cbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('film2', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film3', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film4', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film5', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film6', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film7', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film8', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film9', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('film10', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'film10')
    op.drop_column('user', 'film9')
    op.drop_column('user', 'film8')
    op.drop_column('user', 'film7')
    op.drop_column('user', 'film6')
    op.drop_column('user', 'film5')
    op.drop_column('user', 'film4')
    op.drop_column('user', 'film3')
    op.drop_column('user', 'film2')
    # ### end Alembic commands ###