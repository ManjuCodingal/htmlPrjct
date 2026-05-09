DROP TABLE IF EXISTS hacker_news;
CREATE TABLE IF NOT EXISTS hacker_news(
    id INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(100),
    points INT,
    comments_count INT,
    post_type VARCHAR(50),
    created_at TIMESTAMP
);

INSERT INTO hacker_news(id, title, author, points, comments_count, post_type, created_at) VALUES
(1, 'Understanding AI Agents', 'alice', 320, 120, 'top', '2026-05-04 10:00:00'),
(2, 'Show HN', 'bob', 210, 85, 'show', '2026-05-04 09:30:00'),
(3, 'Ask HN', 'charlie', 150, 200, 'new', '2026-05-04 08:45:00'),
(4, 'New Javascript Framework Released', 'david', 95, NULL, 'new', '2026-05-04 07:20:00'),
(5, 'Startup for AI research', 'blessy', 400, 180, 'top', '2026-05-04 06:10:00');

SELECT COUNT(points) AS points_count
FROM hacker_news;

SELECT * FROM hacker_news
ORDER BY points DESC;

SELECT * FROM hacker_news
ORDER BY comments_count DESC;

SELECT * FROM hacker_news
WHERE author LIKE 'b%';