DROP USER IF EXISTS 'whatabook_user'@'localhost';
 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

INSERT INTO store(locale)
    VALUES('1000 Galvin Rd S, Bellevue, NE 68005');

INSERT INTO book(book_name, author, details)
    VALUES('It', 'Stephen King', 'Horror Novel Written in 1986');

INSERT INTO book(book_name, author, details)
    VALUES('Misery', 'Stephen King', 'Horror Novel Written in 1987');

INSERT INTO book(book_name, author, details)
    VALUES('Carrie', 'Stephen King', "Horror Novel Written in 1974");

INSERT INTO book(book_name, author, details)
    VALUES('The Stand', 'Stephen King', "Horror Novel Written in 1978");

INSERT INTO book(book_name, author, details)
    VALUES('The Shining', 'Stephen King', "Horror Novel Written in 1977");

INSERT INTO book(book_name, author, details)
    VALUES('Pet Semetary', 'Stephen King', "Horror Novel Written in 1983");

INSERT INTO book(book_name, author, details)
    VALUES('Salems Lot', 'Stephen King', "Horror Novel Written in 1975");

INSERT INTO book(book_name, author, details)
    VALUES('The Green Mile', 'Stephen King', "Horror Novel Written in 1996");

INSERT INTO book(book_name, author, details)
    VALUES('The Long Walk', 'Stephen King', "Horror Novel Written in 1979");

INSERT INTO user(first_name, last_name) 
    VALUES('Jay', 'Carson');

INSERT INTO user(first_name, last_name)
    VALUES('Henry', 'Billow');

INSERT INTO user(first_name, last_name)
    VALUES('Denise', 'Wilson');

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jay'), 
        (SELECT book_id FROM book WHERE book_name = 'The Long Walk')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Denise'),
        (SELECT book_id FROM book WHERE book_name = 'Carrie')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Henry'),
        (SELECT book_id FROM book WHERE book_name = 'The Shining')
    );