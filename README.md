# eos app

### Project for storing two-dimensional lists in csv and json formats using a context manager


## Features
* Context managing json files
* Context managing csv files
* Cli interface to managing and saving json or csv files
* Testing features by unittest


## Installing using GitHub
```bash
git clone https://github.com/yevhenii-nevmyvako/eos_app
````

### How to run
- Clone github repo to your directory
- Go to the project directory
- Run example:
```bash
python module.py "/path/to/output/file.csv" "[[1, 2], [3, 4]]"
python module.py "/path/to/output/file.json" "[[1, 2], [3, 4]]"
```
* Run tests:
```bash
python -m unittest tests/test_eos_app.py
```