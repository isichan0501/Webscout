import os
import subprocess

def run_python_scripts(directory):
    """
    実行するディレクトリ内のすべてのPythonファイル(*.py)を検索し、それぞれを実行します。
    各ファイルの実行結果はテキストファイルに記録されます。

    Parameters:
    directory (str): Pythonスクリプトが含まれているディレクトリのパス。
    """
    # ディレクトリ内のすべての.pyファイルをリストアップ
    python_files = [f for f in os.listdir(directory) if f.endswith('.py')]
    
    # 各ファイルを実行し、結果をファイルに出力
    error_files = []  # エラーが発生したファイル名を格納するリスト
    for file in python_files:
        filepath = os.path.join(directory, file)
        with open(f"{file}_output.txt", "w") as output_file:
            # subprocessを使用してPythonスクリプトを実行
            result = subprocess.run(["python", filepath], stdout=output_file, stderr=subprocess.PIPE)
            if result.returncode != 0:  # エラーが発生した場合
                error_files.append(file)  # エラーリストにファイル名を追加

    if error_files:  # エラーが発生したファイルがある場合
        print("エラーが発生したファイル:")
        for ef in error_files:
            print(ef)
    else:
        print("全てのファイルが正常に実行されました。")



if __name__ == "__main__":
    # 実行するディレクトリを指定
    run_python_scripts("./data")

