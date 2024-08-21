# PDF-Image-Extractor
Python script that allows for quick image extraction from PDFs

# Installation
1. Install python
2. Install PyMuPDF: `pip install PyMuPDF`
3. ?? profit

# Usage
## Single page mode
Will extract all images from one PDF's page
`python process_page.py 'pdf_path.pdf' page_number`

Eg. Extract images from page 230 from `greatest_pdf.pdf`
`python process_page.py 'greatest_pdf.pdf' 230` 
## Range mode
Will extract all images from pages range
`python process_page.py 'pdf_path.pdf' page_number page_range_end`

Eg. Extract images from page 230-235 from `greatest_pdf.pdf`
`python process_page.py 'greatest_pdf.pdf' 230 235` 
