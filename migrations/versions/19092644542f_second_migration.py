"""second migration.

Revision ID: 19092644542f
Revises: b5134f0d732a
Create Date: 2022-08-24 17:20:50.264216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19092644542f'
down_revision = 'b5134f0d732a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=120), nullable=False))
        # batch_op.create_unique_constraint(None, ['password'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        # batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('password')

    # ### end Alembic commands ###
