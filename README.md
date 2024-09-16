

---

**AI Chatbot for Food Ordering and Tracking**

---

### Project Description
The **AI Chatbot for Food Ordering and Tracking** is a smart solution designed to streamline food orders and track their status. Users can interact with the chatbot to manage orders and track their progress in real time. The chatbot utilizes Dialogflow for natural language processing and connects to a FastAPI backend to handle order management. A MySQL database is used to store and retrieve order details.

---

### Features

- **Place Orders**: Users can add items to their orders through the chatbot.
- **Modify Orders**: Users can update or remove items from their orders.
- **Track Orders**: Users can track their orders' status in real time.
- **Real-time Interaction**: The chatbot provides instant responses and order updates.
- **Database Integration**: Order details are stored and managed using a MySQL database.

---

### Tech Stack

- **Frontend**: HTML, Dialogflow API for chatbot interaction
- **Backend**: FastAPI, Python
- **Database**: MySQL
- **Deployment**: ngrok for HTTP to HTTPS conversion, integrated with Dialogflow

---

### Installation

#### Prerequisites
- Python 3.7+
- MySQL Server
- Ngrok for tunneling
- FastAPI
- Dialogflow account to configure intents

#### Steps to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-chatbot-food-ordering-tracking.git
   cd ai-chatbot-food-ordering-tracking
   ```

2. **Create a Python Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi mysql-connector-python uvicorn
   ```

4. **Set Up MySQL Database**:
   - Create a new MySQL database named `track_n_treat`.
   - Update the database credentials in the `db_helper.py` file.
   - Import necessary SQL scripts from the `/sql` folder (if available).

5. **Run FastAPI Backend**:
   ```bash
   uvicorn main:app --reload
   ```

6. **Set Up Ngrok**:
   - Download and install [ngrok](https://ngrok.com/).
   - Run the following to expose your FastAPI server:
     ```bash
     ngrok http 8000
     ```
   - Copy the HTTPS URL from ngrok and use it in Dialogflow's webhook settings.

7. **Integrate with Dialogflow**:
   - Create a Dialogflow agent and set up intents (e.g., add, remove, and track orders).
   - Use the ngrok HTTPS URL as the webhook URL for real-time backend communication.

8. **Access the Frontend**:
   - Open the `index.html` file in a browser to interact with the embedded chatbot.

---

### Usage

1. **Place an Order**: Mention food items and quantities to the chatbot.
2. **Track an Order**: Provide the order ID, and the chatbot will give you the current status.
3. **Modify an Order**: Remove items before completing the order.

---

### Project Structure

```
📁 ai-chatbot-food-ordering-tracking/
├── 📁 frontend/
│   └── index.html           # Frontend with embedded chatbot
├── 📁 backend/
│   ├── main.py              # FastAPI backend
│   ├── db_helper.py         # MySQL operations
│   ├── generic_helper.py    # Utility functions
├── README.md                # Project documentation
```

---

### Frontend Sample

```html
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Right-aligned Iframe</title>
  </head>
  <body style="background-color: #2B2222;">
    <center>
      <img src="1.png" alt="chatbot not found">
      <img src="2.png" alt="chatbot not found">
    </center>
    <iframe
      width="350"
      height="430"
      allow="microphone;"
      src="https://console.dialogflow.com/api-client/demo/embedded/6ef1cbeb-bde8-4bbb-8761-3b2511fcc343"
      frameborder="0"
      allowfullscreen
      align="right">
    </iframe>
  </body>
</html>
```

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Contact

For questions or suggestions, contact **Elamaran V** at [elamaran893@gmail.com](mailto:elamaran893@gmail.com).

---
