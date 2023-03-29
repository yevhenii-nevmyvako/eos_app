class OutputFileExistsError(Exception):
    """Should raise exception if file is already exist."""
    pass


class FileExtensionError(Exception):
    """should raise exception if format file is not `.JSON`."""
    pass


class NotTwoDimensionalArrayError(Exception):
    """Should raise exception if the entered array is not two-dimensional"""
    pass
