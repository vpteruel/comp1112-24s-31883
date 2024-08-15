from docx import Document

def docx_replace(fname, oldWord, newWord):
    doc = Document(fname)
    
    for paragraph in doc.paragraphs:
        if oldWord in paragraph.text:
            paragraph.text = paragraph.text.replace(oldWord, newWord)
            print(oldWord, "repleced by", newWord)
    
    doc.save(fname)

docx_replace('replace_words_in_docx.docx', 'apple', 'banana')