import subprocess


def test_ruff_compliance():
    """Test to ensure codebase is compliant with Ruff linting."""

    result = subprocess.run(
        ["ruff", "check", "."],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert result.returncode == 0, f"Ruff found issues:\n{result.stdout}"
