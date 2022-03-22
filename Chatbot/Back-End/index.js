const express = require("express");
const app = express();
const http = require("http");
const cors = require("cors");
const { Server } = require("socket.io");
app.use(cors());

//---------------------- AI Init PART BEGIN -------------------------------//
const {ai_handler} = require("./components/ai/ai_handler.js");

let obj = new ai_handler();

const initialize_Ai = async function () {
  await obj.initialize();
};

let aiInitialized = false;
initialize_Ai().then(()=>{
  aiInitialized = true;
} );
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
    if(aiInitialized){
      const ai_response = await obj.ask(data.message);
      cb(ai_response);
    }
   else{
     cb("I am sorry the system is not ready yet. Please ask again soon!")
    }
  });

  socket.on("disconnect", () => {
    console.log("User Disconnected", socket.id);
  });
});

server.listen(3001, () => {
  console.log("SERVER RUNNING");
});
