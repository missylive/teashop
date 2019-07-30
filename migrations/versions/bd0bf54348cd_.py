"""empty message

Revision ID: bd0bf54348cd
Revises: dc1f4accfff7
Create Date: 2019-07-29 21:46:59.624775

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bd0bf54348cd'
down_revision = 'dc1f4accfff7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('order_item_ibfk_2', 'order_item', type_='foreignkey')
    op.drop_column('order_item', 'menu_item_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_item', sa.Column('menu_item_number', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False))
    op.create_foreign_key('order_item_ibfk_2', 'order_item', 'menu_item', ['menu_item_number'], ['menu_item_number'])
    # ### end Alembic commands ###
