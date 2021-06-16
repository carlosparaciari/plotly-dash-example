# Plotly-Dash Example

This repo contains a small example I made for learning the basis of Plotly and Plotly-Dash. The whole project was developed in VS Code, to familiarize with the IDE.

There are two main files of interest,

- `plotly_examples.ipynb`: this notebook file contains some examples of plotly figures, and uses different datasets provided by plotly itself.

- `app.py`: this Dash app contains a very simple view on the data contained in the gapminder dataset. A dockerfile is present, that can be used to create a container where the app can be deployed for production.

Additionally, there are two files (`lib.py` and `lib_test.py`) that are not used for the above project. They were made to familiarize with the testing environement in VS Code.
