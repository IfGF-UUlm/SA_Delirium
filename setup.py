import os
import subprocess
import platform
import venv


def create_virtual_env(env_dir):
    """
    Create a virtual environment in the specified directory.

    Args:
    env_dir (str): The path to the directory where the virtual environment should be created.
    """
    venv.create(env_dir, with_pip=True)
    print(f"Virtual environment created at {env_dir}")


def install_packages(env_dir):
    """
    Install packages from requirements.txt into the virtual environment.

    Args:
    env_dir (str): The path to the virtual environment directory.
    """
    if platform.system() == "Windows":
        pip_executable = os.path.join(env_dir, 'Scripts', 'pip.exe')
    else:
        pip_executable = os.path.join(env_dir, 'bin', 'pip')

    requirements_file = os.path.join(
        os.path.dirname(__file__), 'requirements.txt')

    subprocess.check_call([pip_executable, 'install', '-r', requirements_file])
    print("Packages installed successfully")


def main():
    """
    Create a virtual environment and install packages from requirements.txt.
    """
    env_dir = os.path.join(os.getcwd(), 'env')

    create_virtual_env(env_dir)
    install_packages(env_dir)


if __name__ == "__main__":
    main()
