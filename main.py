!pip install docx2txt
import docx2txt 
from google.colab import files
uploaded=files.upload() 
resumedoc=open("templateresume.docx",r)
resume=docx2txt.process(resumedoc)
print(resume) 
jobdoc=open("Software Engineer Requirements.docx",r)
job_description=docx2txt.process(jobdoc)
print(job_description) 
text=[resume,job_description] 
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
count_matrix=cv.fit_transform(text) 
from sklearn.metrics.pairwise import cosine_similarity
print("\nSimilarity Scores:")
print(cosine_similarity(count_matrix)) 
matchPercentage=cosine_similarity(count_matrix)[0][1]*100
matchPercentage=round(matchPercentage,2)
print("Your resume matches about "+str(matchPercentage)+" % of the job description.")