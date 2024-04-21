CREATE TABLE `Course` (
    `course_id` VARCHAR (500) PRIMARY KEY,
    `course_name` VARCHAR (500),
    `department_id` INT,
    `subordinate` VARCHAR (500),
    `class_point` INT, 
    `description` VARCHAR (500),
    `time_stamp` VARCHAR (500),
    `maxstudent` INT,
    `nowstudent` INT
);


INSERT INTO `Course` VALUES ('IECS0666', '��Ʈw�t��', 1, 'yes', 3, '�K�K�ڬO�Ĥ@�����յ���','131434',5,0);
INSERT INTO `Course` VALUES ('IECS0001', '�{���]�pI', 1, 'no', 2, '�K�K�ڬO�ĤG�����յ���','373857',5,0);
INSERT INTO `Course` VALUES ('IECS0002', '�L�n��', 1, 'no', 3, '�K�K�ڬO�ĤT�����յ���','474849',5,0);
INSERT INTO `Course` VALUES ('IECS0003', '�p�������', 1, 'no', 2, '�K�K�ڬO�ĥ|�����յ���','124344',5,0);
INSERT INTO `Course` VALUES ('IECS0004', '��|(�@)	', 1, 'no', 2, '�K�K�ڬO�Ĥ������յ���','2a2b',5,0);
INSERT INTO `Course` VALUES ('IECS0005', '������P��F(�@)', 1, 'no', 2, '�K�K�ڬO�Ĥ������յ���','5152',5,0);
INSERT INTO `Course` VALUES ('EE0001', '�u�{�ƾ�', 2, 'no', 3, '�q���t�d���H�����1','313233',5,0);
INSERT INTO `Course` VALUES ('EE0013', '��¦���z', 2, 'no', 3, '�q���t�d���H�����3','2a3b4c',5,0);
INSERT INTO `Course` VALUES ('EE0012', '�q����', 2, 'yes', 3, '�q���t�d���H�����2','4a4b4c',5,0);
INSERT INTO `Course` VALUES ('ECE0001', '�q�l��', 3, 'no', 3, '�q�l�Ǩt�d���H�����1','4a4b4c',5,0);
INSERT INTO `Course` VALUES ('STAT0087', '�έp��', 10, 'no', 3, '�έp�Ǩt','6c6d7e',5,0);

INSERT INTO `Course` VALUES ('IECS2003', '�t�ε{��',1, 'yes', 3, 'Introduction of common system software in computer systems','131434',69,0);
INSERT INTO `Course` VALUES ('IECS359', '�H�u���z�ɽ�', 1, 'no', 3, 'Introduction of Al','121314',60,0);
INSERT INTO `Course` VALUES ('IECS303', '�p������c��', 1, 'yes', 3, 'Introduction of Design of CPU in computer systems','285354',73,0);
INSERT INTO `Course` VALUES ('IECS471', '�{���]�p�P���D�ѨM', 1, 'no', 2, 'Introduction of Based on various problem-solving algorithms', '4647',60,0);
INSERT INTO `Course` VALUES ('EEEN2001','�u�{�ƾ�(�G)', 2, 'yes', 3, 'Introduction of how to express scientific or engineering problems using mathematical methods','123132',83,0);
INSERT INTO `Course` VALUES ('EEEN2012', '�L�B�z���t��', 2, 'yes', 3, 'Introduction of CPU, I/O, TIMERS COUNTERS, and Serial Communication','161741',80,0);
INSERT INTO `Course` VALUES ('EEEN2018', '�q�i�u�{����', 2, 'no', 2, 'Introduction of the basic and professional knowledge in the field of radio wave engineering, the latest developments in the field of radio wave engineering','2627',60,0);
INSERT INTO `Course` VALUES ('ELEN2003', '�q�l��(�G)', 3, 'yes', 3, 'Introduction of how to express scientific or engineering problems using mathematical methods','384243',70,0);
INSERT INTO `Course` VALUES ('ELEN2016', '�n��q���ɽ�', 3, 'no', 3, 'Introduction of the basic concepts of integrated circuits','2a3132',120,0);
INSERT INTO `Course` VALUES ('MKT1030', '��P�N�H�u�{', 13, 'yes', 3, 'This course is an introductory introduction to art and design','424344',80,0);