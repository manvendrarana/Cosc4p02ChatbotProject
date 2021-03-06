require('dotenv').config()
const app = require('express')();
const server = require('http').createServer(app);
const io = require('socket.io')(server, {cors: {origin: "*"}});
const crypto = require('crypto') // for md5

dev_mode = true

/*
* Logs info in console if dev mode is on.
* */
function log(...args) {
    if (dev_mode) {
        console.log(args);
    }
}

//---------------------- Updates BEGIN -------------------------------//
let num_users_connected = 0
const components_status = {
    "scraper": {
        "status": "not_initialized", "msg_log": []
    }, "database": {
        "status": "not_initialized", "msg_log": []
    }, "ai": {
        "status": "not_initialized", "msg_log": []
    }, "test": {
        "status": "not_initialized", "msg_log": []
    }
}

/*
* This method notifies the single admin and empties the logs for each component for that specific component.
* It notifies the user by emitting update_components event.
* */
function notify_single_admin(admin) {
    admin.socket.emit("update_components", {
        "num_users_connected": num_users_connected, "components_status": admin.components_status
    })
    for (const [type, values] of Object.entries(admin.components_status)) {
        admin.components_status[type]["msg_log"] = []
    }

}

// This method notifies all the logged in admins.
function notify_all_admins() {
    for (const [key, admin] of Object.entries(admins)) {
        notify_single_admin(admin);
    }
}

// This method updates the component status logs for server and each admin.
function components_updater(component, status, message) {
    log(component, message, status);
    components_status[component]["status"] = status
    if (components_status[component]["msg_log"].length > 50) {
        components_status[component]["msg_log"].slice(50 - components_status[component]["msg_log"].length);
    }
    components_status[component]["msg_log"].push(message)
    for (const [key, admin] of Object.entries(admins)) {
        admin.components_status[component]["msg_log"].push(message)
        admin.components_status[component]["status"] = status
    }
    notify_all_admins();
}

//---------------------- Updates END -------------------------------//

//---------------------- Init PART BEGIN -------------------------------//
const {py_handler} = require("./components/py_handler.js");

const python_handler = new py_handler();

python_handler.initialize(components_updater, log).then(r => {
    log("py handler ready");
});

//---------------------- Init PART END -------------------------------//

//---------------------- Admin Begin ---------------------------//

let date = new Date();
let admins = {}

// This method handles different requests for admin such as live scrape and show documents .
function handlerAdminRequest(requestType, socket_id, sid, callback, input_data=undefined) {
    if (admins[socket_id] !== undefined) {
        if (admins[socket_id]["sid"] === sid && admins[socket_id]["socket"] !== undefined) {
            python_handler.request(requestType, input_data, socket_id).then((resolve) => {
                if (resolve) {
                    callback({"result": "success", "response": resolve});
                }
            }).catch((error)=>{
                callback({"result": "failed", "response": error});
            });
        } else {
            callback({"result": "failed", "response": "Invalid session id please login again."});
        }
    } else {
        callback({"result": "failed", "response": "Session lost please login again."});
    }
}

//--------------------- Admin End ----------------------------//

io.on("connection", (socket) => {
    num_users_connected += 1;
    notify_all_admins();
    log(`User Connected: ${socket.id}`);

    // login event observer method, Checks if username and password is correct and provides the session id.
    socket.on("login", async function (credentials, callback) {
        if (admins[socket.id] === undefined) {
            if (credentials.username === "admin") {
                if (credentials.password === process.env.ADMIN_PASSWORD) {
                    let clone_component_status = {}
                    for (const [type, values] of Object.entries(components_status)) {
                        clone_component_status[type] = {
                            "msg_log": [...components_status[type]["msg_log"]],
                            "status": components_status[type]["status"]
                        }
                    }
                    admins[socket.id] = {
                        username: credentials.username,
                        sid: crypto.createHash('md5').update(socket.id + process.env.SALT).digest("hex"),
                        date: date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear() + " at " + date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds(),
                        socket: socket,
                        components_status: clone_component_status
                    }
                    callback({result: "verified", sid: admins[socket.id].sid, status: components_status});
                    log("Created session for "+ credentials.username+", session id "+ admins[socket.id]["sid"])
                    notify_single_admin(admins[socket.id]);

                } else {
                    callback({result: "failed", msg: "Invalid Password"});
                }
            } else {
                callback({result: "failed", msg: "User does not exist"});
            }
        } else {
            callback({result: "failed", msg: "User already logged in"})
        }
    })

    // Component latest state request observer, checks if sid is correct and emits .
    socket.on("components_update_request", async function (sid, callback) {
        if (admins[socket.id] !== undefined) {
            if (admins[socket.id]["sid"] === sid && admins[socket.id]["socket"] !== undefined) {
                notify_single_admin(admins[socket.id])
                callback({"result": "notified"});
            } else {
                callback({"result": "failed", "msg": "Invalid session id please login again."});
            }
        } else {
            callback({"result": "failed", "msg": "Session lost please login again."});
        }
    })

    // Observer for a live scrape request sent by admin.
    socket.on("scrape_system", async function (sid, callback) {
        handlerAdminRequest("scrape_pages", socket.id, sid, callback);
    })

    // Observer for a request to see documents scraped sent by admin
    socket.on("view_scraped_documents", async function (sid, callback) {
        handlerAdminRequest("view_scraped_data", socket.id, sid, callback);
    })

    // Observer to change the max amount of Ai processing running.
    socket.on("change_max_ai_processes", async function(sid, value, callback){
        handlerAdminRequest("change_ai_max_process_by", socket.id, sid, callback, value)
    })

    // Observer to launch tests
    socket.on("execute_tests", async function(sid,callback){
      handlerAdminRequest("system_test", socket.id, sid,callback);
    })

    // Observer to Check if logged in admin has a valid sid.
    socket.on("check_sid", async function (sid, callback) {
        if (admins[socket.id] !== undefined && admins[socket.id].sid !== sid) {
            callback({"result": "failed"})
        } else {
            callback({"result": "verified"})
        }
    })

    // Observer for logout request.
    socket.on("logout", async function (user, callback) {
         if (admins[socket.id] === undefined) {
             callback({result: "user already logged out"})
        }
        else if (admins[socket.id].sid === user.sid) {
            delete admins[socket.id]
            log("logged out " + socket.id)
            callback({result: "logged out"});
        } else {
            log("Possible leaked admin id " + admins[socket.id])
            callback({result: "WTF"})
        }
    })

    // Observer for handling customer queries.
    socket.on("message", async function (data, callback) {
        if (components_status["ai"]["status"] === "working" && python_handler !== undefined) {
            const ai_response = await python_handler.ask(data.message, socket.id);
            callback(ai_response);
        } else {
            callback({"title": "N/A", "url": "N/A", "answer": "I am sorry the bot is currently busy."})
        }
    });

    socket.on("disconnect", () => {
        num_users_connected -= 1;
        log("User Disconnected", socket.id);
    });
});

server.listen(3001, () => {
    console.log("SERVER RUNNING");
});
