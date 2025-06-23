import mkdocs_gen_files
import os
from pathlib import Path

nav = mkdocs_gen_files.Nav()

root = Path(__file__).parent.parent
docs_path = root / "docs"
plots_path = root / "docs" / "static" / "memprof_plots"

for dir, subdirs, files in os.walk(plots_path):
    rel_path = Path(dir).relative_to(plots_path)
    if rel_path == Path("."):
        rel_path = Path("memory_usage")
        full_doc_path = Path( "memory_usage.md")
    else:
        full_doc_path = Path("memory_usage", rel_path.with_suffix(".md"))

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        for subd in subdirs:
            print(f"[{subd}]({rel_path}/{subd}.md)  ", file=fd)
        for f in files:
            if f.endswith(".png"):
                rp = Path('.')
                for _  in range(len(rel_path.parts)):
                    rp /= ".."
                rp = rp / "static" / "memprof_plots" / rel_path / f
                print(f"![{rel_path / Path(f).stem}]({rp})  ", file=fd)
