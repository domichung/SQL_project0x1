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


INSERT INTO `Course` VALUES ('IECS0666', '資料庫系統', 1, 'yes', 3, '嘿嘿我是第一條測試註解','131434',5,0);
INSERT INTO `Course` VALUES ('IECS0001', '程式設計I', 1, 'no', 2, '嘿嘿我是第二條測試註解','373857',5,0);
INSERT INTO `Course` VALUES ('IECS0002', '微積分', 1, 'no', 3, '嘿嘿我是第三條測試註解','474849',5,0);
INSERT INTO `Course` VALUES ('IECS0003', '計算機概論', 1, 'no', 2, '嘿嘿我是第四條測試註解','124344',5,0);
INSERT INTO `Course` VALUES ('IECS0004', '體育(一)	', 1, 'no', 2, '嘿嘿我是第五條測試註解','2a2b',5,0);
INSERT INTO `Course` VALUES ('IECS0005', '中文思辨與表達(一)', 1, 'no', 2, '嘿嘿我是第六條測試註解','5152',5,0);
INSERT INTO `Course` VALUES ('EE0001', '工程數學', 2, 'no', 3, '電機系搞死人的科目1','313233',5,0);
INSERT INTO `Course` VALUES ('EE0013', '基礎物理', 2, 'no', 3, '電機系搞死人的科目3','2a3b4c',5,0);
INSERT INTO `Course` VALUES ('EE0012', '電路學', 2, 'yes', 3, '電機系搞死人的科目2','4a4b4c',5,0);
INSERT INTO `Course` VALUES ('ECE0001', '電子學', 3, 'no', 3, '電子學系搞死人的科目1','4a4b4c',5,0);
INSERT INTO `Course` VALUES ('STAT0087', '統計學', 10, 'no', 3, '統計學系','6c6d7e',5,0);

INSERT INTO `Course` VALUES ('IECS2003', '系統程式',1, 'yes', 3, 'Introduction of common system software in computer systems','131434',69,0);
INSERT INTO `Course` VALUES ('IECS359', '人工智慧導論', 1, 'no', 3, 'Introduction of Al','121314',60,0);
INSERT INTO `Course` VALUES ('IECS303', '計算機結構學', 1, 'yes', 3, 'Introduction of Design of CPU in computer systems','285354',73,0);
INSERT INTO `Course` VALUES ('IECS471', '程式設計與問題解決', 1, 'no', 2, 'Introduction of Based on various problem-solving algorithms', '4647',60,0);
INSERT INTO `Course` VALUES ('EEEN2001','工程數學(二)', 2, 'yes', 3, 'Introduction of how to express scientific or engineering problems using mathematical methods','123132',83,0);
INSERT INTO `Course` VALUES ('EEEN2012', '微處理機系統', 2, 'yes', 3, 'Introduction of CPU, I/O, TIMERS COUNTERS, and Serial Communication','161741',80,0);
INSERT INTO `Course` VALUES ('EEEN2018', '電波工程概論', 2, 'no', 2, 'Introduction of the basic and professional knowledge in the field of radio wave engineering, the latest developments in the field of radio wave engineering','2627',60,0);
INSERT INTO `Course` VALUES ('ELEN2003', '電子學(二)', 3, 'yes', 3, 'Introduction of how to express scientific or engineering problems using mathematical methods','384243',70,0);
INSERT INTO `Course` VALUES ('ELEN2016', '積體電路導論', 3, 'no', 3, 'Introduction of the basic concepts of integrated circuits','2a3132',120,0);
INSERT INTO `Course` VALUES ('MKT1030', '行銷意象工程', 13, 'yes', 3, 'This course is an introductory introduction to art and design','424344',80,0);