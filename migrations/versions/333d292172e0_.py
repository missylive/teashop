"""empty message

Revision ID: 333d292172e0
Revises: 4bb68bfb6dfe
Create Date: 2019-07-26 20:40:52.371574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '333d292172e0'
down_revision = '4bb68bfb6dfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'password_hash')
    # ### end Alembic commands ###
