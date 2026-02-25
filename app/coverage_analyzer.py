def analyze_coverage(requirements: list, testcases: list):
    """
    Analyzes coverage for each requirement.
    Checks if functional, negative and edge testcases exist.
    """

    total_requirements = len(requirements)
    fully_covered = 0
    coverage_report = []

    for req in requirements:
        req_id = req["requirement_id"]

        # Find matching testcases
        matching = next((tc for tc in testcases if tc["requirement_id"] == req_id), None)

        if not matching:
            coverage_report.append({
                "requirement_id": req_id,
                "status": "NO TEST CASES",
                "missing": ["functional", "negative", "edge"]
            })
            continue

        types_present = [tc["type"] for tc in matching["testcases"]]

        missing_types = []

        for required_type in ["functional", "negative", "edge"]:
            if required_type not in types_present:
                missing_types.append(required_type)

        if not missing_types:
            fully_covered += 1
            status = "FULLY COVERED"
        else:
            status = "PARTIALLY COVERED"

        coverage_report.append({
            "requirement_id": req_id,
            "status": status,
            "missing": missing_types
        })

    coverage_percentage = (fully_covered / total_requirements) * 100 if total_requirements > 0 else 0

    return {
        "total_requirements": total_requirements,
        "fully_covered": fully_covered,
        "coverage_percentage": coverage_percentage,
        "details": coverage_report
    }