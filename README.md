# Plotly-Dash Example

This repo contains a small example I made for learning the basics of Plotly and Plotly-Dash. The whole project was developed in VS Code, to familiarize with the IDE.

There are two main files of interest,

- `plotly_examples.ipynb`: this notebook file contains some examples of Plotly figures, and uses different datasets provided by Plotly itself.

- `app.py`: this Dash app contains a very simple view of the data contained in the gapminder dataset. A Dockerfile is present, that can be used to create a container where the app can be deployed for production.

Additionally, there are two files (`lib.py` and `lib_test.py`) that are not used for the above project. They were made for familiarizing with the testing environment in VS Code.
