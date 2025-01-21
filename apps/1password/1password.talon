app.exe: 1password.exe
-
password new: user.password_new()
password dup: user.password_duplicate()
password edit: user.password_edit()
password delete: user.password_delete()
pass copy: key(ctrl-shift-c)