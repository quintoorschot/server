from flask import Flask

def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "! 2"
      print(greeting)
      return {"body": greeting}
  