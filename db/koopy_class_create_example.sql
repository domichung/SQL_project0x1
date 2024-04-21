use OnlineCourseRegisterSystem;
CREATE TABLE `Teacher` (
    `teacher_id` INT PRIMARY KEY,
    `teacher_name` VARCHAR (20),
    `department_id` INT,
    `gender` VARCHAR (10),
    `mailbox` VARCHAR (100)
);

INSERT INTO `Teacher` VALUES(3746, '���w��', 1, 'male', 'dschen@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3750, '�\�h��', 1, 'male', 'hjhsu@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3761, '�L�p��', 1, 'male', 'fclin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3765, '�B�v�N', 1, 'male', 'tjliu@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3768, '�B����', 1, 'male', 'mingcliu@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3729, '���C��', 1, 'male', 'chingwen@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3736, '���K�q', 1, 'female', 'chunhyeh@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(7777, '���p��', 1, 'female', 'mememe@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3816, '���ӱj', 2, 'male', 'cchiang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3836, '�L�ܷ�', 2, 'male', 'rclin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3805, '�}�h��', 2, 'male', 'shihhhsu@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4962, '������', 3, 'male', 'pcyang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5058, '�L����', 7, 'male', 'tyson@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5070, '���K�H', 7, 'male', 'shma@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(2137, '���k�y', 8, 'male', 'cheeny@ms6.hinet.net');
INSERT INTO `Teacher` VALUES(5630, '���Ӧt', 8, 'male', 'wangcy@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5667, '�i�Ӭ�', 8, 'male', 'cschang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5670, '����[', 8, 'male', 'rktai@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5125, '���P��', 9, 'female', 'huangty@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(6213, '��_�p', 9, 'male', 'chlay@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3001, '�P�A��', 10, 'male', 'chz@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4385, '������', 13, 'male', 'yuehtli@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4387, '�B���R', 13, 'female', 'mcding@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3118, '�����', 14, 'male', 'jslai@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3121, '������', 14, 'male', 'wctseng@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4714, '���綧', 15, 'male', 'rylee@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(1029, '��E��', 4, 'male', 'fang0129.tw@yahoo.com.tw');






CREATE TABLE `Department` (
    `department_id` INT PRIMARY KEY,
    `department_name` VARCHAR (500)
);

INSERT INTO `Department` VALUES(1, '��T�u�{�Ǩt');
INSERT INTO `Department` VALUES(2, '�q���u�{�Ǩt');
INSERT INTO `Department` VALUES(3, '�q�l�u�{�Ǩt');
INSERT INTO `Department` VALUES(4, '�۰ʱ���u�{�Ǩt');
INSERT INTO `Department` VALUES(5, '��T�q���ǰ|�Ǥh�Z');
INSERT INTO `Department` VALUES(6, '�q�T�u�{�Ǩt');
INSERT INTO `Department` VALUES(7, '���q��ǻP�u�{�Ǩt');
INSERT INTO `Department` VALUES(8, '�q�Ѥ���');
INSERT INTO `Department` VALUES(9, '���μƾǾǨt');
INSERT INTO `Department` VALUES(10, '�έp�Ǩt');
INSERT INTO `Department` VALUES(11, '��ӻP�t�Τu�{�Ǩt');
INSERT INTO `Department` VALUES(12, '�~��y��Ǩt');
INSERT INTO `Department` VALUES(13, '��P�Ǩt');
INSERT INTO `Department` VALUES(14, '�g��u�{�Ǩt');
INSERT INTO `Department` VALUES(15, '�g�a�޲z�Ǩt');




CREATE TABLE `Course` (
    `course_id` VARCHAR (500) PRIMARY KEY,
    `course_name` VARCHAR (500),
    `department_id` INT,
    `required` VARCHAR (500),
    `credit` INT, 
    `description` VARCHAR (500)
);


INSERT INTO `Course` VALUES ('IECS322', '��Ʈw�t��', 1, 'yes', 3, 'Introduction of database system');
INSERT INTO `Course` VALUES ('IECS241', '���p����', 1, 'no', 3, 'Introduction of network system');
INSERT INTO `Course` VALUES ('IECS108', '�{���]�p(III)', 1, 'yes', 4, 'Introduction of programming 3');
INSERT INTO `Course` VALUES ('IECS109', '�{���]�p(IV)', 1, 'yes', 4, 'Introduction of programming 4');
INSERT INTO `Course` VALUES ('CIEE105', '�u�ʥN��', 3, 'yes', 3, 'Introduction of linear algebra');
INSERT INTO `Course` VALUES ('MATH106', '�L�n��(�G)', 9, 'yes', 3, 'Introduction of Calclus');
INSERT INTO `Course` VALUES ('CIEE111', '���q���z-�q�B�ϡB������', 3, 'yes', 3, 'Introduction of physcial');
INSERT INTO `Course` VALUES ('CIEE106', '�޿�]�p', 3, 'yes', 3, 'Introduction of logical');
INSERT INTO `Course` VALUES ('GHUC201', '����媫�Y��', 8, 'no', 2, 'Introduction of China');
INSERT INTO `Course` VALUES ('GHUC205', '�饻���v�P���', 8, 'no', 2, 'Introduction of Japan');
INSERT INTO `Course` VALUES ('GHUR302', '�x�W�����H��', 8, 'no', 2, 'Introduction of Taiwan');
INSERT INTO `Course` VALUES ('IDSS3002', '�b�s�ұƻP�Ҩ���p��', 8, 'no', 2, 'Introduction of Earth');
INSERT INTO `Course` VALUES ('COB102', '��T����', 10, 'no', 2, 'Introduction of Internet');
INSERT INTO `Course` VALUES ('PHYS105', '���q���z(�@)', 9, 'yes', 4, 'Introduction of Physical');
INSERT INTO `Course` VALUES ('PHYS202', '�q�Ͼ�(�G)', 7, 'yes', 3, 'Introduction of maganaic');
INSERT INTO `Course` VALUES ('IECS888', '�v�ɵ{��', 1, 'no', 4, 'Introduction of Programming Contest');
INSERT INTO `Course` VALUES ('IECS2003', '�t�ε{��', 1, 'yes', 3, 'Introduction of common system software in computer systems');
INSERT INTO `Course` VALUES ('IECS359', '�H�u���z�ɽ�', 1, 'no', 3, 'Introduction of AI');
INSERT INTO `Course` VALUES ('IECS303', '�p������c��', 1, 'yes', 3, 'Introduction of Design of CPU in computer systems');
INSERT INTO `Course` VALUES ('IECS471', '�{���]�p�P���D�ѨM', 1, 'no', 2, 'Introduction of Based on various problem-solving algorithms');
INSERT INTO `Course` VALUES ('EEEN2001', '�u�{�ƾ�(�G)', 2, 'yes', 3, 'Introduction of how to express scientific or engineering problems using mathematical methods');
INSERT INTO `Course` VALUES ('EEEN2012', '�L�B�z���t��', 2, 'yes', 3, 'Introduction of CPU, I/O, TIMERS/COUNTERS, and Serial Communication');
INSERT INTO `Course` VALUES ('EEEN2018', '�q�i�u�{����', 2, 'no', 2, 'Introduction of the basic and professional knowledge in the field of radio wave engineering, the latest developments in the field of radio wave engineering');
INSERT INTO `Course` VALUES ('ELEN2003', '�q�l��(�G)', 3, 'yes', 3, 'Introduction of how to express scientific or engineering problems using mathematical methods');
INSERT INTO `Course` VALUES ('ELEN2016', '�n��q���ɽ�', 3, 'no', 3, 'Introduction of the basic concepts of integrated circuits');
INSERT INTO `Course` VALUES ('MKT1030', '��P�N�H�u�{', 13, 'yes', 3, 'This course is an introductory introduction to art and design');
INSERT INTO `Course` VALUES ('MKT2051', '��P�����P�Ӯפ��R', 13, 'no', 3, 'This course explores the core concepts ofstrategic marketing, implementation, andtheir integration in practical operations.');
INSERT INTO `Course` VALUES ('CE2085', '�g�[�O��(�@)', 14, 'yes', 3, 'The content studied is an essential tool for the analysis and design of geotechnical engineering such as building foundations and retaining structures.');
INSERT INTO `Course` VALUES ('CE2080', '�a�δ��q', 14, 'no', 3, 'This course aims to enable students to understand the principles of topographic surveying, operational techniques and drawing methods, and become proficient in the operation and maintenance of surveying instruments, integrating theory with practice.');
INSERT INTO `Course` VALUES ('LAND2040', '�a�z��T�t�η���', 15, 'yes', 3, 'Introduction of the theory, application level and software operation of geographic information system (GIS) and spatial information');


CREATE TABLE `Course_Instance` (
    `course_instance_id` INT PRIMARY KEY,
    `course_id` VARCHAR (500),
    `teacher_id` INT,
    `max_people` INT,
    `now_people` INT
);


INSERT INTO `Course_Instance` VALUES (1248, 'IECS322', 3750, 75, 0);
INSERT INTO `Course_Instance` VALUES (1260, 'IECS241', 3765, 75, 0);
INSERT INTO `Course_Instance` VALUES (1222, 'IECS108', 3768, 80, 0);
INSERT INTO `Course_Instance` VALUES (1223, 'IECS109', 3768, 80, 0);
INSERT INTO `Course_Instance` VALUES (1227, 'CIEE105', 3761, 80, 0);
INSERT INTO `Course_Instance` VALUES (1224, 'CIEE111', 5070, 72, 0);
INSERT INTO `Course_Instance` VALUES (1218, 'CIEE106', 3746, 78, 0);
INSERT INTO `Course_Instance` VALUES (2767, 'GHUC201', 5670, 70, 0);
INSERT INTO `Course_Instance` VALUES (2774, 'GHUC205', 2137, 79, 0);
INSERT INTO `Course_Instance` VALUES (2779, 'GHUR302', 5667, 72, 0);
INSERT INTO `Course_Instance` VALUES (2780, 'GHUR302', 5630, 72, 0);
INSERT INTO `Course_Instance` VALUES (1226, 'MATH106', 5125, 72, 0);
INSERT INTO `Course_Instance` VALUES (3529, 'IDSS3002', 6213, 40, 0);
INSERT INTO `Course_Instance` VALUES (0497, 'COB102', 3001, 60, 0);
INSERT INTO `Course_Instance` VALUES (2233, 'PHYS105', 1029, 60, 0);
INSERT INTO `Course_Instance` VALUES (2471, 'PHYS202', 5058, 60, 0);
INSERT INTO `Course_Instance` VALUES (8888, 'IECS8888', 7777, 90, 0);
INSERT INTO `Course_Instance` VALUES (1312, 'IECS2003', 3765, 69, 0);
INSERT INTO `Course_Instance` VALUES (1348, 'IECS359', 3761, 60, 0);
INSERT INTO `Course_Instance` VALUES (1336, 'IECS303', 3729, 73, 0);
INSERT INTO `Course_Instance` VALUES (1365, 'IECS471', 3736, 60, 0);
INSERT INTO `Course_Instance` VALUES (1607, 'EEEN2001', 3836, 83, 0);
INSERT INTO `Course_Instance` VALUES (1612, 'EEEN2012', 3805, 80, 0);
INSERT INTO `Course_Instance` VALUES (1623, 'EEEN2018', 3816, 60, 0);
INSERT INTO `Course_Instance` VALUES (1486, 'ELEN2003', 4962, 70, 0);
INSERT INTO `Course_Instance` VALUES (1503, 'ELEN2016', 4962, 120, 0);
INSERT INTO `Course_Instance` VALUES (0714, 'MKT1030', 4385, 80, 0);
INSERT INTO `Course_Instance` VALUES (0737, 'MKT2051', 4387, 60, 0);
INSERT INTO `Course_Instance` VALUES (0945, 'CE2085', 3121, 62, 0);
INSERT INTO `Course_Instance` VALUES (0956, 'CE2080', 3118, 62, 0);
INSERT INTO `Course_Instance` VALUES (2320, 'LAND2040', 4714, 60, 0);




CREATE TABLE `Selected_Course` (
    `student_id` VARCHAR (500),
    `course_instance_id` INT,
    PRIMARY KEY(`student_id`, `course_instance_id`)
);

INSERT INTO `Selected_Course` VALUES ('D0901234', 1248);
INSERT INTO `Selected_Course` VALUES ('D0901234', 1223);
INSERT INTO `Selected_Course` VALUES ('D0901234', 0497);
INSERT INTO `Selected_Course` VALUES ('D0901234', 1226);
INSERT INTO `Selected_Course` VALUES ('D0901234', 3729);

CREATE TABLE `Sections` (
    `course_instance_id` INT,
    `section` INT,
    PRIMARY KEY(`course_instance_id`, `section`)
);

INSERT INTO `Sections` VALUES (1248, 104);
INSERT INTO `Sections` VALUES (1248, 406);
INSERT INTO `Sections` VALUES (1248, 407);
INSERT INTO `Sections` VALUES (1260, 106);
INSERT INTO `Sections` VALUES (1260, 107);
INSERT INTO `Sections` VALUES (1260, 108);
INSERT INTO `Sections` VALUES (1222, 308);
INSERT INTO `Sections` VALUES (1222, 309);
INSERT INTO `Sections` VALUES (1222, 401);
INSERT INTO `Sections` VALUES (1222, 402);
INSERT INTO `Sections` VALUES (1222, 403);
INSERT INTO `Sections` VALUES (1222, 404);
INSERT INTO `Sections` VALUES (1227, 107);
INSERT INTO `Sections` VALUES (1227, 408);
INSERT INTO `Sections` VALUES (1227, 409);
INSERT INTO `Sections` VALUES (1224, 302);
INSERT INTO `Sections` VALUES (1224, 303);
INSERT INTO `Sections` VALUES (1224, 304);
INSERT INTO `Sections` VALUES (1218, 106);
INSERT INTO `Sections` VALUES (1218, 107);
INSERT INTO `Sections` VALUES (1218, 401);
INSERT INTO `Sections` VALUES (2767, 201);
INSERT INTO `Sections` VALUES (2767, 202);
INSERT INTO `Sections` VALUES (2774, 101);
INSERT INTO `Sections` VALUES (2774, 102);
INSERT INTO `Sections` VALUES (2779, 406);
INSERT INTO `Sections` VALUES (2779, 407);
INSERT INTO `Sections` VALUES (2780, 308);
INSERT INTO `Sections` VALUES (2780, 309);
INSERT INTO `Sections` VALUES (1226, 103);
INSERT INTO `Sections` VALUES (1226, 104);
INSERT INTO `Sections` VALUES (1226, 301);
INSERT INTO `Sections` VALUES (3529, 106);
INSERT INTO `Sections` VALUES (3529, 107);
INSERT INTO `Sections` VALUES (0497, 101);
INSERT INTO `Sections` VALUES (0497, 102);
INSERT INTO `Sections` VALUES (2233, 203);
INSERT INTO `Sections` VALUES (2233, 204);
INSERT INTO `Sections` VALUES (2233, 501);
INSERT INTO `Sections` VALUES (2233, 502);
INSERT INTO `Sections` VALUES (2471, 207);
INSERT INTO `Sections` VALUES (2471, 503);
INSERT INTO `Sections` VALUES (2471, 504);
INSERT INTO `Sections` VALUES (8888, 506);
INSERT INTO `Sections` VALUES (8888, 507);
INSERT INTO `Sections` VALUES (8888, 508);
INSERT INTO `Sections` VALUES (8888, 509);

CREATE TABLE `Student` (
    `student_id` VARCHAR(500) PRIMARY KEY,
    `student_name` VARCHAR(500),
    `class_id` INT,
    `gender` VARCHAR (500),
    `mailbox` VARCHAR (500),
    `address` VARCHAR (500),
    `credits` INT
);

INSERT INTO `Student` VALUES ('D0901234', 'Mark', 202, 'Male', 'example@gmail.com', '�x�����x���ϥx����1��', 0);
INSERT INTO `Student` VALUES ('D0901235', 'Jack', 201, 'Male', 'example1@gmail.com', '�x�����x���ϥx����2��', 10);
INSERT INTO `Student` VALUES ('D0901236', 'Chark', 101, 'Male', 'example2@gmail.com', '�x�����x���ϥx����3��', 0);
INSERT INTO `Student` VALUES ('D1149488', 'Koopy', 202, 'Female', 'koopy@gmail.com', '�x�����x���ϥx����4��', 70);
INSERT INTO `Student` VALUES ('D1149489', 'Jungwon', 204, 'Male', 'yjw@gmail.com', '�x�����x���ϥx����5��', 0);
INSERT INTO `Student` VALUES ('D1149490', 'Heeseung', 401, 'Male', 'les@gmail.com', '�x�����x���ϥx����6��', 0);
INSERT INTO `Student` VALUES ('D1149495', 'Jay', 303, 'Male', 'pjs@gmail.com', '�x�����x���ϥx����7��', 0);
INSERT INTO `Student` VALUES ('D1149510', 'Jake', 303, 'Male', 'sjy@gmail.com', '�x�����x���ϥx����8��', 0);
INSERT INTO `Student` VALUES ('D1149231', 'Sunghoon', 303, 'Male', 'psh@gmail.com', '�x�����x���ϥx����9��', 0);
INSERT INTO `Student` VALUES ('D1149500', 'Sunoo', 304, 'Male', 'ksw@gmail.com', '�x�����x���ϥx����10��', 0);
INSERT INTO `Student` VALUES ('D1149654', 'Niki', 103, 'Male', 'niki@gmail.com', '�x�����x���ϥx����11��', 0);
INSERT INTO `Student` VALUES ('D1149123', 'Enhypen', 202, 'Male', 'en-@gmail.com', '�x�����x���ϥx����12��', 0);



CREATE TABLE `Class` (
    `class_id` INT PRIMARY KEY,
    `class_name` VARCHAR (500),
    `department_id` INT,
    `building_id` INT
);

INSERT INTO `Class` VALUES (101, '��T�@��', 1, 10);
INSERT INTO `Class` VALUES (102, '��T�@�A', 1, 10);
INSERT INTO `Class` VALUES (103, '��T�@��', 1, 10);
INSERT INTO `Class` VALUES (201, '��T�G��', 1, 10);
INSERT INTO `Class` VALUES (202, '��T�G�A', 1, 10);
INSERT INTO `Class` VALUES (203, '��T�G��', 1, 10);
INSERT INTO `Class` VALUES (204, '��T�G�B', 1, 10);
INSERT INTO `Class` VALUES (301, '��T�T��', 1, 10);
INSERT INTO `Class` VALUES (302, '��T�T�A', 1, 10);
INSERT INTO `Class` VALUES (303, '��T�T��', 1, 10);
INSERT INTO `Class` VALUES (304, '��T�T�B', 1, 10);
INSERT INTO `Class` VALUES (401, '��T�|��', 1, 10);
INSERT INTO `Class` VALUES (402, '��T�|�A', 1, 10);
INSERT INTO `Class` VALUES (403, '��T�|��', 1, 10);
INSERT INTO `Class` VALUES (404, '��T�|�B', 1, 10);

CREATE TABLE `Building` (
    `building_id` INT PRIMARY KEY,
    `building_name` VARCHAR (500)
);

INSERT INTO `Building` VALUES(1, '�ǫ��');
INSERT INTO `Building` VALUES(2, '��|�]');
INSERT INTO `Building` VALUES(3, '�g����Q�]');
INSERT INTO `Building` VALUES(4, '�z�Ǥj��');
INSERT INTO `Building` VALUES(5, '��X�B�ʳ�');
INSERT INTO `Building` VALUES(6, '�|���]');
INSERT INTO `Building` VALUES(7, '�y��j��');
INSERT INTO `Building` VALUES(8, '���Լ�');
INSERT INTO `Building` VALUES(9, '�u�Ǽ�');
INSERT INTO `Building` VALUES(10, '��T�q���ǰ|');

-- ALTER TABLE `Teacher`
-- ADD FOREIGN KEY (`department_id`) REFERENCES `Department`(`department_id`) ON DELETE SET NULL;

-- ALTER TABLE `Course`
-- ADD FOREIGN KEY (`department_id`) REFERENCES `Department`(`department_id`) ON DELETE SET NULL;

-- ALTER TABLE `Course_Instance`
-- ADD FOREIGN KEY (`teacher_id`) REFERENCES `Teacher`(`teacher_id`) ON DELETE SET NULL;

-- ALTER TABLE `Course_Instance`
-- ADD FOREIGN KEY (`Course_Instance_id`) REFERENCES `Course`(`course_id`) ON DELETE SET NULL;

-- ALTER TABLE `Selected_Course`
-- ADD FOREIGN KEY (`course_lists_id`) REFERENCES `Course_Instance`(`Course_Instance_id`) ON DELETE SET NULL;

-- ALTER TABLE `Selected_Course`
-- ADD FOREIGN KEY (`student_id`) REFERENCES `Student`(`student_id`) ON DELETE SET NULL;

-- ALTER TABLE `Student`
-- ADD FOREIGN KEY (`class_id`) REFERENCES `Class`(`class_id`) ON DELETE SET NULL;

-- ALTER TABLE `Class`
-- ADD FOREIGN KEY (`department_id`) REFERENCES `Department`(`department_id`) ON DELETE SET NULL;

-- ALTER TABLE `Class`
-- ADD FOREIGN KEY (`building_id`) REFERENCES `Building`(`building_id`) ON DELETE SET NULL;