"""
This module converts javacode to python code1
"""
import os
from datetime import datetime
from pathlib import Path

from openai import OpenAI
# Replace 'YOUR_API_KEY' (as an ENV variable) with your actual GPT-3 API key

import urllib.parse
import re


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    # api_key=api_key,
)
MODEL_NAME = "gpt-3.5-turbo-1106"

def remove_multiline_comments(code1):
    """
    Removes all multiline comments from the given code1.
    """

    # Create a regular expression that matches multiline comments.
    comment_regex = re.compile(r'/\*(?:[^*]+|\*(?!/)|[^*])*\*/')

    # Remove all multiline comments from the code1.
    return comment_regex.sub('', code1)


def remove_block_comments(code2):
    """
    Removes all block comments from Java code1.
    block comments are start with //
    Args:
      code2: The Java code1 to remove comments from.

    Returns:
      The Java code1 with all comments removed.
    """

    # Create a regular expression to match block comments.
    pattern = re.compile(r'/\*.*?\*/')

    # Remove all block comments from the code1.
    return re.sub(pattern, '', code2)


def convert_code(code_snippet):
    """
    Convert the given code1 snippet using GPT-3.
    """
    # Call the GPT-3 API to generate the converted code1
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """In this session you will be converting Java classes to python. 
                                Use snake_case attributes including the comments and, instead of the initial value of None, use the java type as a class method call. 
                                Use the Typical values as an argument to the Java class method call. 
                                assume the attributes are initialized to the class type as a method call.
                                include the comments as inline comments for the code1 when you convert it.
                                add the super().__init__() call right after the __init__ method definition.
                                add the comments.
                                add them as single line comments to the end of the assignment.
                                add the class comments"""
                    # "content": "Given this Java class, convert this code1 to python, using snake_case methods and "
                    #            "attributes, include the original comments, and add python typing to the python class. "
                    #            "Keep the class name CamelCase. Keep the imports in their original form."
                },
                {
                    "role": "user",
                    "content": code_snippet
                }
            ],
            model=MODEL_NAME,
            # model="code1-davinci-002",
            # model="gpt-3.5-turbo",
            # max_tokens=500,  # Adjust as needed
            # temperature=0.7  # Adjust the temperature for creativity
        )

        # Extract and return the generated code1 from the response

        converted_code1 = chat_completion.choices[0].message.content
    except Exception as e1:
        print(e1)
        converted_code1 = ''
    return converted_code1


MAX_TOKENS = 10000  # Maximum number of tokens that can be used with the OPENAI model (model dependant)


if __name__ == "__main__":
    directory_path = f"{os.path.expanduser('~')}/Documents/Git/GitHub/TC57CIM/py/IEC61970/InfIEC61970/SCADA_EMS/Messages/MeasValueConfigurationReply/"
    output_path = f"{directory_path}/Converted/"
    try:
        starting_time = datetime.ctime(datetime.now())
        for filename in os.listdir(directory_path):
            if filename.endswith(".java"):
                file_path = os.path.join(directory_path, filename)
                if os.path.isfile(file_path):
                    print(f"#######\nOpening {filename} for conversion")
                    file_size = os.path.getsize(file_path)
                    with open(directory_path + filename, 'r') as file:
                        code = file.readlines()

                    # remove all imports here
                    REMOVE_IMPORTS = True
                    if REMOVE_IMPORTS:
                        clean_code = []

                        for line in code:
                            if not line.find('import') == 0:
                                clean_code.append(line)
                    else:
                        clean_code = code
                    # create a blob of code1
                    code_string = '\n'.join(clean_code)
                    # remove comments
                    if file_size > MAX_TOKENS:
                        code_string = remove_block_comments(code_string)
                        code_string = remove_multiline_comments(code_string)
                    print(f"File: {filename}, Orig size: {file_size}, cleaned size: {len(code_string)} (bytes)")

                    # URL-encode the text
                    try:
                        code_string.encode('ascii', 'ignore')
                    except UnicodeDecodeError:
                        raise ValueError('code1 is not ASCII')
                    encoded_text = urllib.parse.quote(code_string)
                    converted_code = convert_code(encoded_text)
                    if converted_code:
                        # get rid of the leading and trailing python quoting

                        converted_code = converted_code.replace("```python", f"# Converted by an OPENAI API call using model: {MODEL_NAME} on {starting_time}")
                        converted_code = converted_code[:-3] if converted_code[-3:] == "```" else converted_code
                        converted_code = converted_code.replace("```", '"""')
                        new_filename = filename.replace('java', 'py')
                        output_filename = output_path + new_filename
                        print(f"Done with {new_filename}: {output_filename}")
                        Path(output_path).mkdir(parents=True, exist_ok=True)
                        with open(output_filename, 'w') as f:
                            f.write(converted_code)
                        # print(converted_code)
                    else:
                        print(f"{filename} conversion failed")
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")




