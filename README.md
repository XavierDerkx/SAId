# SAId

SAId (Serial Alpha Identifier) is script to produce the alpha decays chains for any given isotopes.

## Description

SAId is a refactor and rewrite of an old ROOT/C++ script in Python 3, using modern software engineering practices. It's currently just a proof of concept.

## Getting Started

### Dependencies

* Pandas

* coverage (to run the unit tests) 
  
  ### Installing
  
  ```
  # using pip
  pip install -r requirements.txt
  
  # using Conda
  conda create --name <env_name> --file requirements.txt
  ```
  
  ### Executing
  
  ```
  # running the code
  python src/main.py <atomic mass> <atomic number>
  
  # running the test
  ./run_tests.sh
  ```

## Version History

* 0.1 Initial Release - November 2024
  
  ## License
  
  This project is licensed under the CeCILL 2.1 License - see the LICENCE.md file for details

## QA

* Test coverage

* PEP8-compliant

* Documentation

## Road Map

### Data

* Check/clean data source (some half-lifes are identical for all dcay channels of a given isotope)

* Update data (missing decays for heavier isotopes) -> NNDC?

* Improve data (uncertainties are missing on energies and half-lives)

### Design

* Refactor the code to get a proper module

* Redesign interface (for which functional specs?)

* Improve test coverage

* Add an UI with a Dash dashboard

* Add more search options

* Plot decay hierarchy as image (GraphViz? plotly?)

* Add a SQL DB for local (sqlite) and web (Postgre) usages

* Benchmark CSV/Dataframe VS SQL -> should all the decay chains be created once and store?

### Deploy

- Autogenerated documentation (Sphinx?)

- Dockerise

- Deploy process on a web server (Docker, Traefik)

- Add an API (REST) for the web app version as an exercice

### Version 2

- Add data analysis and statistics tools

- Add gamma decays
