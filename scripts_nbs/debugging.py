# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Some Jupyter foobar
# 
# This notebook explores some of the features of jupyter notebook.
# 
# ## First task
# 
# Explore some of the magic commands...

# %%
get_ipython().run_line_magic('pinfo', '%%script')


# %%
import matplotlib.pyplot as plt
plt.plot([1, 23, 2, 4])
plt.ylabel("some numbers")
plt.show()

# %% [markdown]
# ## Task
# 
# I'm going to try to run a python module within a jupyter notebook...

# %%
get_ipython().run_line_magic('run', './foobar_script.py "Jupyter"')

