"""empty message

Revision ID: a363641b57d9
Revises: 6e896f44564a
Create Date: 2020-06-30 16:21:04.151169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a363641b57d9'
down_revision = '6e896f44564a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('realname', sa.String(length=24), nullable=True),
    sa.Column('gender', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_info')
    # ### end Alembic commands ###