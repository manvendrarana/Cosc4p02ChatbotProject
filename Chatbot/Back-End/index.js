require('dotenv').config()
// const app = require("express")();
// const http = require("http");
// const cors = require("cors");
// const {Server} = require("socket.io");
// app.use(cors());
const app = require('express')();
const server = require('http').createServer(app);
const io = require('socket.io')(server, {cors: {origin: "*"}});

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

io.on("connection", (socket) => {
    num_users_connected += 1;
    log(`User Connected: ${socket.id}`);
    socket.on("message", async function (data, cb) {
        log("got a message from", socket.id, data)
        log("current status", components_status)
        if (components_status["ai"]["status"] === "working" && python_handler !== undefined) {
            const ai_response = await python_handler.ask(data.message, socket.id);
            cb(ai_response);
        } else {
            cb({"title": "N/A", "url": "N/A", "answer": "I am sorry the bot is currently busy."})
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
