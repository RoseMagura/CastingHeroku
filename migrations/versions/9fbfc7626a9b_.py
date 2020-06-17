"""empty message

Revision ID: 9fbfc7626a9b
Revises: 
Create Date: 2020-06-06 17:38:59.952271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fbfc7626a9b'
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