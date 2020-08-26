# messingWithStockData
Pull stock data and manipulate it 


# Setup

### Virtual Environment

#### in the folder/directory above the folder/repository run:
pip install virtualenv (could probably be anywhere but whatever)
#### change to the repository using
cd messingWithStockData
#### setup the virtual environment by
python -m virtualenv .
######  ( "." is the location for virtualenv installation, in this case the repo )
#### finally, activate the venv
.\Scripts\activate

later to deactivate, in command line do: 
"deactivate"


### Dependencies
Following: https://www.youtube.com/watch?v=d2kXmWzfS0w

pip install pandas
pip install alpha_vantage

Go to https://www.alphavantage.co/support/#api-key to get your API key

### Notes
A file imported to app.py is ignored because it has authentification stuff, don't want online

## TODO
Move files and figure out how to import files into others?