"""
This module converts javacode to python code1
"""
import os

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
                    "content": "Given the Java class, convert that code1 to python keeping the comments, using snake_case methods and local imports. Keep the class name CamelCase,"
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

    subdir = """/Documents/Git/GitHub/TC57CIM/py/IEC62325/MarketOperations/ReferenceData/"""
    directory_path = f"{os.path.expanduser('~')}{subdir}"
    directory_path += '/' if not directory_path.endswith('/') else ""
    try:
        for filename in os.listdir(directory_path):
            if filename.endswith(".java"):
                file_path = os.path.join(directory_path, filename)
                if os.path.isfile(file_path):
                    print(f"#################################################\nOpening {filename} for conversion")
                    file_size = os.path.getsize(file_path)
                    with open(directory_path + filename, 'r') as file:
                        code = file.readlines()

                    # remove all imports here
                    REMOVE_IMPORTS = False
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
                        code_string.encode('ascii')
                    except UnicodeEncodeError:
                        print("... Removing non ascii characters")
                        code_string = ''.join([i if ord(i) < 128 else ' ' for i in code_string])
                        # raise ValueError('code1 is not ASCII')
                    encoded_text = urllib.parse.quote(code_string)
                    converted_code = convert_code(encoded_text)
                    if converted_code:
                        # get rid of the leading and trailing python quoting
                        converted_code = converted_code.replace("```python", f"# Converted by an OPENAI API call using model: {MODEL_NAME}")
                        converted_code = converted_code[:-3] if converted_code[-3:] == "```" else converted_code

                        output_filename = directory_path + filename.replace('java', 'py')
                        print(f"{output_filename} written")
                        with open(output_filename, 'w') as f:
                            f.write(converted_code)
                        # print(converted_code)
                    else:
                        print(f"{filename} conversion failed")
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")




