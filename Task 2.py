import os
import shutil
from datetime import datetime

# ============================================================
# AUTOMATED FILE PROCESSING AND REPORT GENERATION SYSTEM
# ============================================================

# File categories based on extensions
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"]
}


# ------------------------------------------------------------
# Function to identify the category of a file
# ------------------------------------------------------------
def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


# ------------------------------------------------------------
# Function to create a folder
# ------------------------------------------------------------
def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)


# ------------------------------------------------------------
# Function to create sample files automatically
# ------------------------------------------------------------
def create_sample_files(input_folder):

    sample_files = [
        ("assignment.txt", "This is a sample text document."),
        ("report.pdf", "Sample PDF report file."),
        ("photo.jpg", "Sample image file."),
        ("marks.csv", "Name,Marks\nStudent1,85\nStudent2,90"),
        ("presentation.pptx", "Sample presentation file."),
        ("notes.docx", "Sample Word document."),
        ("data.xlsx", "Sample Excel spreadsheet."),
        ("unknown.xyz", "Sample file with unknown extension.")
    ]

    create_folder(input_folder)

    for filename, content in sample_files:
        file_path = os.path.join(input_folder, filename)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)


# ------------------------------------------------------------
# Function to generate processing report
# ------------------------------------------------------------
def generate_report(input_folder, processed, skipped, errors,
                    category_count):

    report_folder = "reports"
    create_folder(report_folder)

    report_file = os.path.join(
        report_folder,
        "processing_report.txt"
    )

    with open(report_file, "w", encoding="utf-8") as file:

        file.write("FILE PROCESSING AUTOMATION REPORT\n")
        file.write("=" * 45 + "\n\n")

        file.write(
            "Date and Time: "
            + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n"
        )

        file.write("Input Folder: " + input_folder + "\n\n")

        file.write("PROCESSING SUMMARY\n")
        file.write("-" * 45 + "\n")

        file.write(
            "Files Successfully Processed: "
            + str(processed)
            + "\n"
        )

        file.write(
            "Files Skipped: "
            + str(skipped)
            + "\n"
        )

        file.write(
            "Errors: "
            + str(errors)
            + "\n\n"
        )

        file.write("CATEGORY SUMMARY\n")
        file.write("-" * 45 + "\n")

        if category_count:

            for category, count in category_count.items():
                file.write(
                    category + ": " + str(count) + "\n"
                )

        else:
            file.write("No files were processed.\n")

        file.write(
            "\nAutomation completed successfully.\n"
        )

    return report_file


# ------------------------------------------------------------
# Function to process and organize files
# ------------------------------------------------------------
def process_files(input_folder, output_folder):

    processed = 0
    skipped = 0
    errors = 0

    category_count = {}

    create_folder(output_folder)

    files = [
        file
        for file in os.listdir(input_folder)
        if os.path.isfile(
            os.path.join(input_folder, file)
        )
    ]

    print("\nStarting file automation...")
    print("-" * 50)

    for filename in files:

        source_path = os.path.join(
            input_folder,
            filename
        )

        try:

            category = get_category(filename)

            category_folder = os.path.join(
                output_folder,
                category
            )

            create_folder(category_folder)

            destination_path = os.path.join(
                category_folder,
                filename
            )

            # Check for duplicate files
            if os.path.exists(destination_path):

                skipped += 1

                print(
                    "Skipped: "
                    + filename
                    + " (already exists)"
                )

                continue

            # Move file to appropriate category
            shutil.move(
                source_path,
                destination_path
            )

            processed += 1

            category_count[category] = (
                category_count.get(category, 0) + 1
            )

            print(
                "Moved: "
                + filename
                + " -> "
                + category
            )

        except Exception as error:

            errors += 1

            print(
                "Error processing "
                + filename
                + ": "
                + str(error)
            )

    # Generate report
    report_file = generate_report(
        input_folder,
        processed,
        skipped,
        errors,
        category_count
    )

    print("-" * 50)

    print("\nFILE PROCESSING COMPLETED")
    print("Files Processed :", processed)
    print("Files Skipped   :", skipped)
    print("Errors          :", errors)

    print("\nCategory Summary:")

    for category, count in category_count.items():
        print(
            "  "
            + category
            + " : "
            + str(count)
        )

    print("\nReport generated at:")
    print(report_file)


# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
def main():

    print("=" * 60)
    print(" AUTOMATED FILE ORGANIZATION & REPORT GENERATION SYSTEM")
    print("=" * 60)

    print("\nThis program automatically:")
    print("1. Creates sample files")
    print("2. Identifies file types")
    print("3. Creates category folders")
    print("4. Organizes the files")
    print("5. Generates a processing report")

    # Everything is created automatically
    input_folder = "Input_Files"
    output_folder = "Organized_Files"

    print("\nCreating sample files...")

    create_sample_files(input_folder)

    print("Sample files created successfully.")

    # Process the files
    process_files(
        input_folder,
        output_folder
    )

    print("\n" + "=" * 60)
    print("AUTOMATION FINISHED SUCCESSFULLY")
    print("=" * 60)


# ------------------------------------------------------------
# Program execution
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
