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
        "flameshot",
        "kerberoast",
        "gobuster",
        "mimikatz",
        "mono-complete",
        "nikto",
        "powershell-empire",
        "powersploit",
        "responder",
        "seclists",
        "sublist3r",
        "veil",
    ],
)
def test_packages(host, pkg):
    """Test that appropriate packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize(
    "pkg",
    ["mitm6"],
)
def test_pip_packages(host, pkg):
    """Test that appropriate pip packages were installed."""
    assert pkg in host.pip_package.get_packages(pip_path="pip3")


@pytest.mark.parametrize(
    "dir",
    [
        "aquatone",
        "CACTUSTORCH",
        "checkpwnedemails",
        "datapipe",
        "demiguise",
        "dirsearch",
        "dns-profile-randomizer",
        "DomainTrustExplorer",
        "Egress-Assess",
        "ftpenum",
        "GhostPack/Lockless",
        "GhostPack/Rubeus",
        "GhostPack/SafetyKatz",
        "GhostPack/Seatbelt",
        "GhostPack/SharpDPAPI",
        "GhostPack/SharpDump",
        "GhostPack/SharpRoast",
        "GhostPack/SharpUp",
        "GhostPack/SharpWMI",
        "gnmap-parser",
        "Hasher",
        "ImpDump",
        "Internal-Monologue",
        "KeeThief",
        "mikto",
        "Misc",
        "morphHTA",
        "MS17-010",
        "nlzr",
        "PowerTools",
        "PowerUpSQL",
        "RandomPS-Scripts",
        "SessionGopher",
        "SharpShooter",
        "shellshocker-pocs",
        "SimplyEmail",
        "SimplyTemplate",
        "sshenum",
        "TikiTorch",
        "ysoserial",
    ],
)
def test_directories(host, dir):
    """Test that appropriate directories were created."""
    dir_full_path = f"/tools/{dir}"
    directory = host.file(dir_full_path)
    assert directory.exists
    assert directory.is_directory
    # Make sure that the directory is not empty
    assert host.run_expect([0], f'[ -n "$(ls -A {dir_full_path})" ]')
