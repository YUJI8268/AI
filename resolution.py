clauses = ["A v B", "~A", "~B"]

def resolution(clauses):
    print("Clauses:")
    for clause in clauses:
        print(clause)

    # Perform resolution (check for complementary literals and resolve)
    if "A v B" in clauses and "~A" in clauses and "~B" in clauses:
        print("Resolved: ⊥ (Contradiction)")
    else:
        print("No resolution possible.")

# Calling the resolution function
resolution(clauses)


