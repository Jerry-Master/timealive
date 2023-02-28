"""Django's command-line utility for administrative tasks."""
import os
import sys
import streamlit.web.bootstrap
from streamlit import config as _config
from multiprocessing import Process

def launch_streamlit():
    dirname = os.path.join(
        os.path.dirname(__file__),
        'viz',
        'streamlit_app',
    )
    filename = os.path.join(dirname, 'BuLiAn.py')

    _config.set_option("server.headless", True)
    args = []

    #streamlit.cli.main_run(filename, args)
    streamlit.web.bootstrap.run(filename,'',args, flag_options={})


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
