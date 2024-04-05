import os
import time
from PyPDF2 import PdfFileMerger

def merge_pdfs_with_bookmarks(folder_path):
    # Change directory to the specified folder
    os.chdir(folder_path)
    
    # Get a list of PDF files in the folder
    pdf_files = sorted([file for file in os.listdir() if file.endswith('.pdf')])
    
    # Initialize PdfFileMerger object
    merger = PdfFileMerger()
    
    # Iterate through the PDF files, adding them to the merger and creating bookmarks
    for pdf_file in pdf_files:
        # Add the PDF file to the merger
        merger.append(pdf_file)
        
        # Add a bookmark with the file name
        merger.addBookmark(pdf_file.split('.pdf')[0], merger.getNumPages() - 1)
    
    # Output file name for the merged PDF
    output_folder = os.path.join(folder_path, "merged_PDF")
    os.makedirs(output_folder, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_pdf = os.path.join(output_folder, f"merged_pdf_{timestamp}.pdf")
    
    # Write the merged PDF with bookmarks to the output file
    with open(output_pdf, 'wb') as output_file:
        merger.write(output_file)
    
    print(f"Merged PDF file with bookmarks created: {output_pdf}")

if __name__ == "__main__":
    # Ask user to input folder full path
    folder_path = input("Enter the full path of the folder containing the PDF files: ")
    
    # Check if the folder path is valid
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        merge_pdfs_with_bookmarks(folder_path)
    else:
        print("Invalid folder path. Please provide a valid folder path.")
