class Workflow:
    def execute(self):
        data = self.reader.read()
        result = self.analyzer.analyze(data)
        self.writer.write(result)

class SimpleReader:
    def read(self):
        return "Hugo"

class ConsoleReader:
    def read(self):
        return input("Geben Sie Daten ein: ")


class SimpleAnalyzer:
    def analyze(self, data):
        return len(data)

class WordCountAnalyzer:
    def analyze(self, data):
        return len(data.split(' '))


class ConsoleWriter:
    def write(self, result):
        print(result)         

def application():
    wf = Workflow()
    wf.reader = ConsoleReader()
    wf.analyzer = WordCountAnalyzer()
    wf.writer = ConsoleWriter()

    wf.execute()

application()