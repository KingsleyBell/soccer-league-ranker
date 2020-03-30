# Soccer League Ranker Python CLI tool

Author: Luke Bell (lukekingsleybell@gmail.com) 

## Requirements

- Python 3
- pytest

## Install

`pip install -e .`

(You should see `Successfully installed soccer-league-ranker`)

## Usage

- stdin:
 
   ```bash
   ranker "Lions 3, Snakes 3
   Tarantulas 1, FC Awesome 0
   Lions 1, FC Awesome 1
   Tarantulas 3, Snakes 1
   Lions 4, Grouches 0"
   ```
   
- file input/output:
  
  ```
  ranker -ifile <path_to_input_file> -ofile <path_to_output_file>
  ```
  
## Testing

```bash
pytest
```
