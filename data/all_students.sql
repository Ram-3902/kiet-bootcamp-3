-- all_students.sql — 200 students across 12 intermediate colleges and 8 cities.
-- Build the database:   sqlite3 all_students.db < all_students.sql
--
-- Exact counts (quoted by the material's Expected output blocks):
--   total rows: 200
--
--   per college (SELECT inter_college, COUNT(*) FROM students GROUP BY inter_college ORDER BY inter_college):
--     Aditya Junior College             13
--     Bhashyam Junior College           12
--     Government Junior College          6
--     Krishnaveni Junior College         5
--     NRI Junior College                18
--     Narayana Junior College           49
--     Sasi Junior College                3
--     Sri Chaitanya Junior College      57
--     Sri Gayatri Junior College        14
--     Sri Prakash Junior College         4
--     Tirumala Junior College            9
--     Vignan Junior College             10
--
--   per city (SELECT inter_city, COUNT(*) FROM students GROUP BY inter_city ORDER BY inter_city):
--     Guntur                            30
--     Kakinada                          24
--     Kurnool                            9
--     Nellore                           16
--     Rajahmundry                       20
--     Tirupati                          14
--     Vijayawada                        41
--     Visakhapatnam                     46
--
--   Sri Prakash Junior College appears in exactly one city: Kakinada (4 rows).
--   Kurnool has exactly one college: Narayana Junior College (9 rows).
--
--   college x city (rows):
--     Aditya Junior College: Kakinada 7, Rajahmundry 6
--     Bhashyam Junior College: Visakhapatnam 8, Vijayawada 4
--     Government Junior College: Guntur 2, Kakinada 4
--     Krishnaveni Junior College: Vijayawada 4, Nellore 1
--     NRI Junior College: Vijayawada 10, Guntur 8
--     Narayana Junior College: Visakhapatnam 12, Vijayawada 10, Guntur 6, Rajahmundry 3, Nellore 9, Kurnool 9
--     Sasi Junior College: Guntur 2, Rajahmundry 1
--     Sri Chaitanya Junior College: Visakhapatnam 11, Vijayawada 11, Guntur 4, Kakinada 9, Rajahmundry 10, Nellore 6, Tirupati 6
--     Sri Gayatri Junior College: Visakhapatnam 8, Tirupati 6
--     Sri Prakash Junior College: Kakinada 4
--     Tirumala Junior College: Visakhapatnam 7, Tirupati 2
--     Vignan Junior College: Vijayawada 2, Guntur 8
CREATE TABLE students (
    student_name TEXT,
    inter_college TEXT,
    inter_city TEXT
);

INSERT INTO students VALUES ('Meghana Harini Tummala', 'Sri Chaitanya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Ramesh Anand Achari', 'Sri Gayatri Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Aishwarya Lakshmi Kakarla', 'Tirumala Junior College', 'Tirupati');
INSERT INTO students VALUES ('Gayathri Priya Boddu', 'Government Junior College', 'Kakinada');
INSERT INTO students VALUES ('Sekhar Kumar Chowdary', 'Narayana Junior College', 'Nellore');
INSERT INTO students VALUES ('Sruthi Varshini Boddu', 'Sri Prakash Junior College', 'Kakinada');
INSERT INTO students VALUES ('Navya Lakshmi Goud', 'Bhashyam Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Lavanya Bhavani Achari', 'NRI Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Chandana Sindhu Vasireddy', 'Vignan Junior College', 'Guntur');
INSERT INTO students VALUES ('Murali Babu Boddu', 'Narayana Junior College', 'Nellore');
INSERT INTO students VALUES ('Hemanth Teja Vasireddy', 'Tirumala Junior College', 'Tirupati');
INSERT INTO students VALUES ('Ramya Varshini Pothula', 'Narayana Junior College', 'Guntur');
INSERT INTO students VALUES ('Arun Kiran Annam', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Rohith Chandra Vasireddy', 'Sri Chaitanya Junior College', 'Tirupati');
INSERT INTO students VALUES ('Sneha Sindhu Pothana', 'Tirumala Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Rajesh Prasad Tadi', 'NRI Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Usha Sree Yarlagadda', 'Aditya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Pallavi Kumari Mallela', 'Bhashyam Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Nandini Kumari Annam', 'Narayana Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Harika Devi Jampala', 'Vignan Junior College', 'Guntur');
INSERT INTO students VALUES ('Srilatha Kumari Reddy', 'Sri Gayatri Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Aishwarya Durga Lanka', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Meghana Kumari Gudla', 'Vignan Junior College', 'Guntur');
INSERT INTO students VALUES ('Harika Sree Jampala', 'NRI Junior College', 'Guntur');
INSERT INTO students VALUES ('Hima Durga Reddy', 'Tirumala Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Nandini Devi Peddi', 'Aditya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Santhosh Surya Palla', 'Sri Chaitanya Junior College', 'Guntur');
INSERT INTO students VALUES ('Ravi Rama Ravella', 'Narayana Junior College', 'Kurnool');
INSERT INTO students VALUES ('Varun Surya Dasari', 'NRI Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Srilatha Sai Puli', 'Bhashyam Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Sowmya Rani Setty', 'Bhashyam Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Prakash Vardhan Puli', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Jagadeesh Reddy Sastry', 'Aditya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Siva Reddy Nalluri', 'Sri Gayatri Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Bhargav Charan Chintala', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Mounika Lakshmi Bommu', 'Vignan Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Chaitanya Kumar Uppala', 'Krishnaveni Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Gayathri Sri Gudla', 'Narayana Junior College', 'Kurnool');
INSERT INTO students VALUES ('Rakesh Krishna Setty', 'Aditya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Santhosh Babu Vemula', 'Sri Chaitanya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Yaswanth Krishna Puli', 'Narayana Junior College', 'Nellore');
INSERT INTO students VALUES ('Teja Surya Zilla', 'Narayana Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Bindu Rani Zilla', 'Sri Gayatri Junior College', 'Tirupati');
INSERT INTO students VALUES ('Gowtham Krishna Lanka', 'Aditya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Usha Varshini Bommu', 'Vignan Junior College', 'Guntur');
INSERT INTO students VALUES ('Sai Babu Chowdary', 'Bhashyam Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Eswar Surya Yarlagadda', 'Vignan Junior College', 'Guntur');
INSERT INTO students VALUES ('Vennela Sai Nalluri', 'Krishnaveni Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Sneha Harini Ravella', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Ramesh Kiran Babu', 'Sri Chaitanya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Manasa Sindhu Dasari', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Sindhu Sri Sastry', 'NRI Junior College', 'Guntur');
INSERT INTO students VALUES ('Bhargav Kumar Nadella', 'Sri Chaitanya Junior College', 'Nellore');
INSERT INTO students VALUES ('Tarun Chandra Setty', 'Sri Gayatri Junior College', 'Tirupati');
INSERT INTO students VALUES ('Pooja Harini Tummala', 'NRI Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Bhavani Prasanna Gorantla', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Divya Sai Yarlagadda', 'Narayana Junior College', 'Nellore');
INSERT INTO students VALUES ('Chandana Devi Lanka', 'Sri Chaitanya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Jyothi Sree Zilla', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Balaji Kumar Babu', 'Sri Chaitanya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Teja Reddy Ravella', 'Narayana Junior College', 'Guntur');
INSERT INTO students VALUES ('Nandini Bhavani Babu', 'Bhashyam Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Bindu Varshini Sunkara', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Rohith Kiran Sastry', 'NRI Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Gowtham Naga Vemula', 'Sri Chaitanya Junior College', 'Guntur');
INSERT INTO students VALUES ('Siva Krishna Pothula', 'NRI Junior College', 'Guntur');
INSERT INTO students VALUES ('Deepika Kumari Gupta', 'Sri Chaitanya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Mahesh Vardhan Sharma', 'Narayana Junior College', 'Guntur');
INSERT INTO students VALUES ('Rohith Babu Nadella', 'Sri Chaitanya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Srinivas Rama Chowdary', 'Sri Gayatri Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Chandana Harini Zilla', 'Sri Chaitanya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Nikhil Rama Chowdary', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Aishwarya Kumari Kanchi', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Supriya Varshini Nalluri', 'Narayana Junior College', 'Kurnool');
INSERT INTO students VALUES ('Karthik Chandra Pilla', 'Government Junior College', 'Kakinada');
INSERT INTO students VALUES ('Sandeep Reddy Palla', 'Bhashyam Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Lavanya Prasanna Kumar', 'Narayana Junior College', 'Nellore');
INSERT INTO students VALUES ('Bhargav Sai Prasad', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Meghana Lakshmi Kondapalli', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Anusha Sree Sunkara', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Phani Naga Sharma', 'Narayana Junior College', 'Nellore');
INSERT INTO students VALUES ('Sahithi Sindhu Ravella', 'Tirumala Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Indu Sri Annam', 'Narayana Junior College', 'Nellore');
INSERT INTO students VALUES ('Venkat Chandra Goud', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Pallavi Harini Kumar', 'Sri Chaitanya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Deepak Naga Sastry', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Meghana Harini Kanchi', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Anusha Sree Gudla', 'Krishnaveni Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Vasavi Prasanna Bommu', 'Narayana Junior College', 'Kurnool');
INSERT INTO students VALUES ('Harsha Krishna Naidu', 'Tirumala Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Ramesh Naga Chowdary', 'Sri Chaitanya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Yaswanth Kiran Gupta', 'Bhashyam Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Suresh Anand Rao', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Venkat Satya Kota', 'Narayana Junior College', 'Kurnool');
INSERT INTO students VALUES ('Ravi Kumar Goud', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Pavan Naga Bezawada', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Ashok Rama Sunkara', 'Government Junior College', 'Kakinada');
INSERT INTO students VALUES ('Akhil Krishna Kumar', 'Sri Chaitanya Junior College', 'Nellore');
INSERT INTO students VALUES ('Mahesh Sai Annam', 'Vignan Junior College', 'Guntur');
INSERT INTO students VALUES ('Sruthi Priya Setty', 'Aditya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Indu Durga Varma', 'Tirumala Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Hemanth Babu Meka', 'Narayana Junior College', 'Nellore');
INSERT INTO students VALUES ('Kavya Harini Reddy', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Karthik Chandra Vemula', 'Sri Chaitanya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Vamsi Rama Bommu', 'NRI Junior College', 'Guntur');
INSERT INTO students VALUES ('Pooja Rani Prasad', 'Sri Chaitanya Junior College', 'Tirupati');
INSERT INTO students VALUES ('Divya Sai Chowdary', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Balaji Prasad Vemula', 'Sri Chaitanya Junior College', 'Tirupati');
INSERT INTO students VALUES ('Srinivas Mohan Chintala', 'Bhashyam Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Vijay Surya Gorantla', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Sahithi Harini Gupta', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Mounika Kumari Kondapalli', 'Narayana Junior College', 'Kurnool');
INSERT INTO students VALUES ('Prakash Naga Jampala', 'Sri Chaitanya Junior College', 'Tirupati');
INSERT INTO students VALUES ('Sahithi Devi Meka', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Srilatha Sree Vemula', 'Sri Gayatri Junior College', 'Tirupati');
INSERT INTO students VALUES ('Madhavi Lakshmi Bezawada', 'Sri Chaitanya Junior College', 'Nellore');
INSERT INTO students VALUES ('Navya Rani Kakarla', 'Government Junior College', 'Kakinada');
INSERT INTO students VALUES ('Harsha Kumar Bhimavarapu', 'Sri Gayatri Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Ashok Kumar Gupta', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Vamsi Kumar Varma', 'Bhashyam Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Rakesh Naga Bommu', 'Sri Chaitanya Junior College', 'Tirupati');
INSERT INTO students VALUES ('Sneha Lakshmi Lanka', 'Government Junior College', 'Guntur');
INSERT INTO students VALUES ('Ashok Surya Chowdary', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Santhosh Naga Tummala', 'NRI Junior College', 'Guntur');
INSERT INTO students VALUES ('Akhil Babu Achari', 'Bhashyam Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Pallavi Sindhu Kondapalli', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Sandeep Rama Pothana', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Venkat Chandra Zilla', 'Aditya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Gopi Rama Meka', 'Sri Gayatri Junior College', 'Tirupati');
INSERT INTO students VALUES ('Rohith Naga Pothana', 'Sri Chaitanya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Aishwarya Madhuri Bommu', 'NRI Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Phani Krishna Naidu', 'Sri Chaitanya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Bindu Sri Rao', 'Sri Chaitanya Junior College', 'Guntur');
INSERT INTO students VALUES ('Siva Kiran Gupta', 'Narayana Junior College', 'Guntur');
INSERT INTO students VALUES ('Gayathri Rani Achari', 'Vignan Junior College', 'Guntur');
INSERT INTO students VALUES ('Siva Anand Sastry', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Ashok Sai Bhimavarapu', 'NRI Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Pooja Devi Nadella', 'Sri Gayatri Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Lakshmi Sai Gudla', 'Sri Prakash Junior College', 'Kakinada');
INSERT INTO students VALUES ('Madhavi Varshini Setty', 'Krishnaveni Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Ramesh Reddy Chowdary', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Lavanya Madhuri Chintala', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Ravi Rama Yadav', 'Vignan Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Neelima Sree Dasari', 'Sri Gayatri Junior College', 'Tirupati');
INSERT INTO students VALUES ('Hari Chandra Dasari', 'Tirumala Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Navya Bhavani Vasireddy', 'Aditya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Praveen Sai Vemula', 'Aditya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Praveen Anand Reddy', 'Sri Chaitanya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Rohith Prasad Puli', 'Government Junior College', 'Guntur');
INSERT INTO students VALUES ('Sahithi Madhuri Gupta', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Kishore Charan Vemula', 'NRI Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Eswar Naga Yarlagadda', 'Narayana Junior College', 'Nellore');
INSERT INTO students VALUES ('Kavya Varshini Kumar', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Sruthi Sai Ravella', 'Sasi Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Karthik Naga Nalluri', 'NRI Junior College', 'Guntur');
INSERT INTO students VALUES ('Harika Sindhu Gorantla', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Meghana Sindhu Kakarla', 'Sri Gayatri Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Navya Varshini Zilla', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Dinesh Kumar Jampala', 'Sri Chaitanya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Yamini Sai Sastry', 'Narayana Junior College', 'Kurnool');
INSERT INTO students VALUES ('Kiran Rama Kondapalli', 'Sri Chaitanya Junior College', 'Nellore');
INSERT INTO students VALUES ('Deepak Venkata Vasireddy', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Rajesh Charan Kanchi', 'Narayana Junior College', 'Kurnool');
INSERT INTO students VALUES ('Hemanth Sai Prasad', 'Sri Chaitanya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Tarun Mohan Pothana', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Sruthi Kumari Lanka', 'Sri Chaitanya Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Nagendra Satya Uppala', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Bhavani Priya Nadella', 'Narayana Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Suresh Kumar Naidu', 'Sri Chaitanya Junior College', 'Tirupati');
INSERT INTO students VALUES ('Deepak Krishna Pothana', 'Sri Chaitanya Junior College', 'Nellore');
INSERT INTO students VALUES ('Kavya Sree Murthy', 'Narayana Junior College', 'Guntur');
INSERT INTO students VALUES ('Pavan Kiran Puli', 'Sri Prakash Junior College', 'Kakinada');
INSERT INTO students VALUES ('Bhargav Charan Varma', 'Sri Gayatri Junior College', 'Tirupati');
INSERT INTO students VALUES ('Mounika Sri Tadi', 'Sri Chaitanya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Deepika Kumari Mallela', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Mounika Sindhu Murthy', 'Tirumala Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Kavya Kumari Prasad', 'NRI Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Ashok Krishna Pothana', 'Sri Chaitanya Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Sudheer Chandra Gupta', 'Sasi Junior College', 'Guntur');
INSERT INTO students VALUES ('Tejaswini Harini Achari', 'Sasi Junior College', 'Guntur');
INSERT INTO students VALUES ('Varun Krishna Setty', 'Bhashyam Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Sirisha Durga Lanka', 'Narayana Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Yamini Lakshmi Pilla', 'NRI Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Nikhil Chandra Chowdary', 'Narayana Junior College', 'Guntur');
INSERT INTO students VALUES ('Praveen Sai Reddy', 'Sri Gayatri Junior College', 'Visakhapatnam');
INSERT INTO students VALUES ('Vamsi Vardhan Murthy', 'Sri Chaitanya Junior College', 'Nellore');
INSERT INTO students VALUES ('Navya Bhavani Mallela', 'Sri Chaitanya Junior College', 'Rajahmundry');
INSERT INTO students VALUES ('Sirisha Rani Achari', 'Aditya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Chandana Rani Bezawada', 'Sri Chaitanya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Naveen Teja Murthy', 'Aditya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Anusha Sree Sastry', 'Sri Chaitanya Junior College', 'Guntur');
INSERT INTO students VALUES ('Srilatha Sai Vemula', 'Narayana Junior College', 'Vijayawada');
INSERT INTO students VALUES ('Pradeep Babu Jampala', 'Aditya Junior College', 'Kakinada');
INSERT INTO students VALUES ('Supriya Priya Babu', 'Vignan Junior College', 'Guntur');
INSERT INTO students VALUES ('Gowtham Prasad Dasari', 'NRI Junior College', 'Guntur');
INSERT INTO students VALUES ('Mounika Rani Kondapalli', 'NRI Junior College', 'Guntur');
INSERT INTO students VALUES ('Deepak Satya Tummala', 'Krishnaveni Junior College', 'Nellore');
INSERT INTO students VALUES ('Arun Rama Sunkara', 'Narayana Junior College', 'Kurnool');
INSERT INTO students VALUES ('Rohith Reddy Boddu', 'Sri Prakash Junior College', 'Kakinada');
INSERT INTO students VALUES ('Gowtham Vardhan Yadav', 'Aditya Junior College', 'Kakinada');
