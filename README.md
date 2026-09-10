# Automated File Organiser

The Automated File Organizer is a Python command-line utility designed to clean up cluttered directories (like your Downloads folder) automatically. It scans a specified folder, detects the extension of each file, and moves it into an appropriately named subfolder (e.g., .pdf goes to Documents, .mp4 goes to Videos).

---

## 📂 Project Structure
   ```
   Automated_File_Organiser/
   ├── src/
   │   ├── main.py         # Entry point script
   │   └── file_utils.py   # File organisation logic
   ├── README.md
   ├── LICENSE
   └── .gitignore
   ```

---

## ✨ Features
- Organises files by extension into dedicated folders.
- Works with any directory you specify.
- Creates folders automatically if they don’t exist.
- GUI build through Tkinter
  
---

## How to Run

1. Open **Command Prompt** or **Git Bash**.
2. Navigate to your project folder:
   ```bash
   cd path\to\Automated_File_Organiser
   ```
3. Run the script by specifying the folder path you want to organise:
   ```bash
   python src/main.py --path "C:\Users\example\Downloads"
   ```
4. To Launch the **Graphical User Interface**:
   ```bash
   python src/main.py --gui
   ```
   *(NOTE: Change 'main.py --gui' to whatever command actually launches your GUI, e.g., 'python gui.py')*

---

## How It Works

1. The script scans the specified directory.
2. It identifies file extensions.
3. It creates folders named <EXTENSION>_Files (e.g., PDF_Files, PNG_Files).
4. It moves each file into its respective folder.
---

## Example Output
After running the program, your Downloads folder will look neatly organised by file type — similar to this:

Below is how the Downloads folder looks after running the organiser:

![Organised Downloads Folder](https://github.com/user-attachments/assets/6f15e4ba-2853-4165-8901-7ba50f76bb3b)
---

## Requirements
No external dependencies — works with standard Python libraries. [As of now, will change the requirements if needed after future updates]

---

## LICENSE
This code is open source and free to use for learning and personal automation
