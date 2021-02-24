class linesToLine_class:

    def __init__(self, fileDirection):
        self.fileDirection = fileDirection

    def processing(self):

        fileDir = self.fileDirection
        fr = open(fileDir, 'r')
        contents = fr.readlines()
        fr.close()

        line = ""

        for content in contents:
            content = content.replace("\n", "").strip()
            line = line + " " + content

        return line
