"""empty message

Revision ID: 1986077ca1bd
Revises: 
Create Date: 2020-06-19 19:12:06.537151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1986077ca1bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Movies', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Movies', type_='unique')
    # ### end Alembic commands ###
