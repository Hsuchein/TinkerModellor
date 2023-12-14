import os
import pathlib
from typing import Tuple

import pytest


def pytest_configure():
    this_dir = pathlib.Path(__file__).parent
    pytest.EXAMPLE_PATH = str(this_dir.joinpath("dataset"))
    pytest.OUTPUT_PATH = str(this_dir.joinpath("test_output"))
    

@pytest.fixture(scope='session')
def get_file_path():
    def _get_file_path(data_name) -> Tuple[str, str]:
        gro = os.path.join(pytest.EXAMPLE_PATH, data_name, 'gromacs.gro')
        top = os.path.join(pytest.EXAMPLE_PATH, data_name, 'gromacs.top')
        return (gro, top)
    return _get_file_path
