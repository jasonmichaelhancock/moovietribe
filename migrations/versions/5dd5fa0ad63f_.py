"""empty message

Revision ID: 5dd5fa0ad63f
Revises: 40c02135bb30
Create Date: 2021-10-14 07:59:20.954193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dd5fa0ad63f'
down_revision = '40c02135bb30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('moovie', sa.String(length=140), nullable=True))
    op.add_column('post', sa.Column('rating', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'rating')
    op.drop_column('post', 'moovie')
    # ### end Alembic commands ###
