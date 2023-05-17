import ast
import openai
openai.api_key = 'ENTER_API_KEY'

def generate_docstring(func_def):
    """This function generates a docstring for a given function definition using the numpydoc format. It takes a function definition as an input parameter and returns the same function definition with the generated docstring inserted at the beginning. The docstring includes a summary, description, parameters, returns, and examples sections that adhere to the numpydoc format and conventions."""
    func_name = func_def.name
    args = func_def.args.args
    arg_names = [arg.arg for arg in args]
    arg_string = ', '.join(arg_names)
    prompt = f"Write a docstring for the '{func_name}' function that follows the numpydoc format. Ensure the docstring includes the following sections:\n\n1. Summary: Provide a concise summary of the function's purpose and functionality.\n\n2. Description: Describe in detail what the function does, its behavior, and any important considerations.\n\n3. Parameters: List and describe the input parameters of the function, including their types, names, and any required or optional status.\n\n4. Returns: Explain the return value(s) of the function, including their types and any special meaning.\n\n5. Examples: Provide one or more usage examples that demonstrate how to call the function and its expected output.\n\nRemember to adhere to the numpydoc format and conventions throughout the docstring.\n\nFunction Definition:\n{ast.unparse(func_def)}\n\nDocstring:\n\nSummary:\n\nDescription:\n\nParameters:\n\nReturns:\n\nExamples:\n"
    response = openai.Completion.create(engine='text-davinci-003', prompt=prompt, temperature=0, max_tokens=1000, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=['\n\n'])
    docstring = response.choices[0].text.strip()
    func_def.body.insert(0, ast.Expr(ast.Str(docstring)))
    return func_def

def add_docstrings_to_file(filename):
    '''"""
This function adds docstrings to a given file using the numpydoc format. It takes a filename as an input parameter and parses the file using the ast module. It then finds all function definitions in the file and generates a docstring for each one using the numpydoc format. Finally, it writes the new docstrings to the file.'''
    with open(filename) as f:
        tree = ast.parse(f.read())
    func_defs = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    new_func_defs = [generate_docstring(func_def) for func_def in func_defs]
    for (i, node) in enumerate(tree.body):
        if isinstance(node, ast.FunctionDef):
            tree.body[i] = new_func_defs.pop(0)
    with open(filename, 'w') as f:
        f.write(ast.unparse(tree))

def main():
    '''"""Main function to add docstrings to a Python file.'''
    filename = input('Enter the absolute path of the Python file: ')
    add_docstrings_to_file(filename)
    print('done')
if __name__ == '__main__':
    main()
