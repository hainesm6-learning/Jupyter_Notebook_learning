# Jupyter Notebook notes

- [Jupyter Notebook notes](#jupyter-notebook-notes)
  - [Description](#description)
  - [Useful resources](#useful-resources)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Jupyter Notebooks in VSCode](#jupyter-notebooks-in-vscode)
  - [Useful features](#useful-features)
  - [Why use Jupyter Notebook?](#why-use-jupyter-notebook)
  - [Sharing Jupyter Notebooks](#sharing-jupyter-notebooks)
  - [Suggestions](#suggestions)

## Description

These notes were taken by [Matthew Haines](hainesm6@gmail.com) as part of learning Jupyter Notebook.

## Useful resources

- https://jupyter-notebook.readthedocs.io/en/latest/
- [Examples of Jupyter notebooks for sciences](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#physics-chemistry-and-biology)
- [VSCode JN tutorial][jn_in_vscode_url]
- [datacamp tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook) - This article is free and from my perspective struck a good balance between being practically useful and yet concise.  

## Installation

Making Jupyter Notebooks requires installation of the [jupyter metapackage](https://pypi.org/project/jupyter/) within a python environment. This can be accomplished by a number of package installers including pip:

```python
pip install jupyter
```

## Usage

Once jupyter has been installed within your environment, you can work with jupyter notebooks either using the web application:

```shell
$ jupyter notebook
```

 or an IDE e.g. [VSCode][jn_in_vscode_url]. Note the web application can also be accessed in WSL by pasting the url containing the port and token into a web browser.

### Jupyter Notebooks in VSCode

- Within VSCode, cells can be in 3 states: unselected, command mode and edit mode. Once a cell has been selected, you can switch to and from command and edit modes using the `ENTER` and `ESC` keys, respectively.
- Plots can be further explored by clicking theplot viewer buttton in the top, lefthand corner.
- Debugging involves:
  - Conversion to a *.py* file.
  - Either debugging the entire file by executing the `Python: Debug Current File in Python Interactive Window` command from the command palette.
  - Or Debugging individual cells.
  - To convert back to a *.ipynb*, execute the `Python: Export Current Python File as Jupyter Notebook` command from the command palette, replacing the existing file.

Some useful keyboard shortcuts:

Key | Action
--- | ------
A | In command mode, add cell above
B | In command mode, add cell below
Up/down arrows | Toggle between cells
Ctrl+Enter | Runs currently selected cell
M | In command mode, switch to Markdown
Y | In command mode, switch to code
L | Toggle line numbers
ENTER | In command mode, switch to edit mode
ESC | In edit mode, switch to command mode

## Useful features

- LaTeX math can be inserted into Markdown cells by encasing math in `$$` statements.
- There are several **magic** commands available within the interpreter. Execute `%lsmagic` to view these. To retrieve help on these commands run them with a `?` prefix e.g. `?%alias_magic`. Some potentially useful commands are:
  - `%pdb` debugs.
  - `%writefile` saves the contents of a cell to an external file.
  - `%load` inserts code from an exertnal script.
  - `%run` runs a file within the interpreter. This can useful for keeping code dry between modules, although it is worth considering packaging where required.
- Widgets can be incorporated to enable simple UIs e.g. [dashboards](https://blog.dominodatalab.com/interactive-dashboards-in-jupyter/).
- `%%script` is equivalent to a shebang and can be used to call a specific interpreter. One application of this is in the development of Python CLIs, for instance those developed using [click](https://click.palletsprojects.com/en/7.x/). This is achieved by calling `%%script python` and overriding sys.argv e.g. [example][click_cli_example].

## Why use Jupyter Notebook?

The Jupyter Notebook enables a variety of content within one document. For instance: code, explanatory markdown text, mathematics, images etc. This makes it particularly desirable for exploring data and code interactively and dynamically.

## Sharing Jupyter Notebooks

Often you wouldn't share the ".ipynb" directly. One option is to convert to a different file extension. One option is to use the "`$ jupyter nbconvert`" subcommand (use the "`--help`" flag for documentation).

Alrterantively, the [nbviewer](https://nbviewer.jupyter.org/) can be used:

> "...any notebook document available from a public URL or on GitHub can be shared via nbviewer. This service loads the notebook document from the URL and renders it as a static web page. The resulting web page may thus be shared with others without their needing to install the Jupyter Notebook."

## Suggestions

- As per most things, keep Jupyter Notebooks versioned controlled via Git and shareable via GitHub.
- **Use VSCode over the web app**. VSCode integrates well for those using WSL and has a lot of existing functionality. Debugging is a bit challenging but doable. [**JupyterLab**](https://jupyterlab.readthedocs.io/en/stable/index.html) is another alternative which could provide useful extensions and functionality. However, I have not yet explored this option.
- Aim to keep cells within notebooks simple and structured:
  - Aim to import packages on the first line of the first cell.
  - Limit the number of characters per line to the width of the cell.

[jn_in_vscode_url]: [https://code.visualstudio.com/docs/python/jupyter-support]
[click_cli_example]: [https://stackoverflow.com/questions/47820040/using-click-library-in-jupyter-notebook-cell]