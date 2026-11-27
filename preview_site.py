"""Build and serve the complete website, independently of the shell's cwd."""

from __future__ import annotations

import argparse
import functools
import http.server
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8768)
    parser.add_argument("--no-build", action="store_true", help="Use the existing staged website")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("port must be between 1 and 65535")
    directory = ROOT / "build/site-preview"
    if not args.no_build:
        subprocess.run(
            [sys.executable, "-X", "utf8", "-B", str(ROOT / "home/package_site.py")],
            cwd=ROOT,
            check=True,
        )
    if not (directory / "index.html").is_file() or not (directory / "docs/index.html").is_file():
        parser.error("the complete website is missing; run again without --no-build")
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(directory))
    try:
        server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    except OSError as error:
        parser.error(f"cannot start the preview on port {args.port}: {error}")
    print(f"Serving: {directory}", flush=True)
    print(f"Homepage: http://127.0.0.1:{args.port}/", flush=True)
    print(f"Documentation: http://127.0.0.1:{args.port}/docs/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
