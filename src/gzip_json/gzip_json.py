"""
Gzip JSON Processing Module

Provides utilities for reading and writing gzip-compressed JSON files.
All operations use UTF-8 encoding and compact JSON format (no spaces, no ASCII escaping).
"""

import gzip
import json
import logging
from pathlib import Path
from typing import Any, Union

from .exceptions import GzipJsonReadError, GzipJsonWriteError

logger = logging.getLogger(__name__)


class GzipJson:
    """
    Utility class for reading and writing gzip-compressed JSON files.

    All methods are static and provide a simple interface for working with
    gzip-compressed JSON data. Files are always read/written with UTF-8 encoding,
    and JSON output uses compact format (no spaces, no ASCII escaping).
    """

    @staticmethod
    def read(path: Union[str, Path]) -> Any:
        """
        Read a gzip-compressed JSON file.

        Opens the file in text mode with UTF-8 encoding, decompresses it,
        and parses the JSON content.

        Args:
            path: Path to the gzip-compressed JSON file (str or Path).

        Returns:
            Parsed JSON data (dict, list, or other JSON-serializable types).

        Raises:
            GzipJsonReadError: If reading fails due to:
                - File not found
                - Invalid gzip format
                - JSON parsing errors
                - I/O errors
        """
        path_str = str(path)
        try:
            with gzip.open(path_str, "rt", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError as e:
            raise GzipJsonReadError(f"File not found: {path_str}", file_path=path_str) from e
        except gzip.BadGzipFile as e:
            raise GzipJsonReadError(f"Invalid gzip format: {path_str}", file_path=path_str) from e
        except json.JSONDecodeError as e:
            raise GzipJsonReadError(f"JSON parsing error in {path_str}: {e}", file_path=path_str) from e
        except OSError as e:
            raise GzipJsonReadError(f"I/O error reading {path_str}: {e}", file_path=path_str) from e
        except Exception as e:
            raise GzipJsonReadError(f"Unexpected error reading {path_str}: {e}", file_path=path_str) from e

    @staticmethod
    def write(path: Union[str, Path], data: Any) -> None:
        """
        Write data to a gzip-compressed JSON file.

        Serializes the data to JSON and writes it as a gzip-compressed file
        in text mode with UTF-8 encoding. Uses compact JSON format (no spaces,
        no ASCII escaping) for efficient storage.

        Args:
            path: Path to the output file (str or Path).
            data: Data to serialize (must be JSON-serializable).

        Raises:
            GzipJsonWriteError: If writing fails due to:
                - Permission denied
                - Disk space issues
                - I/O errors
            TypeError: If data is not JSON-serializable.
        """
        path_str = str(path)
        try:
            with gzip.open(path_str, "wt", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
        except PermissionError as e:
            raise GzipJsonWriteError(f"Permission denied writing to {path_str}", file_path=path_str) from e
        except OSError as e:
            raise GzipJsonWriteError(f"I/O error writing to {path_str}: {e}", file_path=path_str) from e
        except TypeError as e:
            # Re-raise TypeError for non-serializable data (not wrapped in GzipJsonWriteError)
            raise
        except Exception as e:
            raise GzipJsonWriteError(f"Unexpected error writing to {path_str}: {e}", file_path=path_str) from e
