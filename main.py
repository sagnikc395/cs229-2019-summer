import click

@click.command()
def init_project():
    click.echo("welcome to the cs229-2019 course\n")
    click.echo("this repo stores my solution")



def main():
    init_project()


if __name__ == "__main__":
    main()
