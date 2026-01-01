# gzip-json

A lightweight Python library for reading and writing gzip-compressed JSON files with UTF-8 encoding and compact JSON format.

## Features

- **Simple API**: Two static methods (`read` and `write`) for all operations
- **UTF-8 encoding**: Automatic handling of UTF-8 encoding for international characters
- **Compact JSON format**: Uses minimal JSON format (no spaces, no ASCII escaping) for efficient storage
- **Type safety**: Supports both `str` and `Path` objects for file paths
- **Error handling**: Comprehensive exception hierarchy for precise error handling
- **Zero dependencies**: Uses only Python standard library (gzip, json)

## Installation

```bash
pip install gzip-json
```

## Quick Start

### Reading a gzip-compressed JSON file

```python
from gzip_json import GzipJson

# Read a gzip-compressed JSON file
data = GzipJson.read("data.json.gz")

# data can be a dict, list, or any JSON-serializable type
print(data)
```

### Writing to a gzip-compressed JSON file

```python
from gzip_json import GzipJson

# Write data to a gzip-compressed JSON file
data = {"key": "value", "number": 42, "list": [1, 2, 3]}
GzipJson.write("output.json.gz", data)
```

### Using Path objects

```python
from pathlib import Path
from gzip_json import GzipJson

# Both str and Path objects are supported
path = Path("data.json.gz")
data = GzipJson.read(path)

GzipJson.write(Path("output.json.gz"), {"example": "data"})
```

## API Reference

### GzipJson

Main utility class for reading and writing gzip-compressed JSON files. All methods are static.

#### `GzipJson.read(path)`

Read a gzip-compressed JSON file.

**Parameters:**

- `path` (str | Path): Path to the gzip-compressed JSON file.

**Returns:**

- Any: Parsed JSON data (dict, list, or other JSON-serializable types).

**Raises:**

- `GzipJsonReadError`: If reading fails due to:
  - File not found
  - Invalid gzip format
  - JSON parsing errors
  - I/O errors

**Example:**

```python
from gzip_json import GzipJson

data = GzipJson.read("data.json.gz")
```

#### `GzipJson.write(path, data)`

Write data to a gzip-compressed JSON file.

The file is written in compact JSON format (no spaces, no ASCII escaping) with UTF-8 encoding for efficient storage.

**Parameters:**

- `path` (str | Path): Path to the output file.
- `data` (Any): Data to serialize (must be JSON-serializable).

**Raises:**

- `GzipJsonWriteError`: If writing fails due to:
  - Permission denied
  - Disk space issues
  - I/O errors
- `TypeError`: If data is not JSON-serializable.

**Example:**

```python
from gzip_json import GzipJson

data = {"key": "value", "number": 42}
GzipJson.write("output.json.gz", data)
```

### Exceptions

#### `GzipJsonError`

Base exception class for all gzip-json related errors.

**Attributes:**

- `message`: Primary error message (required)
- `file_path`: Path to the file that caused the error (optional)

#### `GzipJsonReadError`

Raised when reading a gzip-compressed JSON file fails.

This exception indicates that an error occurred during the read operation, such as file not found, invalid gzip format, JSON parsing errors, or I/O errors.

**Attributes:**

- `message`: Human-readable error message describing the issue
- `file_path`: Path to the file that caused the error (optional)

**Example:**

```python
from gzip_json import GzipJson, GzipJsonReadError

try:
    data = GzipJson.read("nonexistent.json.gz")
except GzipJsonReadError as e:
    print(f"Error reading file: {e.message}")
    print(f"File path: {e.file_path}")
```

#### `GzipJsonWriteError`

Raised when writing a gzip-compressed JSON file fails.

This exception indicates that an error occurred during the write operation, such as permission denied, disk space issues, or I/O errors.

**Attributes:**

- `message`: Human-readable error message describing the issue
- `file_path`: Path to the file that caused the error (optional)

**Example:**

```python
from gzip_json import GzipJson, GzipJsonWriteError

try:
    GzipJson.write("/readonly/output.json.gz", {"data": "value"})
except GzipJsonWriteError as e:
    print(f"Error writing file: {e.message}")
    print(f"File path: {e.file_path}")
```

## Requirements

- Python >= 3.10

No external dependencies required. This package uses only Python standard library modules (`gzip` and `json`).

## License

MIT License
