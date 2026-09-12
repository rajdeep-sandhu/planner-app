import marimo

__generated_with = "0.24.2"
app = marimo.App(width="full", app_title="Planner")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Planner App
    """)
    return


if __name__ == "__main__":
    app.run()
