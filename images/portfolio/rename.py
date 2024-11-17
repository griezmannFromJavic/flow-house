import os

# Get a list of all .jpg files in the current directory
jpg_files = [file for file in os.listdir() if file.lower().endswith('.jpg')]

# Sort the files to ensure consistent ordering
jpg_files.sort()

# Rename files with incremental numbers
for index, file in enumerate(jpg_files, start=1):
    new_name = f"{index:02}.jpg"  # Generates 01.jpg, 02.jpg, etc.
    os.rename(file, new_name)
    print(f"Renamed '{file}' to '{new_name}'")

print("Renaming complete!")

