
# Ansible Role:  `glauth-ui` 

Ansible role to install and configure [/glauth-ui](https://github.com/yvesago/glauth-ui-light).

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bodsch/ansible-/glauth-ui/CI)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-/glauth-ui)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-/glauth-ui)][releases]

[ci]: https://github.com/bodsch/ansible-/glauth-ui/actions
[issues]: https://github.com/bodsch/ansible-/glauth-ui/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-/glauth-ui/releases


If `latest` is set for `glauth_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/bin/glauth-ui/${glauth_ui_version}` and later linked to `/usr/bin`. 
This should make it possible to downgrade relatively safely.

The Prometheus archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/glauth-ui`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `glauth_direct_download` to `true`.


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

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-/glauth-ui/tags)!

## Configuration

```yaml
glauth_ui_version: 1.4.3

glauth_ui_release_download_url: https://github.com/yvesago/glauth-ui-light/releases

glauth_ui_system_user: glauth-ui
glauth_ui_system_group: glauth-ui
glauth_ui_config_dir: /etc/glauth-ui
glauth_ui_data_dir: /var/lib/glauth-ui

glauth_ui_direct_download: false

glauth_ui_config:
  debug: false
  db_file: "/etc/glauth/glauth.cfg"
  listen:
    address: "0.0.0.0"
    port: "8080"
  application:
    name: "glauth-ui-light"
    description: "Manage users and groups for glauth ldap server"
  mask_otp: false
  defaults:
    home_dir: "/home"
    login_shell: "/bin/false"

glauth_ui_security:
  trusted_proxies:
    - "127.0.0.1"
    - "::1"
  # TODO set random secrets for CSRF token
  csrf_random: "secret1"

glauth_ui_ssl:
  crt: ""
  key: ""

glauth_ui_logs:
  path: "/var/logs/glauth-ui/"
  rotation_count: 7

glauth_ui_locale:
  lang: "en"
  path: "{{ glauth_ui_config_dir }}/locales/"
  langs:
    - "en-US"

glauth_ui_passpolicy:
  min: 6
  max: 42
  allow_reads_sha256: true  # to be set to false when all passwords are bcrypt
  entropy: 60               # optional constraint. Between 40 and 120 for very high strength password

glauth_ui_cfg_users:
  start: 5000               # start with this uid number
  gid:
    admin: 5501             # members of this group are admins
    can_change_pass: 5501   # members of this group can change their password
    use_otp: 5501           # members of this group use OTP

glauth_ui_cfg_groups:
  start: 5500               # start with this gid number
```

---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

`FREE SOFTWARE, HELL YEAH!`
