## Class

```plantuml
class Times {
    + void post()
    + void recall()
    + string db_path
    - void _create_table()
    list<Message> message_list
}
class Message{
    string message
    datetime dt
}

Times "1" o-- "*" Message
```

## Sequence

### post

```plantuml
actor User
participant Times
participant DB
autoactivate on
User -> Times : post() or recall()
Times -> DB : query
return
return
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
