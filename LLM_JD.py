import streamlit as st
import text_generation

def generate_job_responsibilities(job_title, work_experience_required, skillset_required, company_name, job_type, job_location):
    client = text_generation.InferenceAPIClient("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")

    complete_answer = ""
    for response in client.generate_stream(
        f"<|prompter|>Write Job Description for {job_title} with {work_experience_required} years of experience and {skillset_required} skills for {company_name} as a {job_type} in {job_location}. The salary range, other benefits, and job details are.<|endoftext|><|assistant|>",
        max_new_tokens=500,
    ):
        if response.token.special:
            continue
        complete_answer += response.token.text

    return complete_answer


def main():
    st.title("Mini JD :blue[Generator App]")
    st.markdown('This app is an mini version of generating job description and a time saver for HRs in terms of writting job description in **"Just One Click"**.')
    st.write('**_By - Deepak Kaura (an Data Science Enthusiast) built this with the help of Open-Source GPT/LLM Model_**')

    job_title = st.text_input("Enter the job title: ")
    work_experience_required = st.text_input("Enter the work experience required: ")
    skillset_required = st.text_input("Enter the skills required: ")
    company_name = st.text_input("Enter the company name: ")
    about_company = st.text_area("Enter the about company: ")
    no_of_employees = st.text_input("Enter the company's number of employees: ")
    job_type = st.text_input("Enter the job type: ")
    job_location = st.text_input("Enter the job location: ")
    date_posted = st.date_input("Enter the date: ")



    job_details = f"""
Date Posted: {date_posted}
Company: {company_name}
About Company: {about_company}
Company's no. of employees: {no_of_employees}
Job Title: {job_title}
Job Type: {job_type}
Location: {job_location}

"""
    generate_button = st.button("Generate Job Description",key=f"Generate")

    def job_reponsibilities_app():

         job_responsibilities = generate_job_responsibilities(
        job_title, work_experience_required, skillset_required, company_name, job_type, job_location
    )
         st.write(f"**Job Description for {job_title}:**\n{job_responsibilities}")



    if generate_button:
        st.write(f"**Job Details:**\n{job_details}")
        job_reponsibilities_app()

if __name__ == "__main__":
    main()