-- -----------------------------------------------------
-- Table `adult_event`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adult_event` (
  `event_id` INT NOT NULL,
  `event_name` VARCHAR(45) NULL,
  `event_price` VARCHAR(45) NULL,
  `isBYOB` TINYINT NULL,
  `isKidFriendly` TINYINT NULL,
  `adult_eventcol` VARCHAR(45) NULL,
  PRIMARY KEY (`event_id`)
  );


-- -----------------------------------------------------
-- Table `children_event`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `children_event` (
  `event_id` INT NOT NULL,
  `event_name` VARCHAR(45) NULL,
  `event_price` DECIMAL NULL,
  `event_for_toddler` TINYINT NULL,
  `event_for_preschooler` TINYINT NULL,
  `event_for_highschooler` TINYINT NULL,
  PRIMARY KEY (`event_id`)
  );


-- -----------------------------------------------------
-- Table `events`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `events` (
  `event_id` INT NOT NULL,
  `event_count` INT NULL,
  `event_time` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`event_id`),
  CONSTRAINT `event_id`
    FOREIGN KEY (`event_id`)
    REFERENCES `adult_event` (`event_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE UNIQUE INDEX `eventID_UNIQUE` ON `events` (`event_id` ASC);


-- -----------------------------------------------------
-- Table `has_created_event`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `has_created_event` (
  `event_id` VARCHAR(45) NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`event_id`));


-- -----------------------------------------------------
-- Table `has_registered_for_event`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `has_registered_for_event` (
  `event_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`event_id`));


-- -----------------------------------------------------
-- Table `user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `user` ;

CREATE TABLE IF NOT EXISTS `user` (
  `user_id` INT NOT NULL,
  `username` VARCHAR(45) NULL,
  `user_password` VARCHAR(45) NULL,
  `user_email` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `has_registered_for_event` (`event_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE UNIQUE INDEX `username_UNIQUE` ON `user` (`username` ASC);



