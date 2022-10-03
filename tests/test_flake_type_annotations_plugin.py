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

    assert b"tests/fixtures/invalid_flake_file.py:3:12: TAN002:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:3:22: TAN001:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:4:17: TAN001:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:4:23: TAN002:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:4:34: TAN002:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:7:21: TAN002:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:7:26: TAN001:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:8:21: TAN002:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:8:26: TAN001:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:17:25: TAN001:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:17:43: TAN001:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:22:26: TAN002:" in stdout
    assert b"tests/fixtures/invalid_flake_file.py:22:41: TAN002:" in stdout
