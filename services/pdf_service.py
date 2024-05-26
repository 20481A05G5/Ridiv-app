import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

class PDFManager:
    def __init__(self):
        self.pdfs = {}
        self.docs = {}

    def upload_pdf(self, file):
        pdf_id = str(uuid4())
        text = self.extract_text(file)
        self.pdfs[pdf_id] = text
        self.docs[pdf_id] = nlp(text)
        return pdf_id

    def search_text(self, pdf_id, query, context_size=500):
        doc = self.docs.get(pdf_id)
        if not doc:
            return "PDF not found."

        matcher = PhraseMatcher(nlp.vocab)
        matcher.add("Query", None, nlp(query))
        matches = matcher(doc)

        if matches:
            start, end = matches[0]
            start = max(start - context_size, 0)
            end = min(end + context_size, len(doc))
            return doc[start:end].text
        return "No relevant information found."
    # Handles PDF processing
    def process_pdf(file_path):
        return "Processed data from PDF at: " + file_path
