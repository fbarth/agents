# Search implementations

In this folder we have four (4) groups of source code:

* `Graph.py`, `Map.py`, and `SearchAlgoritms.py`: those files implement the search algorithms discussed in this subject;
* `VacuumWorld.py`, `PlusOneTwo.py`, `TaxiDriver.py`, and `N_QueensProblem.py`: are implementations of examples that we see in this subject;
* `ProblemSpecificationExample.py`, and `VacuumWorldQuestion.py`: are mockups that you can reuse in order to deliver your exercises. 
* Files starting with `test_*` are testing files. You can run those files to understand the algorithm's behavior or to check if your implementation is correct. 

## Testing scripts

* Execute all tests: `pytest`. 
* Execute all tests showing stdout `pytest --capture=tee-sys`. 
* Execute a specific file test: `pytest <file.py>`.
* Execute a single test, for example: `pytest test_VacuumWorld.py -k 'test_BPI'`.

You can also use the test scripts to understand the behavior of some algorithms. For example, try to run this command:

```bash
pytest test_PlusOneTwo.py --capture=tee-sys
```




