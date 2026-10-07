# File Processing Automation

A simple automated file processing and organization system developed using Python. The application automatically creates sample files, identifies their file types, organizes them into appropriate folders, and generates a processing report.

## Project Overview

The File Processing Automation system is a Python-based automation project designed to demonstrate file handling, directory management, file processing, exception handling, and automated report generation through a practical repetitive workflow.

The application automatically creates a set of sample files with different extensions. It then identifies each file based on its extension and moves it into the appropriate category folder such as Documents, Images, Spreadsheets, Presentations, or Others.

The project also generates a processing report containing the number of files processed, skipped, or affected by errors, along with a category-wise summary.

## Features

* Automatic creation of sample files
* Automatic file type identification
* File organization based on extensions
* Automatic creation of category folders
* Documents categorization
* Images categorization
* Spreadsheet categorization
* Presentation categorization
* Handling of unknown file types
* Duplicate file detection
* Exception handling
* Automatic report generation
* Fully automated workflow
* No external Python libraries required

## Technologies Used

* **Python 3**
* **os** – for file and directory management
* **shutil** – for moving files
* **datetime** – for recording report date and time
* **Command Prompt / Terminal / Online Python Compiler** – for running the application
* **Git & GitHub** – for version control and project hosting

## Project Structure

```text
File-Processing-Automation/
│
├── file_automation.py
├── Input_Files/
├── Organized_Files/
└── reports/
    └── processing_report.txt
```

### `file_automation.py`

Contains the complete Python automation program, including:

* Sample file creation
* File type identification
* File categorization
* Folder creation
* File movement
* Duplicate file handling
* Exception handling
* Report generation
* Main automation workflow

### `Input_Files/`

Contains the sample files created automatically by the program before processing.

Example files include:

```text
assignment.txt
report.pdf
photo.jpg
marks.csv
presentation.pptx
notes.docx
data.xlsx
unknown.xyz
```

### `Organized_Files/`

Contains the automatically created category folders and the processed files.

Example:

```text
Organized_Files/
│
├── Documents/
├── Images/
├── Spreadsheets/
├── Presentations/
└── Others/
```

### `reports/`

Contains the automatically generated processing report.

```text
processing_report.txt
```

## Requirements

Make sure Python 3 is available on the system.

You can check the installed Python version using:

```bash
python --version
```

No external Python packages are required because the application uses only built-in Python modules.

## Installation

1. Download or clone the repository:

```bash
git clone <your-github-repository-url>
```

2. Open the project folder:

```bash
cd File-Processing-Automation
```

3. Run the application:

```bash
python file_automation.py
```

The program automatically creates the required sample files and folders.

The application can also be copied directly into an online Python compiler and executed without installing any external libraries.

## How to Use

After running the program, the application displays the automation process:

```text
============================================================
 AUTOMATED FILE ORGANIZATION & REPORT GENERATION SYSTEM
============================================================

This program automatically:
1. Creates sample files
2. Identifies file types
3. Creates category folders
4. Organizes the files
5. Generates a processing report
```

### 1. Create Sample Files

The program automatically creates an `Input_Files` folder and places sample files inside it.

Example:

```text
Input_Files/
├── assignment.txt
├── report.pdf
├── photo.jpg
├── marks.csv
├── presentation.pptx
├── notes.docx
├── data.xlsx
└── unknown.xyz
```

This removes the need for the user to manually prepare input files.

### 2. Identify File Types

The program examines the extension of every file.

For example:

```text
.txt  → Documents
.pdf  → Documents
.jpg  → Images
.csv  → Spreadsheets
.xlsx → Spreadsheets
.pptx → Presentations
.xyz  → Others
```

The file extension is converted to lowercase so that different capitalization styles can be handled correctly.

### 3. Organize Files

After identifying the file type, the program automatically creates the appropriate folder and moves the file into it.

Example:

```text
Moved: assignment.txt -> Documents
Moved: photo.jpg -> Images
Moved: marks.csv -> Spreadsheets
Moved: presentation.pptx -> Presentations
Moved: unknown.xyz -> Others
```

