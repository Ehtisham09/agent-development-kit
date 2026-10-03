# =============================================================================
# FILE: file_writer_tool.py
# PURPOSE:
#   This module defines tools for database agents to persist generated database
#   schemas and SQLite database files. It includes functions for writing SQL
#   requirements, design specifications, and complete SQLite databases.
# =============================================================================

import sqlite3
import datetime
from pathlib import Path


# -----------------------------------------------------------------------------
# TOOL FUNCTION: write_database_file
# -----------------------------------------------------------------------------
def write_database_file(sql_statements: str) -> dict:
    """
    Creates a SQLite database file from a series of SQL statements.

    Args:
        sql_statements (str): Complete SQL script containing CREATE TABLE,
                             CREATE INDEX, and other DDL statements.

    Returns:
        dict: A dictionary containing the status and generated database filename.
    """

    # Get the current date and time, format it as YYMMDD_HHMMSS.
    # Example: "250611_142317"
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

    # Construct the output filename using the timestamp.
    # Example: "output/250611_142317_database.sqlite"
    filename = f"output/{timestamp}_database.sqlite"

    # Ensure the "output" directory exists. If it doesn't, create it.
    # `exist_ok=True` prevents an error if the directory already exists.
    Path("output").mkdir(exist_ok=True)

    try:
        # Create a new SQLite database connection.
        connection = sqlite3.connect(filename)
        cursor = connection.cursor()

        # Split the SQL script into individual statements and execute each one.
        # This handles multiple CREATE TABLE and CREATE INDEX statements.
        statements = [stmt.strip() for stmt in sql_statements.split(';') if stmt.strip()]

        for statement in statements:
            cursor.execute(statement)

        # Commit all changes to the database.
        connection.commit()

        # Close the database connection.
        connection.close()

        # Return success status with the filename.
        return {
            "status": "success",
            "file": filename,
            "message": f"Database created successfully with {len(statements)} statements executed."
        }

    except sqlite3.Error as e:
        # If there's a SQLite error, return the error details.
        return {
            "status": "error",
            "file": filename,
            "message": f"SQLite Error: {str(e)}"
        }

    except Exception as e:
        # If there's any other error, return the error details.
        return {
            "status": "error",
            "file": filename,
            "message": f"Error: {str(e)}"
        }


# -----------------------------------------------------------------------------
# TOOL FUNCTION: write_requirements_to_file
# -----------------------------------------------------------------------------
def write_requirements_to_file(content: str) -> dict:
    """
    Writes database requirements documentation to a timestamped text file.

    Args:
        content (str): Database requirements documentation as a string.

    Returns:
        dict: A dictionary containing the status and generated filename.
    """

    # Get the current date and time, format it as YYMMDD_HHMMSS.
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

    # Construct the output filename.
    # Example: "output/250611_142317_requirements.txt"
    filename = f"output/{timestamp}_requirements.txt"

    # Ensure the "output" directory exists.
    Path("output").mkdir(exist_ok=True)

    try:
        # Write the requirements content to the file.
        Path(filename).write_text(content, encoding="utf-8")

        # Return success status with the filename.
        return {
            "status": "success",
            "file": filename,
            "message": "Requirements document saved successfully."
        }

    except Exception as e:
        # If there's an error, return the error details.
        return {
            "status": "error",
            "file": filename,
            "message": f"Error: {str(e)}"
        }


# -----------------------------------------------------------------------------
# TOOL FUNCTION: write_design_to_file
# -----------------------------------------------------------------------------
def write_design_to_file(content: str) -> dict:
    """
    Writes database design specification to a timestamped text file.

    Args:
        content (str): Database design specification as a string.

    Returns:
        dict: A dictionary containing the status and generated filename.
    """

    # Get the current date and time, format it as YYMMDD_HHMMSS.
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

    # Construct the output filename.
    # Example: "output/250611_142317_design.txt"
    filename = f"output/{timestamp}_design.txt"

    # Ensure the "output" directory exists.
    Path("output").mkdir(exist_ok=True)

    try:
        # Write the design content to the file.
        Path(filename).write_text(content, encoding="utf-8")

        # Return success status with the filename.
        return {
            "status": "success",
            "file": filename,
            "message": "Design specification saved successfully."
        }

    except Exception as e:
        # If there's an error, return the error details.
        return {
            "status": "error",
            "file": filename,
            "message": f"Error: {str(e)}"
        }
