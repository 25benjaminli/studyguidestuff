DROP TABLE IF EXISTS `cell`;
DROP TABLE IF EXISTS `row`;
DROP TABLE IF EXISTS `subject`;
--   UPDATE `sqlite_sequence` SET `seq` = 0 WHERE `name` = 'cell'

CREATE TABLE `cell` (
    `cellId` INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` varchar(128) NOT NULL,
    `type` varchar(128) NOT NULL,
    `contributors` varchar(128) NOT NULL,
    `rowId` varchar(128) NOT NULL
    

);
CREATE TABLE `row` (
    `rowId` INTEGER PRIMARY KEY AUTOINCREMENT,
    `subjectId` varchar(128) NOT NULL

);


CREATE TABLE `subject` (
    `subjectName` varchar(128) NOT NULL,
    `subjectId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT

);

INSERT INTO subject values ('english', 1);

INSERT INTO subject values ('math', 2);

INSERT INTO subject values ('science', 3);

INSERT INTO row values (?, '1'); -- create a row

INSERT INTO row values (?, '2'); -- create a row

-- INSERT INTO rowsubject values (?, '1', 'english'); -- link row 1 to subject 1
-- INSERT INTO rowsubject values (?, '2', 'math'); -- link row 1 to subject 1

INSERT INTO cell values (?, 'engtest', 'engtype1', 'ben1', '1'); -- link cell to row 1
INSERT INTO cell values (?, 'engtest2', 'engtype2', 'ben2', '1'); -- link cellto row 1
INSERT INTO cell values (?, 'mathtest1', 'mathtype1', 'ben3', '2'); -- link cell to row 1
INSERT INTO cell values (?, 'scitest1', 'scitype1', 'ben4', '3'); -- link cell to row 1


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
