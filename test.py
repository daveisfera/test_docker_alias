from urllib.request import urlopen
from sys import exit


_EXPECTED = \
"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href="main.py">main.py</a></li>
<li><a href="test.py">test.py</a></li>
</ul>
<hr>
</body>
</html>
"""

def _main() -> None:
    url = "http://local.testme.com:8000"
    response = urlopen(url)

    code = response.getcode()
    print(code)
    if code != 200:
        exit(1)

    data = response.read().decode()
    print(data)
    print(_EXPECTED)
    if data != _EXPECTED:
        exit(2)

    exit(0)


if __name__ == "__main__":
    _main()
