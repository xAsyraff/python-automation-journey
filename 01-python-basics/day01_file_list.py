from pathlib import Path

print("=== File Listing Automation ===")

folder_path = input(
    "Enter a folder path (example: C:\\Users\\YourName\\Downloads): "
).strip()

folder = Path(folder_path)

if not folder.exists():
    print("❌ That path does not exist.")
    exit()

if not folder.is_dir():
    print("❌ That path is not a folder.")
    exit()

output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

output_file = output_folder / "file_list.txt"

with output_file.open("w", encoding="utf-8") as f:
    f.write(f"Files in: {folder}\n")
    f.write("=" * 40 + "\n")

    for item in folder.iterdir():
        label = "[DIR]" if item.is_dir() else "     "
        f.write(f"{label} {item.name}\n")

print("✅ Done!")
print(f"Saved to: {output_file.resolve()}")