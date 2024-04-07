import os
import subprocess

resp_tree = {
    "agi":{"base.py":None, "openai":{},"wenxinyiyan":{},"linkai":{},"__init__.py":None},
    "front_end":{"gradio":{"run_gradio.py":None},"__init__.py":None},
    "scripts":{"__init__.py":None, "test_gradio.py":None,"test_movie_generator.py":None},
    "movie_generator":{"__init__.py":None,"movie_generator.py":None},
    "__init__.py":None,
}

def init_folder(repository_tree):
    def _init_folder(repository_tree, folder_nm):
        for key, value in repository_tree.items():
            if value == None:
                status, ret=subprocess.getstatusoutput(f"touch  {os.path.join(folder_nm, key)}")
                print(f"touch {os.path.join(folder_nm, key)} {status} {ret}")
            else:
                status, ret= subprocess.getstatusoutput(f"mkdir -p {os.path.join(folder_nm, key)}")
                print(f"mkdir -p {os.path.join(folder_nm, key)} {status} {ret}")
                _init_folder(value, os.path.join(folder_nm, key))
        return
    print(os.getcwd())
    _init_folder(repository_tree, os.getcwd())

if __name__ == "__main__":
    print("Initiating the repository")
    print(resp_tree)
    init_folder(resp_tree)

