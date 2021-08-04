import PyPDF3
import os


def main():
    folder = 'C:/nltk_data/corpora/framenet_v15/docs'
    for file in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, file)) or not file.endswith('.pdf'):
            continue
        with open(os.path.join(folder, file), 'rb') as pdfFileObj:
            pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
            for i in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(i)
                text = pageObj.extractText()
                result = [o for o in ['databases', 'Spreadsheet-like', 'public'] if(o in text)]
                if result:
                    print(file, i, result)


if __name__ == '__main__':
    main()
