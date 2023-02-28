"""Django's command-line utility for administrative tasks."""
import os
import sys
from multiprocessing import Process
import runpy

def launch_streamlit():
    dirname = os.path.join(
        os.path.dirname(__file__),
        'viz',
        'streamlit_app',
    )
    filename = os.path.join(dirname, 'BuLiAn.py')

    sys.argv = ["streamlit", "run", filename, '--server.headless', 'true']; 
    runpy.run_module("streamlit", run_name="__main__")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timealive.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    if sys.argv[1] == 'runserver':
        p = Process(target=launch_streamlit)
        p.start()
    main()
    if sys.argv[1] == 'runserver':
        p.join()
