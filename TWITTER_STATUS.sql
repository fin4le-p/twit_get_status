create table TWITTER_STATUS(
created_at datetime,
twit int,
follow int,
follower int,
my_favo int
)CHARSET=utf8mb4;

alter table TWITTER_STATUS add primary key (created_at);