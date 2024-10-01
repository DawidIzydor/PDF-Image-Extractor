import fitz  # PyMuPDF
import os
import sys

def extract_images_from_pdf(pdf_path, page_number, output_folder):
    # Get the base name of the PDF file without the extension
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Append the PDF name to the output folder
    output_folder = os.path.join(output_folder, pdf_name)
    
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Check if the specified page number is within range
    if page_number < 0 or page_number >= pdf_document.page_count:
        print(f"Page number {page_number} is out of range.")
        return
    
    # Select the specified page
    page = pdf_document.load_page(page_number)
    
    # Get the images on the page
    image_list = page.get_images(full=True)
    
    if not image_list:
        print(f"No images found on page {page_number}.")
        return
    
    print(f"Found {len(image_list)} images on page {page_number}.")
    
    # Extract and save the images
    for i, img in enumerate(image_list):
        xref = img[0]
        smask = img[1]
        base_image = pdf_document.extract_image(xref)

        pix1 = fitz.Pixmap(base_image["image"])
        
        try:
            mask = fitz.Pixmap(pdf_document.extract_image(smask)["image"])
            pix = fitz.Pixmap(pix1, mask)  # Combine image with mask
            print(f"Mask found and applied for image {i + 1}")
        except:
            pix = pix1  # Use the base image without mask
            print(f"Mask not found for image {i + 1}, saving without mask")
        
        # Prepend the page number to the image filename
        image_filename = os.path.join(output_folder, f"{page_number + 1}_image_{i + 1}.png")
        
        pix.save(image_filename)
        
        print(f"Saved image to {image_filename}")


def extract_images_range_from_pdf(pdf_path, page_number, page_number_end, output_folder):
    for i in range(page_number, page_number_end):
        extract_images_from_pdf(pdf_path, i, output_folder)

if __name__ == "__main__":
    # Set the output folder base name
    output_folder = "extracted_images"  # You can modify this if needed

    # Check if the correct number of arguments were passed
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Usage: script.py <pdf_path> <page_number> <optional:page_number_range_end>")
        sys.exit(1)
    

    # Read pdf_path and page_number from command-line arguments
    pdf_path = sys.argv[1]
    try:
        page_number = int(sys.argv[2])
    except ValueError:
        print("Invalid page number. Please enter a valid integer.")
        sys.exit(1)

    try:
        page_number_end = int(sys.argv[3])
        print("Page range mode")
        page_range = 1
    except:
        print("One page only mode")
        page_range = 0

    if page_range == 1:
        extract_images_range_from_pdf(pdf_path,page_number-1, page_number_end-1, output_folder)
    else:
        extract_images_from_pdf(pdf_path, page_number-1, output_folder)