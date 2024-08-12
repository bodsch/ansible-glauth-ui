
# Ansible Role:  `glauth-ui` 

Ansible role to install and configure [glauth-ui](https://github.com/yvesago/glauth-ui-light).

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-glauth-ui/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-glauth-ui/glauth-ui)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-glauth-ui/glauth-ui)][releases]
[![Ansible Downloads](https://img.shields.io/ansible/role/d/bodsch/glauth_ui?logo=ansible)][galaxy]

[ci]: https://github.com/bodsch/ansible-glauth-ui/actions
[issues]: https://github.com/bodsch/ansible-glauth-ui/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-glauth-ui/releases
[galaxy]: https://galaxy.ansible.com/ui/standalone/roles/bodsch/glauth_ui


If `latest` is set for `glauth_ui_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/bin/glauth-ui/${glauth_ui_version}` and later linked to `/usr/bin`. 
This should make it possible to downgrade relatively safely.

The Prometheus archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/glauth-ui`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `glauth_ui_direct_download` to `true`.

## Requirements & Dependencies

Ansible Collections

- [bodsch.core](https://github.com/bodsch/ansible-collection-core)
- [bodsch.scm](https://github.com/bodsch/ansible-collection-scm)

```bash
ansible-galaxy collection install bodsch.core
ansible-galaxy collection install bodsch.scm
```
or
```bash
ansible-galaxy collection install --requirements-file collections.yml
```

## Operating systems

Tested on

* Arch Linux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.10


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-glauth-ui/tags)!

## IMPORTANT

> **glauth-ui only supports the configuration file and not a database backend!**  
> glauth-ui-light update only users and groups.  
> All lines after the first `[[users]]` in glauth configuration file will be updated.  
> The use of same model structure than glauth V2 allow to keep manual edition of non managed features as  
> `capabilities`, `loginShell`, `sshkeys`, `otpsecret`, `yubikey`, `includegroups`, ....  
> Only comments on these lines are lost.
>
> For more information, please read the [project documentation](https://github.com/yvesago/glauth-ui-light/blob/main/README.md)!


## Configuration

```yaml
glauth_ui_version: 1.4.3

glauth_ui_release_download_url: https://github.com/yvesago/glauth-ui-light/releases

glauth_ui_system_user: glauth-ui
glauth_ui_system_group: glauth-ui
glauth_ui_config_dir: /etc/glauth-ui
glauth_ui_data_dir: /var/lib/glauth-ui

glauth_ui_direct_download: false

glauth_ui_config: {}
glauth_ui_security: {}
glauth_ui_ssl: {}
glauth_ui_logs: {}
glauth_ui_locale: {}
glauth_ui_passpolicy: {}
glauth_ui_cfg_users: {}
glauth_ui_cfg_groups: {}
```

- [glauth_ui_config](docs/glauth_ui_config.md)
- [glauth_ui_security](docs/glauth_ui_security.md)
- [glauth_ui_ssl](docs/glauth_ui_ssl.md)
- [glauth_ui_logs](docs/glauth_ui_logs.md)
- [glauth_ui_locale](docs/glauth_ui_locale.md)
- [glauth_ui_passpolicy](docs/glauth_ui_passpolicy.md)
- [glauth_ui_cfg_users](docs/glauth_ui_cfg_users.md)
- [glauth_ui_cfg_groups](docs/glauth_ui_cfg_groups.md)

---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
