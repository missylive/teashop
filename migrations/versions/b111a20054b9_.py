"""empty message

Revision ID: b111a20054b9
Revises: a2af8e556bac
Create Date: 2019-07-27 20:59:11.743997

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b111a20054b9'
down_revision = 'a2af8e556bac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('add_on_item', 'price',
               existing_type=mysql.DOUBLE(precision=3, scale=2, asdecimal=True),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('add_on_item', 'price',
               existing_type=mysql.DOUBLE(precision=3, scale=2, asdecimal=True),
               nullable=False)
    # ### end Alembic commands ###
