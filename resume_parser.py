# !pip install pypdf2
# !pip install docx2txt
# !pip install spacy
# !pip install pandas 
# !pip install nltk
# py -m spacy download en_core_web_sm    


import os
import docx2txt
from PyPDF2 import PdfReader

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


#Extract skills 
import spacy
nlp_model = spacy.load('en_core_web_sm')
doc = nlp_model("The website is abc.com.")
chunks = list(doc.noun_chunks)
skills_list = [
    "Python",
    "Java",
    "C++",
    "C",
    "Data Structures",
    "Algorithms",
    "Database Management",
    "Web Development",
    "HTML", 
    "CSS", 
    "JavaScript",
    "Reactjs",
    "Nodejs",
    "Object-Oriented Programming",
    "Object Oriented Programming",
    "Operating Systems",
    "Network Security",
    "Machine Learning",
    "Artificial Intelligence",
    "Data Analysis",
    "Data Science",
    "Cloud Computing",
    "Distributed Systems",
    "Cybersecurity",
    "Mobile App Development",
    "Linux",
    "Unix",
    "Computer Graphics",
    "Computer Vision",
    "Natural Language Processing",
    "Big Data Technologies",
    "Hadoop", 
    "Spark",
    "Data Mining",
    "IoT",
    "Internet of Things",
    "Dynamic Programming"
    "Parallel Programming",
    "Compiler Design",
    "Game Development",
    "Robotics",
    "Software Testing",
    "User Interface (UI) Design",
    "UI Design"
    "User Experience (UX) Design",
    "UX Design",
    "UI",
    "UX",
    "UI/UX",
    "Cryptography",
    "Concurrency",
    "Agile Methodology",
    "Computer Networks",
    "Image Processing",
    "Quantum Computing",
    "Blockchain Technology",
    "Linear Algebra", 
    "Probability", 
    "Calculus",
    "Problem Solving",
    "Critical Thinking",
    "Communication Skills",
    "Teamwork",
    "Project Management",
    "Data Visualization",
    "Statistical Analysis",
    "Systems Design",
]

import pandas as pd

def extract_skills(resume_text):
    nlp_text = nlp_model(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    skillset = []

    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills_list:
            skillset.append(token)

    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        if token in skills_list:
            skillset.append(token)
    return [i.capitalize() for i in set([i.lower() for i in skillset])]

import re
from nltk.corpus import stopwords


# Grad all general stop words
STOPWORDS = set(stopwords.words('english'))

# Education Degrees
EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S',
            'ME', 'M.E', 'M.E.', 'M.B.A', 'MBA', 'MS', 'M.S',
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
            'SSLC', 'SSC' 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

def extract_education(resume_text):
    nlp_text = nlp_model(resume_text)
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]

    edu = {}
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]

    # Extract year
    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{})))'), edu[key])
        if year:
            education.append((key, ''.join(year[0])))
        else:
            education.append(key)
    return education

