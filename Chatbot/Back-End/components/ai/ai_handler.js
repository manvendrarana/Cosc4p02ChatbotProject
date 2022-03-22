let {PythonShell} = require('python-shell')


class ai_handler {
    pyshell;

    async initialize(){
        console.log("starting to initialize")
        this.pyshell = new PythonShell(__dirname + "/main.py");
        this.pyshell.send("start");
        return new Promise(resolve=>{
            this.pyshell.on("message", function(message){
                if (message === "Ai is ready for query"){
                    resolve("ready");
                }
            })
        })
    }

    ask(message){
        return new Promise((resolve,reject)=>{
            console.log("sent")
            this.pyshell.send(message)
            this.pyshell.on('message', function(message){
                resolve(message);
            });
            this.pyshell.on("pythonError", function(error){
                reject(error);
            })
        })
    }
}

module.exports.ai_handler = ai_handler;