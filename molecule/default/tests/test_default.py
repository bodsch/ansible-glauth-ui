# coding: utf-8
from __future__ import annotations, unicode_literals

import os

import pytest
import testinfra.utils.ansible_runner
from helper.molecule import get_vars, infra_hosts, local_facts

testinfra_hosts = infra_hosts(host_name="instance")

# --- tests -----------------------------------------------------------------

# _facts = local_facts(host=host, fact="glauth_ui")


@pytest.mark.parametrize(
    "dirs",
    [
        "/etc/glauth-ui",
        "/usr/local/opt/glauth-ui",
    ],
)
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


def test_files(host, get_vars):
    """ """
    distribution = host.system_info.distribution
    release = host.system_info.release

    print(f"distribution: {distribution}")
    print(f"release     : {release}")

    version = local_facts(host=host, fact="glauth_ui").get("version")

    install_dir = get_vars.get("glauth_ui_install_path")
    defaults_dir = get_vars.get("glauth_ui_defaults_directory")
    config_dir = get_vars.get("glauth_ui_config_dir")

    if "latest" in install_dir:
        install_dir = install_dir.replace("latest", version)

    files = []
    files.append("/usr/bin/glauth-ui")

    if install_dir:
        files.append(f"{install_dir}/glauth-ui")
    if defaults_dir and not distribution == "artix":
        files.append(f"{defaults_dir}/glauth-ui")
    if config_dir:
        files.append(f"{config_dir}/glauth-ui.cfg")

    print(files)

    for _file in files:
        f = host.file(_file)
        assert f.is_file


def test_user(host, get_vars):
    """ """
    user = get_vars.get("glauth_ui_system_user", "glauth-ui")
    group = get_vars.get("glauth_ui_system_group", "glauth-ui")

    assert host.group(group).exists
    assert host.user(user).exists
    assert group in host.user(user).groups
    assert host.user(user).home == "/nonexistent"


def test_service(host, get_vars):
    service = host.service("glauth-ui")
    assert service.is_enabled
    assert service.is_running


def test_open_port(host, get_vars):
    """ """
    listen_address = "127.0.0.1:8080"

    service = host.socket(f"tcp://{listen_address}")
    assert service.is_listening
