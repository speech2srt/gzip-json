"""
Gzip JSON - A Python library for reading and writing gzip-compressed JSON files.

This package provides utilities for:
- Reading gzip-compressed JSON files
- Writing data to gzip-compressed JSON files
- Automatic UTF-8 encoding handling
- Compact JSON format for efficient storage
"""

import logging

from .exceptions import GzipJsonError, GzipJsonReadError, GzipJsonWriteError
from .gzip_json import GzipJson

__version__ = "0.1.0"

# Configure library root logger
# Use NullHandler to ensure library remains silent when user hasn't configured logging
# If user configures logging (e.g., logging.basicConfig()), logs will bubble up to root logger for processing
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

__all__ = [
    "GzipJson",
    "GzipJsonError",
    "GzipJsonReadError",
    "GzipJsonWriteError",
]
