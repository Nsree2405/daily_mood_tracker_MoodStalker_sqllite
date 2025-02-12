alter table users add constraint primary key (uid);

desc users;

-- alter table users add constraint email check(email in '@gamil.com' );
alter table users modify email varchar(30) not null;
alter table users modify gender varchar(1) not null;
alter table users modify dob 

alter table moods add constraint primary key (mid);

desc moods;

alter table moods add constraint booster check(booster between -10 and 10);
insert into moods values(5555,'Happy','positive',70,'Talk to your loved ones,share your happiness.');

alter table feels add constraint foreign key (uid) references users(uid);

desc feels;

alter table feels add constraint foreign key (mid) references moods(mid);

desc feels;
alter table feels add constraint scale check(scale between 1 and 5);
insert into feels values(48,1624,'2022-05-05',9,'evasion of my personal space');

alter table feels modify day date not null;

--displays all tables
desc users;
desc moods;
desc feels;