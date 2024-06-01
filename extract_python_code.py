import os
import re

def extract_python_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return code

def extract_and_write_python_code(readme_path, output_dir):
    # ファイルを読み込む
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Pythonコードを抽出するための正規表現パターン
    pattern = r'```python\n(.*?)\n```'
    
    # 正規表現を使用してPythonコードを抽出
    matches = re.findall(pattern, content, re.DOTALL)
    
    # 抽出したコードを指定されたディレクトリに個別のファイルとして書き込む
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for index, match in enumerate(matches):
        file_path = os.path.join(output_dir, f'extracted_code_{index + 1}.py')
        with open(file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(match + '\n\n')
        print(f"Pythonコードが {file_path} に書き出されました。")


if __name__ == "__main__":
    readme_path = "README.md"
    output_path = "data"
    extract_and_write_python_code(readme_path, output_path)

