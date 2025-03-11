# %% [markdown]
# # Python Grundlagen

# %% [markdown]
# ## Ein erstes Programm

# %% [markdown]
# * Dieses Programm macht eine Konsolenausgabe
# * Hierzu wird die [BuiltIn-Funktion](https://www.w3schools.com/python/python_ref_functions.asp) `print` genutzt

# %%
message = 'Hello World!!!'

# %%
message = 'Hugo'
message.lower()

# %%
with open('names.txt') as file:
    names = file.readlines()
names     


