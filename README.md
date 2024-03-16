# MOSAIC AI ChatBot (This is not the original reprository of the project as its private, but can be provided if requested along side deployed version of the application)

## Introduction
The MOSAIC AI ChatBot is developed by the SFU Blueprint Team to enhance the engagement and satisfaction of users interacting with MOSAIC's services. By leveraging advanced AI and machine learning technologies, this chatbot aims to streamline the dissemination of information and improve user experience on the MOSAIC website, with a focus on accessibility and multi-language support.

## Vision
To significantly improve user satisfaction and streamline the dissemination of information, making MOSAIC's services more accessible and efficient for newcomers, immigrants, refugees, and individuals from diverse backgrounds.

## Technology Stack
- **Frontend:** React, Vite for a modern, efficient UI development experience.
- **Backend:** Flask (Python) to handle backend services, providing a lightweight and flexible web server.
- **Language Learning Model (LLM):** Utilization of both OpenAI models and free open-source options, depending on the specific requirements and constraints of the project, this is to be Finalized

## Project Setup
### Prerequisites
- Node.js (for React and Vite)
- Python (for Flask)
- Access to OpenAI API (if using OpenAI models)

## Installation
1. #### Clone the repository
   
   ```sh
          git clone https://github.com/SFU-Blueprint/mosaic-chatbot.git
    ```

   **ensure you have the secrets /.env file(s)**

3. ### Client setup
   
      ```sh
          cd ./client
          npm install
          npm run dev
      ```

4. ### Server setup

   **Virtual Environment Setup**
- **Windows:**
   **Create and activate a virtual environment:**
     - Create a virtual environment named `myenv`:
       
       ```sh
          python -m venv myenv
       ```
     - Activate the virtual environment:
       
       ```sh
       myenv\Scripts\activate
       ```

- **Linux/Mac:**
  1. **Create and activate a virtual environment:**
     - Create a virtual environment named `myenv`:
       
       ```bash
       python3 -m venv myenv
       ```
     - Activate the virtual environment:
       
       ```bash
       source myenv/bin/activate
       ```
 4. ### Install Dependancies
    - In the `./server` folder, install the required Python packages from the `requirements.txt` file:
      
     ```bash
     pip install -r ./dependencies/requirements.txt
      ```
5. ### Set Flask Application Environment Variable
  - In the `./server/src` folder run:    
  - **Windows:**
    
     ```bash
     set FLASK_APP=app.py     
      ```

  - **Linux/Mac:**
    
      ```bash
     export FLASK_APP=app.py     
      ```
6. ### Run the Flask Server
   - In the `./server/src` folder run:
     
      ```bash
     flask run    
      ```
### Note for Development:
   **If you are developing and not in production, make sure your client URL is set to localhost, and you run the server locally during development.**

   **This setup will start the Flask server, which serves as the backend for the MOSAIC AI ChatBot, allowing it to handle requests and interact with the frontend.**



## Usage
Provide instructions on how to use the chatbot, including any available commands or features specific to interacting with the chatbot on the MOSAIC website.

## Core Features
- Personalized recommendations for programs and services.
- Multi-language processing capabilities.
- Integration with MOSAIC's database for real-time information updates.

## The Figma prototype of this application
https://www.figma.com/file/RuFiaNVxkVBbae99GMtpEg/INITIAL-RESEARCH_MOSAIC?type=design&node-id=0%3A1&mode=design&t=pt5c6QObU4uWJCgN-1

## Acknowledgments
Special thanks to all team members, MOSAIC executives, and the SFU Blueprint team for their dedication and hard work in bringing this project to life.


