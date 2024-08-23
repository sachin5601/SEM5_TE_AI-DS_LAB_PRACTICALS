-- Set the default database
USE COLLEGE;

-- SLICE: Filtering data based on a specific department (AI&DS)
SELECT 
    fe.enrollment_id, 
    st.student_name, 
    c.course_name, 
    i.instructor_name, 
    s.semester_name, 
    fe.grade
FROM 
    fact_enrollments fe
JOIN 
    students st ON fe.student_id = st.student_id
JOIN 
    courses c ON fe.course_id = c.course_id
JOIN 
    instructors i ON fe.instructor_id = i.instructor_id
JOIN 
    semesters s ON fe.semester_id = s.semester_id
JOIN 
    departments d ON st.department_id = d.department_id
WHERE 
    d.department_name = 'AI&DS';

-- DICE: Filtering data for a specific course and grade (Introduction to AI, Grade A)
SELECT 
    fe.enrollment_id, 
    st.student_name, 
    c.course_name, 
    fe.grade, 
    fe.enrollment_date
FROM 
    fact_enrollments fe
JOIN 
    students st ON fe.student_id = st.student_id
JOIN 
    courses c ON fe.course_id = c.course_id
WHERE 
    c.course_name = 'Introduction to AI' 
    AND fe.grade = 'A';

-- ROLLUP: Aggregating data by department and semester
SELECT 
    d.department_name, 
    s.semester_name, 
    COUNT(fe.enrollment_id) AS total_enrollments
FROM 
    fact_enrollments fe
JOIN 
    students st ON fe.student_id = st.student_id
JOIN 
    departments d ON st.department_id = d.department_id
JOIN 
    semesters s ON fe.semester_id = s.semester_id
GROUP BY 
    d.department_name, s.semester_name
WITH ROLLUP;

-- DRILLDOWN: Viewing detailed enrollment data for a specific semester (Fall 2023)
SELECT 
    fe.enrollment_id, 
    st.student_name, 
    c.course_name, 
    i.instructor_name, 
    s.semester_name, 
    fe.grade
FROM 
    fact_enrollments fe
JOIN 
    students st ON fe.student_id = st.student_id
JOIN 
    courses c ON fe.course_id = c.course_id
JOIN 
    instructors i ON fe.instructor_id = i.instructor_id
JOIN 
    semesters s ON fe.semester_id = s.semester_id
WHERE 
    s.semester_name = 'Fall 2023';

-- PIVOT: Simulating a pivot table by converting rows into columns for grades
SELECT 
    d.department_name,
    SUM(CASE WHEN fe.grade = 'A' THEN 1 ELSE 0 END) AS grade_A,
    SUM(CASE WHEN fe.grade = 'B+' THEN 1 ELSE 0 END) AS grade_B_plus,
    SUM(CASE WHEN fe.grade = 'A-' THEN 1 ELSE 0 END) AS grade_A_minus
FROM 
    fact_enrollments fe
JOIN 
    students st ON fe.student_id = st.student_id
JOIN 
    departments d ON st.department_id = d.department_id
GROUP BY 
    d.department_name;
