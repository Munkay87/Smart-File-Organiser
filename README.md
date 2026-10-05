# Smart File Organiser

Smart File Organiser is a Python command-line utility that automatically organises files into configurable categories based on their file extensions.

The project was developed as a practical Python application with a focus on flexible file classification, safe file handling, input validation, and code that can adapt to changing requirements.

## Features

- Organises files by extension
- Validates folder paths before processing
- Supports Images, Videos, Audio, Documents, Archives, and Others
- Creates destination folders automatically
- Ignores directories while scanning
- Supports custom file categories and extensions
- Provides movement summaries
- Handles uppercase and lowercase file extensions

### Dry Run Mode

Dry Run Mode previews proposed file movements without modifying the filesystem.

This allows users to check what the organiser intends to do before allowing files to be moved.

### Collision Protection

Before moving a file, Smart File Organiser checks whether a file with the same name already exists in the destination folder.

Existing files are not overwritten.

### Custom Categories

Additional categories can be created at runtime.

For example:

```text
Code -> .py
```

Multiple comma-separated extensions can also be assigned to a custom category.

Custom categories automatically integrate with file classification, folder creation, movement tracking, and the final summary.

## Technologies and Concepts

- Python
- `pathlib`
- File and directory handling
- Dictionaries and lists
- List comprehensions
- Input validation
- File movement
- Collision detection
- Dynamic categories and counters
- Dry-run safety design
- Refactoring

## How to Run

### Requirements

- Python 3

### Running the Program

1. Clone or download this repository.
2. Open the project folder.
3. Run:

```bash
python Smart_File_Organiser.py
```

4. Enter the path of the folder you want to organise.
5. Choose whether to perform a dry run.
6. Optionally create custom categories.
7. Review the movement summary.

## Safety

When using the program on important files, running it in Dry Run Mode first is recommended.

The organiser also includes collision protection to prevent existing destination files from being overwritten.

## Project Status

Completed portfolio project.

Future versions may explore features such as a graphical interface, persistent configuration, recursive folder organisation, undo functionality, operation logging, automated testing, and executable packaging.