CREATE TABLE `Course` (
    `course_id` VARCHAR (500) PRIMARY KEY,
    `course_name` VARCHAR (500),
    `department_id` INT,
    `subordinate` VARCHAR (500),
    `class_point` INT, 
    `description` VARCHAR (500),
    `time_stamp` VARCHAR (500)
);


INSERT INTO `Course` VALUES ('IECS0666', '資料庫系統', 1, 'yes', 3, '嘿嘿我是第一條測試註解','131434');
INSERT INTO `Course` VALUES ('IECS0001', '程式設計I', 1, 'no', 2, '嘿嘿我是第二條測試註解','373857');
INSERT INTO `Course` VALUES ('IECS0002', '微積分', 1, 'no', 3, '嘿嘿我是第三條測試註解','474849');
INSERT INTO `Course` VALUES ('IECS0003', '計算機概論', 1, 'no', 2, '嘿嘿我是第四條測試註解','124344');
INSERT INTO `Course` VALUES ('IECS0004', '體育(一)	', 1, 'no', 2, '嘿嘿我是第五條測試註解','2a2b');
INSERT INTO `Course` VALUES ('IECS0005', '中文思辨與表達(一)', 1, 'no', 2, '嘿嘿我是第六條測試註解','5152');
INSERT INTO `Course` VALUES ('EE0001', '工程數學', 2, 'no', 3, '電機系搞死人的科目1','313233');
INSERT INTO `Course` VALUES ('EE0013', '基礎物理', 2, 'no', 3, '電機系搞死人的科目3','2a3b4c');
INSERT INTO `Course` VALUES ('EE0012', '電路學', 2, 'yes', 3, '電機系搞死人的科目2','4a4b4c');
INSERT INTO `Course` VALUES ('ECE0001', '電子學', 3, 'no', 3, '電子學系搞死人的科目1','4a4b4c');
INSERT INTO `Course` VALUES ('STAT0087', '統計學', 10, 'no', 3, '統計學系','6c6d7e');
