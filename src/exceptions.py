"""
Exception classes for gzip-json processing errors.

Provides a hierarchy of exceptions for different error conditions,
enabling precise error handling and debugging.
"""

from typing import Optional


class GzipJsonError(Exception):
    """
    Base exception class for gzip-json processing errors.

    All gzip-json related exceptions inherit from this class.
    """

    def __init__(self, message: str, file_path: Optional[str] = None):
        """
        Initialize exception with error context.

        Args:
            message: Primary error message (required).
            file_path: Path to the file that caused the error (optional).
        """
        super().__init__(message)
        self.message = message
        self.file_path = file_path


class GzipJsonReadError(GzipJsonError):
    """
    Raised when reading a gzip-compressed JSON file fails.

    This exception indicates that an error occurred during the read operation,
    such as file not found, invalid gzip format, JSON parsing errors, or I/O errors.
    """

    def __init__(self, message: str, file_path: Optional[str] = None):
        """
        Initialize exception.

        Args:
            message: Human-readable error message describing the issue.
            file_path: Path to the file that caused the error (optional).
        """
        super().__init__(message, file_path)


class GzipJsonWriteError(GzipJsonError):
    """
    Raised when writing a gzip-compressed JSON file fails.

    This exception indicates that an error occurred during the write operation,
    such as permission denied, disk space issues, or I/O errors.
    """

    def __init__(self, message: str, file_path: Optional[str] = None):
        """
        Initialize exception.

        Args:
            message: Human-readable error message describing the issue.
            file_path: Path to the file that caused the error (optional).
        """
        super().__init__(message, file_path)
