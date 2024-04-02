CREATE TABLE user_box (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20),
    password VARCHAR(255),
    mail VARCHAR(255),
    birthday DATE,
    grade VARCHAR(10),
    Department VARCHAR(50),
    MORECLASS INT(50),
    user_photo VARCHAR(10000)
);

INSERT INTO user_box (username, password, mail, birthday, grade, Department, MORECLASS, user_photo)
VALUES ('john_doe', 'password123', 'john@example.com', '1990-05-15', '大四', '資工系', 0,'base64_encoded_image_data');