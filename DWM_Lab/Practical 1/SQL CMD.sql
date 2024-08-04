

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender CHAR(1) NOT NULL,
    address VARCHAR(255) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_description TEXT NOT NULL,
    credits INT NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE instructors (
    instructor_id INT PRIMARY KEY,
    instructor_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE semesters (
    semester_id INT PRIMARY KEY,
    semester_name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE fact_enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    instructor_id INT NOT NULL,
    semester_id INT NOT NULL,
    grade VARCHAR(2) NOT NULL,
    enrollment_date DATE NOT NULL,
    enrollment_time TIME NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    FOREIGN KEY (semester_id) REFERENCES semesters(semester_id)
);


INSERT INTO departments (department_id, department_name) VALUES
(1, 'AI&DS'),
(2, 'COMPS'),
(3, 'IT'),
(4, 'IOT'),
(5, 'EXTC');

-- Students
INSERT INTO students (student_id, student_name, date_of_birth, gender, address, contact_number, email, department_id) VALUES
(1, 'Alice Johnson', '2000-01-15', 'F', '123 Main St, Cityville', '123-456-7890', 'alice.johnson@acpce.ac.in', 1),
(2, 'Bob Smith', '1999-06-23', 'M', '456 Elm St, Townsville', '987-654-3210', 'bob.smith@acpce.ac.in', 2),
(3, 'Charlie Brown', '2001-08-30', 'M', '789 Oak St, Villagetown', '555-123-4567', 'charlie.brown@acpce.ac.in', 3);

-- Courses
INSERT INTO courses (course_id, course_name, course_description, credits, department_id) VALUES
(1, 'Introduction to AI', 'Basics of Artificial Intelligence', 4, 1),
(2, 'Data Structures', 'Fundamentals of Data Structures', 3, 2),
(3, 'Database Systems', 'Introduction to Database Systems', 3, 3);


INSERT INTO instructors (instructor_id, instructor_name, email, department_id) VALUES
(1, 'Dr. Sarah Lee', 'sarah.lee@acpce.ac.in', 1),
(2, 'Prof. James Brown', 'james.brown@acpce.ac.in', 2),
(3, 'Dr. Emily Davis', 'emily.davis@acpce.ac.in', 3);


INSERT INTO semesters (semester_id, semester_name, start_date, end_date) VALUES
(1, 'Fall 2023', '2023-08-01', '2023-12-15'),
(2, 'Spring 2024', '2024-01-15', '2024-05-15');


INSERT INTO fact_enrollments (enrollment_id, student_id, course_id, instructor_id, semester_id, grade, enrollment_date, enrollment_time) VALUES
(1, 1, 1, 1, 1, 'A', '2023-08-05', '10:00:00'),
(2, 2, 2, 2, 1, 'B+', '2023-08-10', '11:00:00'),
(3, 3, 3, 3, 2, 'A-', '2024-01-20', '09:00:00');


SELECT * FROM departments;


SELECT * FROM students;


SELECT * FROM courses;

-- Instructors Table
SELECT * FROM instructors;


SELECT * FROM semesters;


SELECT * FROM fact_enrollments;
