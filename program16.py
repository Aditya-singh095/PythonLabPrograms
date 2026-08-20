import traceback


# --------------------------------
# Custom Exceptions
# --------------------------------

class FileProcessorError(Exception):
    """Base exception for file processing."""
    pass


class InvalidFileFormatError(FileProcessorError):
    """Raised when the file format is invalid."""
    pass


class InvalidDataError(FileProcessorError):
    """Raised when file data is invalid."""
    pass


# --------------------------------
# File Processor
# --------------------------------

def process_file(filename):
    file = None

    try:
        # Open file
        file = open(filename, "r")

        # Check file extension
        if not filename.endswith(".txt"):
            raise InvalidFileFormatError(
                "Only .txt files are supported."
            )

        lines = file.readlines()

        if not lines:
            raise InvalidDataError(
                "The file is empty."
            )

        numbers = []

        for line in lines:
            line = line.strip()

            if line:
                try:
                    numbers.append(int(line))
                except ValueError:
                    raise InvalidDataError(
                        f"Invalid number: {line}"
                    )

    except FileNotFoundError:
        print("Error: File does not exist.")

    except InvalidFileFormatError as e:
        print("Format Error:", e)

    except InvalidDataError as e:
        print("Data Error:", e)

        # Log traceback
        with open("error.log", "a") as log:
            traceback.print_exc(file=log)

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected error:", e)

        # Log unexpected error
        with open("error.log", "a") as log:
            traceback.print_exc(file=log)

    else:
        # Runs only when no exception occurs
        print("File processed successfully.")
        print("Numbers:", numbers)
        print("Total:", sum(numbers))

    finally:
        # Always executes
        if file is not None:
            file.close()

        print("File resource cleanup completed.")


# --------------------------------
# Example
# --------------------------------

process_file("numbers.txt")
