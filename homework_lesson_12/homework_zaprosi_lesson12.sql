


select * from vocabulary;   - подивитися бiльш детально вміст таблиці
truncate table vocabulary;  - ochishaet tablicu(zna4enija)
truncate table vocabulary restart identity;   - ochishaet tablicu(zna4enija) i id 
insert into word (word, vocabulary_id) values ('python', 1); - dodaty v table word  zna4ennia python
select * from word; 
insert into word (word, vocabulary_id) values ('c#', 1), ('ruby', 1), ('java', 1);
select * from word; 
insert into word (word, vocabulary_id) values ('c', 2), ('pascal', 2), ('java scrypt', 2);
select * from word; 
update word set vocabulary_id = 3 where id = 5; - zmina vocabulary_id
update word set vocabulary_id = 2 where id = 5; - povernennia vocabulary_id
select * from word; 
insert into word (word, vocabulary_id) select word, 3 from word where vocabulary_id = 2; - обираємо значення з vocabulary_id 2 - та переносимо 
			до vocabulary_id 3, id присвоюються унікальні, не повторюються
select word from word;  - pokazue zapisi bez tablic`
select distinct word from word;  - pokazue zapisi bez tablic` i bez dubliv, distinct не видаляє дублюючи записи з таблички, він показує тільки унікальні
select * from word where id > 6;
select * from word where id between 1 and 6;
select * from word where word like '%al';
select * from word where word like '%al' and id > 7;
select vocabulary_id from word group by vocabulary_id; - згрупувало 3 групки
select word from word group by word; - складає стопачками
select word, count(*) from word group by word; 
select word, count(*) from word where id > 2 group by word;
select word, count(*) from word where id > 2 group by word having count(*) > 1; 
select word, count(*) from word group by word order by word; - розставив по алфавіту, без регістру
select word, count(*) from word group by word order by lower(word);  -  розставив по алфавіту, з регістром
select word, count(*) from word group by word order by lower(word) asc; - теж саме
select word, count(*) from word group by word order by lower(word) desc; - зворотній напрямок(алфавіту)
select word, count(*) from word group by word order by 2; - сортує по зростанню по count
select word, count(*) from word group by word order by 2 desc, 1 asc; - по групам по кількості елементів, і в них по алфавіту
 select word, count(*) from word group by word order by 2 desc, 1 asc limit 2;  - перші 2
 select word, count(*) from word group by word order by 2 desc, 1 asc limit 2 offset 2; - другі 2 після перших 2))
update word set word = 'c, c++' where id = 10; - обновили данні в id10
delete from word where vocabulary_id = 2; - видалили всі елементи з vocabulary_id = 2 :(

 select title, genre from books inner join genres on books.genre_id = genres.id;
 select title, genre from books left join genres on books.genre_id = genres.id;  бере все з лівої таблички та додає те що є в перерізі з правої таблички
 select title from books left join genres on books.genre_id = genres.id where genre is null;
 select title, genre from books full join genres on books.genre_id = genres.id;

select title, genre from books b left join genres g on b.genre_id = g.id; - спрощення
alter table genres rename column id to genre_id; - перейменуваня колонки
select title, genre from books right join genres using (genre_id);
select genre from books right join genres using (genre_id) where title is null; 