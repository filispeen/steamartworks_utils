from local_ffmpeg import is_installed, install
import click
import os

@click.command()
@click.option('--path', help='FFmpeg path')
def checkandInstall(path=None):
    if path==None: raise RuntimeError("--path must be not empty")
    path=os.path.normpath(path)
    print(f"Checking {path} for ffmpeg")
    if not is_installed(path):
        success, message = install(path)
        if success:
            print(message)
        else:
            print(f"Error: {message}")
    else:
        print("FFmpeg is already installed")

if __name__ == "__main__":
    checkandInstall()