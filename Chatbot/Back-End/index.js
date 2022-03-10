const express = require("express");
const app = express();
const http = require("http");
const cors = require("cors");
const { Server } = require("socket.io");
app.use(cors());

let {PythonShell} = require('python-shell')

let ai = new PythonShell("./components/ai/main.py");

let ai_response = ""

ai.send("start")



const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"],
  },
});

io.on("connection", (socket) => {
  console.log(`User Connected: ${socket.id}`);

  socket.on("join_room", (data) => {
    socket.join(data);
    console.log(`User with ID: ${socket.id} joined room: ${data}`);
  });


  socket.on("send_message", function(data,cb) {
    console.log("got something", data)
    // ai_response = ""
    // ai.send(data.msg)
    // ai.on("message",function(message){
    //   console.log(message);
    //   ai_response = message;
    // })
    cb("ai_response");
    //socket.to(data.room).emit("send_message", data);
  });

  socket.on("disconnect", () => {
    console.log("User Disconnected", socket.id);
  });
});

server.listen(3001, () => {
  console.log("SERVER RUNNING");
});
