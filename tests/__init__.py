from pathlib import Path
import sys

CWD = Path(__file__).parent # tests
ROOT_PATH = CWD.parent
sys.path.append(ROOT_PATH.joinpath("src").as_posix())
RESOURCES_PATH = CWD / "resources"

__all__ = ["RESOURCES_PATH"]