/*
Database Tables for Chatbot 
*/
--AI Tables
CREATE TABLE `intent`
(
    `id`     INT PRIMARY KEY NOT NULL,
    `intent` varchar(255)
);

CREATE TABLE `pattern`
(
    `id`       INT PRIMARY KEY NOT NULL,
    `intentID` INT,
    `intent`   varchar(255)
);

CREATE TABLE `response`
(
    `id`       INT PRIMARY KEY NOT NULL,
    `response` varchar(255)
);

CREATE TABLE `pattern_response`
(
    `patternID`  INT NOT NULL,
    `responseID` INT NOT NULL
);

-- Regional/Event Tables 
CREATE TABLE `Niagara`
(
    `id`    INT PRIMARY KEY NOT NULL,
    `links` varchar(255),
    `info`  varchar(255)
);

CREATE TABLE `Canada Games`
(
    `id`    INT PRIMARY KEY NOT NULL,
    `links` varchar(255),
    `info`  varchar(255)
);

--Province Medals Table
CREATE TABLE `Province Medals`
(
    `id`       INT PRIMARY KEY NOT NULL,
    `province` varchar(30),
    `gold`     INT,
    `silver`   INT,
    `bronze`   INT,
    `total`    INT
);

--Athlete Table
CREATE TABLE `Athletes`
(
    `id`        INT PRIMARY KEY NOT NULL,
    `name`      varchar(255),
    `province`  varchar(30),
    `home town` varchar(255),
    `club`      varchar(255),
    `coach`     varchar(255),
    `type`      INT,
    `sport`     INT,
    `age`       INT,
    `height`    INT,
    `weight`    INT,
    `alumni`    INT
);

-- Sport Tables 
CREATE TABLE `Sports`
(
    `id`    INT PRIMARY KEY NOT NULL,
    `sport` varchar(20)
);

CREATE TABLE `Baseball`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255)
        `game` INT,
    `location`   varchar(255),
    `home`       INT,
    `away`       INT,
    `home score` INT,
    `away score` INT
);

CREATE TABLE `Basketball`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `game`       INT,
    `location`   varchar(255),
    `home`       INT,
    `away`       INT,
    `home score` INT,
    `away score` INT
);

CREATE TABLE `Box Lacrosse`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `game`       INT,
    `location`   varchar(255),
    `home`       INT,
    `away`       INT,
    `home score` INT,
    `away score` INT
);

CREATE TABLE `Canoe Kayak`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `heat`       INT,
    `location`   varchar(255),
    `name`       varchar(255),
    `time`       varchar(255)
);

CREATE TABLE `Cycling`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `location`   varchar(255),
    `number`     INT,
    `name`       varchar(255),
    `time`       varchar(255),
    `heat one`   varchar(255),
    `heat two`   varchar(255),
    `heat three` varchar(255),
    `heat four`  varchar(255),
    `heat five`  varchar(255),
    `heat six`   varchar(255)
);

CREATE TABLE `Diving`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `location`   varchar(255),
    `name`       varchar(255),
    `points`     INT
);

CREATE TABLE `Golf`
(
    `id`          INT PRIMARY KEY NOT NULL,
    `date`        varchar(255),
    `time`        varchar(255),
    `event`       varchar(255),
    `event type`  varchar(255),
    `location`    varchar(255),
    `name`        varchar(255),
    `round one`   INT,
    `round two`   INT,
    `round three` INT
        `final round` INT
        `total` INT
);

CREATE TABLE `Rowing`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `heat`       INT,
    `location`   varchar(255),
    `name`       varchar(255),
    `time`       varchar(255)
);

CREATE TABLE `Rugby Sevens`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `game`       INT,
    `location`   varchar(255),
    `home`       INT,
    `away`       INT,
    `home score` INT,
    `away score` INT
);

CREATE TABLE `Sailing`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `location`   varchar(255),
    `name`       varchar(255),
    `race one`   varchar(255),
    `race two`   varchar(255),
    `race three` varchar(255),
    `race four`  varchar(255),
    `position`   varchar(255),
    `number`     INT
);

CREATE TABLE `Soccer`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `game`       INT,
    `location`   varchar(255),
    `home`       INT,
    `away`       INT,
    `home score` INT,
    `away score` INT
);

CREATE TABLE `Softball`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `game`       INT,
    `location`   varchar(255),
    `home`       INT,
    `away`       INT,
    `home wins`  INT,
    `away wins`  INT
);

CREATE TABLE `Swimming`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `race`       INT,
    `location`   varchar(255),
    `name`       varchar(255),
    `time`       varchar(255)
);

