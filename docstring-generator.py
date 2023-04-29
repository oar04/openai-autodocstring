import ast
import openai
openai.api_key = 'ENTER_API_KEY'

def generate_docstring(func_def):
    '''"""
Generate a docstring for a given function definition using OpenAI's Completion API.'''
    func_name = func_def.name
    args = func_def.args.args
    arg_names = [arg.arg for arg in args]
    arg_string = ', '.join(arg_names)
    prompt = f"Write a docstring for the '{func_name}' function that follows the numpydoc format. Include the following sections: \n\n1. Summary\n\n2. Description\n\n3. Parameters\n\n4. Returns\n\n5. Examples\n\nFunction Definition:\n{ast.unparse(func_def)}\n\nDocstring:"
    response = openai.Completion.create(engine='text-davinci-003', prompt=prompt, temperature=0, max_tokens=1000, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=['\n\n'])
    docstring = response.choices[0].text.strip()
    func_def.body.insert(0, ast.Expr(ast.Str(docstring)))
    return func_def

def add_docstrings_to_file(filename):
    '''"""
Summary
-------
Adds docstrings to a given file.'''
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
    '''"""
Summary:
This function prompts the user for a file path and calls the add_docstrings_to_file() function to add docstrings to the file.'''
    filename = input('Enter the absolute path of the Python file: ')
    add_docstrings_to_file(filename)
if __name__ == '__main__':
    main()
