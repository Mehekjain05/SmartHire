# pip install pypdf2
# pip install docx2txt
# pip install openai

import os
import docx2txt
from PyPDF2 import PdfReader
import openai

#Converting resume from pdf or docx to text
class Convert2Text:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_file_extension(self):
        _, file_extension = os.path.splitext(self.file_path)
        return file_extension.lower()

    def convert_to_text(self):
        file_extension = self.check_file_extension()
        if file_extension == '.pdf':
            return self.pdftotext(self.file_path)
        elif file_extension == '.docx':
            return self.doctotext(self.file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}. Only .pdf and .docx files are supported.")

    def doctotext(self, m):
        temp = docx2txt.process(m)
        resume_text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
        text = ' '.join(resume_text)
        return text

    def pdftotext(self, m):
        pdfFileObj = open(m, 'rb')
        pdfFileReader = PdfReader(pdfFileObj)
        num_pages = len(pdfFileReader.pages)
        currentPageNumber = 0
        text = ''
        while currentPageNumber < num_pages:
            pdfPage = pdfFileReader.pages[currentPageNumber]
            text = text + pdfPage.extract_text()
            currentPageNumber += 1
        pdfFileObj.close()
        return text

resume = 'GET FROM DATABASE'

converter = Convert2Text()

resume_text = converter.convert_to_text()

# Chatgpt model to extract skills
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "AI", "content": "As a member of the HR team, your task is to extract a python list of skills from the resumes of candidates applying for a job. Your goal is to provide a concise and focused list of skills (techinical and non-technical skills) without any elaboration or irrelevant information. Your prompt should ensure that the list of skills extracted accurately reflects the candidate's relevant expertise and qualifications. Avoid including any additional details or explanations in the list. Your prompt should guide the AI model to provide a straightforward and precise python list of skills from the candidate's resume. Template - ```AI : [Python list of skills]``` " },
    {"role": "Applicant", "content": "{resume_text}"}
  ]
)

print(response.choices[0].message)

# Ranking CV
applicant_skills = response.choices[0].message
required_skills = {'GET FROM DATABASE': 'weightage'}

def cv_ranker(applicant_skills, required_skills):
    skillset = []
    extra_skills = []
    for skill in applicant_skills:
        if skill in required_skills:
            skillset.append(skill)
        else:
            extra_skills.append(skill)

    

    return skillset, extra_skills
