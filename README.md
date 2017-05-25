# pyaccessories
All my python accessory classes

## Installation

```console
git clone https://github.com/devonpmack/pyaccessories.git
cd dist
pip install py-accessories-*.tar
```

### Submodule
```console
git submodule add https://github.com/devonpmack/pyaccessories.git
```

#### SaveLoad
```python
from pyaccessories.SaveLoad import SaveLoad

# Create a new SaveLoad instance which loads the file config.json, creating it
# if it doesn't already exist
loader = SaveLoad('config.json', create=True)

# Loads the value 'output' from the config file and stores it in the variable output_file
# if output isn't in the config file then ask the user to input it. To turn this ask off use
# ask=False and then it will throw an error if the config option isn't there
output_file = loader.get('output', default='/home/out.txt')

# Use the loaded config option and write to the file
open(output_file, 'w').write('Hello World')
```

#### TimeLog
```python
from pyaccessories.TimeLog import Timer

# Create a new instance of Timer which will log all time_prints to log.txt
# If no log file is specified it will not log
t = Timer(log_file='log.txt')

# Set the colour to lime green
t.set_colour(30)

# Print the message hi
t.time_print('Hi')
```
