CREATE TABLE user_box (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20),
    password VARCHAR(255),
    mail VARCHAR(255),
    birthday DATE,
    grade VARCHAR(10),
    Department VARCHAR(50),
    MORECLASS INT(50),
    user_photo VARCHAR(10000),
    user_class_count INT(50),
    newusercheck INT(20),
    ABCDclass   VARCHAR(50)
);

INSERT INTO user_box (username, password, mail, birthday, grade, Department, MORECLASS, user_photo, user_class_count, newusercheck ,ABCDclass)
VALUES ('domichung', '123', 'tmy@example.com', '2002-09-15', '�j�G', '��T�u�{�Ǩt', 0,'base64_encoded_image_data', 0, 1, '�A�Z');
VALUES ('koopy', '123456', 'koopy@example.com', '2004-05-2', '�j�G', '��T�u�{�Ǩt', 0,'base64_encoded_image_data', 0, 1, '�A�Z');
VALUES ('jungwon', '040209', 'yjw@example.com', '2004-02-09', '�j�G', '��T�u�{�Ǩt', 0,'base64_encoded_image_data', 0, 1, '�B�Z');
VALUES ('heeseung', '011015', 'lhs@example.com', '2001-10-15', '�j�|', '��T�u�{�Ǩt', 0,'base64_encoded_image_data', 0, 1, '�үZ');
VALUES ('jay', '020420', 'pjs@example.com', '2002-04-20', '�j�T', '��T�u�{�Ǩt', 0,'base64_encoded_image_data', 0, 1, '���Z');
VALUES ('jake', '021115', 'sjy@example.com', '2002-11-15', '�j�T', '��T�u�{�Ǩt', 0,'base64_encoded_image_data', 0, 1, '���Z');
VALUES ('sunghoon', '021208', 'psh@example.com', '2002-12-08', '�j�T', '��T�u�{�Ǩt', 0,'base64_encoded_image_data', 0, 1, '���Z');
VALUES ('sunoo', '030624', 'ksw@example.com', '2003-06-24', '�j�T', '��T�u�{�Ǩt', 0,'base64_encoded_image_data', 0, 1, '�B�Z');
VALUES ('niki', '051209', 'niki@example.com', '2005-12-09', '�j�@', '��T�u�{�Ǩt', 0,'base64_encoded_image_data', 0, 1, '���Z');
VALUES ('enhypen', '040711', 'en-@example.com', '2004-07-11', '�j�@', '��T�u�{�Ǩt', 0,'base64_encoded_image_data', 0, 1, '�A�Z');