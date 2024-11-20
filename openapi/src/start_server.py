import connexion

def main():
    port = 8080
    app = connexion.AsyncApp(__name__, specification_dir="./api-description")
    app.add_api("api.yaml", base_path="/api")
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
