import json
import os
from typing import Dict
import requests
from requests import Response

from data_structures.parsed_document import ParsedDocument
from exceptions.dedoc_exception import DedocException


class DedocClient:

    def __init__(self, dedoc_host: str, dedoc_port: int) -> None:
        super().__init__()
        self.dedoc_host = dedoc_host
        self.dedoc_port = dedoc_port

    @property
    def version(self) -> str:
        url = f"http://{self.dedoc_host}:{self.dedoc_port}/version"
        r = requests.get(url)
        return r.content.decode().strip()

    def parse_file(self,
                   file_path: str,
                   parameters: Dict[str, str]) -> ParsedDocument:
        response = self._send_request(file_path=file_path, data=parameters)
        parsed_document = self._handle_response(response=response)
        return parsed_document

    def _send_request(self, file_path: str, data: dict = None) -> Response:
        if data is None:
            data = {}

        file_name = os.path.basename(file_path)
        url = f"http://{self.dedoc_host}:{self.dedoc_port}/upload"
        with open(file_path, 'rb') as file:
            files = {'file': (file_name, file)}
            response = requests.post(url, files=files, data=data)
        return response

    @staticmethod
    def _handle_response(response: Response) -> ParsedDocument:
        code = response.status_code
        if code != 200:
            text = response.text
            raise DedocException(status_code=code, message=text)
        else:
            result = json.loads(response.content.decode())
            return ParsedDocument(**result)
