"""empty message

Revision ID: 2994aa96da90
Revises: 
Create Date: 2024-08-28 02:20:10.288789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2994aa96da90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
