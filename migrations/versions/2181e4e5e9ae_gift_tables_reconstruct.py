"""gift tables reconstruct

Revision ID: 2181e4e5e9ae
Revises: 8e45e0dcb8f3
Create Date: 2019-06-18 12:56:48.420125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2181e4e5e9ae'
down_revision = '8e45e0dcb8f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gifts_books')
    op.drop_table('gifts_tasks')
    op.drop_table('gifts_types')
    op.drop_table('gifts_games')
    op.add_column('gifts', sa.Column('data', sa.String(length=256), nullable=True))
    op.add_column('gifts', sa.Column('type', sa.String(length=16), nullable=True))
    op.drop_column('gifts', 'type_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gifts', sa.Column('type_id', sa.INTEGER(), nullable=True))
    op.drop_column('gifts', 'type')
    op.drop_column('gifts', 'data')
    op.create_table('gifts_games',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('gift_id', sa.INTEGER(), nullable=True),
    sa.Column('codes', sa.VARCHAR(length=140), nullable=True),
    sa.ForeignKeyConstraint(['gift_id'], ['gifts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gifts_types',
    sa.Column('type_id', sa.INTEGER(), nullable=False),
    sa.Column('type_name', sa.VARCHAR(length=20), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['gifts.type_id'], ),
    sa.PrimaryKeyConstraint('type_id')
    )
    op.create_table('gifts_tasks',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('gift_id', sa.INTEGER(), nullable=True),
    sa.Column('text', sa.VARCHAR(length=140), nullable=True),
    sa.ForeignKeyConstraint(['gift_id'], ['gifts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gifts_books',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('gift_id', sa.INTEGER(), nullable=True),
    sa.Column('link', sa.VARCHAR(length=140), nullable=True),
    sa.ForeignKeyConstraint(['gift_id'], ['gifts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
