import os
import sys
from urllib.request import urlretrieve

wasm_version = "0.1.39-pygwalker-0"

url = f"https://pygwalker-public-bucket.s3.amazonaws.com/gw-dsl-parser-wasm/dsl_parser_{wasm_version}.wasm"
outout_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "gw_dsl_parser",
    "dsl_parser.wasm"
)

try:
    urlretrieve(url, outout_path)
except Exception as e:
    print(f"Error: could not download the file\n{e}", file=sys.stderr)
    sys.exit(1)
