create table userFeel(
    ufeel_id serial primary key,
    feelID_FK serial references feelings (feel_id),
    userID_FK char(10) serial references user (user_id), -- to be accessed from myEskwela db
    cfeelID_FK serial references customFeel (cfeel_id),
    itemID_FK char(10) serial references item (item_id), -- to be accessed from myEskwela db
    ufeel_date text,
);