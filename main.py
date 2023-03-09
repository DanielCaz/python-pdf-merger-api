from flask import Flask, request, render_template
from PyPDF2 import PdfMerger, PdfReader
import os

app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template('form.html')


@app.route('/merge', methods=['POST'])
def merge_pdf():
    try:
        pdf_files = request.files.getlist('pdf')
        file_name = request.form['file_name']
        merger = PdfMerger()
        counter = 0
        for pdf in pdf_files:
            merger.merge(page_number=counter, fileobj=pdf)
            reader = PdfReader(pdf)
            counter += len(reader.pages)
        merger.write(f'{file_name}.pdf')
        merger.close()

        return render_template('results.html', page_count=counter, title='Success!', message='PDF files merged successfully!')
    except Exception as e:
        return render_template('results.html', title='Error!', message=str(e))


@app.route('/clear', methods=['GET'])
def clear():
    try:
        counter = 0
        for file in os.listdir():
            if file.endswith('.pdf'):
                os.remove(file)
                counter += 1
        return render_template('results.html', title='Success!', message=f'{counter} PDF files cleared successfully!')
    except Exception as e:
        return render_template('results.html', title='Error!', message=str(e))


if __name__ == '__main__':
    app.run()
