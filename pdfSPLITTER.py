from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_file, output_folder):

    with open(input_file, 'rb') as input_pdf:
        reader = PdfReader(input_pdf)
        for page_num in range(len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            output_file = f"{output_folder}/page_{page_num + 1}.pdf"
            with open(output_file, 'wb') as output_pdf:
                writer.write(output_pdf)

if __name__ == "__main__":
    input_file = input("Enter the path to the input PDF file: ")
    output_folder = input("Enter the path to the output folder: ")
    split_pdf(input_file, output_folder)
