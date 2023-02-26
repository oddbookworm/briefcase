import pytest

from briefcase.console import Console, Log
from briefcase.exceptions import BriefcaseCommandError
from briefcase.platforms.iOS.xcode import iOSXcodeCreateCommand


@pytest.fixture
def create_command(tmp_path):
    return iOSXcodeCreateCommand(
        logger=Log(),
        console=Console(),
        base_path=tmp_path / "base_path",
        data_path=tmp_path / "briefcase",
    )


def test_binary_path(create_command, first_app_config, tmp_path):
    binary_path = create_command.binary_path(first_app_config)

    assert binary_path == (
        tmp_path
        / "base_path"
        / "build"
        / "first-app_0.0.1"
        / "iOS"
        / "Xcode"
        / "build"
        / "Debug-iphonesimulator"
        / "First App.app"
    )


def test_distribution_path(create_command, first_app_config, tmp_path):
    with pytest.raises(
        BriefcaseCommandError,
        match=r"Can't generate distribution artefacts for iOS apps.",
    ):
        create_command.distribution_path(first_app_config)
