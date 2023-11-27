# Python to LaTeX Algorithm Converter

The Python to LaTeX Algorithm Converter is a tool that translates Python code snippets into equivalent LaTeX algorithms. This can be particularly useful for documenting algorithms in academic papers, reports, or any LaTeX-supported document.

## How to run 

You can use the `conv` executable to convert a given python file to its quivilent latex algorythm file.  
```bash
./conv the_file.py
```
The above code will output the new latex file into `the_file.py.tex`

# Example 
The example code is contained in the `ex` directory.  From the root directory of this subproject, execute the following code:
```bash
./conv ex/factorial.py
``` 
The function will result in the creation of the file `ex/factorial.py.tex` which will contain a near equivilant (or at least a good base) of the given python code in `ex/factorial.py`