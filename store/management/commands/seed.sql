-- Insert data into store_genre
INSERT INTO store_genre
  (id, name)
VALUES
  (1, 'Motivational & Non-Fictional'),
  (2, 'Fantasy'),
  (3, 'Science Fiction'),
  (4, 'Dystopian'),
  (5, 'Action & Adventure'),
  (6, 'Mystery'),
  (7, 'Horror'),
  (8, 'Thriller & Suspense'),
  (9, 'Historical Fiction'),
  (10, 'Romance'),
  (11, 'Women’s Fiction'),
  (12, 'Dystopian'),
  (13, 'Mystery'),
  (14, 'Horror'),
  (15, 'Action & Adventure'),
  (16, 'Mystery'),
  (17, 'Horror'),
  (18, 'Thriller & Suspense'),
  (19, 'Historical Fiction'),
  (20, 'Contemporary Fiction'),
  (21, 'Literary Fiction'),
  (22, 'Magical Realism'),
  (23, 'Graphic Novel'),
  (24, 'Short Story'),
  (25, 'Children’s'),
  (26, 'Memoir & Autobiography'),
  (27, 'Biography'),
  (28, 'Food & Drink'),
  (29, 'Art & Photography'),
  (30, 'History'),
  (31, 'Travel'),
  (32, 'True Crime'),
  (33, 'Humor'),
  (34, 'Religion & Spirituality'),
  (35, 'Science & Technology'),
  (36, 'Parenting & Families'),
  (37, 'Humanities & Social Sciences'),
  (38, 'Tragedy'),
  (39, 'Finance & Management');

-- Insert data into store_book
INSERT INTO store_book
  (id, ISBN, title, number_in_stock, daily_rate, genre_id, description, date_created, last_updated, unit_price)
VALUES
  (1, '9780141012292', 'King Lear', 5, 1.5, 38, 'King Lear is a tragedy written by William Shakespeare...', '2021-07-10 02:11:31', '2024-10-19 23:47:27.333629', 120),
  (2, '1853260185', 'Testing & Engineering', 4, 2.0, 39, 'Optimize the effectiveness of your business...', '2021-07-10 02:20:43.574110', '2024-10-19 23:47:27.333629', 220),
  (3, '9789147107483', 'Affärsmannaskap för ingenjörer, jurister och alla andra specialister', 1, 5.0, 39, 'I Affärsmannaskap har Rolf Laurelli...', '2021-07-10 02:23:23.819423', '2024-10-19 23:47:27.333629', 220),
  (4, '9780345816023', 'Hamlet', 10, 3.0, 38, 'The Tragedy of Hamlet, Prince of Denmark...', '2021-07-10 02:28:09.883451', '2024-10-21 21:53:45.334125', 100),
  (5, '9781400222247', 'Negotiation', 3, 1.99, 39, 'Tracy teaches readers how to utilize...', '2021-07-10 02:29:16.726227', '2024-10-21 21:54:03.884469', 60),
  (6, '9781439199190', 'How to Win Friends and Influence People', 5, 5.0, 39, 'Dale Carnegie had an understanding of human nature...', '2021-07-10 02:30:15.433202', '2024-10-19 23:47:27.333629', 220),
  (7, '9780814439098', 'The aglie of agile', 4, 3.95, 39, 'The Age of Agile helps readers master...', '2021-07-10 02:34:26.107435', '2024-10-21 21:53:55.959611', 90),
  (8, '1853260185', 'Othello', 5, 2.0, 38, 'An intense drama of love, deception, jealousy...', '2021-07-10 02:20:43.574110', '2024-10-21 21:51:58.947483', 270);
