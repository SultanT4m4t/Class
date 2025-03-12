-- create table books (
-- id serial primary key,
-- author text not null,
-- title text not null
-- year_published int
-- )

-- insert into books(id, title, author, year_published)
-- values (7, 'Heart', 'Andrew', 1996)
-- ('Love','Tetteh', 1969),
-- ('Feel', 'Kwame', 2000),
-- ('Loyalty', 'Lamar', 2024),
-- ('Duckworth', 'Kendrick', 2019)

-- select * from books


-- select * from books
-- where author = 'Reddington'

-- update books
-- set year_published = 2001
-- where year_published = 2000

-- delete from books
-- where author = 'Grace'

-- create table borrowers(
-- id serial,
-- name text not null,
-- books_id int references books(id)
-- )