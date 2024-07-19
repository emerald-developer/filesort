# PySort

This Python script sorts files into directories based on their file extensions, using a JSON configuration file to specify the sorting rules.

## Features

- Sorts files based on their extensions
- Uses a JSON configuration file for flexible sorting rules
- Creates destination directories if they don't exist
- Prints status messages for each file processed

## Requirements

- Python 3.x

## Usage

1. Clone this repository or download the `sort.py` script.
2. Create a JSON configuration file named `file_sorter_config.json` in the same directory as the script.
3. Run the script using Python:

```
python sort.py
```

## Configuration File Format

The configuration file should be named `file_sorter_config.json` and have the following structure:

```json
{
    "source_directory": "/path/to/source/directory",
    "mappings": {
        "/path/to/images": [".jpg", ".jpeg", ".png", ".gif"],
        "/path/to/documents": [".pdf", ".doc", ".docx", ".txt"],
        "/path/to/music": [".mp3", ".wav", ".flac"],
        "/path/to/videos": [".mp4", ".avi", ".mov"]
    }
}
```

- `source_directory`: The directory containing the files to be sorted. If not specified, the current directory will be used.
- `mappings`: A dictionary where each key is a destination directory, and the value is a list of file extensions that should be moved to that directory.

## Example

Given the configuration above, a file named `vacation.jpg` in the source directory would be moved to `/path/to/images/vacation.jpg`.

## Notes

- The script will skip any subdirectories in the source directory.
- If a file's extension doesn't match any in the configuration, it will remain in the source directory.
- If a destination directory doesn't exist, it will be created.

## License

This project is open source and available under the [GNU GENERAL PUBLIC LICENSE](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/emerald-developer/pySort/issues) if you want to contribute.

## Author

emerald-developer