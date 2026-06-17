import argparse
import sys
from file_utils import organise_files

def run_gui():
    import gui
    gui.launch_app()

def run_cli():
    print("Running in Cli mode")

def main():
    parser = argparse.ArgumentParser(description="Automated File Organiser")
    parser.add_argument("--path", required=True, help="Path to organise")
    args = parser.parse_args()

    organise_files(args.path)

if __name__ == "__main__":
    if "--gui" in sys.argv:
        run_gui()
    else:
        run_cli()
        main()
