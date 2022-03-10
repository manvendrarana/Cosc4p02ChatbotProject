let {PythonShell} = require('python-shell')


class ai_handler {
    constructor(response){
        console.log("running")
        const pyshell = new PythonShell(__dirname + "/main.py");
        this.pyshell = pyshell;
        pyshell.send("start");
        pyshell.on('message', function(message){
            response(message);
        })
        pyshell.on("pythonError", function(error){
            console.log(error);
        })
    }

    ask(message){
        this.pyshell.send(message)
    }
}


function resp (message){
    console.log(message)
}

let obj = new ai_handler(resp);
obj.ask("what are the locations of steeplechase events?");