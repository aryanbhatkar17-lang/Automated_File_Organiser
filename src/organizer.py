import argparse
from file_utils import organise_files

def main():
    parser = argparse.ArgumentParser(description="Automated File Organiser")
    parser.add_argument("--path", required=True, help="Path to organise")
    args = parser.parse_args()

    organise_files(args.path)

if __name__ == "__main__":
    main()
