import click
import tabulate as tabulate

from db_client import get_toil_balance, update_toil_balance, get_all_users_data

TOIL_DESCRIPTION = """
TOIL stands for "Time Off In Lieu." It is a policy in many workplaces where employees can take time off as compensation for working extra hours beyond their regular working hours.
"""


@click.group(help=TOIL_DESCRIPTION)
def cli():
    pass


@click.command()
@click.option("--user-id", required=True, help="User ID for the TOIL balance.")
@click.option(
    "--submit-hours",
    required=True,
    type=int,
    help="Number of TOIL hours to submit.",
)
def submit_toil(user_id, submit_hours):
    """Submit TOIL hours and update the balance."""
    current_toil_hours, current_toil_days_off = get_toil_balance(user_id)

    # Update TOIL balance
    new_toil_hours = current_toil_hours + submit_hours
    update_toil_balance(user_id, new_toil_hours)

    click.echo(f"TOIL balance updated. Your current balance: {new_toil_hours} hours.")

    # Check if new balance qualifies for days off
    if new_toil_hours // 8 > current_toil_days_off:
        click.echo(f"Congratulations! You have earned {new_toil_hours // 8 - current_toil_days_off} day(s) off!")


cli.add_command(submit_toil)


@click.command()
@click.option("--user-id", required=True, help="User ID for the TOIL balance.")
@click.option(
    "--delete-hours",
    required=True,
    type=int,
    help="Number of TOIL hours to delete.",
)
def delete_toil(user_id, delete_hours):
    """Delete TOIL hours and update the balance."""
    current_toil_hours, current_toil_days_off = get_toil_balance(user_id)

    # Calculate the new TOIL balance after deleting hours
    new_toil_hours = max(0, current_toil_hours - delete_hours)
    update_toil_balance(user_id, new_toil_hours)

    click.echo(f"TOIL balance updated. Your current balance: {new_toil_hours} hours.")

    # Check if new balance qualifies for days off
    if new_toil_hours // 8 > current_toil_days_off:
        click.echo(f"Congratulations! You have earned {new_toil_hours // 8 - current_toil_days_off} day(s) off!")


cli.add_command(delete_toil)


@click.command()
@click.option("--user-id", required=True, help="User ID for the TOIL balance.")
def check_balance(user_id):
    """Check the current TOIL balance."""
    toil_hours, toil_days_off = get_toil_balance(user_id)
    click.echo(f"Your TOIL balance: {toil_hours} hours, Days off: {toil_days_off}")


cli.add_command(check_balance)


@click.command()
def show_all_users():
    """Show a table of all users and their total TOIL days and hours."""
    all_users_data = []

    # Get all users' data
    all_users_data = get_all_users_data()

    headers = ["User ID", "TOIL Hours", "TOIL Days Off"]
    table = tabulate.tabulate(all_users_data, headers=headers, tablefmt="grid")
    click.echo(table)


cli.add_command(show_all_users)

if __name__ == "__main__":
    cli()
