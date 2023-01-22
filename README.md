# anonymfile
upload tool for anonymousfile.com

## upload example
```python
import os
import anonymfile

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'BigBuckBunny.mp4')
r = anonymfile.anonymfile().upload(file_path)
print(r) # print {'name': 'BigBuckBunny.mp4', 'url': 'https://anonymfile.com/6N0jd'}
```
