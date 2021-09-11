#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    os.environ["CUSTOM_COMPILE_COMMAND"] = "requirements/compile.py"
    os.environ.pop("PIP_REQUIRE_VIRTUALENV")
    common_args = [
        "-m",
        "piptools",
        "compile",
        "--generate-hashes",
        "--allow-unsafe",
    ] + sys.argv[1:]
    # mysqlclient requirements found on each version's "Databases" documentation page:
    # https://docs.djangoproject.com/en/3.0/ref/databases/#mysql-db-api-drivers
    subprocess.run(
        [
            "python3.6",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-P",
            "mysqlclient>=1.3.13",
            "-o",
            "py36-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.6",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-P",
            "mysqlclient>=1.3.13",
            "-o",
            "py36-django30.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.6",
            *common_args,
            "-P",
            "Django>=3.1a1,<3.2",
            "-P",
            "mysqlclient>=1.4.0",
            "-o",
            "py36-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.6",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-P",
            "mysqlclient>=1.4.0",
            "-o",
            "py36-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.7",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-P",
            "mysqlclient>=1.3.13",
            "-o",
            "py37-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.7",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-P",
            "mysqlclient>=1.3.13",
            "-o",
            "py37-django30.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.7",
            *common_args,
            "-P",
            "Django>=3.1a1,<3.2",
            "-P",
            "mysqlclient>=1.4.0",
            "-o",
            "py37-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.7",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-P",
            "mysqlclient>=1.4.0",
            "-o",
            "py37-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-P",
            "mysqlclient>=1.3.13",
            "-o",
            "py38-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-P",
            "mysqlclient>=1.3.13",
            "-o",
            "py38-django30.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "-P",
            "Django>=3.1a1,<3.2",
            "-P",
            "mysqlclient>=1.4.0",
            "-o",
            "py38-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-P",
            "mysqlclient>=1.4.0",
            "-o",
            "py38-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-P",
            "mysqlclient>=1.3.13",
            "-o",
            "py39-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-P",
            "mysqlclient>=1.3.13",
            "-o",
            "py39-django30.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "-P",
            "Django>=3.1a1,<3.2",
            "-P",
            "mysqlclient>=1.4.0",
            "-o",
            "py39-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-P",
            "mysqlclient>=1.4.0",
            "-o",
            "py39-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
