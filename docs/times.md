# Times:Memorize Your minutes

## Installation

`git clone https://github.com/gatakaba/times.git`

## Usage

### memorize

`times {your great thinking}`

### recall past times

`times recall -n 10`

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
        Time
        Message
    }
}
```
