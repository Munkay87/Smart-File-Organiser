from pathlib import Path


folder = input("Enter the folder path: ")
folder_path = Path(folder)
while True:
    choice = input("dry run? (yes/no): ").strip().lower()

    if choice == 'yes':
        dry_run = True
        print("Dry run mode: No files will be moved.")
        break
    elif choice == 'no':
        dry_run = False
        print("Files will be moved to their respective folders.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Audios': ['.mp3', '.wav'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.csv'],
    'Archives': ['.zip', '.rar', '.7z'],
}

moved_files_count = {
    'Images': 0,
    'Videos': 0,
    'Audios': 0,
    'Documents': 0,
    'Archives': 0,
    'Others': 0
}

custom_choice = input("Do you want to add custom file categories? (yes/no): ").strip().lower()
if custom_choice == 'yes':
    while True:
        category_name = input("Enter the category name (or type 'done' to finish): ").strip()
        if category_name.lower() == 'done':
            break
        extensions = input(f"Enter the file extensions for {category_name} (comma-separated, e.g., .ext1,.ext2): ").strip().split(',')
        extensions = [ext.strip().lower() for ext in extensions]
        file_categories[category_name] = extensions
        moved_files_count[category_name] = 0


if not folder_path.exists() or not folder_path.is_dir():
    print("The specified folder does not exist or is not a directory.")
else:
    print("Folder Found")
    for item in folder_path.iterdir():
        if item.is_file():
            file_extension = item.suffix.lower()
            for category_name, extensions in file_categories.items():
                if file_extension in extensions:
                    category = category_name
                    break
            else:
                category = 'Others'

            print("Dictionary category:", category)


            destination_folder = folder_path / category
            destination_path = destination_folder / item.name

            if dry_run:
                print(f"Dry run: Would move {item.name} to {destination_folder}")
            else:
                if destination_path.exists():
                    print(f"File {item.name} already exists in {destination_folder}. Skipping.")
                else:
                    destination_folder.mkdir(exist_ok=True)
                    item.rename(destination_path)
                    print(f"Moved {item.name} to {destination_folder}")

                    if category in moved_files_count:
                        moved_files_count[category] += 1

    if dry_run:
        print("Dry run completed. No files were moved.")
    else:
        print("File organization completed.")
        for category, count in moved_files_count.items():
            print(f"{category} Moved: {count}")