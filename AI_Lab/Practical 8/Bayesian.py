from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
student_performance_model = BayesianNetwork([
    ('Prior Knowledge', 'Study Hours'),
    ('Prior Knowledge', 'Pass Exam'),
    ('Study Hours', 'Pass Exam'),
    ('Class Attendance', 'Pass Exam')
])

# Define the CPDs
cpd_prior_knowledge = TabularCPD(
    variable='Prior Knowledge', variable_card=2,
    values=[[0.7], [0.3]]  # P(Prior Knowledge = 0), P(Prior Knowledge = 1)
)

cpd_study_hours = TabularCPD(
    variable='Study Hours', variable_card=2,
    values=[[0.9, 0.4], [0.1, 0.6]],  # P(Study Hours | Prior Knowledge)
    evidence=['Prior Knowledge'], evidence_card=[2]
)

cpd_class_attendance = TabularCPD(
    variable='Class Attendance', variable_card=2,
    values=[[0.8], [0.2]]  # P(Class Attendance = 0), P(Class Attendance = 1)
)

cpd_pass_exam = TabularCPD(
    variable='Pass Exam', variable_card=2,
    values=[
        [0.95, 0.8, 0.7, 0.2, 0.9, 0.7, 0.6, 0.1],  # P(Pass Exam = 0 | Study Hours, Class Attendance, Prior Knowledge)
        [0.05, 0.2, 0.3, 0.8, 0.1, 0.3, 0.4, 0.9]   # P(Pass Exam = 1 | Study Hours, Class Attendance, Prior Knowledge)
    ],
    evidence=['Study Hours', 'Class Attendance', 'Prior Knowledge'], evidence_card=[2, 2, 2]
)

# Add CPDs to the model
student_performance_model.add_cpds(
    cpd_prior_knowledge, 
    cpd_study_hours, 
    cpd_class_attendance, 
    cpd_pass_exam
)

# Check if the model is valid
assert student_performance_model.check_model()

# Perform inference using Variable Elimination
infer = VariableElimination(student_performance_model)

# Query 1: Probability of passing the exam given class attendance and study hours
result = infer.query(variables=['Pass Exam'], evidence={'Class Attendance': 1, 'Study Hours': 1})
print("Probability of passing the exam (attended class, studied):")
print(result)

# Query 2: Probability of passing the exam given weak prior knowledge and study hours
result = infer.query(variables=['Pass Exam'], evidence={'Prior Knowledge': 0, 'Study Hours': 1})
print("Probability of passing the exam (weak prior knowledge, studied):")
print(result)



'''FUNCTION DefineBayesianNetwork():
    model ← NEW BayesianNetwork([
        ('Prior Knowledge', 'Study Hours'),
        ('Prior Knowledge', 'Pass Exam'),
        ('Study Hours', 'Pass Exam'),
        ('Class Attendance', 'Pass Exam')
    ])
    
    // Define CPDs
    model.ADD_CPDS(
        NEW TabularCPD('Prior Knowledge', 2, [[0.7], [0.3]]),
        NEW TabularCPD('Study Hours', 2, [[0.9, 0.4], [0.1, 0.6]], ['Prior Knowledge'], [2]),
        NEW TabularCPD('Class Attendance', 2, [[0.8], [0.2]]),
        NEW TabularCPD('Pass Exam', 2, [
            [0.95, 0.8, 0.7, 0.2, 0.9, 0.7, 0.6, 0.1],
            [0.05, 0.2, 0.3, 0.8, 0.1, 0.3, 0.4, 0.9]
        ], ['Study Hours', 'Class Attendance', 'Prior Knowledge'], [2, 2, 2])
    )

    IF NOT model.CHECK_MODEL() THEN THROW Error("Invalid Model")

    RETURN model


FUNCTION PerformInference(model):
    infer ← NEW VariableElimination(model)
    PRINT "Probability (attended class, studied):", infer.QUERY(['Pass Exam'], {'Class Attendance': 1, 'Study Hours': 1})
    PRINT "Probability (weak prior knowledge, studied):", infer.QUERY(['Pass Exam'], {'Prior Knowledge': 0, 'Study Hours': 1})


FUNCTION Main():
    PerformInference(DefineBayesianNetwork())

Main()
'''