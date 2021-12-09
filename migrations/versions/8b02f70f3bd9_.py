"""empty message

Revision ID: 8b02f70f3bd9
Revises: e1ad6341523d
Create Date: 2021-09-14 09:21:41.789766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b02f70f3bd9'
down_revision = 'e1ad6341523d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('film1', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'film1')
    # ### end Alembic commands ###
