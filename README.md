# ejax

Windows EVTX to JSON and XML converter

## Requirements

```sh
pip install python-evtx
pip install xmltodict
```

## Usage

```sh
python ejax.py Windows-Security.evtx -m json
python ejax.py Windows-Security.evtx -m xml
```

## References

Adapted from williballenthin's [evtx-dump](https://github.com/williballenthin/python-evtx/blob/master/scripts/evtx_dump.py) script.
