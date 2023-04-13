
## `glauth_ui_passpolicy`

```yaml
glauth_ui_passpolicy:
  min: 6
  max: 42
  allow_reads_sha256: true  # to be set to false when all passwords are bcrypt
  entropy: 60               # optional constraint. Between 40 and 120 for very high strength password
```
