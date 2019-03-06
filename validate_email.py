from tomerater_main import *

email_validation = TomeRater()

print(email_validation.add_user("Bob Roberts", "@roberts.com"))
print(email_validation.add_user("Bob Roberts", "bob.@roberts.com"))
print(email_validation.add_user("Bob Roberts", "bob @roberts.com"))
print(email_validation.add_user("Bob Roberts", "bob@.roberts.com"))
print(email_validation.add_user("Bob Roberts", ".bob@roberts.com"))
print(email_validation.add_user("Bob Roberts", "bob@roberts."))
print(email_validation.add_user("Bob Roberts", "bob@roberts.c"))
print(email_validation.add_user("Bob Roberts", "bob@.com"))
print(email_validation.add_user("Bob Roberts", "bobroberts.com"))
print(email_validation.add_user("Bob Roberts", "bob@roberts.co"))
print(email_validation.add_user("Bob Roberts", "bob@roberts.co.uk"))
print(email_validation.add_user("Bob Roberts", "bob@roberts.com"))

print(email_validation.users["bob@roberts.com"].change_email("bob@roberts.com"))
print(email_validation.users["bob@roberts.com"].change_email("bob@roberts.c"))

email_validation.print_users()
