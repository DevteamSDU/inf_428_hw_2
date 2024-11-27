import pandas as pd
import pdfplumber


def extract_pdf_data(pdf_path):
    data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines:
                parts = line.split()
                if len(parts) >= 3:
                    data.append({
                        "id": parts[1],
                        "name": " ".join(parts[2:]),
                        "pair": parts[0]
                    })
    return pd.DataFrame(data)
