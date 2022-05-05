"""create question table

Revision ID: 5ae22a4275c9
Revises: 
Create Date: 2022-05-04 12:40:06.683617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ae22a4275c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'questions',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('external_id', sa.BigInteger, nullable=True, unique=True),
        sa.Column('question', sa.String, nullable=False, unique=True),
        sa.Column('answer', sa.String, nullable=False),
        sa.Column('created_at_jservice', sa.DateTime, nullable=True),
        sa.Column('created_at_db', sa.DateTime, nullable=False),
        sa.Column('category_id', sa.String, nullable=True)
    )




def downgrade():
    op.drop_table('questions')

