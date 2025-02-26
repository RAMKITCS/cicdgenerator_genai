import os
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from io import BytesIO

# Load OpenAI API Key securely
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("\U0001F6D1 Missing OpenAI API Key! Set it as an environment variable.")
    st.stop()

# Initialize OpenAI model
llm = ChatOpenAI(
    model_name="gpt-4o",
    openai_api_key=openai_api_key,
    temperature=0.1,
    max_retries=3
)

# Initialize session state for iteration count
if "refinement_iteration" not in st.session_state:
    st.session_state.refinement_iteration = 0

# Function to generate CI/CD pipeline based on selected tool, language, and build tool
def generate_pipeline(ci_tool, language, build_tool, deployment_target):
    instructions = {
        "Azure DevOps": "Generate a YAML pipeline file (.yml) with appropriate stages for build, test, security scan, artifact upload, containerization, and deployment.",
        "Jenkins": "Generate a Jenkinsfile written in Groovy format for declarative pipelines, including build, test, security scanning, artifact storage, and deployment.",
        "GitHub Actions": "Generate a YAML workflow file (.yml) for GitHub Actions, ensuring proper job separation for build, test, security, and deployment.",
        "GitLab CI/CD": "Generate a YAML pipeline (.gitlab-ci.yml) for GitLab CI/CD, incorporating best practices for testing, security scanning, and deployment."
    }

    prompt = f"""
    Generate a {ci_tool} CI/CD pipeline for a {language} project using {build_tool}.
    {instructions.get(ci_tool, 'Provide a structured pipeline file in the appropriate format.')}
    Ensure the output is structured properly and easy to read, using clear formatting.
    Include best practices such as caching dependencies, parallel execution, unit testing, security scans, artifact storage, rollback strategies, and containerization using Docker.
    Deploy to {deployment_target} (AKS/OpenShift).
    """

    file_format = "yaml" if ci_tool in ["Azure DevOps", "GitHub Actions", "GitLab CI/CD"] else "groovy"
    file_extension = ".yml" if file_format == "yaml" else "Jenkinsfile"

    try:
        response = llm.invoke(prompt)
        return response.content.strip() if hasattr(response, 'content') else str(response).strip() if response else "❌ No response received!", file_format, file_extension
    except Exception as e:
        st.error(f"❌ Error generating pipeline: {str(e)}")
        return None, None, None

# Function to refine pipeline based on user feedback
def refine_pipeline(feedback, pipeline_code, ci_tool):
    prompt = f"""
    Refine the following {ci_tool} CI/CD pipeline based on this user feedback:
    
    Feedback: {feedback}
    
    Pipeline:
    {pipeline_code}
    
    Ensure the output remains structured, clean, and easy to read.
    Improve security, efficiency, maintainability, and ensure best practices in CI/CD.
    Output only the updated configuration.
    """
    try:
        response = llm.invoke(prompt)
        return response.content.strip() if hasattr(response, 'content') else str(response).strip() if response else "❌ No response received!"
    except Exception as e:
        st.error(f"❌ Error refining pipeline: {str(e)}")
        return None

# Function to provide file download option
def get_download_link(pipeline_code, file_extension):
    file_name = f"pipeline{file_extension}"
    file_bytes = BytesIO(pipeline_code.encode('utf-8'))
    return st.download_button(label="📥 Download Pipeline", data=file_bytes, file_name=file_name, mime="text/plain")

# Streamlit UI
st.set_page_config(layout="wide")  # Enable full-width layout
st.title("🚀 AI-Powered CI/CD Pipeline Generator")

# Sidebar for configuration
st.sidebar.header("🔧 Configuration")
ci_tool = st.sidebar.selectbox("Choose CI Tool", ["Azure DevOps", "Jenkins", "GitHub Actions", "GitLab CI/CD"])
language = st.sidebar.selectbox("Choose Programming Language", ["Java", ".NET", "Node.js", "Python"])
build_tool = st.sidebar.selectbox("Choose Build Tool", ["Maven", "Gradle", "MSBuild", "NPM", "Yarn", "Pip"])
deployment_target = st.sidebar.selectbox("Choose Deployment Target", ["AKS", "OpenShift"])

# Generate pipeline
if st.sidebar.button("Generate Pipeline"):
    st.session_state.refinement_iteration = 0  # Reset iteration count
    pipeline_code, file_format, file_extension = generate_pipeline(ci_tool, language, build_tool, deployment_target)
    if pipeline_code:
        st.session_state.pipeline_code = pipeline_code
        st.session_state.pipeline_language = file_format
        st.session_state.pipeline_extension = file_extension
        st.success(f"✅ {ci_tool} Pipeline generated successfully!")
        st.code(pipeline_code, language=file_format, line_numbers=True)
        get_download_link(pipeline_code, file_extension)  # Provide download button

# Refinement section
st.subheader("🔄 Interact with the pipeline to refine to your need in Natural Language ")
st.write("Use the text box below to provide suggestions for improving the pipeline.")
refine_feedback = st.text_area("✍️ Provide feedback to refine the pipeline:", height=150)
if st.button("Refine Pipeline"):
    if "pipeline_code" not in st.session_state or not st.session_state.pipeline_code:
        st.warning("⚠️ Generate a pipeline first before refining.")
    elif not refine_feedback.strip():
        st.warning("⚠️ Please provide feedback before refining.")
    else:
        st.session_state.refinement_iteration += 1  # Increment iteration count
        refined_pipeline = refine_pipeline(refine_feedback, st.session_state.pipeline_code, ci_tool)
        if refined_pipeline:
            st.session_state.pipeline_code = refined_pipeline
            st.success(f"✅ Pipeline refined successfully! (Iteration {st.session_state.refinement_iteration})")
            st.code(refined_pipeline, language=st.session_state.pipeline_language, line_numbers=True)
            get_download_link(refined_pipeline, st.session_state.pipeline_extension)
