import os
import pathlib
import typing


class WriteData:

    @staticmethod
    def write(fp: typing.TextIO):
        # What will the following two lines give me ?
        fp.mode
        fp.encoding

        fp.write()

    def json_write(path: pathlib.Path, data: dict, file: str):
        import json

        if not os.path.exists(path):
            os.makedirs(path)

        file_path = pathlib.Path.joinpath(path, f"{file}.json")

        with open(file_path, "r") as fp:
            json.dump(data, fp)