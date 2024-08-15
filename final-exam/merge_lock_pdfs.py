from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import sys

def merge_and_lock_pdfs(output_filename, password, *pdf_filenames):
    merger = PdfMerger()
    
    # Merge all PDFs
    for pdf in pdf_filenames:
        merger.append(pdf)
    
    # Write the merged PDF to a temporary file
    with open("merge_lock_pdfs/temp_merged.pdf", "wb") as temp_file:
        merger.write(temp_file)
    
    # Encrypt the merged PDF with the password
    reader = PdfReader("merge_lock_pdfs/temp_merged.pdf")
    writer = PdfWriter()
    
    for page_num in range(len(reader.pages)):
        writer.add_page(reader.pages[page_num])
    
    writer.encrypt(password)
    
    # Save the final locked PDF
    with open(output_filename, "wb") as locked_file:
        writer.write(locked_file)
    
    print(f"Created locked PDF: {output_filename}")
    print(f"Password: {password}")

if __name__ == "__main__":
    # Usage: python merge_lock_pdfs.py test merge_lock_pdfs/sample1.pdf merge_lock_pdfs/sample2.pdf merge_lock_pdfs/sample3.pdf
    output_filename = "merge_lock_pdfs/merged.pdf"
    password = sys.argv[1]
    pdf_filenames = sys.argv[2:]
    
    merge_and_lock_pdfs(output_filename, password, *pdf_filenames)
