"""empty message

Revision ID: 4d6ef7aeb2d8
Revises: 5407f77a0084
Create Date: 2020-02-04 01:27:23.193412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d6ef7aeb2d8'
down_revision = '5407f77a0084'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('common_name', 'label_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('common_name', 'language_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('common_name', 'language_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('common_name', 'label_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###