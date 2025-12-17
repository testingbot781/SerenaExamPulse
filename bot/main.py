def run_pyrogram():
    import sys
    import os

    # absolute path to project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    subprocess.Popen(
        [
            sys.executable,     # ALWAYS RUN CORRECT PYTHON
            "-m",
            "bot.worker"
        ],
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

