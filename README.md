# Streamlit LLM Hackathon

## **Documentation: The Advanced Job Description Generation Engine**


App Link - *[JD Generator](https://app-llm-hackathon-jd.streamlit.app/)*

* This app cost me zero penny 

### **Overview**


The JD Generator (an Automated Job Descriptions generator) is a powerful web application designed to create customised job descriptions (JDs) based on user input. By leveraging the state-of-the-art language model "Open-Source GPT/LLM Model'' from HuggingFace, the application can generate comprehensive job responsibilities that align with specific job titles, work experience requirements, skill sets, company information, job type, location, and salary package.


This tool is ideal for HR professionals and recruiters, as it streamlines the process of crafting accurate and engaging job descriptions.


 ### **How to Use :**



1. Input Details: Enter essential job details such as the job title, required work experience, skillset, company name, job type, location. More user input can be add as per requirements


2. Generate Job Details: The application will automatically combine the entered information to produce a structured and comprehensive job details section, highlighting crucial aspects of the job opportunity.


3. Create Job Responsibilities: The JD Generator utilises the advanced capabilities of the "Open-Source GPT/LLM" language model to generate precise and engaging job responsibilities. The model seamlessly integrates the provided input to tailor the responsibilities for the specific job position.


4. Review and Edit: The generated job details and job responsibilities will be displayed on the user interface. Review the content and make any necessary edits to ensure accuracy and completeness.


5. Generate Job Description: Once satisfied with the input and generated content, click the "Generate Job Description" button to get the final job description ready for use.


### **Sources -**


The JD Generator relies on the HuggingFace  [Open-Source GPT/LLM Model](https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5)  as the core language model. This model has been pre-trained on a vast and diverse dataset, empowering it to produce human-like responses based on the provided inputs.



### **Advantages -**



1. Time-Efficient: The JD Generator significantly reduces the time and effort required to craft detailed job descriptions, accelerating the recruitment process.


2. Personalization: Users can customise the generated job descriptions to match the unique requirements of each job opportunity, ensuring precision in the language used.


3. User-Friendly Interface: The web application offers an intuitive and interactive user interface, making it easy to generate job descriptions even for non-technical users.



 ### **Limitations -**



1. Input Clarity: The accuracy and relevance of the generated output can be influenced by the clarity and specificity of the user's input. Clearly articulated input yields more accurate results.


2. Internet Connectivity: The application requires a stable internet connection to access external resources and ensure seamless operation.


### **Considerations**


1. Resource Usage: Users should be mindful of the computational resources required when running the model, as it may consume significant processing power and memory.


2. Model Dependency: The quality of the generated text is dependent on the performance and capabilities of the model.


 ### **Tools and Languages : -**



- Deployment tool (Streamlit): The application's interactive web interface is developed using Streamlit, facilitating easy and dynamic user interaction.



- Programming language (Python): The entire Rework_AI JD Generator is implemented in Python, making use of various libraries and tools to handle data and interface with the HuggingFace model.



- Model ref. (HuggingFace): The "Open-Source GPT/Open-Assistant" model from HuggingFace serves as the core language model for generating job responsibilities.



### **Architecture Overview :**



1. User Interface (Streamlit Web Application):


   - The front-end of the application is built using Streamlit, a Python framework for creating interactive web applications.


   - Users interact with the user-friendly interface to input job details and trigger the job description generation process.


   - Actionable Step: Design the web interface with clear input fields and instructions, ensuring a smooth user experience.



2. Back-End Processing (Python Script):


   - The back-end is implemented in Python, using libraries and functions to handle data processing and model interaction.

   - The user-provided job details are collected and organized in a structured format for further processing.


   - Actionable Step: Develop robust data preprocessing functions to validate and sanitize user inputs.




3. Open-Source GPT Model (OpenAssistant):


   - The core of the JD generation process is the "OpenAssistant" model from HuggingFace.


   - The HuggingFace library is utilized to interface with the model and, sending the structured job details for generation.

   



4. Generated Job Description:


   - The output from the model consists of generated job responsibilities tailored to the user's input.


   - The generated content is then presented back to the user through the web interface for review.


   - Actionable Step: Format and present the generated output in a readable and structured manner.




5. User Feedback Loop:


   - Optionally, the application can incorporate a user feedback loop to gather feedback on the quality of the generated job descriptions.


   - Feedback can be collected through form submissions or rating systems.


   - Actionable Step: Implement a feedback mechanism and collect user suggestions for improvements.





### **Flow of Information :-**


1. User Input:


   - Users provide various job-related details through the web interface, including job title, experience required, skills, company information, etc.


   - Actionable Step: Include clear instructions and placeholders for users to input the required information accurately.



2. Data Preprocessing:


   - The input provided by the user is preprocessed and validated to ensure data consistency and accuracy.


   - Actionable Step: Implement data validation functions to handle potential errors in user input.



3. Model Interaction:


   - Preprocessed data is sent to the "OpenAssistant" model through the HuggingFace library for generating job responsibilities.


   - Actionable Step: Set up library calls with proper error handling to interact with the language model effectively.



4. Generated Output:


   - The generated job responsibilities are obtained from the model's response.


   - Actionable Step: Parse the model's response to extract the relevant job responsibilities.




5. Display to User:


   - The generated job details and job responsibilities are displayed on the Streamlit web application interface for user review.


   - Actionable Step: Format and present the information in a user-friendly and aesthetically pleasing manner.






6. User Feedback (Optional):


   - Users may provide feedback on the quality and relevance of the generated job descriptions.


   - Actionable Step: Implement a feedback collection mechanism and encourage users to share their thoughts.





### **Data Flow Diagram**


```

+----------------------------+

| User Interface           |

| (Streamlit Web App) |

+----------------------------+

           |

           | User Input

           v

+----------------------------+

| Data Preprocessing  |

+----------------------------+

           |

           | Preprocessed Data

           v

+------------------------------------------------------+

| OpenAssistant Model (via HuggingFace) |

+-------------------------------------------------------+

           |

           | Generated Job Responsibilities

           v

+---------------------+

| Display to User |

+---------------------+

           |

           | User Feedback (Optional)

           v

+----------------------------+

| User Feedback Loop |

+----------------------------+

```





***In Nutshell,
The application evolves, continuous refinement and user engagement will be pivotal to ensure it meets the dynamic needs of HR professionals and recruiters in creating compelling job descriptions.***
