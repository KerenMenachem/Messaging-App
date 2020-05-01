"""messages table

Revision ID: 0015bdc1c87a
Revises: 327e2e0d5111
Create Date: 2020-04-28 16:38:39.599076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0015bdc1c87a'
down_revision = '327e2e0d5111'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.String(length=50), nullable=True),
    sa.Column('participants', sa.PickleType(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.applicatio_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    # ### end Alembic commands ###
