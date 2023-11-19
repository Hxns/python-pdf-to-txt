import PyPDF2

def pdf_to_txt_line_by_line(pdf_path, txt_path):
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)

        with open(txt_path, "w") as txt_file:
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                content = page.extact_text()
                lines = content.split('\n')

                for line in lines:
                    txt_file.write(line +'\n')

    print(f"Conversion complete. TXT file saved at: {txt_path}")