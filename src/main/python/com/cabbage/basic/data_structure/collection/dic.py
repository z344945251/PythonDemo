
def dic_construction():
    # 一个空的字典
    print({})
    print({"name": "Ken"})
    info = {"name": "Ken", "age": 16}
    print(info)
    hobbies = {"hobbies": ["reading", "running"]}
    print(hobbies)

    print(info.get("name"), info.get("age"), info.get("hobbies"), hobbies.get("hobbies"))

    print("a" in hobbies, "reading" in hobbies, "hobbies" in hobbies)


if __name__ == "__main__":
    dic_construction()