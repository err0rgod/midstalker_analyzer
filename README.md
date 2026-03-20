# Midstalker Analyzer

Midstalker Analyzer is a lightweight analysis tool designed to process and inspect data efficiently through an interactive interface. It is built with a focus on simplicity, local execution, and ease of use, allowing users to work with their data without relying on heavy cloud infrastructure.

The application can be run locally using Docker for full control and performance, or accessed directly through the hosted Streamlit version.

---

## Features

* Interactive interface built with Streamlit
* Local file processing without size limitations (Docker mode)
* Simple and fast setup
* Minimal dependencies and optimized runtime
* Clean and modular codebase

---

## Getting Started

You can run the project in two ways:

1. Locally using Docker (recommended)
2. Using the hosted web version

---

## Running Locally with Docker

Running the application locally removes file size limits and improves performance by using your system resources directly.

### Prerequisites

* Docker installed on your system
* Git (optional, for cloning the repository)

### Steps

Clone the repository:

```bash
git clone https://github.com/err0rgod/midstalker_analyzer.git
cd midstalker_analyzer
```

Build the Docker image:

```bash
docker build -t midstalker .
```

Run the container:

```bash
docker run -p 8501:8501 midstalker
```

Open your browser and go to:

```
http://localhost:8501
```

---

## Running via Web (Streamlit)

If you do not want to set up Docker, you can use the hosted version:

https://mid-stalker-analyzer.streamlit.app

Note: The hosted version may have limitations on file size and processing speed.

---

## Project Structure

```
midstalker_analyzer/
├── app.py
├── utils/
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── notebooks/ (development only)
```

---

## Development

To run the project without Docker:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Design Notes

* The application is designed to run fully locally when needed
* Docker support ensures consistent environments across systems
* Non-essential files such as notebooks are excluded from production builds

---

## Contributing

Contributions are welcome. If you find an issue or want to improve the project, feel free to open a pull request or submit an issue.

---

## License

This project is open-source and available under the MIT License.
