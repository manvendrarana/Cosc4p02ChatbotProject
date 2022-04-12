const express = require("express");
const app = express();
const http = require("http");
const cors = require("cors");
const { Server } = require("socket.io");
app.use(cors());

//---------------------- AI Init PART BEGIN -------------------------------//
const {ai_handler} = require("./components/ai/ai_handler.js");

let obj = new ai_handler();

var initialize_Ai = async function(){
    console.log(await obj.initialize());
}

initialize_Ai();
//---------------------- AI Init PART END -------------------------------//

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


  socket.on("send_message",async function(data,cb) {
    console.log("got something", data)
    var ai_respose = await obj.ask(data.message);
    cb(ai_respose);

    var element = document.getElementById("state");
    element.innerHTML = "Waiting for user...";
  });

  socket.on("disconnect", () => {
    console.log("User Disconnected", socket.id);
  });
});

server.listen(3001, () => {
  console.log("SERVER RUNNING");
});
