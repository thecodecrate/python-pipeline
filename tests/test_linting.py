import subprocess


def test_ruff_compliance():
    """Test to ensure codebase is compliant with Ruff linting."""

    result = subprocess.run(
        ["uvx", "ruff", "check", "."],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert result.returncode == 0, f"Ruff found issues:\n{result.stdout}"


def test_zizmor_compliance():
    """Test to ensure codebase is compliant with Zizmor linting."""

    result = subprocess.run(
        ["uvx", "zizmor", "--min-severity", "low", ".github/workflows/"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert result.returncode == 0, f"Zizmor found issues:\n{result.stdout}"
