"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "pkg",
    [
        "crackmapexec",
        "eyewitness",
        "powershell-empire",
        "powersploit",
        "responder",
        "seclists",
        "veil",
    ],
)
def test_packages(host, pkg):
    """Test that appropriate packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize(
    "dir",
    [
        "datapipe",
        "dirsearch",
        "DomainTrustExplorer",
        "Egress-Assess",
        "ftpenum",
        "Hasher",
        "ImpDump",
        "KeeThief",
        "shellshocker-pocs",
        "SimplyEmail",
        "SimplyTemplate",
        "sshenum",
        "ysoserial",
    ],
)
def test_directories(host, dir):
    """Test that appropriate directories were created."""
    directory = host.file(f"/tools/{dir}")
    assert directory.exists
    assert directory.is_directory
    # Make sure that the directory is not empty
    assert host.run_expect([0], f'[ -n "$(ls -A /tools/{dir})" ]')