CREATE TABLE `Tennis`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `game`       INT,
    `location`   varchar(255),
    `home`       INT,
    `away`       INT,
    `home wins`  INT,
    `away wins`  INT
);

CREATE TABLE `Triathlon`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `race`       INT,
    `location`   varchar(255),
    `number`     INT,
    `name`       varchar(255),
    `time`       varchar(255)
);

CREATE TABLE `Volleyball`
(
    `id`               INT PRIMARY KEY NOT NULL,
    `date`             varchar(255),
    `time`             varchar(255),
    `event`            varchar(255),
    `event type`       varchar(255),
    `match`            INT,
    `location`         varchar(255),
    `home`             INT,
    `away`             INT,
    `home sets won`    INT,
    `away sets won`    INT,
    `points set one`   INT,
    `points set two`   INT,
    `points set three` INT,
    `points set four`  INT,
    `points set five`  INT
);

CREATE TABLE `Wrestling`
(
    `id`          INT PRIMARY KEY NOT NULL,
    `date`        varchar(255),
    `time`        varchar(255),
    `event`       varchar(255),
    `event type`  varchar(255),
    `duel`        INT,
    `location`    varchar(255),
    `home`        INT,
    `away`        INT,
    `home points` INT,
    `away points` INT
);

CREATE TABLE `Race`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `heat`       varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `time`       varchar(255)
);

CREATE TABLE `Hurdles`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `heat`       varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `time`       varchar(255)
);

CREATE TABLE `Steeplechase`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `heat`       varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `time`       varchar(255)
);

CREATE TABLE `Relay`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `heat`       varchar(20),
    `name`       varchar(255),
    `time`       varchar(255)
);

CREATE TABLE `High Jump`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `group`      varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `height`     varchar(255),
    `miss`       varchar(255)
);

CREATE TABLE `Long Jump`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `group`      varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `length`     varchar(255)
);

CREATE TABLE `Pole Vault`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `group`      varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `group 1`    varchar(255),
    `group 2`    varchar(255),
    `height`     varchar(255)
);

CREATE TABLE `Triple Jump`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `group`      varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `length`     varchar(255)
);

CREATE TABLE `Discus`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `group`      varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `group 1`    varchar(255),
    `group 2`    varchar(255),
    `length`     varchar(255)
);

CREATE TABLE `Hammer`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `group`      varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `group 1`    varchar(255),
    `group 2`    varchar(255),
    `length`     varchar(255)
);

CREATE TABLE `Javelin`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `group`      varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `group 1`    varchar(255),
    `group 2`    varchar(255),
    `length`     varchar(255)
);

CREATE TABLE `Shot Put`
(
    `id`         INT PRIMARY KEY NOT NULL,
    `date`       varchar(255),
    `time`       varchar(255),
    `event`      varchar(255),
    `event type` varchar(255),
    `group`      varchar(20),
    `number`     INT,
    `name`       varchar(255),
    `group 1`    varchar(255),
    `group 2`    varchar(255),
    `length`     varchar(255)
);

CREATE TABLE `Heptathlon Dates`
(
    `id`       INT PRIMARY KEY NOT NULL,
    `event`    varchar(255),
    `date`     varchar(255),
    `time`     varchar(255),
    `location` varchar(255)
);

CREATE TABLE `Heptathlon Scores`
(
    `id`           INT PRIMARY KEY NOT NULL,
    `name`         varchar(255),
    `100m Hurdles` varchar(255),
    `High Jump`    varchar(255),
    `Shot Put`     varchar(255),
    `200m`         varchar(255),
    `Long Jump`    varchar(255),
    `Javelin`      varchar(255),
    `800m`         varchar(255),
    `Points`       varchar(255)
);

CREATE TABLE `Decathlon Dates`
(
    `id`       INT PRIMARY KEY NOT NULL,
    `event`    varchar(255),
    `date`     varchar(255),
    `time`     varchar(255),
    `location` varchar(255)
);

CREATE TABLE `Decathlon Scores`
(
    `id`                INT PRIMARY KEY NOT NULL,
    `name`              varchar(255),
    `100m`              varchar(255),
    `Long Jump`         varchar(255),
    `Shot Put`          varchar(255),
    `High Jump Group 1` varchar(255),
    `High Jump Group 2` varchar(255),
    `400m`              varchar(255),
    `100m Hurdles`      varchar(255),
    `Discus`            varchar(255),
    `Pole Vault`        varchar(255),
    `Javelin`           varchar(255),
    `1500m`             varchar(255),
    `Points`            INT
);