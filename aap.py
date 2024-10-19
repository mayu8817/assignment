# node.py
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left            # Reference to left child
        self.right = right          # Reference to right child (for operators)
        self.value = value          # Optional value for operand nodes


# rule_engine.py
import json

def parse_rule_string(rule_string):
    # Pseudo-code for parsing the rule string
    # This function should convert the rule string into an AST
    # For simplicity, we will assume a basic parsing logic here
    # Implement a full parser as needed
    # This is a placeholder for actual parsing logic
    # You can use libraries like `pyparsing` for complex parsing
    pass

def create_rule(rule_string):
    try:
        root = parse_rule_string(rule_string)  # Implement this parsing logic
        return root
    except Exception as e:
        raise ValueError(f"Invalid rule string: {rule_string}. Error: {e}")

def combine_ast(ast1, ast2):
    # Combine two ASTs. This is a placeholder for the actual logic.
    # You may want to implement a more sophisticated combining strategy.
    return Node("operator", ast1, ast2, "AND")  # Example combining with AND

def combine_rules(rules):
    combined_root = None
    for rule in rules:
        rule_ast = create_rule(rule)
        if combined_root is None:
            combined_root = rule_ast
        else:
            combined_root = combine_ast(combined_root, rule_ast)
    return combined_root

def evaluate_operand(operand_node, data):
    # Implement the logic to evaluate operand nodes
    # Example for comparison
    if operand_node.value.startswith("age"):
        return data["age"] > int(operand_node.value.split(">")[1].strip())
    elif operand_node.value.startswith("salary"):
        return data["salary"] > int(operand_node.value.split(">")[1].strip())
    # Add more comparisons as needed
    return False

def evaluate_operator(operator, left_result, right_result):
    if operator == "AND":
        return left_result and right_result
    elif operator == "OR":
        return left_result or right_result
    return False

def evaluate_rule(ast, data):
    if ast.node_type == "operand":
        return evaluate_operand(ast, data)
    elif ast.node_type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        return evaluate_operator(ast.value, left_result, right_result)

# Example usage
if __name__ == "__main__":
    # Sample rules
    rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    
    # Create individual rules
    ast1 = create_rule(rule1)
    ast2 = create_rule(rule2)
    
    # Combine rules
    combined_ast = combine_rules([rule1, rule2])
    
    # Sample data for evaluation
    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    
    # Evaluate the combined rule
    result = evaluate_rule(combined_ast, data)
    print(result)  # Expected output: True or False based on the rules
