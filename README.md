**AI-CHATBOT-FOR-FOOD-ORDERING-AND-TRACKING**



**Project Description**

The **AI Chatbot for Food Ordering and Tracking** is a smart solution designed to streamline food orders and track their status. It allows users to interact with the chatbot to add, remove, and complete food orders, as well as track the status of their orders in real time. The chatbot is built using Dialogflow for natural language processing and is connected to a FastAPI backend for order management. The backend communicates with a MySQL database to store and retrieve order information.

 **Features** **:**
 
 **Place Orders**: Users can add items to their orders via the chatbot.
 
 **Modify Orders**: Users can update or remove items from their orders.
 
 **Track Orders**: Users can check the status of their orders.
 
 **Real-time Interaction**: The chatbot provides real-time responses and updates on order status.
 
 **Database Integration**: All orders are stored in a MySQL database.
 

 **Tech Stack** **:**
 
 **Frontend**: HTML, Dialogflow API for chatbot interface
 
 **Backend**: FastAPI, Python
 
 **Database**: MySQL
 
 **Deployment**: ngrok for HTTP to HTTPS conversion, integrated with Dialogflow for backend connectivity.

 

 **Installation** **:**

 **Prerequisites**
-> Python 3.7+
-> MySQL Server
-> Ngrok for tunneling
-> FastAPI
-> Dialogflow account for setting up chatbot intents

 **Steps to Run Locally** **:**

1. **Clone the Repository**
   CMD
   git clone https://github.com/yourusername/ai-chatbot-food-ordering-tracking.git
   cd ai-chatbot-food-ordering-tracking
   

2. **Create a Python Virtual Environment**
   
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. **Install Dependencies**
   
   pip install fastapi mysql-connector-python uvicorn
 

4. **Set Up the MySQL Database**
   - Create a new MySQL database named `track_n_treat`.
   - Update the database credentials in the `db_helper.py` file.
   - Import the necessary tables and procedures from the `/sql` folder (if available).

5. **Run the FastAPI Backend**
   
   uvicorn main:app --reload
   

6. **Set Up Ngrok for HTTPS**
   - Download and install [ngrok](https://ngrok.com/).
   - Run ngrok to expose your FastAPI server:
     
     ngrok http 8000
    
   - Copy the HTTPS URL from ngrok and use it as the webhook URL in Dialogflow.

7. **Integrate with Dialogflow**
   - Create a new agent in Dialogflow and set up intents (e.g., for adding, removing, and tracking orders).
   - Add the ngrok HTTPS URL in Dialogflow's webhook settings for real-time communication with the FastAPI backend.

8. **Access the Frontend**
   - The HTML file (`index.html`) in the project folder includes an embedded Dialogflow chatbot. Open this file in a browser to interact with the chatbot.

 **Usage**
1. **Place an Order**: Start by mentioning food items and quantities to the chatbot.
2. **Track an Order**: Provide the order ID, and the chatbot will give you the current status of the order.
3. **Modify an Order**: You can ask the chatbot to remove items from your current order before completion.

 **Project Structure**

📁 ai-chatbot-food-ordering-tracking/

├── 📁 frontend/

│   └── index.html           # Frontend with embedded chatbot

├── 📁 backend/

│   ├── main.py              # FastAPI backend

│   ├── db_helper.py         # MySQL operations

│   ├── generic_helper.py    # Utility functions

├── README.md                # Project documentation


 **Frontend Sample**

The frontend integrates the chatbot using an iframe. Here's a preview of the HTML structure:
```html
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Right-aligned Iframe</title>
</head>
<Body style="background-color: #2B2222;">
    <center>
        <img src="1.png" alt="chatbot not found">
        <img src="2.png" alt="chatbot not found">
    </center>
    <iframe width="350" height="430" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/6ef1cbeb-bde8-4bbb-8761-3b2511fcc343" frameborder="0" allowfullscreen align="right"></iframe>
</Body>
</html>
```

 **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 **Contact**
For any questions or suggestions, please reach out to ELAMARAN V (mailto:elamaran893@gmail.com).
```
