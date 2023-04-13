
## `glauth_ui_cfg_users`

Behind the user administration of glauth-ui ...


The admin is also just a user!

To give them extended rights, they must be added to the corresponding group `admin`.


If users are to be able to manage their own password, they must be added to the group 'can_change_pass'.

```yaml
glauth_ui_cfg_users:
  start: 5000               # start with this uid number
  gid:
    admin: 5501             # members of this group are admins
    can_change_pass: 5501   # members of this group can change their password
    use_otp: 5501           # members of this group use OTP
```
