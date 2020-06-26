# Medicine name seperator
this project is used to seperate medicine names from the massive json of pakistan DRA. outputs the list of medicine names available in pakistan. it formats the json of medicines that contains name price etc and only outputs the name. you can change it for your own use

# RUN
first install
`brew install gawk`

then type in root of directory
`python3 main.py`

then type in terminal when code successfully run
`awk 'NF' temp.txt > medicineNames.txt`