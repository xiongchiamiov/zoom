Zoom
====

An internal link shortener designed for easy installation.

Purpose
-------

Inspired by Google's `go/` links, Zoom is intended to be used inside an
internal network to provide memorable or printable shortlinks.

For instance, you might host it in the same domain as your workstations and
under the hostname 'zoom'; then if a user adds a shortlink of 'subprocess' to
https://docs.python.org/3/library/subprocess.html , another user visiting
`zoom/subprocess` in their browser will be redirected to that Python
documentation page.

Features/Non-Features
---------------------

Zoom is designed for a very specific purpose.  It may or may not be what you
want.

Zoom:

* Installs with one command
* Runs with one command
* Trusts all users

Use
---

    [$]> pip install zoom_shortener
    [$]> zoom --port 8080

Hacking
-------

    [$]> python3 -m venv venv
    [$]> source venv/bin/activate
    [$]> pip install -r requirements.txt
    [$]> pip install -e .
    [$]> zoom --port 8080
