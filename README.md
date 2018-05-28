# depreciation-engineering-econ-scripts
I created these scripts to double check my engineering economics homework on four standard depreciation methods.

### Straight-Line (SL),
To run: `python sl.py 4000 700  5`
  - 4000 is the Book Value (initial cost)
  - 700 is the Salvage Value
  - 5 is the number of depreciation years

### Double Declining Balance (DDB)
To run: `python DDB.py 4000 700  5`
  - 4000 is the Book Value (initial cost)
  - 700 is the Salvage Value
  - 5 is the number of depreciation years
### Sum-Of-Years-Digit (SOYD)
To run: `python SOYD.py 4000 700  5`
  - 4000 is the Book Value (initial cost)
  - 700 is the Salvage Value
  - 5 is the number of depreciation years


Usage in terminal(Except for MACRS):
### `python  "method_name.py"  Book-Value  Salvage-Value  Depreciation-Year(s)`
Salvage-Value can be 0.


### `Modified Accelerated Cost Recovery System (MACRS)` for Non-residential property
To run: 'python MACRS.py 4000  5'
  - 4000 is the Book Value (initial cost)
  - 5 is the number of depreciation years
  ##### Note* Salvage value is assumed to be 0 for MACRS
