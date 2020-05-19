"""empty message

Revision ID: 87f97bb9cfa7
Revises: 
Create Date: 2020-05-17 15:50:46.977498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87f97bb9cfa7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_form',
    sa.Column('contactId', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=45), nullable=True),
    sa.Column('lastName', sa.String(length=45), nullable=True),
    sa.Column('email', sa.String(length=45), nullable=True),
    sa.Column('organization', sa.String(length=45), nullable=True),
    sa.Column('phoneNumber', sa.String(length=45), nullable=True),
    sa.Column('message', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('contactId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact_form')
    # ### end Alembic commands ###