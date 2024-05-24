import databases
import sqlalchemy

metadata = sqlalchemy.MetaData()

post_table = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("body",sqlalchemy.String)
)

comment_table = sqlalchemy.Table(
    "comments",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("post_id",sqlalchemy.ForeignKey("posts.id"),nullable=False),
    sqlalchemy.Column("body",sqlalchemy.String)
)


engine = sqlalchemy.create_engine(
    "sqlite:///storeapi.db",connect_args = {"check_same_thread": False}
)
metadata.create_all(engine)
database = databases.Database(
    "sqlite:///storeapi.db",force_rollback=False
)