require('dotenv').config()
// const app = require("express")();
// const http = require("http");
// const cors = require("cors");
// const {Server} = require("socket.io");
// app.use(cors());
const app = require('express')();
const server = require('http').createServer(app);
const io = require('socket.io')(server, {cors: {origin: "*"}});
const crypto = require('crypto') // for md5

dev_mode = true

function log(...args) {
    if (dev_mode) {
        console.log(args);
    }
}

//---------------------- Updates BEGIN -------------------------------//
let num_users_connected = 0
const components_status = {
    "scraper": {
        "status": "not_initialized",
        "msg_log": ["N/A"]
    },
    "database": {
        "status": "not_initialized",
        "msg_log": ["N/A"]
    },
    "ai": {
        "status": "not_initialized",
        "msg_log": ["N/A"]
    },
    "test": {
        "status": "not_initialized",
        "msg_log": ["N/A"]
    }
}

function notify_single_admin(admin) {
    admin.socket.emit("update_components", {
        "num_users_connected": num_users_connected,
        "components_status": admin.components_status
    })
    for (const [type, values] of Object.entries(admin.components_status)) {
        admin.components_status[type]["msg_log"] = []
    }

}

function notify_all_admins() {
    for (const [key, admin] of Object.entries(admins)) {
        notify_single_admin(admin);
    }
}


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
    log(components_status)
});

//---------------------- Init PART END -------------------------------//

//---------------------- Admin Begin ---------------------------//

let date = new Date();
let admins = {}


//--------------------- Admin End ----------------------------//


io.on("connection", (socket) => {
    num_users_connected += 1;
    notify_all_admins();
    log(`User Connected: ${socket.id}`);
    socket.on("login", async function (credentials, callback) {
        if (admins[socket.id] === undefined) {
            if (credentials.username === "a") {
                if (credentials.password === "a") {
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
                        date: date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear() + " at "
                            + date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds(),
                        socket: socket,
                        components_status: clone_component_status
                    }
                    callback({result: "verified", sid: admins[socket.id].sid, status: components_status});
                    notify_single_admin(admins[socket.id]);
                    log("Created session for ", credentials.username, "session id ", admins[socket.id]["sid"])
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

    socket.on("components_update_request", async function (sid, callback) {
        if (admins[socket.id] !== undefined) {
            if (admins[socket.id]["sid"] === sid && admins[socket.id]["socket"] !== undefined) {
                notify_single_admin(admins[socket.id])
                callback({"result": "notified"});
            } else {
                callback({"result": "failed", "msg": "Invalid session id please login again."})
            }
        } else {
            callback({"result": "failed", "msg": "Session lost please login again."})
        }
    })

    socket.on("check_sid", async function (sid, callback) {
        if (admins[socket.id] !== undefined) {
            if (admins[socket.id].sid !== sid) {
                callback({"result": "failed"})
            }
        } else {
            callback({"result": "failed"})
        }
    })

    socket.on("logout", async function (user, callback) {
        if (admins[socket.id] === user.sid) {
            admins.splice(socket.id);
            log("logged out " + socket.id)
            callback({result: "logged out"});
        } else {
            if (admins[socket.id] === undefined) {
                callback({result: "user already logged out"})
            } else {
                log(admins[socket.id])
                callback({result: "WTF"})
            }
        }
    })

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
