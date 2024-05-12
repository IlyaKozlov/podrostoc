import logging
import os
import sys
import time

from requests.exceptions import ConnectionError

from client import DedocClient

log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

client = DedocClient(
    dedoc_host=os.getenv("DEDOC_HOST", "localhost"),
    dedoc_port=int(os.getenv("DEDOC_PORT", 1231)),
)

for i in range(60):
    try:
        version = client.version
        log.info(f"connected to dedoc at {version}")
        break
    except ConnectionError:
        log.info(f"Attempt num {i + 1:02d} failed. Waiting for connection...")
        time.sleep(1)
