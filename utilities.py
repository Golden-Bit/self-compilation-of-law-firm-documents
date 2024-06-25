import os
from pathlib import Path


def find_executable_by_partial_path(start_directory, partial_path):
    """
    Recursively search for an executable in a given directory using pathlib
    by matching a partial path.

    Parameters:
    - start_directory: Directory to start the search from.
    - partial_path: Partial path to match the executable.

    Returns:
    - The path to the executable if found, otherwise None.
    """
    start_path = Path(start_directory)
    for path in start_path.rglob('*'):
        print(path)
        if partial_path in str(path) and path.is_file() and os.access(path, os.X_OK):
            print(f"Executable matching '{partial_path}' found at: {path}")
            return str(path)
    print(f"No executable matching '{partial_path}' found in {start_directory}.")
    return None


# Example usage
search_directory = "C:\\"  # Root directory (use with caution)
partial_path = "soffice.exe"
find_executable_by_partial_path(search_directory, partial_path)
