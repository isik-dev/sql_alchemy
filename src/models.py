from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()


workers_table = Table(
    "workers",
    metadata_obj,
    Column(name="id", type_=Integer, primary_key=True),
    Column(name="username", type_=String),
)
