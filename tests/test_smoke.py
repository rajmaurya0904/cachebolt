"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import cachebolt


def test_version_is_set() -> None:
    assert cachebolt.__version__
