CREATE TABLE hero
(
    id         integer primary key autoincrement,
    name       text    not null,
    power      text    not null,
    age        integer not null,
    created_at datetime default current_timestamp,
    updated_at datetime default current_timestamp
);