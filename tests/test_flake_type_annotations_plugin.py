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
