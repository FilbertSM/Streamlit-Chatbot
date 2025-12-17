# GAIA

Gaia is a modular, extensible platform designed for advanced chatbot, data analysis, and AI-driven applications. It features a robust client-server architecture, supporting multimodal interactions, role-based workflows, and seamless integration with custom models and data sources.

---

## Table of Contents

- Project Structure
- Features
- Installation & Local Setup
- Usage
- Configuration
- Development
- Contributing
- License

---

## Project Structure

```
gaia/
│
├── client/         # Frontend & user interface logic
│   ├── assets/     # Static assets (images, roleplay resources)
│   ├── components/ # UI components (sidebar, upload, history, etc.)
│   ├── pages/      # Streamlit app pages (chatbots, dashboards, etc.)
│   ├── utils/      # Utility functions (API, helpers)
│   ├── config.py   # Client configuration
│   ├── main.py     # Main entry point for client
│   └── requirements.txt
│
├── server/         # Backend logic, APIs, and data handling
│   ├── chroma_store/ # Vector DB & storage
│   ├── configs/      # Server configuration files
│   ├── data/         # Data and prompt files
│   ├── models/       # Model definitions
│   ├── modules/      # Modular backend logic (PDF, query, etc.)
│   ├── logger.py     # Logging utility
│   ├── main.py       # Main server entry point
│   └── requirements.txt
│
├── uploaded_pdfs/   # User-uploaded documents
├── LICENSE
└── README.md
```

---

## Features

- **Multi-Role Chatbots:** Specialized bots for advisory, research, design thinking, and more.
- **Multimodal Support:** Handles text, images, and document uploads.
- **Extensible UI:** Modular Streamlit components for rapid customization.
- **Backend Flexibility:** Pluggable models, vector storage, and data pipelines.
- **Roleplay & Scenario Assets:** Prebuilt assets for interactive role-based experiences.
- **Secure & Configurable:** Environment-based configs and user session management.

---

## Installation & Local Setup

### Prerequisites

- Python 3.10+
- [pip](https://pip.pypa.io/en/stable/)
- (Recommended) Virtual environment tool: `venv` or `conda`

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/gaia.git
cd gaia
```

### 2. Set Up Virtual Environment

```sh
python -m venv myenv
# On Windows:
myenv\Scripts\activate
# On Unix/Mac:
source myenv/bin/activate
```

### 3. Install Dependencies

Install client and server requirements:

```sh
pip install -r server/requirements.txt
```

### 4. Run the Server

```sh
cd server
uvicorn main:app --reload
```

### 5. Run the Client

In a new terminal:

```sh
cd client
streamlit run main.py
```

---

## Usage

- Access the client UI via the Streamlit app (usually at `http://localhost:8501`).
- Interact with various chatbots, upload documents, and explore dashboards.
- Backend APIs and models are managed via the server.

---

## Configuration

- **Client:** Edit config.py for UI and API endpoint settings.
- **Server:** Adjust db.py and other config files for database, model, and storage options.
- **Assets:** Place custom images or roleplay assets in assets.

---

## Development

- Modularize new features by adding components to components or modules.
- Use pages to add new Streamlit pages.
- Backend logic and models go in models and modules.
- Logging is handled via logger.py.

---

## Contributing

Pull requests and issues are welcome! Please open an issue to discuss major changes or new features.

---

## License

This project is licensed under the terms of the LICENSE file.

---

**Author:**  
Filbert Sembiring Meliala  