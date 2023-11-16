import sys
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

THIRD_PARTY_PATH = Path(__file__).parent
LIST_PATH_SUBMODULES = []
LIST_NAME_SUBMODULES = []

for path in THIRD_PARTY_PATH.iterdir():
    src_path = path.joinpath("src")
    if src_path.is_dir() and src_path.parent.exists():
        LIST_PATH_SUBMODULES.append(src_path)
        LIST_NAME_SUBMODULES.append(next(src_path.iterdir()).name)
        logger.info("adding \"{}\" to sys.path".format(src_path))
        sys.path.append(path.joinpath("src").as_posix())





