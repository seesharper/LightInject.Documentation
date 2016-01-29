
import subprocess

def download(url, file):
    outfile = open(file, "wb")
    subprocess.call(["curl", url], stdout=outfile)

download('https://raw.githubusercontent.com/seesharper/LightInject/master/readme.md', 'docs/index.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.xUnit/master/readme.md', 'docs/xunit.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.AutoFactory/master/readme.md', 'docs/autofactory.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Annotation/master/readme.md', 'docs/annotation.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Interception/master/readme.md', 'docs/interception.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Web/master/readme.md', 'docs/web.md')
download('https://raw.githubusercontent.com/seesharper/LightMock/master/readme.md', 'docs/lightmock.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Microsoft.DependencyInjection/master/readme.md', 'docs/microsoft.dependencyinjection.md')


