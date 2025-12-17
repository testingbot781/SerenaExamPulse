def run_pyrogram():
    import sys
    import os

    print(">>> Starting Pyrogram subprocess...")

    project_root = os.path.dirname(os.path.abspath(__file__))
    
    subprocess.Popen(
        [
            sys.executable,
            "-m",
            "bot.worker"
        ],
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    print(">>> Pyrogram subprocess launched ✔")
