"""third migration.

Revision ID: 370133ed618d
Revises: 19092644542f
Create Date: 2022-08-24 17:24:30.394480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '370133ed618d'
down_revision = '19092644542f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('middle_name', sa.String(length=80), nullable=True))
        # batch_op.create_unique_constraint(None, ['password'])
        # batch_op.create_unique_constraint(None, ['middle_name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        # batch_op.drop_constraint(None, type_='unique')
        # batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('middle_name')

    # ### end Alembic commands ###
