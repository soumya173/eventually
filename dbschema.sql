CREATE TABLE `events` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `title` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `event_start_date` timestamp NOT NULL,
  `event_end_date` timestamp NOT NULL,
  `reg_start_date` timestamp NOT NULL,
  `reg_end_date` timestamp NOT NULL,
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `max_user` INTEGER NOT NULL DEFAULT 1,
  `min_user` INTEGER NOT NULL DEFAULT 1,
  `accept_file_type` varchar(255) DEFAULT null,
  `accept_video_file` boolean,
  `location` varchar(255),
  `allow_comment` boolean
);

CREATE TABLE `users` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  'logged' boolean DEFAULT false,
  FOREIGN KEY(id) REFERENCES teams(lead_user_id)
);

CREATE TABLE `teams` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `event_id` INTEGER NOT NULL,
  `name` varchar(255) NOT NULL,
  `reward_id` INTEGER DEFAULT null,
  `user_ids` varchar(255) NOT NULL,
  `lead_user_id` INTEGER NOT NULL,
  `type` varchar(255) NOT NULL,
  FOREIGN KEY(event_id) REFERENCES events(id),
  FOREIGN KEY(id) REFERENCES submission(team_id)
  -- FOREIGN KEY(lead_user_id) REFERENCES users(id),
);

CREATE TABLE `rewards` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `event_id` INTEGER NOT NULL,
  `amount` INTEGER NOT NULL DEFAULT 0,
  `type` varchar(255),
  `title` varchar(255) NOT NULL,
  `position` INTEGER,
  FOREIGN KEY(event_id) REFERENCES events(id),
  FOREIGN KEY(id) REFERENCES teams(reward_id)
);

CREATE TABLE `submission` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `title` varchar(255),
  `submitted_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `team_id` INTEGER NOT NULL,
  `event_id` INTEGER NOT NULL,
  `location` varchar(255),
  `video_file` varchar(255),
  `views` INTEGER DEFAULT 0,
  FOREIGN KEY(event_id) REFERENCES events(id)
);

CREATE TABLE `subscription` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER NOT NULL,
  `event_id` INTEGER NOT NULL,
  FOREIGN KEY(user_id) REFERENCES users(id),
  FOREIGN KEY(event_id) REFERENCES events(id)
);

CREATE TABLE `comments` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `comment` varchar(255),
  `commented_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `user_id` INTEGER,
  `submission_id` INTEGER NOT NULL,
  `rating` INTEGER,
  FOREIGN KEY(user_id) REFERENCES users(id),
  FOREIGN KEY(submission_id) REFERENCES submission(id)
);

-- User table
INSERT INTO users (name, password,type,email) values ('admin','Welcome@123','admin','admin@gmail.com');
INSERT INTO users (name, password,type,email) values ('shashi','Welcome@123','user','shashi@gmail.com');
INSERT INTO users (name, password,type,email) values ('sgorai','Welcome@123','user','sgorai@gmail.com');
INSERT INTO users (name, password,type,email) values ('nikil','Welcome@123','user','nikil@gmail.com');
INSERT INTO users (name, password,type,email) values ('mohit','Welcome@123','user','mohit@gmail.com');
INSERT INTO users (name, password,type,email) values ('mahipal','Welcome@123','user','mahipal@gmail.com');

