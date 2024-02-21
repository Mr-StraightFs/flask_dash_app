import os
import subprocess

PROJECT_NAME = os.path.basename(os.getcwd())
VIRTUAL_ENV = os.path.join(os.getcwd(), '.venv')
LOCAL_PYTHON = os.path.join(VIRTUAL_ENV, 'Scripts', 'python.exe' if os.name == 'nt' else 'bin/python3')

HELP = """
Manage {}. Usage:

python run.py          - Run {} locally.
python install.py      - Create local virtualenv & install dependencies.
python deploy.py       - Set up project & run locally.
python update.py       - Update dependencies via Poetry and output resulting `requirements.txt`.
python format.py       - Run Python code formatter & sort dependencies.
python lint.py         - Check code formatting with flake8.
python clean.py        - Remove extraneous compiled files, caches, logs, etc.
""".format(PROJECT_NAME, PROJECT_NAME)

def print_help():
    print(HELP)

def create_virtualenv():
    if not os.path.exists(VIRTUAL_ENV):
        print(f"Creating Python virtual env in `{VIRTUAL_ENV}`")
        subprocess.run(['python', '-m', 'venv', VIRTUAL_ENV])

def run():
    create_virtualenv()
    subprocess.run([LOCAL_PYTHON, '-m', 'main'])

def install():
    create_virtualenv()
    subprocess.run([LOCAL_PYTHON, '-m', 'pip', 'install', '--upgrade', 'pip', 'setuptools', 'wheel'])
    subprocess.run([LOCAL_PYTHON, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    subprocess.run(['npm', 'i', '-g', 'less'])
    print(f"Installed dependencies in `{VIRTUAL_ENV}`")

def deploy():
    install()
    run()

# Define other tasks similarly...

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Manage {}.".format(PROJECT_NAME))
    parser.add_argument('task', nargs='?', default='help', help='Task to execute')

    args = parser.parse_args()

    if args.task == 'help':
        print_help()
    elif args.task == 'run':
        run()
    elif args.task == 'install':
        install()
    elif args.task == 'deploy':
        deploy()
    else:
        print("Invalid task. Run 'python run.py help' for usage instructions.")
