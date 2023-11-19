import PyPDF2

def pdf_to_txt_line_by_line(pdf_path, txt_path):
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        with open(txt_path, "w", encoding="utf-8") as txt_file:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                content = page.extract_text()
                lines = content.split('\n')

                for line in lines:
                    txt_file.write(line +'\n')

    print(f"Conversion complete. TXT file saved at: {txt_path}")

pdf_path = 'pdftest.pdf'
txt_path = 'txtest.txt'
pdf_to_txt_line_by_line(pdf_path, txt_path)