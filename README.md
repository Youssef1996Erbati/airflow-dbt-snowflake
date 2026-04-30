# 🚀 Airflow dbt Snowflake Pipeline

## 📌 Overview

This project orchestrates a modern data pipeline using **Apache Airflow**, **dbt**, and **Snowflake**.

Airflow is used to schedule and manage dbt transformations that run in Snowflake.

---

## 🏗️ Architecture

```text
GitHub
   ↓
Airflow (Docker)
   ↓
dbt
   ↓
Snowflake
```

---

## ⚙️ Tech Stack

* Apache Airflow (Docker)
* dbt (data transformation)
* Snowflake (data warehouse)
* GitHub (version control)

---

## 📂 Project Structure

```text
dags/                → Airflow DAGs
docker-compose.yaml  → Airflow setup
Dockerfile           → Custom Airflow image
requirements.txt     → Python dependencies
```

---

## 🚀 Pipeline

The Airflow DAG executes:

* dbt run → build models
* dbt test → validate data

---

## ▶️ Run locally

```bash
docker compose up -d
```

Then open:

```text
http://localhost:8080
```

---

## 📈 Features

* Orchestrated dbt pipeline
* Automated scheduling
* Modular data transformations
* Scalable architecture

---

## 🔮 Future Improvements

* Add alerts (Slack / Email)
* Add CI/CD (GitHub Actions)
* Add monitoring
* Deploy on cloud (AWS / GCP)

---

## 👤 Author

Youssef ER-BATI
