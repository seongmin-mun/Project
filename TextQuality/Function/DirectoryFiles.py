class directoryFiles_class:

    def __init__(self, fileDirection):
        self.fileDirection = fileDirection

    def processing(self):

        import os

        #설정한 경로에 포함된 파일 및 폴더의 리스트를 생성
        dirPath = self.fileDirection
        fileList = os.listdir(dirPath)

        #분석에 필요한 파일만을 추리기
        neededFileList = []

        #'.csv'라는 단서를 기반으로 파일 추리기
        for x in fileList:
            if x.find('.txt')==-1:    #java에서 contains같은 역활
                continue
            else:
                neededFileList.append(x)

        return neededFileList