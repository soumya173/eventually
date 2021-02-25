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


INSERT INTO users (name, password,type,email) values ('admin','Welcome@123','admin','admin@gmail.com');

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
