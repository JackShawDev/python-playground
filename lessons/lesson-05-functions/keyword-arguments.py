def create_account(username, role, active):
    print(username, role, active)

create_account(
    username="Jack",
    role="admin",
    active=True
)

create_account(
    active=True,
    username="Jack",
    role="admin"
)