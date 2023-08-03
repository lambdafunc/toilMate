# toilMate
TOIL counting tool 

Fairly simple and straight forward tool to keep track of TOIL hours ;)
Usage:
```
✦ ❯ python cli.py
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

  TOIL stands for "Time Off In Lieu." It is a policy in many workplaces where
  employees can take time off as compensation for working extra hours beyond
  their regular working hours.

Options:
  --help  Show this message and exit.

Commands:
  check-balance   Check the current TOIL balance.
  delete-toil     Delete TOIL hours and update the balance.
  show-all-users  Show a table of all users and their total TOIL days and...
  submit-toil     Submit TOIL hours and update the balance.
```

---
```
✦ ❯ python cli.py submit-toil --user-id user1 --submit-hours 8
TOIL balance updated. Your current balance: 8 hours.
Congratulations! You have earned 1 day(s) off!

✦ ❯ python cli.py submit-toil --user-id user2 --submit-hours 12
TOIL balance updated. Your current balance: 12 hours.
Congratulations! You have earned 1 day(s) off!

❯ python cli.py show-all-users
+-----------+--------------+-----------------+
| User ID   |   TOIL Hours |   TOIL Days Off |
+===========+==============+=================+
| testuser  |            8 |               1 |
+-----------+--------------+-----------------+
| user1     |            8 |               1 |
+-----------+--------------+-----------------+
| user2     |           12 |               1 |
+-----------+--------------+-----------------+

❯ python cli.py check-balance --user-id user1
Your TOIL balance: 8 hours, Days off: 1

❯ python cli.py delete-toil --user-id user1  --delete-hours 4
TOIL balance updated. Your current balance: 4 hours.

❯ python cli.py show-all-users
+-----------+--------------+-----------------+
| User ID   |   TOIL Hours |   TOIL Days Off |
+===========+==============+=================+
| testuser  |            8 |               1 |
+-----------+--------------+-----------------+
| user1     |            4 |               0 |
+-----------+--------------+-----------------+
| user2     |           12 |               1 |
+-----------+--------------+-----------------+
```