"""empty message

Revision ID: c2f4c75ed440
Revises: 
Create Date: 2020-10-06 22:58:29.307180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2f4c75ed440'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sceance_image')
    op.drop_table('image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('url', sa.VARCHAR(length=200), nullable=False),
    sa.Column('ima_sceance', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['ima_sceance'], ['sceance.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sceance_image',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('url', sa.VARCHAR(length=200), nullable=False),
    sa.Column('ima_sceance', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['ima_sceance'], ['sceance.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
