CREATE TABLE people (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20),
    password VARCHAR(255),
    mail VARCHAR(255),
    birthday DATE,
    grade VARCHAR(10),
    user_photo VARCHAR(10000)
);

INSERT INTO people (username, password, mail, birthday, grade, user_photo)
VALUES ('john_doe', 'password123', 'john@example.com', '1990-05-15', '大四', 'base64_encoded_image_data');

select * from people;