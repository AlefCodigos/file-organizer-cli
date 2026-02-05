from pathlib import Path
from typing import Dict, List
import shutil
import argparse


def file_filter(file_path: Path) -> str:
    file_extension = file_path.suffix.lower()
    if file_extension in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
        return "images"
    if file_extension in {".mp4", ".avi", ".mkv", ".rmvb"}:
        return "videos"
    if file_extension in {".pdf", ".txt", ".md", ".docx"}:
        return "documents"
    if file_extension in {".mp3", ".flac", ".ape"}:
        return "audio"
    if file_extension in {".zip", ".rar", ".7z"}:
        return "archives"

    return "others"


def get_unique_path(path: Path) -> Path:
    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent

    counter = 1

    while True:
        new_path = parent / f"{stem} ({counter}){suffix}"
        if not new_path.exists():
            return new_path
        counter += 1


def plan_organization(directory: Path) -> Dict[Path, Path]:
    """
    Given a directory, return a mapping of source file paths to destination paths.
    No filesystem changes are made.
    """
    organized_dict = {}
    for file_path in directory.iterdir():
        if file_path.is_file():
            organized_dict[file_path] = Path(str(directory) + "/" + file_filter(file_path) +
                                             "/" + file_path.name)
    return organized_dict


def apply_organization(directory: Path) -> str:
    operation_log = ""
    organized_dict = plan_organization(directory)
    for source, destination in organized_dict.items():
        if source.is_file():
            destination.parent.mkdir(parents=True, exist_ok=True)
            try:
                final_destination = get_unique_path(destination)
                shutil.move(source, final_destination)
                operation_log = operation_log + f"Moved {source.name} from {directory} to {final_destination}\n"
            except shutil.Error as e:
                operation_log = operation_log + f"Error moving {source.name}: {e}\n"
    return operation_log


def main():
    parser = argparse.ArgumentParser(description="Move files in a source folder into "
                                                 "different folders according to the file type.",
                                     formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=45))
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-d', '--dry_run',
                       type=str,
                       metavar='',
                       help='Input a directory path to simulate a organized file to folder structure'
                       )
    group.add_argument('-e', '--execute_organizer',
                       type=str,
                       metavar='',
                       help='Input a directory path to organized the files within'
                       )
    args = parser.parse_args()
    if args.dry_run:
        organized_directory = plan_organization(Path(args.dry_run))
        for key, value in organized_directory.items():
            print(f"{key.name} will be moved to {value.parent}")
    elif args.execute_organizer:
        print(apply_organization(Path(args.execute_organizer)))


if __name__ == "__main__":
    main()

