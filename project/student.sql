use student;
create table student(std_id int primary key , std_f_name varchar(50) not null,std_s_name varchar(50) not null , std_cgpa int not null);

INSERT INTO `student` (`std_id`, `std_f_name`, `std_s_name`, `std_cgpa`) VALUES
(22010317, 'ahmed', 'fekry', 4),
(22010047, 'osama', 'mohamed', 4),
(22011010, 'mazen', 'shaban', 4),
(22011044, 'mazen', 'yacoup', 4),
(22011558, 'shehab', 'magdy', 4);

SELECT * FROM student;