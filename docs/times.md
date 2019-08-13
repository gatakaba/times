## Class

```plantuml
class Times {
    void save()
    void recall()
    string db_path
}
```

## Save

```plantuml
actor User
participant Times
participant DB

User -> Times : Save() or Recall()
Times -> DB : Save() or Recall()
DB --> Times
Times --> User
```

## Schema

```plantuml
package DB as ext <<Database>> {
    entity "Times" {
        + ID [Primary Key]
        --
        time
        message
    }
}
```
