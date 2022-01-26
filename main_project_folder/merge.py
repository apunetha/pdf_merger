import os
import logging as lg
import PyPDF2

def PDFmerge(files,output,path):
    #creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()
    
    #appending pdfs in object
    for file in files:
        path_with_file = os.path.join(path, file)
        try:
            
            lg.info("merger object creation")
            pdfMerger.append(path_with_file)
        except Exception as e:
            lg.error("Error while merging ",e)
    
    #writing combined pdf to output pdf file
    output_file= os.path.join(path,output)
    try:
        with open(output_file,'wb') as f:
            pdfMerger.write(f)
    except Exception as e:
        lg.error("Error while writint to output pd file,",e)