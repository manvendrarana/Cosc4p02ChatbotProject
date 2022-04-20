let {PythonShell} = require('python-shell')
const path = require("path");


class py_handler {
    pyshell;
    initResolve;
    initReject;
    user_message_buffer = {}
    admin_request_buffer = {}
    components_updater;


    async initialize(component_updater, log) {
        //console.log("starting to initialize"+__dirname)
        this.components_updater = component_updater;
        let options = {
            mode: 'json',
            pythonPath: path.join(__dirname, '..', "venv", "Scripts", "python.exe"),
            pythonOptions: ['-u'], // get print results in real-time
            scriptPath: __dirname,
            args: [process.env.MYSQL_USER, process.env.MYSQL_PASSWORD, "testDb", 1]
        };
        this.pyshell = new PythonShell("main.py", options);
        this.pyshell.on("message", (result) => {
            log(result)
            switch (result["type"]) {
                case "init": { // gets back message
                    this.initResolve();
                    break;
                }
                case "update": { // gets back component, update and update_msg
                    this.components_updater(result["component"], result["update"], result["update_message"])
                    break;
                }
                case "test_result": {
                    let t_result = {
                        component_name: "xyz",
                        unit_name: "",
                        test_result: ""
                    }
                    break;
                }
                case "ai_query": { // gets back id, url, title and answer
                    const id = result["id"];
                    this.user_message_buffer[id]["resolve"]({
                        "title": result["title"],
                        "url": result["url"],
                        "answer": result["answer"]
                    });
                    // rejection not handled !!!
                    break;
                }
                case "failed_admin": {
                    break;
                }
                case "success_admin": {
                    break;
                }
            }
        })
        let crashed = (message) => {
            this.components_updater("scraper", "crashed", message)
            this.components_updater("database", "crashed", message)
            this.components_updater("ai", "crashed", message)
            console.log(message)
        }
        this.pyshell.on("pythonError", (message) => {
            crashed(message);
        })
        this.pyshell.on("error", (message) => {
            crashed(message);
        })
        return new Promise((resolve, reject) => {
            this.initResolve = resolve;
        })

    }

    ask(query, id) {
        return new Promise((resolve, reject) => {
            this.pyshell.send({"type": "ai_query", "id": id, "query": query})
            this.user_message_buffer[id] = {
                "resolve": resolve,
                "reject": reject
            }
        })
    }

    request(request_type, id) {
        return new Promise((resolve, reject) => {
            this.pyshell.send({"type": request_type, "id": id})
            if (this.admin_request_buffer[id] === undefined) {
                this.admin_request_buffer[id] = {
                    request_type: {
                        "resolve": resolve,
                        "reject": reject
                    }
                }
            } else {
                this.admin_request_buffer[id][request_type] = {
                    "resolve": resolve,
                    "reject": reject
                }
            }
        })
    }
}

module.exports = {
    py_handler
};
