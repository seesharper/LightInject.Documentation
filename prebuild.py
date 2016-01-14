
import subprocess

def download(url, file):
    outfile = open(file, "wb")
    subprocess.call(["curl", url], stdout=outfile)


download('https://raw.githubusercontent.com/seesharper/LightInject.xUnit/master/readme.md', 'docs/xunit.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.AutoFactory/master/readme.md', 'docs/autofactory.md')
