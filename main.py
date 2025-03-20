def imports(moduls: list[str]):
    import subprocess as sub
    while True:
        try:
            for i in moduls:
                eval(f"import {i}")
            break
        except:
            for i in moduls:
                sub.run(f"pip install {i}")

if __name__ == "__main__":
  # Example Usage
  moduls_list = ["os","base64","requests"]
  imports(moduls_list)
