import pandas as pd
import os


def export_testcases(testcases: list):
    """
    Exports testcases to CSV
    """

    rows = []

    for req in testcases:
        for tc in req["testcases"]:
            rows.append({
                "Requirement ID": req["requirement_id"],
                "Type": tc["type"],
                "Title": tc["title"],
                "Steps": " | ".join(tc["steps"]),
                "Expected Result": tc["expected_result"]
            })

    df = pd.DataFrame(rows)

    os.makedirs("output", exist_ok=True)
    df.to_csv("output/testcases.csv", index=False)

    print("✅ Testcases exported to output/testcases.csv")


def export_coverage(coverage_result: dict):
    """
    Exports coverage analysis to CSV
    """

    rows = []

    for detail in coverage_result["details"]:
        rows.append({
            "Requirement ID": detail["requirement_id"],
            "Status": detail["status"],
            "Missing Types": ", ".join(detail["missing"])
        })

    df = pd.DataFrame(rows)

    os.makedirs("output", exist_ok=True)
    df.to_csv("output/coverage_report.csv", index=False)

    print("✅ Coverage report exported to output/coverage_report.csv")