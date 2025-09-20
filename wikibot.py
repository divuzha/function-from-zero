from mylib.bot import scrape
import click

@click.command()
@click.option('--name', help='Web page we want to scrape')
@click.option('--length', help='length of the output')
def cli(name, length):
    result = scrape(name, length=length)
    click.echo(click.style(f"{result}", bg="green", fg="white"))

if __name__ == '__main__':
    cli()