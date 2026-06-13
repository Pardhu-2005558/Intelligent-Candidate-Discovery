from docx import Document

doc = Document("job_description.docx")

print("\nJOB DESCRIPTION\n")
print("=" * 50)

for para in doc.paragraphs:
    if para.text.strip():
        print(para.text)