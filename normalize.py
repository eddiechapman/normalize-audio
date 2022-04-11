import click
import pathlib
import subprocess


@click.command()
@click.option("--src", "-s",
    type=click.Path(dir_okay=True, path_type=pathlib.Path),
    help="Directory containing wav files for processing"
)
@click.option("--dest", "-d",
    type=click.Path(dir_okay=True, path_type=pathlib.Path),
    help="Directory where processed copies of audio files will be moved"
)
def normalize(src, dest):
    dest.mkdir(exist_ok=True)
    filepaths = (p for p in src.rglob("*") if p.suffix == ".wav")
    click.echo(f"Normalizing audio in {click.style(src, fg='blue')}")
    with click.progressbar(filepaths) as bar:
        for infile in bar:
            outfile = dest / infile.relative_to(src)
            outfile.parents[0].mkdir(parents=True, exist_ok=True)
            completed = subprocess.run(
                ["sox", infile, "-b", "16", outfile, "rate", "44100",  "norm", "-0.1"],
                stdout=subprocess.PIPE
            )

    click.echo(f"Normalized files saved to: {click.style(dest, fg='blue')}")
