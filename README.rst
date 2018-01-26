dbbackup
==========

CLI for backing up remote SQL databases locally or to the cloud

Preparing for Development
-------------------------

1. Ensure ``pip``, and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:fgmonad/dbbackup.git``
3. Fetch development dependencies: ``make install``

Usage
-----

Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:

::

  $ dbbackup --host dbhostname --user john --pass doe --driver s3 backups

::

  $ dbbackup --host localhost --user john --pass doe --driver local pathToBackup/dump.sql


Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active

::

  $ make

If virtualenv isn't active then use:

::

  $ pipenv run make


