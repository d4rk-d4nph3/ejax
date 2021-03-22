# ejax

Windows EVTX to JSON and XML converter. Comes in handy when playing blue team CTFs.

## Requirements

```sh
pip install python-evtx
pip install xmltodict
```

## Usage

```powershell
python ejax.py Windows-Security.evtx -m json
python ejax.py Windows-Security.evtx -m xml
```

## References

Adapted from williballenthin's [evtx-dump](https://github.com/williballenthin/python-evtx/blob/master/scripts/evtx_dump.py) script.