### 4. Handle Unknown File Types

If a file extension is not included in the predefined categories, the file is placed inside the `Others` folder.

For example:

```text
unknown.xyz
```

is automatically moved to:

```text
Organized_Files/Others/
```

This ensures that unsupported files are not ignored.

### 5. Handle Duplicate Files

Before moving a file, the application checks whether a file with the same name already exists in the destination folder.

If the file already exists, it is skipped instead of being overwritten.

Example:

```text
Skipped: assignment.txt (already exists)
```

The skipped file count is also included in the final report.

### 6. Generate Processing Report

After completing the file processing operation, the program automatically creates:

```text
reports/processing_report.txt
```

The report contains:

```text
FILE PROCESSING AUTOMATION REPORT
=============================================

Date and Time: 2026-10-07 14:00:00
Input Folder: Input_Files

PROCESSING SUMMARY
---------------------------------------------
Files Successfully Processed: 8
Files Skipped: 0
Errors: 0

CATEGORY SUMMARY
---------------------------------------------
Documents: 3
Images: 1
Spreadsheets: 2
Presentations: 1
Others: 1

Automation completed successfully.
```

## Exception Handling

Exception handling is implemented to prevent unexpected errors from terminating the entire automation process.

The application handles situations such as:

* Missing folders
* File movement errors
* File access errors
* Duplicate files
* Unexpected file processing errors

When an error occurs, the program records the error and continues processing other files whenever possible.

Example:

```text
Error processing filename.txt: <error message>
```

The number of errors is also recorded in the processing report.

## File Categorization

The application uses predefined file extensions to determine the category of each file.

| Category      | File Extensions                         |
| ------------- | --------------------------------------- |
| Documents     | `.pdf`, `.doc`, `.docx`, `.txt`         |
| Images        | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| Spreadsheets  | `.xls`, `.xlsx`, `.csv`                 |
| Presentations | `.ppt`, `.pptx`                         |
| Others        | Unsupported extensions                  |

This approach allows the automation system to organize different types of files without requiring manual sorting.

## Automation Workflow

The complete workflow of the application is:

```text
Start
  ↓
Create Input Folder
  ↓
Create Sample Files
  ↓
Scan Files
  ↓
Identify File Extension
  ↓
Determine Category
  ↓
Create Category Folder
  ↓
Check for Duplicate
  ↓
Move File
  ↓
Count Processed / Skipped / Errors
  ↓
Generate Processing Report
  ↓
End
```

## Concepts Demonstrated

This project demonstrates the following Python concepts:

* Variables and data types
* Functions
* Conditional statements
* Loops
* Lists
* Dictionaries
* File handling
* Directory management
* File extensions
* File movement
* Exception handling
* String manipulation
* Date and time handling
* Automation
* Report generation

## Advantages

* Reduces repetitive manual file organization
* Saves time when handling multiple files
* Automatically creates required folders
* Handles unknown file types
* Prevents accidental overwriting of duplicate files
* Generates a processing summary automatically
* Requires no external Python libraries
* Easy to understand and modify
* Can be executed using an online Python compiler

## Future Enhancements

Possible improvements for future versions include:

* User-selected input folders
* Support for additional file formats
* Automatic file renaming
* File size-based categorization
* Date-based folder organization
* Recursive processing of subfolders
* CSV or Excel report generation
* Graphical user interface
* Scheduled automatic execution
* Cloud storage integration
* Detailed logging system
* File backup before processing

## Real-World Applications

The automation approach used in this project can be applied to several real-world situations, including:

* Organizing downloaded files
* Managing office documents
* Sorting photographs
* Organizing academic files
* Managing project resources
* Processing business documents
* Organizing reports and spreadsheets
* Automated document management systems
* Repetitive administrative workflows

## Project Purpose

This project was developed as part of a Python Developer Internship task to demonstrate the practical application of Python automation for file processing, organization, and report generation.

The project focuses on replacing repetitive manual file management activities with a simple and reliable automated workflow.

## Author

**M. Ayshwarya**
