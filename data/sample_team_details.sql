-- A 4-student example team: 2 colleges, 2 cities.
-- Every Expected output in the material uses exactly these rows.
-- Use this only if you skipped Stage 1:
--     sqlite3 team_details.db < sample_team_details.sql
CREATE TABLE students (
    student_name TEXT,
    inter_college TEXT,
    inter_city TEXT
);

INSERT INTO students VALUES ('Ravi Teja Kanchi', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Lakshmi Prasanna Gudla', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Sai Kiran Bommu', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Divya Sree Pothula', 'Narayana Junior College', 'Vijayawada');
