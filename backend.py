print("Local Development")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.api:app", host="localhost", port=8008, reload=True)
