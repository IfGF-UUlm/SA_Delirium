import subprocess
import os
import sys


def activate_virtualenv(env_dir):
    """
    Get the path to the activate script for the specified virtual environment.

    Args:
        env_dir (str): The path to the environment directory.

    Returns:
        str: The path to the activate script in the virtual environment.
    """
    if sys.platform.startswith('win'):
        activate_script = os.path.join(env_dir, 'Scripts', 'activate.bat')
    else:
        activate_script = os.path.join(env_dir, 'bin', 'activate')
    return activate_script


def main():
    """
    Run the application `app.py` using the virtual environment.

    This function activates the virtual environment, sets up the necessary paths, and executes the application using
    a subprocess.
    """
    env_dir = os.path.join(os.path.dirname(__file__), 'env')
    activate_script = activate_virtualenv(env_dir)
    script_path = os.path.join(os.path.dirname(__file__), 'app.py')

    if sys.platform.startswith('win'):
        command = f'cmd /k "{activate_script} & python {script_path}"'
    else:
        command = f'/bin/bash -c "source {activate_script} && python {script_path}"'

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
