[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18148318&assignment_repo_type=AssignmentRepo)
# Assignment-01
# Assignment 01: EC2 Instance Setup and Data Processing

**Name:** [maihongxu]  
**Computing ID:** [xumaihong]  

## Description
This assignment involves setting up an EC2 instance on AWS, installing necessary software, and performing basic shell scripting and Python programming tasks. The key steps include:

1. **Create and Configure an EC2 Instance**
   - Choose an Ubuntu 22.04 LTS image.
   - Select an EC2 instance type (t3.large recommended).
   - Configure SSH key pairs and security settings.
   - Set up storage (100GB root volume + additional 100GB EBS volume).
   
2. **Install Required Software**
   - Install `pip3`.
   - Install Jupyter Notebook.
   
3. **Collect System Information**
   - Capture OS, CPU, and memory details.
   - Verify `pip3` and Jupyter Notebook installations.

4. **Process StackOverflow Data**
   - Download and extract dataset.
   - Write a shell script (`count_python.sh`) to count occurrences of "python" in CSV files.
   - Write a Python script (`count_github.py`) to count occurrences of "GitHub" in CSV files.
   
5. **Submit the Work**
   - Organize files as specified.
   - Push to GitHub and submit the repository link.

## Instructions to Run Scripts

### Running the Shell Script (`count_python.sh`)
```bash
bash count_python.sh
```

### Running the Python Script (`count_github.py`)
```bash
python3 count_github.py
```

Ensure both scripts are placed in the `_output` folder before submission.


