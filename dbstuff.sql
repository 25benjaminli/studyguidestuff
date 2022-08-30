DROP TABLE IF EXISTS `cell`;
DROP TABLE IF EXISTS `row`;
DROP TABLE IF EXISTS `subject`;
DROP TABLE IF EXISTS `moderator`;

--   UPDATE `sqlite_sequence` SET `seq` = 0 WHERE `name` = 'cell'

CREATE TABLE `row` (
    `rowId` INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` varchar(128) NOT NULL,
    `url` varchar(128) NOT NULL,
    `type` varchar(128) NOT NULL,
    `contributors` varchar(128) NOT NULL,
    `subjectId` varchar(128) NOT NULL,
    `isaccepted` INTEGER DEFAULT 0
);


CREATE TABLE `subject` (
    `subjectId` INTEGER PRIMARY KEY NOT NULL,
    `subjectName` varchar(128) NOT NULL,
    `category` varchar(128) NOT NULL
);

CREATE TABLE `moderator` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `email` varchar(128) NOT NULL,
    `passw` varchar(256) NOT NULL,
    `isapproved` tinyint DEFAULT 0
);

-- INSERT INTO subject values ('english', ?);

-- INSERT INTO subject values ('math', ?);

-- INSERT INTO subject values ('science', ?);

-- INSERT INTO row values (?, 'engtest', 'engtype1', 'ben1', '1'); -- link cell to row 1
-- INSERT INTO row values (?, 'engtest2', 'engtype2', 'ben2', '1'); -- link cell to row 1
-- INSERT INTO row values (?, 'mathtest1', 'mathtype1', 'ben3', '2'); -- link cell to row 1
-- INSERT INTO row values (?, 'scitest1', 'scitype1', 'ben4', '3'); -- link cell to row 1
-- INSERT INTO rowsubject values (?, '1', 'english'); -- link row 1 to subject 1
-- INSERT INTO rowsubject values (?, '2', 'math'); -- link row 1 to subject 1




-- INSERT INTO cell values (?, "cell1", "1");

-- select COUNT(*) from subject;

-- select * from subject;
-- select "------";
-- select * from row;
-- select "------";
-- select * from cell;

-- DROP TABLE IF EXISTS `cell`;
-- DROP TABLE IF EXISTS `row`;
-- DROP TABLE IF EXISTS `subject`;

-- select "selecting cell 1 and 2 from row 2"
-- select * from cell;
