import subprocess


def test_flake_process_runs_correctly() -> None:
    """Confirms that flake8 runs correctly via subprocess."""
    process = subprocess.Popen(
        ["flake8", "tests/fixtures/valid_flake_file.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, _ = process.communicate()

    assert len(stdout) == 0


def test_plugin_properly_detects_errors() -> None:
    """Confirms that errors are properly returned from flake."""
    process = subprocess.Popen(
        ["flake8", "tests/fixtures/invalid_flake_file.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, _ = process.communicate()

    assert b"tests/fixtures/invalid_flake_file.py:7:5: TAN001:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:11:21: TAN002:" in stdout
