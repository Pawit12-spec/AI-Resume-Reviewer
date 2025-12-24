# AI-Resume-Reviewer
AI Resume Reviewer in Python

Made this tiny project so you do not have to pay for a resume reviewer or get errors and inaccurate feedback from ChatGPT :)
Project uses prefilled prompt to provide an accurate review and feedback without the need type in commands anywhere. Your uploaded resume content is sent along with the prefilled prompt to your chat AI (Open AI's gpt-4o-mini in this code) to get an analysis done with review and feedback.

The funtionaility of this project is relatively simple, please follow the following instructions to successfully operate the project.

Instructions:
1) ensure all the relavant libraries are installed and accessible within your environment ("pip install library_name" if on Windows or "sudo pip install library_name" for MacOS

2) ensure your api key to a chat model is saved within the same folder as the main.py file in a .env file as "API_KEY", this code is specificially designed for OpenAI's models, you might need to tweak the code for other models and use the okhttps3 library, not much different syntax

3) once all the above are completed, in your terminal, guide yourself to the folder of the app and ruun the following command "streamlit run main.py", this should provide you with the local URL and network URL to access the UI of the app, which should look like this: 
<img width="1351" height="537" alt="image" src="https://github.com/user-attachments/assets/421876b5-24fb-4693-902d-b4fbec725001" />


4) copy and paste any url in your preferred browser, upload your resume and job role (optional), then press "Analyse Resume" to get feedback with strengths and possible improvements

6) fix your resume with the feedback! or not if the model you use is not accurate! gpt-4o-mini provides good feedback
