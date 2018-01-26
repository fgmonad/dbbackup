import pytest
import subprocess
from dbbackup import mysqldump

url = "ssh remotedev mysqldump -uroot -paNh@##@18969rt anproduction"


def test_dump_call_mysqldump(mocker):
    """
    Utilize mysqldump to interact with database
    """
    proc = mocker.Mock()
    mocker.patch("subprocess.Popen", return_value=proc)
    assert mysqldump.dump(url) == proc
    subprocess.Popen.assert_called_with([url], stdout=subprocess.PIPE)


def test_dump_handles_oserror(mocker):
    """
    mysqldump.dump returns a reasonable error if mysqldump isn't installed.
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        mysqldump.dump(url)

