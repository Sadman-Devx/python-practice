def main():
    result = {"name": "shadman", "grade": "A"}
    result.update()
    print(report(result))

def report(result):
    return f"""
    Name: {result.get("name", "unknown")}
    Grade: {result.get("grade", "unknown")}
    House: {result.get("district", "unknown")}
    """
main()