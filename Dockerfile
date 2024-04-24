FROM python:alpine

RUN pip install nltk

WORKDIR /C:/Users/20100/OneDrive/Documents/cloudAssignment

COPY wordFrequency.py /C:/Users/20100/OneDrive/Documents/cloudAssignment/

COPY random_paragraphs.txt /C:/Users/20100/OneDrive/Documents/cloudAssignment/

CMD python wordFrequency.py