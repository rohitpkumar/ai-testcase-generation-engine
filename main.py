from app.prd_parser import load_prd
from app.requirement_extractor import extract_requirements
from app.testcase_generator import generate_testcases
from app.coverage_analyzer import analyze_coverage
from app.report_generator import export_testcases, export_coverage


def main():
    print("🚀 AI Test Case Generator Started")

    prd_path = "sample_prd/login_prd.txt"
    prd_content = load_prd(prd_path)

    if not prd_content:
        print("❌ Failed to load PRD")
        return

    print("\n📄 PRD Loaded Successfully")

    print("\n🧠 Extracting Requirements using AI...\n")
    requirements = extract_requirements(prd_content)
    print("✅ Requirements Extracted\n")

    print("\n🧪 Generating Test Cases...\n")
    testcases = generate_testcases(requirements)
    print("✅ Test Cases Generated\n")

    # Print Test Cases
    for req in testcases:
        print(f"\n{req['requirement_id']}")
        for tc in req["testcases"]:
            print(f"  - [{tc['type']}] {tc['title']}")

    print("\n📊 Analyzing Coverage...\n")
    coverage_result = analyze_coverage(requirements, testcases)

    print("📈 Coverage Summary:")
    print(f"Total Requirements: {coverage_result['total_requirements']}")
    print(f"Fully Covered: {coverage_result['fully_covered']}")
    print(f"Coverage %: {coverage_result['coverage_percentage']:.2f}%")

    print("\n📋 Detailed Coverage Report:")
    for detail in coverage_result["details"]:
        print(f"{detail['requirement_id']} - {detail['status']}")
        if detail["missing"]:
            print(f"   Missing: {detail['missing']}")

    print("\n📁 Exporting Reports...\n")

    export_testcases(testcases)
    export_coverage(coverage_result)

    print("\n🎉 All Reports Generated Successfully!")


if __name__ == "__main__":
    main()