import subprocess

if __name__ == "__main__":
    subprocess.run(['python3', 'manage.py', 'runserver', '0.0.0.0:8000'])
    subprocess.run(['cd', '../../frontend', ])
    subprocess.run(['npm', 'start'])
