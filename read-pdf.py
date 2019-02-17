"""
Read PDF files


1)  PdfFileReader Class
    -------------------
    PdfFileReader(stream, strict=True, warndest=None, overwriteWarnings=True)
    
    Parameters 
    ----------
    Most important
    --------------
    1. stream - A File object or an object that supports the standard read and 
    seek methods similar to a File object. Could also be a string representing a
    path to a PDF file.
    
    Others
    ------
    2. strict (bool) - determines whether user should be warned of all problems 
    and also causes some correctable problems to be fatal. Defaults to True.
    3. warndest - Destination for logging warnings (defaults to sys.stderr).
    4. overwriteWarnings (bool) - Determinees whether to override 
    Python’s warnings.py module with a custom implementation (defaults to True)
    
    
2)  PageObject Class
    ----------------
    - Represents a single page within a PDF file. Typically, this object will
    be created by acessing the getPage() method of the PdfFileReader class,
    but is also possible to create an empty page with createBlankPage() 
    
    Parameters
    ----------
    1. pdf - PDF file the page belongs to  
    2. indirectRef - Stores the original indirect reference to this object in 
    its source PDF
    
    *USAGE* 
    -------
    Below in our script, we indirectly create a PageObject class via 
    pdf.getPage(1) , initialized as page variable.  
    we get 
    
    

"""

from PyPDF2 import PdfFileReader

def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        # get the first page
        page = pdf.getPage(5)
        pagenum = pdf.getPageNumber(page)
        print(pagenum)
        #print(page)
        #print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        print(text)
if __name__ == '__main__':
    path = 'Happiness.pdf'
    text_extractor(path)
