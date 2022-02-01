# If you have the .py file somewhere on your computer, you can create an alias
# in your .bash_profile file and run this calculator on your terminal
# without having to type in the full path of the .py file each time.

# Either of these will work

# Change to main2.py as needed

alias 2021-taxes-calculator=py { pathToPythonFile }/main3.py

function 2021-taxes-calculator() {
    py { pathToPythonFile }/main3.py
}
