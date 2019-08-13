# SW Specification

## Class

```plantuml
class Times {
    void save()
    void recall()
    string db_path
}
```

## Sequence

```plantuml
actor User
participant Times
participant DB

User -> Times : Save() or Recall()
Times -> DB : query
DB --> Times
Times --> User
```

## Database

### Schema

```plantuml
package DB as ext <<Database>> {
    entity "times" {
        +id [Primary Key]
        --
        time
        message
    }
}
```

### Query

#### create table

`create table times(time,message)`

#### add record

`insert into times (time,message) values(?,?)`

#### selectrecord

`select time,message from times;`
