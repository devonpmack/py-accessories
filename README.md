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

loader = SaveLoad('config.json', create=True)
output_file = loader.get('output', default='/home/out.txt')
open(output_file, 'w').write('Hello World')
```

#### TimeLog
```python
from pyaccessories.TimeLog import Timer

t = Timer(log_file='log.txt')
t.time_print('Hi')
```
