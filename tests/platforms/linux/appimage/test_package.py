import pytest

from briefcase.console import Console, Log
from briefcase.platforms.linux.appimage import LinuxAppImagePackageCommand

from ....utils import create_file


@pytest.fixture
def package_command(tmp_path, first_app_config):
    command = LinuxAppImagePackageCommand(
        logger=Log(),
        console=Console(),
        base_path=tmp_path / "base_path",
        data_path=tmp_path / "briefcase",
    )
    # Mock the host architecture to something repeatable
    command.tools.host_arch = "wonky"

    # Ensure the dist folder exists
    (tmp_path / "base_path" / "dist").mkdir(parents=True)

    return command


def test_package_app(package_command, first_app_config, tmp_path):
    """An AppImage can be packaged."""

    # Create the app binary
    create_file(
        tmp_path
        / "base_path"
        / "build"
        / "first-app_0.0.1"
        / "linux"
        / "appimage"
        / "First_App-0.0.1-wonky.AppImage",
        "AppImage",
    )

    # Package the app
    package_command.package_app(first_app_config)

    # The binary has been copied to the dist folder
    assert (tmp_path / "base_path" / "dist" / "First_App-0.0.1-wonky.AppImage").exists()
