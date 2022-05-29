from importlib.resources import files

def main() -> None:
  print("You are running the test package")

  data_resource = files("setuptoolstest").joinpath("data.json")
  with data_resource.open("r") as fp:
    print("fetching data...")
    print(data_resource.read_text())


if __name__ == "__main__":
  main()