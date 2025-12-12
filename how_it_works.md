### How does SQLAlchemy work?

```mermaid
architecture-beta
    group sqlorm(disk) [SQLAlchemy ORM]
    service orm [Object Relation Mapper] in sqlorm

    group sqlcore(server) [SQLAlchemy Core]
    service st[Schema Types] in sqlcore
    service sel[SQL Expression Language] in sqlcore
    service engine[Engine] in sqlcore
    service cnp[Connection Pooling] in sqlcore
    service d[Dialect] in sqlcore

    group sqldbapi(database) [DBAPI]
    service dbapi [Database API] in sqldbapi
```
