from pathlib import Path
from shutil import copyfile


# Resolve the source beside this script so it works from any working directory.
source = Path(__file__).resolve().parent / "happy.png"
destination = Path("/output/entry.png")
destination.parent.mkdir(parents=True, exist_ok=True)
copyfile(source, destination)
