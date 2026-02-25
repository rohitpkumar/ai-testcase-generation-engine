def load_prd(file_path: str) -> str:
    """
    Loads PRD text file and returns content as string
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error loading PRD: {e}")
        return ""
