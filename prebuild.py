import pycurl
import subprocess

def download(url, file):
    # As long as the file is opened in binary mode, both Python 2 and Python 3
    # can write response body to it without decoding.
    with open(file, 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()



download('https://raw.githubusercontent.com/seesharper/LightInject.xUnit/master/readme.md', 'docs/xunit.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.AutoFactory/master/readme.md', 'docs/autofactory.md')
subprocess.call(["mkdocs", "build", "--clean"])