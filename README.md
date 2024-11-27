# inf_428_hw_2

# Homework 2 Report

Threat Score Aggregation with Elasticsearch and Docker.

This project implements a system for:
1. Generating random threat data for company departments.
2. Aggregating and analyzing the data using Elasticsearch.
3. Extracting and processing a list of debugging tasks from a PDF.
4. Assigning debugging tasks between team members.

All components are fully automated using Docker and Python.

---

## Project Structure
```bash
│
├── Dockerfile                                    # Dockerfile для Python-приложения
├── docker-compose.yml                            # Docker Compose для запуска Elasticsearch и Python-приложения
├── requirements.txt                              # Зависимости Python
├── main.py                                       # Главный скрипт с основной логикой
├── helpers/                                      # Вспомогательные модули
│   ├── data_generation.py                        # Модуль для генерации случайных данных
│   ├── elasticsearch_utils.py                    # Модуль для работы с Elasticsearch
│   ├── pdf_parser.py                             # Модуль для обработки PDF-файла
│   └── task_assigner.py                          # Модуль для назначения задач по проверке
├── data/                                         # Папка с данными
│   ├── homework-2-task-2-email-list.pdf          # Предоставленный PDF-файл с парами студентов
│   ├── random_data.csv                           # Сгенерированные данные угроз
│   ├── debug_tasks.json                          # Список задач по проверке
│   └── extracted_data.csv                        # Извлечённые данные из PDF-файла
└── README.md                                     # Документация проекта
```

---

### Workflow

1. **Random Threat Data Generation**:
   - Generates user threat scores (0-90) for 5 departments.
   - Each department has a random number of users (10-200).
   - The data is saved to a CSV file for reproducibility.

2. **Elasticsearch Integration**:
   - Creates an Elasticsearch index for storing threat scores.
   - Uploads the generated data to Elasticsearch.
   - Aggregates threat scores to calculate:
     - Overall threat score.
     - Department-wise average scores.

3. **PDF Parsing**:
   - Parses the input PDF (`homework-2-task-2-email-list.pdf`) to extract pairs of team members.

4. **Task Assignment**:
   - Assigns debugging tasks such that each person checks the code of another in their pair.
   - Saves the assignments to a JSON file (`debug_tasks.json`).

5. **Full Automation with Docker**:
   - Combines Elasticsearch and Python services using Docker Compose.
   - Running a single command sets up the entire project.

---

## Installation

### Prerequisites

1. **Docker and Docker Compose**:
   - Install Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
   - Install Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

2. **Clone the repository**:
   ```bash
   git clone https://github.com/DevteamSDU/inf_428_hw_2.git
   cd inf_428_hw_2
   ```

---

### Running the project

```bash
docker-compose up --build
```
