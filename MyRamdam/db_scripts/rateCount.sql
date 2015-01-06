create table rateCount(
    itemID_FK char(10) serial references item (item_id), -- to be accessed from myEskwela db
    r_happy int,
    r_sad int,
    r_angry int,
    r_surprised int
);