-- Events table
INSERT INTO EVENTS (title,description,event_start_date,event_end_date,reg_start_date,reg_end_date,max_user,min_user,accept_file_type,accept_video_file,location,allow_comment) values ('Technothon','Welcome to technothon 2021',"2021-02-23 08:30:00","2021-02-25 08:30:00","2021-02-15 08:30:00","2021-02-22 08:30:00",5,3,'tar',true,'online',true);
INSERT INTO EVENTS (title,description,event_start_date,event_end_date,reg_start_date,reg_end_date,max_user,min_user,accept_file_type,accept_video_file,location,allow_comment) values ('Hackathon','Welcome to Hackathon 2021',"2021-02-10 08:30:00","2021-02-12 08:30:00","2021-01-05 08:30:00","2021-01-22 08:30:00",5,3,'tar',true,'online',true);
INSERT INTO EVENTS (title,description,event_start_date,event_end_date,reg_start_date,reg_end_date,max_user,min_user,accept_file_type,accept_video_file,location,allow_comment) values ('Arm Wrestling','Welcome to Arm Wrestling 2021',"2021-03-10 08:30:00","2021-03-12 08:30:00","2021-02-05 08:30:00","2021-02-22 08:30:00",1,1,'tar',true,'online',true);

-- Subscription table
INSERT INTO Subscription (user_id,event_id) values (2,1);
INSERT INTO Subscription (user_id,event_id) values (2,3);
INSERT INTO Subscription (user_id,event_id) values (3,1);
INSERT INTO Subscription (user_id,event_id) values (3,3);

--Submission table

INSERT INTO submission (title,team_id,event_id,location,video_file) values ('initial',2,1,'/var/initial/','initial.mp4');
INSERT INTO submission (title,team_id,event_id,location,video_file) values ('final',1,1,'/var/final/','final.mp4');
INSERT INTO submission (title,team_id,event_id,location,video_file) values ('intermettent',2,1,'/var/lost/','lost.mp4');

-- rewards tables
INSERT into rewards (event_id,amount,type,title,position) values (1,2000,'best loser','Awards to the best loser',1);
INSERT into rewards (event_id,amount,type,title,position) values (1,1000,'best loser','Awards to the second best loser',2);
INSERT into rewards (event_id,amount,type,title,position) values (1,500,'best loser','Awards to the third best loser',3);

INSERT into rewards (event_id,amount,type,title,position) values (3,20000,'Arm breaker','Best arm breaker',1);
INSERT into rewards (event_id,amount,type,title,position) values (3,10000,'Arm breaker','Better arm breaker',2);
INSERT into rewards (event_id,amount,type,title,position) values (3,5000,'Arm breaker','Good arm breaker',3);
-- teams tables
INSERT INTO teams (event_id,name,reward_id,user_ids,lead_user_id,type) values (3,'Retro style',4,'[6]',6,'participant');
INSERT INTO teams (event_id,name,reward_id,user_ids,lead_user_id,type) values (3,'Broken hand',5,'[3]',3,'participant');
INSERT INTO teams (event_id,name,reward_id,user_ids,lead_user_id,type) values (3,'No One',6,'[2]',2,'participant');

INSERT INTO teams (event_id,name,user_ids,lead_user_id,type) values (1,'Techno Judge','[4,5]',5,'judge');

INSERT INTO teams (event_id,name,reward_id,user_ids,lead_user_id,type) values (1,'EVENTually',1,'[2,3,4,5,6]',4,'participant');

-- ALTER TABLE `teams` ADD FOREIGN KEY (`event_id`) REFERENCES `events` (`id`);

-- ALTER TABLE `submission` ADD FOREIGN KEY (`event_id`) REFERENCES `events` (`id`);

-- ALTER TABLE `rewards` ADD FOREIGN KEY (`event_id`) REFERENCES `events` (`id`);

-- ALTER TABLE `rewards` ADD FOREIGN KEY (`id`) REFERENCES `teams` (`reward_id`);

-- ALTER TABLE `users` ADD FOREIGN KEY (`id`) REFERENCES `teams` (`lead_user_id`);

-- ALTER TABLE `teams` ADD FOREIGN KEY (`id`) REFERENCES `submission` (`team_id`);

-- ALTER TABLE `subscription` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

-- ALTER TABLE `subscription` ADD FOREIGN KEY (`event_id`) REFERENCES `events` (`id`);

-- ALTER TABLE `comments` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

-- ALTER TABLE `comments` ADD FOREIGN KEY (`submission_id`) REFERENCES `submission` (`id`);
