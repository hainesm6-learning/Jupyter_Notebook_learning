# Jupyter Notebook notes

- [Jupyter Notebook notes](#jupyter-notebook-notes)
  - [Description](#description)
  - [Useful resources](#useful-resources)
  - [Installation and usage](#installation-and-usage)
  - [Useful features](#useful-features)
  - [Why use Jupyter Notebook?](#why-use-jupyter-notebook)
  - [Jupyter nbviewer](#jupyter-nbviewer)
  - [Suggestions](#suggestions)

## Description

These notes were taken by [ Matthew Haines](hainesm6@gmail.com) as part of learning Jupyter Notebook.

## Useful resources

- https://jupyter-notebook.readthedocs.io/en/latest/
- [Examples of Jupyter notebooks for sciences](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#physics-chemistry-and-biology)
- [VSCode JN tutorial][jn_in_vscode_url]
- [datacamp tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook)

## Installation and usage

Making Jupyter Notebooks requires the [jupyter metapackage](https://pypi.org/project/jupyter/) is installed within your python environment. This can be accomplished by a number of package handlers including pip:

```python
pip install jupyter
```

Once jupyter has been installed within your environment, you can work with jupyter notebooks either using the web application:

```shell
$ jupyter notebook
```

 or an IDE e.g. [VSCode][jn_in_vscode_url]. Note the web application can also be accessed in WSL by pasting the url containing the port and token into a web browser.

## Useful features

- LaTeX math can be inserted into Markdown cells by encasing the math in `$$`.
- There are several **magic** commands available within the interpreter. Execute `%lsmagic` to view these. To retrieve help on these commands run them with a `?` e.g. `%alias_magic`. Some potentially useful commands are:
  - `%pdb` debugs.
  - `%writefile` saves the contents of a cell to an external file.
  - `%load` inserts code from an exertnal script.
- Widgets can be incorporated to enable simple UIs e.g. [dashboards](https://blog.dominodatalab.com/interactive-dashboards-in-jupyter/).

## Why use Jupyter Notebook?

The Jupyter Notebook enables a variety of content within one document. For instance: code, explanatory markdown text, mathematics, images etc. This makes is particularly desirable for exploring data in terms of analysis, results and interpreatation. Furthermore, analysis can be updated in real time.

## Jupyter [nbviewer](https://nbviewer.jupyter.org/)

> "...any notebook document available from a public URL or on GitHub can be shared via nbviewer. This service loads the notebook document from the URL and renders it as a static web page. The resulting web page may thus be shared with others without their needing to install the Jupyter Notebook."

## Suggestions

- As per most things, keep Jupyter Notebooks versioned controlled via GitHub.
- **Use VSCode over the web app**. VSCode seems to have more functionality and it integrates well for those using WSL. [**JupyterLab**](https://jupyterlab.readthedocs.io/en/stable/index.html) is another alternative which could provide useful extensions and functionality. However, I have not yet explored this option.

[jn_in_vscode_url]: [https://code.visualstudio.com/docs/python/jupyter-support]