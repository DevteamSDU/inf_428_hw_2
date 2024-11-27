from helpers.data_generation import generate_random_data
from helpers.elasticsearch_utils import create_index, upload_to_elasticsearch, calculate_aggregated_threat_score
from helpers.pdf_parser import extract_pdf_data
from helpers.task_assigner import assign_debugging_tasks
import json


if __name__ == "__main__":
    index_name = "user_threat_scores"
    pdf_path = "data/homework-2-task-2-email-list.pdf"

    data = generate_random_data()
    data.to_csv("data/random_data.csv", index=False)
    print("Random data generated and saved.")

    create_index(index_name)
    upload_to_elasticsearch(data, index_name)
    overall_score, department_scores = calculate_aggregated_threat_score(index_name)
    print(f"Overall Threat Score: {overall_score:.2f}")
    for dep in department_scores:
        print(f"{dep['key']} Department Avg Score: {dep['avg_score']['value']:.2f}")

    df = extract_pdf_data(pdf_path)
    df.to_csv("data/extracted_data.csv", index=False)
    print("PDF data extracted and saved.")

    tasks = assign_debugging_tasks(df)
    with open("data/debug_tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
    print("Debugging tasks assigned and saved.")
