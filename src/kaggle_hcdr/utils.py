from pathlib import Path


def get_dir_path(dir_name: str):
    """
    Get path for specified directory, in case it exists.

    Parameters
    ----------
    dir_name : str
        Target directory.

    Returns
    -------
    directory_path: Path
        Returns target directory full path.

    Raises
    ------
    FileNotFoundError
        _description_
    """
    current_directory = Path.cwd()
    parents_dir = current_directory.parents

    for parent in parents_dir:
        for child_dir in parent.iterdir():
            if dir_name in child_dir.parts:
                return child_dir
    raise FileNotFoundError(f"Directory {dir_name!r} not found.")
