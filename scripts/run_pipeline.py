import subprocess
import sys

scripts = [

"scripts/data_ingestion.py",

"scripts/data_cleaning.py",

"scripts/load_to_sqlite.py",

"scripts/live_nav_fetch.py"

]

for script in scripts:

    print(f"Running {script}")

    subprocess.run(
        [sys.executable, script],
        check=True
    )

print(
    "\nPipeline completed successfully."
)