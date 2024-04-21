use OnlineCourseRegisterSystem;
CREATE TABLE `Teacher` (
    `teacher_id` INT PRIMARY KEY,
    `teacher_name` VARCHAR (20),
    `department_id` INT,
    `gender` VARCHAR (10),
    `mailbox` VARCHAR (100)
);

INSERT INTO `Teacher` VALUES(3739, '竇其仁', 1, 'male', 'crdow@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3746, '陳德生', 1, 'male', 'dschen@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3749, '林佩君', 1, 'female', 'peiclin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3750, '許懷中', 1, 'male', 'hjhsu@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3761, '林峰正', 1, 'male', 'fclin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3763, '王益文', 1, 'male', 'ywang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3765, '劉宗杰', 1, 'male', 'tjliu@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3767, '李榮三', 1, 'male', 'leejs@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3768, '劉明機', 1, 'male', 'mingcliu@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3729, '陳青文', 1, 'male', 'chingwen@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3736, '葉春秀', 1, 'female', 'chunhyeh@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(7777, '王小美', 1, 'female', 'mememe@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3808, '黃思倫', 2, 'male', 'srhuang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3810, '何子儀', 2, 'male', 'tyho@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3811, '梁寶芝', 2, 'female', 'bjliang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3815, '謝振中', 2, 'male', 'jjshieh@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3816, '陳志強', 2, 'male', 'cchiang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3825, '李企桓', 2, 'male', 'chihlee@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3827, '鄭進興', 2, 'male', 'chcheng@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3831, '陳坤煌', 2, 'male', 'chenkh@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3838, '王壘', 2, 'male', 'leiwang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5756, '洪耀正', 2, 'male', 'yaochenhung@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3836, '林欽瑞', 2, 'male', 'rclin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3805, '徐士賢', 2, 'male', 'shihhhsu@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4957, '簡鳳佐', 3, 'male', 'ftchien@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4958, '康宗貴', 3, 'male', 'kangtk@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4965, '劉堂傑', 3, 'male', 'dgliu@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4966, '林宗志', 3, 'male', 'tclin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4969, '林成利', 3, 'male', 'clilin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4962, '楊炳章', 3, 'male', 'pcyang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3922, '張興政', 4, 'male', 'hcchang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3926, '鄒慶福', 4, 'male', 'cftsou@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3928, '劉益瑞', 4, 'male', 'erliu@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3934, '洪三山', 4, 'male', 'sshung@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3938, '林賢龍', 4, 'male', 'sllin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3925, '林育德', 5, 'male', 'ydlin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3937, '沈祖望', 5, 'male', 'twshen@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3900, '林昱成', 5, 'male', 'yuchlin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4810, '彭嘉美', 5, 'female', 'may6660@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4813, '袁世一', 5, 'male', 'syyuan@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4816, '林漢年', 6, 'male', 'hnlin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4819, '林立謙', 6, 'male', 'lclin@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4824, '廖知恩', 6, 'male', 'heliao@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4839, '陸清達', 6, 'male', 'chingtlu@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4845, '蔡淵裕', 6, 'male', 'yuanytsai@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5046, '葉建宏', 7, 'male', 'yehch@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5057, '李英德', 7, 'male', 'yinglee@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5058, '林泰生', 7, 'male', 'tyson@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5069, '周哲仲', 7, 'male', 'choucc@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5070, '馬仕信', 7, 'male', 'shma@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(2137, '黃煇慶', 8, 'male', 'cheeny@ms6.hinet.net');
INSERT INTO `Teacher` VALUES(5323, '朱正永', 8, 'male', 'cychu@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5630, '王志宇', 8, 'male', 'wangcy@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5667, '張志相', 8, 'male', 'cschang@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5670, '戴瑞坤', 8, 'male', 'rktai@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(2080, '林彩玉', 9, 'female', 'linty@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5113, '楊菁菁', 9, 'female', 'yangcc@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5118, '魏秀娟', 9, 'female', 'hsiucwei@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5125, '黃同瑤', 9, 'female', 'huangty@fcu.edu.tw');
INSERT INTO `Teacher` VALUES(6213, '賴奇厚', 9, 'male', 'chlay@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3001, '周澤捷', 10, 'male', 'chz@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4013, '林麗芬', 10, 'female', 'lflin@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4402, '鍾冬川', 10, 'male', 'dcjhwueng@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4408, '林文欽', 10, 'male', 'linwc@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4418, '吳榮彬', 10, 'male', 'cwu@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3959, '張淵仁', 11, 'male', 'yjenchang@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3960, '謝宗翰', 11, 'male', 'thshieh@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3975, '楊瑞彬', 11, 'male', 'rbyang@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3976, '方俊', 11, 'male', 'jfang@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3980, '黃柏文', 11, 'male', 'pwhwang@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5502, '闕帝丰', 12, 'male', 'difeng.c@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5609, '李麗秋', 12, 'female', 'lclee@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5610, '莊坤良', 12, 'male', 'klchuang@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5625, '邱源貴', 12, 'male', 'ygchiou@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(5644, '劉顯親', 12, 'female', 'hcliou@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(2600, '賴文祥', 13, 'male', 'whlai@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4272, '簡士超', 13, 'male', 'scchien@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4273, '李元恕', 13, 'male', 'yslii@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4386, '何晉瑋', 13, 'male', 'cweiho@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(6010, '林豐智', 13, 'male', 'fjlin@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4385, '李悅端', 13, 'male', 'yuehtli@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3122, '王起平', 14, 'female', 'cpwang@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3123, '林慶昌', 14, 'male', 'cclin@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3130, '張智元', 14, 'male', 'rchang@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(3150, '林正紋', 14, 'male', 'jwlin@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4273, '林保宏', 14, 'male', 'paolin@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4705, '陳建元', 15, 'male', 'cyuan@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4708, '洪本善', 15, 'male', 'pshung@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4714, '李瑞陽', 15, 'male', 'rylee@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4727, '王珍玲', 15, 'female', 'wangcl@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(4733, '辛年豐', 15, 'male', 'nfshin@mail.fcu.edu.tw');
INSERT INTO `Teacher` VALUES(1029, '方淳民', 4, 'male', 'fang0129.tw@yahoo.com.tw');






CREATE TABLE `Department` (
    `department_id` INT PRIMARY KEY,
    `department_name` VARCHAR (500)
);

INSERT INTO `Department` VALUES(1, '資訊工程學系');
INSERT INTO `Department` VALUES(2, '電機工程學系');
INSERT INTO `Department` VALUES(3, '電子工程學系');
INSERT INTO `Department` VALUES(4, '自動控制工程學系');
INSERT INTO `Department` VALUES(5, '資訊電機學院學士班');
INSERT INTO `Department` VALUES(6, '通訊工程學系');
INSERT INTO `Department` VALUES(7, '光電科學與工程學系');
INSERT INTO `Department` VALUES(8, '通識中心');
INSERT INTO `Department` VALUES(9, '應用數學學系');
INSERT INTO `Department` VALUES(10, '統計學系');
INSERT INTO `Department` VALUES(11, '航太與系統工程學系');
INSERT INTO `Department` VALUES(12, '外國語文學系');
INSERT INTO `Department` VALUES(13, '行銷學系');
INSERT INTO `Department` VALUES(14, '土木工程學系');
INSERT INTO `Department` VALUES(15, '土地管理學系');




CREATE TABLE `Course` (
    `course_id` VARCHAR (500) PRIMARY KEY,
    `course_name` VARCHAR (500),
    `department_id` INT,
    `required` VARCHAR (500),
    `credit` INT, 
    `description` VARCHAR (500)
);


INSERT INTO `Course` VALUES ('IECS322', '資料庫系統', 1, 'yes', 3, 'Introduction of database system');
INSERT INTO `Course` VALUES ('IECS241', '互聯網路', 1, 'no', 3, 'Introduction of network system');
INSERT INTO `Course` VALUES ('IECS108', '程式設計(III)', 1, 'yes', 4, 'Introduction of programming 3');
INSERT INTO `Course` VALUES ('IECS109', '程式設計(IV)', 1, 'yes', 4, 'Introduction of programming 4');
INSERT INTO `Course` VALUES ('CIEE105', '線性代數', 3, 'yes', 3, 'Introduction of linear algebra');
INSERT INTO `Course` VALUES ('MATH106', '微積分(二)', 9, 'yes', 3, 'Introduction of Calclus');
INSERT INTO `Course` VALUES ('CIEE111', '普通物理-電、磁、光實驗', 3, 'yes', 3, 'Introduction of physcial');
INSERT INTO `Course` VALUES ('CIEE106', '邏輯設計', 3, 'yes', 3, 'Introduction of logical');
INSERT INTO `Course` VALUES ('GHUC201', '中國文物欣賞', 8, 'no', 2, 'Introduction of China');
INSERT INTO `Course` VALUES ('GHUC205', '日本歷史與文化', 8, 'no', 2, 'Introduction of Japan');
INSERT INTO `Course` VALUES ('GHUR302', '台灣民間信仰', 8, 'no', 2, 'Introduction of Taiwan');
INSERT INTO `Course` VALUES ('IDSS3002', '淨零碳排與碳足跡計算', 8, 'no', 2, 'Introduction of Earth');
INSERT INTO `Course` VALUES ('COB102', '資訊網路', 10, 'no', 2, 'Introduction of Internet');
INSERT INTO `Course` VALUES ('PHYS105', '普通物理(一)', 9, 'yes', 4, 'Introduction of Physical');
INSERT INTO `Course` VALUES ('PHYS202', '電磁學(二)', 7, 'yes', 3, 'Introduction of maganaic');
INSERT INTO `Course` VALUES ('IECS888', '競賽程式', 1, 'no', 4, 'Introduction of Programming Contest');
INSERT INTO `Course` VALUES ('IECS2003', '系統程式', 1, 'yes', 3, 'Introduction of common system software in computer systems');

INSERT INTO `Course` VALUES ('IECS359', '人工智慧導論', 1, 'no', 3, 'Introduction of AI');
INSERT INTO `Course` VALUES ('IECS303', '計算機結構學', 1, 'yes', 3, 'Introduction of Design of CPU in computer systems');
INSERT INTO `Course` VALUES ('IECS471', '程式設計與問題解決', 1, 'no', 2, 'Introduction of Based on various problem-solving algorithms');
INSERT INTO `Course` VALUES ('EEEN2001', '工程數學(二)', 2, 'yes', 3, 'Introduction of how to express scientific or engineering problems using mathematical methods');
INSERT INTO `Course` VALUES ('EEEN2012', '微處理機系統', 2, 'yes', 3, 'Introduction of CPU, I/O, TIMERS/COUNTERS, and Serial Communication');
INSERT INTO `Course` VALUES ('EEEN2018', '電波工程概論', 2, 'no', 2, 'Introduction of the basic and professional knowledge in the field of radio wave engineering, the latest developments in the field of radio wave engineering');
INSERT INTO `Course` VALUES ('ELEN2003', '電子學(二)', 3, 'yes', 3, 'Introduction of how to express scientific or engineering problems using mathematical methods');
INSERT INTO `Course` VALUES ('ELEN2016', '積體電路導論', 3, 'no', 3, 'Introduction of the basic concepts of integrated circuits');
INSERT INTO `Course` VALUES ('MKT1030', '行銷意象工程', 13, 'yes', 3, 'This course is an introductory introduction to art and design');

INSERT INTO `Course` VALUES ('MKT2051', '行銷策略與個案分析', 13, 'no', 3, 'This course explores the core concepts ofstrategic marketing, implementation, andtheir integration in practical operations.');
INSERT INTO `Course` VALUES ('CE2085', '土壤力學(一)', 14, 'yes', 3, 'The content studied is an essential tool for the analysis and design of geotechnical engineering such as building foundations and retaining structures.');
INSERT INTO `Course` VALUES ('CE2080', '地形測量', 14, 'no', 3, 'This course aims to enable students to understand the principles of topographic surveying, operational techniques and drawing methods, and become proficient in the operation and maintenance of surveying instruments, integrating theory with practice.');
INSERT INTO `Course` VALUES ('LAND2040', '地理資訊系統概論', 15, 'yes', 3, 'Introduction of the theory, application level and software operation of geographic information system (GIS) and spatial information');
INSERT INTO `Course` VALUES ('LAND2048', '不動產行銷管理實務', 15, 'no', 3, 'This course enables students to understand real estate marketing by teaching marketing-related theories and real estate marketing management examples, including real estate marketing plans, market research and analysis, sales field management, advertising planning copywriting, marketing strategies and group practical exercises. Theoretical application and practical operation.');



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

INSERT INTO `Student` VALUES ('D0901234', 'Mark', 202, 'Male', 'example@gmail.com', '台中市台中區台中路1號', 0);
INSERT INTO `Student` VALUES ('D0901235', 'Jack', 201, 'Male', 'example1@gmail.com', '台中市台中區台中路2號', 10);
INSERT INTO `Student` VALUES ('D0901236', 'Chark', 101, 'Male', 'example2@gmail.com', '台中市台中區台中路3號', 0);
INSERT INTO `Student` VALUES ('D1149488', 'Koopy', 202, 'Female', 'koopy@gmail.com', '台中市台中區台中路4號', 70);
INSERT INTO `Student` VALUES ('D1149489', 'Jungwon', 204, 'Male', 'yjw@gmail.com', '台中市台中區台中路5號', 0);
INSERT INTO `Student` VALUES ('D1149490', 'Heeseung', 401, 'Male', 'les@gmail.com', '台中市台中區台中路6號', 0);
INSERT INTO `Student` VALUES ('D1149495', 'Jay', 303, 'Male', 'pjs@gmail.com', '台中市台中區台中路7號', 0);
INSERT INTO `Student` VALUES ('D1149510', 'Jake', 303, 'Male', 'sjy@gmail.com', '台中市台中區台中路8號', 0);
INSERT INTO `Student` VALUES ('D1149231', 'Sunghoon', 303, 'Male', 'psh@gmail.com', '台中市台中區台中路9號', 0);
INSERT INTO `Student` VALUES ('D1149500', 'Sunoo', 304, 'Male', 'ksw@gmail.com', '台中市台中區台中路10號', 0);
INSERT INTO `Student` VALUES ('D1149654', 'Niki', 103, 'Male', 'niki@gmail.com', '台中市台中區台中路11號', 0);
INSERT INTO `Student` VALUES ('D1149123', 'Enhypen', 202, 'Male', 'en-@gmail.com', '台中市台中區台中路12號', 0);



CREATE TABLE `Class` (
    `class_id` INT PRIMARY KEY,
    `class_name` VARCHAR (500),
    `department_id` INT,
    `building_id` INT
);

INSERT INTO `Class` VALUES (101, '資訊一甲', 1, 10);
INSERT INTO `Class` VALUES (102, '資訊一乙', 1, 10);
INSERT INTO `Class` VALUES (103, '資訊一丙', 1, 10);
INSERT INTO `Class` VALUES (201, '資訊二甲', 1, 10);
INSERT INTO `Class` VALUES (202, '資訊二乙', 1, 10);
INSERT INTO `Class` VALUES (203, '資訊二丙', 1, 10);
INSERT INTO `Class` VALUES (204, '資訊二丁', 1, 10);
INSERT INTO `Class` VALUES (301, '資訊三甲', 1, 10);
INSERT INTO `Class` VALUES (302, '資訊三乙', 1, 10);
INSERT INTO `Class` VALUES (303, '資訊三丙', 1, 10);
INSERT INTO `Class` VALUES (304, '資訊三丁', 1, 10);
INSERT INTO `Class` VALUES (401, '資訊四甲', 1, 10);
INSERT INTO `Class` VALUES (402, '資訊四乙', 1, 10);
INSERT INTO `Class` VALUES (403, '資訊四丙', 1, 10);
INSERT INTO `Class` VALUES (404, '資訊四丁', 1, 10);

CREATE TABLE `Building` (
    `building_id` INT PRIMARY KEY,
    `building_name` VARCHAR (500)
);

INSERT INTO `Building` VALUES(1, '學思樓');
INSERT INTO `Building` VALUES(2, '體育館');
INSERT INTO `Building` VALUES(3, '土木水利館');
INSERT INTO `Building` VALUES(4, '理學大樓');
INSERT INTO `Building` VALUES(5, '綜合運動場');
INSERT INTO `Building` VALUES(6, '育樂館');
INSERT INTO `Building` VALUES(7, '語文大樓');
INSERT INTO `Building` VALUES(8, '忠勤樓');
INSERT INTO `Building` VALUES(9, '工學樓');
INSERT INTO `Building` VALUES(10, '資訊電機學院');

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