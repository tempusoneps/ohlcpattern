import typer
import pandas as pd
from ohlcpattern.candlestick import CandlestickPatterns
from ohlcpattern.candlesticks import GET_FULL
from pathlib import Path
from typing import Optional

app = typer.Typer(help="OHLC Pattern Extraction CLI", add_completion=False)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        help="Show current version and exit.",
        is_eager=True,
    ),
):
    if version:
        typer.echo("ohlcpattern version 0.1.0")
        raise typer.Exit()

    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()


@app.command()
def extract(
    input_file: Path = typer.Argument(..., help="Path to the input CSV file", exists=True),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Path to the output CSV file"),
):
    """
    Extract candlestick patterns from an OHLC CSV file.
    """
    try:
        typer.echo(f"Reading data from {input_file}...")
        df = pd.read_csv(input_file)
        
        # Basic validation of required columns
        required_cols = {"Open", "High", "Low", "Close"}
        if not required_cols.issubset(set(df.columns)):
            typer.echo(f"Error: Input CSV must contain columns: {', '.join(required_cols)}", err=True)
            raise typer.Exit(code=1)
            
        typer.echo("Processing patterns...")
        cp = CandlestickPatterns(df)
        cp._add(GET_FULL)
        result_df = cp.pattern_modeling()
        
        if output:
            result_df.to_csv(output, index=False)
            typer.echo(f"Successfully saved results to {output}")
        else:
            # If no output is specified, print the first few rows with patterns
            typer.echo(result_df[result_df['model'] != ''].head())
            typer.echo("\nTip: Use --output to save the full results to a file.")
            
    except Exception as e:
        typer.echo(f"An error occurred: {e}", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
