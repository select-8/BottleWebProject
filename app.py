"""
This script runs the application using a development server.
"""

import os
import sys
from bottle import default_app
from bottle.ext import sqlite
from bottle_log import LoggingPlugin

import routes

if "--debug" in sys.argv[1:] or "SERVER_DEBUG" in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    import bottle

    bottle.debug(True)


def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return default_app()


if __name__ == "__main__":
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, "static").replace("\\", "/")
    # Starts a local test server.
    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(os.environ.get("SERVER_PORT", "5555"))
    except ValueError:
        PORT = 5555
    import bottle

    @bottle.route("/static/<filepath:path>")
    def server_static(filepath):
        """Handler for static files, used with the development server.
        When running under a production server such as IIS or Apache,
        the server should be configured to serve the static files."""
        return bottle.static_file(filepath, root=STATIC_ROOT)

    plugin = sqlite.Plugin(dbfile="./data/simpledb.db")  # not used atm
    bottle.install(plugin)
    app = bottle.Bottle()
    bottle.install(LoggingPlugin(app.config))
    bottle.run(server="wsgiref", host=HOST, port=PORT, reloader=True, debug=True)
