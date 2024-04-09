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
VALUES ('domichung', '123', 'tmy@example.com', '2002-09-15', '大二', '資訊工程學系', 0,'base64_encoded_image_data', 0, 1, '乙班');