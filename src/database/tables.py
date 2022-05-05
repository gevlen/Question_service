import sqlalchemy as sa

metadata = sa.MetaData()

questions = sa.Table(
    'questions',
    metadata,
    sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column('external_id', sa.BigInteger, nullable=True, unique=True),
    sa.Column('question', sa.String, nullable=False, unique=True),
    sa.Column('answer', sa.String, nullable=False),
    sa.Column('created_at_jservice', sa.DateTime, nullable=True),
    sa.Column('created_at_db', sa.DateTime, nullable=False),
    sa.Column('category_id', sa.String, nullable=True)
)
