import json
import os
import typing
from pathlib import Path


class IO:

    @staticmethod
    def write(fp: typing.TextIO, data):
        '''Description
        - This function dose something

        Return
        - Nothing
        '''

        fp.write(data)

    def write_text(self, path: Path, data: str, file: str):
        '''Description
        - This Method will take a path and write a text file based on data that
        is given.

        Return
        - None
        '''

        if not os.path.exists(path):
            os.makedirs(path)

        file_path = Path.joinpath(path, f"{file}.txt")

        with open(file_path, "w") as fp:
            self.write(fp, data)

    @staticmethod
    def json_write(path: Path, data: dict, file: str):       

        if not os.path.exists(path):
            os.makedirs(path)

        file_path = Path.joinpath(path, f"{file}.json")

        with open(file_path, "r") as fp:            
            json.dump(data, fp)

    
