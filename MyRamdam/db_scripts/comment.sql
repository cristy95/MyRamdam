create table comment(
    comment_id serial primary key,
    userID_FK char(10) serial references user (user_id), -- to be accessed from myEskwela db
    comment_msg text,
    mode boolean
);