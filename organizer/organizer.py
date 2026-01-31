from pathlib import Path
from typing import Dict, List


def plan_organization(directory: Path) -> Dict[Path, Path]:
    """
    Given a directory, return a mapping of source file paths to destination paths.
    No filesystem changes are made.
    """
    organized_dict = {}
    for file_path in directory.iterdir():
        organized_dict[file_path] = Path(str(directory) + "/" + file_filter(file_path) +
                                         "/" + file_path.name)
    return organized_dict


def file_filter(file_path: Path) -> str:
    file_extension = file_path.suffix.lower()
    if file_extension in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
        return "images"
    if file_extension in {".mp4", ".avi", ".mkv"}:
        return "videos"
    if file_extension in {".pdf", ".txt", ".md"}:
        return "documents"
    if file_extension in {".zip", ".rar", ".7z"}:
        return "archives"

    return "others"
