"""add description to products

Revision ID: 2a64b871f6fa
Revises: 4b42aaea9e46
Create Date: 2022-01-20 11:49:41.654367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a64b871f6fa'
down_revision = '4b42aaea9e46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'description')
    # ### end Alembic commands ###