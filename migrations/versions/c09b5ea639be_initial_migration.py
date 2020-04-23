"""Initial migration.

Revision ID: c09b5ea639be
Revises: 
Create Date: 2020-04-23 09:35:03.650292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c09b5ea639be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mahasiswa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nim', sa.String(length=10), nullable=True),
    sa.Column('nama', sa.String(length=100), nullable=True),
    sa.Column('alamat', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nim')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mahasiswa')
    # ### end Alembic commands ###