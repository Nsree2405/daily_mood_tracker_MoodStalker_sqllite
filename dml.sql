-- Insert Users
INSERT INTO users (uname, email, passkey) VALUES 
('alice', 'alice@example.com', 'password123'),
('bob', 'bob@example.com', 'securepass'),
('charlie', 'charlie@example.com', 'mypassword');

-- Insert Moods
INSERT INTO moods (mname, type, booster, activity) VALUES
('Happy', 'Positive', 'Sunlight', 'Exercise'),
('Sad', 'Negative', 'Music', 'Meditation'),
('Excited', 'Positive', 'Achievement', 'Dancing'),
('Anxious', 'Negative', 'Deep Breathing', 'Yoga');

-- Insert Mood Logs (Feels)
INSERT INTO feels (uid, mid, day, scale, cause) VALUES
(1, 1, '2024-02-11', 8, 'Had a great day at work'),
(2, 2, '2024-02-11', 4, 'Missed an important meeting'),
(3, 3, '2024-02-10', 9, 'Got a promotion'),
(1, 4, '2024-02-09', 5, 'Too many deadlines');
