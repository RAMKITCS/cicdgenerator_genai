# 🚀 AI-Powered CI/CD Pipeline Generator

This project provides an **AI-powered CI/CD pipeline generator** using **LangChain, OpenAI, and Streamlit**. It allows users to generate, refine, and download **CI/CD pipeline configurations** for different tools like **Azure DevOps, Jenkins, GitHub Actions, and GitLab CI/CD**.

## 📌 Features
- Generate **CI/CD pipelines** based on user-selected tools, languages, and build tools.
- **Refine pipelines** using natural language feedback.
- Supports **Azure DevOps, Jenkins, GitHub Actions, and GitLab CI/CD**.
- Easy **file download** for generated pipelines.
- **Streamlit UI** for interactive experience.

---

## 🚀 Quick Start

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/AI-CICD-Pipeline-Generator.git
cd AI-CICD-Pipeline-Generator
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
```
Activate it:
- **Windows (Command Prompt)**
  ```sh
  venv\Scripts\activate
  ```
- **Windows (PowerShell)**
  ```sh
  .\venv\Scripts\Activate.ps1
  ```
- **Mac/Linux**
  ```sh
  source venv/bin/activate
  ```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```
Or install manually:
```sh
pip install streamlit langchain-community openai
```

### **4️⃣ Set OpenAI API Key**
Create a **`.env`** file in the project root and add:
```
OPENAI_API_KEY=your_openai_api_key_here
```

Or set it as an environment variable:
```sh
export OPENAI_API_KEY="your_openai_api_key_here"  # Mac/Linux
set OPENAI_API_KEY="your_openai_api_key_here"    # Windows CMD
$env:OPENAI_API_KEY="your_openai_api_key_here"   # Windows PowerShell
```

### **5️⃣ Run the Streamlit App**
```sh
streamlit run cicd_generator_3.py
```
This will open the web app in your **default browser**.

---

## 📁 Project Structure
```
📂 AI-CICD-Pipeline-Generator
│── 📄 cicd_generator_3.py     # Main Streamlit App
│── 📄 requirements.txt        # Required Dependencies
│── 📄 README.md               # Documentation
│── 📄 .env                    # OpenAI API Key (add manually)
│── 📂 venv/                   # Virtual Environment (ignored in Git)
```

---

## ⚠️ Troubleshooting
### **1️⃣ ModuleNotFoundError: No module named 'langchain_community'**
Run:
```sh
pip install langchain-community
```

### **2️⃣ Streamlit not found**
Run:
```sh
pip install streamlit
```

### **3️⃣ PowerShell Execution Policy Error**
If running `.\venv\Scripts\Activate.ps1` fails, try:
```sh
Set-ExecutionPolicy Unrestricted -Scope Process
```

### **4️⃣ API Key Not Set**
Ensure your **`.env`** file contains:
```
OPENAI_API_KEY=your_openai_api_key_here
```
Or set it manually before running the app.


## 🔥 Future Enhancements
- Add **more CI/CD tools** like CircleCI and ArgoCD.
- Improve **error handling and debugging**.
- Allow **custom deployment targets** beyond AKS/OpenShift.


## 📜 License
This project is **open-source**. Feel free to use and modify.


