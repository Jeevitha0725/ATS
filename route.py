from flask import Flask, render_template, make_response, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# import pickle

app= Flask(__name__)

# with open("file.pkl","rb") as File:
#     res=pickle.load(File)
# print(res)
@app.route("/")
def hello():
    Resume="""SANTHOSH M

    FULLSTACK WEB ENGINEER

    CONTACT

        MOBILE:	+91 8838144509



        EMAIL:	santhoshmsanthosh.1916@gmail.com



        WEBSITE:	https://santhosh-m0123.github.io/portfolio/



        GITHUB:	https://github.com/Santhosh-M0123/



    INTERSHIPS & EXPOSURES

        FULLSTACK WEB DEVELOPER	MAR 2023 - 



        FREELANSER'S LEAGUE	Ongoing

    Freelancers’ League is a marketplace where brands and businesses can find skilled people to get their job done on time. As a intern I had an opportunity work with live projects and had a

    great collab session with senior developer from top company

        WEB DEVELOPER	JUN 2023 - 



        FREELANCER	JULY 2023

    Contributed as a dedicated web freelancer on two successful live projects, demonstrating proficiency in web development, problemsolving, and client collaboration..

    EDUCATION

        BACHELOR OF ENGINEERING	2021 - 2025



    SNS COLLEGE OF ENGINEERING

    B.E / Computer Science and Engineering

        HIGHER SECONDARY EDUCATION	2016-2020



    VELAMMAL MATRIC HR SECONDAY SCHOOL

    PROFILE

    Hello, I'm Santhosh, Web Developer with a passion for programming and a drive to create exceptional online experiences, Skilled in frontend and back-end development. Delivered highquality solutions that aligned with project objectives, showcasing strong attention to detail and effective communication skills, Let's connect and build the next generation of web solutions together

    PROJECTS

    ARTICLE ECHO



    AUTHENTICATOR



    URL SHORTNER



    STUDIO BLACK



    SKILLS

    Frontend codingApi development

    Backend codingLogical thinking

    Database queryingProblem solving Unit testingSaas development

    PROGAMMING SKILLS

    JavascriptPython + django

    TypescriptJavaSE

    React + ReduxMysql

    Next jsMongoDb

    Nodejs + ExpressGit & Github"""

    resume = re.sub(r'[^a-zA-Z0-9\s.*]', '', Resume)
    # print(resume)
    Review=re.sub('[^a-zA-Z0-9]', " ", resume)
    # print(Review)
    Job_desc="JavascriptPython,django,TypescriptJavaSE,React,ReduxMysql,Pandas , numpy,Nodejs,ExpressGit & Github"
    review=re.sub('[^a-zA-Z]', " ", Job_desc)
    # print(review)
    A=Review.lower()
    B=review.lower()
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform([B])
    text2_tfidf = tfidf.transform([A])
    cosine_sim = cosine_similarity(tfidf_matrix, text2_tfidf)

    print(f"Cosine Similarity of text2 with respect to text1: {cosine_sim[0][0]}")
    data = {"percentage" : cosine_sim[0][0]}

    return jsonify(data)
app.run(debug=True)