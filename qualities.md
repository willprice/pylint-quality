* pylint rules https://pylint.readthedocs.io/en/latest/index.html

* Complexity
  * LOC By method (e.g. max 10)
  * Cyclomatic complexity
    * http://radon.readthedocs.io/en/latest/index.html
  * Number of methods per class (e.g. max 10)
* Dependencies
  * Coupling, discourage feature envy.
    * e.g. a method should not call more than 2 methods of another class
    * e.g. number of method calls
    * Encourage people to extract methods and move them over to envied class
    * Limit number of collaborators per class (maybe excluding superclasses?)
  * Favour composition over inheritance
  * If you're not at the top of the call stack then you can't instantiate classes/
    You can only invoke methods on objects that you are handed
* Readability
  * Can we just reuse complexity?
  * Single letter variables?
  * Very long variable names
  * Conceptual correlation
    * Red/amber/green line rating, 75% of words in names should come from
      requirements
* Duplication
  * Reuse something like simian
  * https://github.com/codeclimate/codeclimate-duplication
* Unit test assurance
  * Mutation testing
    * https://pypi.python.org/pypi/MutPy/0.5.1
    * https://github.com/sixty-north/cosmic-ray


Pylint codes and rules are available
https://pylint.readthedocs.io/en/latest/technical_reference/features.html
