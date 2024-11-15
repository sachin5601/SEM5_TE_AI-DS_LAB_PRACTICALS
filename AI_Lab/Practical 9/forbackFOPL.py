def forward_chaining(knowledge_base, facts):
    new_facts = set(facts)  # Initialize new_facts with the known facts
    changed = True
    
    while changed:
        changed = False  # Reset the changed flag
        
        for premise, conclusion in knowledge_base:
            # Check if all premises are satisfied
            if premise.issubset(new_facts) and conclusion not in new_facts:
                new_facts.add(conclusion)  # Add the conclusion as a new fact
                changed = True  # Indicate that facts have changed
                
    return new_facts

# Knowledge base defined as a list of rules (premises and conclusions)
knowledge_base = [
    ({"P(a)"}, "Q(a)"),
    ({"P(x)"}, "Q(x)"),  # This rule is more of a generalization and may need a different approach
    ({"Q(y)"}, "R(y)"),
    ({"¬R(b)"}, ""),  # A rule that doesn't add any conclusion; can be ignored
    ({"R(z)"}, "S(z)")
]

# Initial known facts
facts = {"P(a)"}
goal = "¬P(b)"  # The goal to check

# Run forward chaining
result = forward_chaining(knowledge_base, facts)

# Print whether the goal is achieved
print(goal in result)


def backward_chaining(knowledge_base, goal, facts):
    # Check if the goal is already known
    if goal in facts:
        return True

    # Iterate through each rule in the knowledge base
    for premise, conclusion in knowledge_base:
        # Check if the conclusion matches the goal
        if conclusion == goal:
            # Recursively check if all premises are true
            if all(backward_chaining(knowledge_base, p, facts) for p in premise):
                return True

    return False

# Define the knowledge base as a list of rules (premises and conclusions)
knowledge_base = [
    ({"P(a)"}, "Q(a)"),
    ({"P(b)"}, "Q(b)"),
    ({"Q(y)"}, "R(y)"),
    ({"R(z)"}, "S(z)")
]

# Initial known facts
facts = {"P(a)", "¬R(b)"}  # Note: '¬R(b)' is treated as a string here
goal = "¬P(b)"  # The goal to check

# Run backward chaining
result = backward_chaining(knowledge_base, goal, facts)

# Print whether the goal can be achieved
print(result)



def resolve(clause1, clause2):
    """Resolve two clauses and return their resolvents."""
    resolvents = []
    for literal in clause1:
        if '¬' + literal in clause2:
            # Create a new clause by removing the resolved literals
            new_clause = (clause1 - {literal}) | (clause2 - {'¬' + literal})
            resolvents.append(new_clause)
    return resolvents

def resolution(clauses, goal):
    """Perform resolution to determine if the goal can be derived from the clauses."""
    # Negate the goal and add it to the clauses
    negated_goal = {"¬" + goal}
    clauses.append(negated_goal)
    
    while True:
        new_clauses = set(tuple(sorted(clause)) for clause in clauses)
        for i, clause1 in enumerate(clauses):
            for j, clause2 in enumerate(clauses):
                if i != j:  # Avoid resolving the same clause with itself
                    resolvents = resolve(clause1, clause2)
                    for resolvent in resolvents:
                        if not resolvent:  # Found an empty clause, which means the goal is proven
                            return True
                        new_clauses.add(tuple(sorted(resolvent)))
        
        # If no new clauses were added, we stop
        if new_clauses == set(tuple(sorted(clause)) for clause in clauses):
            break
        clauses = [set(clause) for clause in new_clauses]  # Update clauses with new clauses
    
    return False  # The goal cannot be derived

# Example clauses and goal
clauses = [{"P(" + str(i) + ")" for i in range(1, 3)}, {"¬P(2)"}, {"Q(x)"}, {"¬R(b)"}]
goal = "P(2)"
result = resolution(clauses, goal)
print(result)  # Expected output: True or False based on resolution





'''FUNCTION ForwardChaining(knowledge_base, facts):
    new_facts ← SET OF facts  // Initialize new_facts with the known facts
    changed ← TRUE
    
    WHILE changed IS TRUE:
        changed ← FALSE  // Reset the changed flag
        
        FOR each (premise, conclusion) IN knowledge_base:
            IF premise IS SUBSET OF new_facts AND conclusion NOT IN new_facts THEN:
                ADD conclusion TO new_facts  // Add the conclusion as a new fact
                changed ← TRUE  // Indicate that facts have changed
                
    RETURN new_facts
 
 
 
 FUNCTION BackwardChaining(knowledge_base, goal, facts):
    // Check if the goal is already known
    IF goal IN facts THEN:
        RETURN TRUE

    // Iterate through each rule in the knowledge base
    FOR each (premise, conclusion) IN knowledge_base:
        // Check if the conclusion matches the goal
        IF conclusion = goal THEN:
            // Recursively check if all premises are true
            IF ALL(Premises IN premise ARE TRUE using BackwardChaining) THEN:
                RETURN TRUE

    RETURN FALSE  // Goal cannot be proven




FUNCTION Resolve(clause1, clause2):
    resolvents ← EMPTY SET  // Initialize resolvents
    FOR each literal IN clause1:
        IF '¬' + literal IN clause2 THEN:
            // Create a new clause by removing the resolved literals
            new_clause ← (clause1 - {literal}) UNION (clause2 - {'¬' + literal})
            ADD new_clause TO resolvents
    RETURN resolvents

FUNCTION Resolution(clauses, goal):
    // Negate the goal and add it to the clauses
    negated_goal ← {"¬" + goal}
    ADD negated_goal TO clauses
    
    WHILE TRUE:
        new_clauses ← EMPTY SET  // Initialize new clauses
        FOR i FROM 0 TO LENGTH(clauses) - 1:
            FOR j FROM 0 TO LENGTH(clauses) - 1:
                IF i ≠ j THEN:  // Avoid resolving the same clause with itself
                    resolvents ← Resolve(clauses[i], clauses[j])
                    FOR each resolvent IN resolvents:
                        IF resolvent IS EMPTY THEN:
                            RETURN TRUE  // Found an empty clause
                        ADD tuple(SORT(resolvent)) TO new_clauses  // Add sorted resolvent
            
        // If no new clauses were added, we stop
        IF new_clauses = SET OF (SORTed clauses) THEN:
            BREAK
        
        clauses ← SET OF (new_clauses)  // Update clauses with new clauses
    
    RETURN FALSE  // The goal cannot be derived
'''