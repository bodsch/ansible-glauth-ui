 

## `glauth_ui_config`

```yaml
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
```
