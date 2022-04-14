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

function log(message) {
    if (dev_mode) {
        console.log(message);
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

function components_updater(component, status, message) {
    log(component, message, status);
    components_status[component]["status"] = status
    components_status[component]["msg_log"].push(message)
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
    log(`User Connected: ${socket.id}`);
    socket.on("login", async function (credentials, callback) {
        if (admins[socket.id] === undefined) {
            if (credentials.username === "a") {
                if (credentials.password === "a") {
                    console.log(credentials)
                    admins[socket.id] = {
                        username: credentials.username,
                        sid: crypto.createHash('md5').update(socket.id + process.env.SALT).digest("hex"),
                        date: date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear() + " at "
                            + date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds()
                    }
                    console.log(admins)
                    log("Creating session for ", credentials.username, "session id ", admins[socket.id]["sid"])
                    callback({result: "verified", sid: admins[socket.id].sid, status: components_status});
                } else {
                    callback({result: "failed", msg: "Invalid Password"});
                }
            } else {
                callback({result: "failed", msg: "User does not exist"});
            }
        }
        else{
            callback({result:"failed", msg:"User already logged in"})
        }
    })

    socket.on("logout", async function(user, callback){
        if(admins[socket.id]=== user.sid){
            admins[socket.id] = undefined;
            callback({result:"logged out"});
        }else{
            if(admins[socket.id]===undefined){
                callback({result: "user already logged out"})
            }else{
                callback({result: "WTF"})
            }
        }
    })

    socket.on("message", async function (data, callback) {
        log("got a message from", socket.id, data)
        log("current status", components_status)
        if (components_status["ai"]["status"] === "working" && python_handler !== undefined) {
            const ai_response = await python_handler.ask(data.message, socket.id);
            callback(ai_response);
        } else {
            callback({"title": "N/A", "url": "N/A", "answer": "I am sorry the bot is currently busy."})
        }
    });

    socket.on("disconnect", () => {
        num_users_connected -= 1;
        if(admins[socket.id]!==undefined){
            admins[socket.id] = undefined
        }
        log("User Disconnected", socket.id);
    });
});

server.listen(3001, () => {
    console.log("SERVER RUNNING");
});
